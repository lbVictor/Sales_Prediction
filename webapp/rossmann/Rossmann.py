import pickle
import inflection
import pandas as pd
import numpy  as np
from datetime import date, datetime, timedelta


# create the rossmann class
class Rossmann(object):
    def __init__(self):
        
        # create the full project path
        self.home_path = ''

        # load pickle's data
        self.competition_distance_scaler   = pickle.load(open(self.home_path + 'parameter/competition_distance_scaler.pkl', 'rb'))
        self.competition_time_month_scaler = pickle.load(open(self.home_path + 'parameter/competition_time_month_scaler.pkl', 'rb'))
        self.promo_time_week_scaler        = pickle.load(open(self.home_path + 'parameter/promo_time_week_scaler.pkl', 'rb'))
        self.year_scaler                   = pickle.load(open(self.home_path + 'parameter/year_scaler.pkl', 'rb'))
        self.store_type_encoding           = pickle.load(open(self.home_path + 'parameter/store_type_encoding.pkl', 'rb'))


    def data_cleaning(self, df1):
        
        # Rename Columns
        cols_old = df1.columns
        df1.columns = list(map(lambda x: inflection.underscore(x), cols_old))
        
        # Change Data Types
        df1['date'] = pd.to_datetime(df1['date'])

        # Fillout NA
        df1['competition_distance'] = df1['competition_distance'].apply(lambda x: 100000 if pd.isna(x) else x)
        df1['competition_open_since_month'].fillna(1, inplace=True) 
        df1['competition_open_since_year'].fillna(2013, inplace=True) 
        df1['promo2_since_week'].fillna(0, inplace=True) 
        df1['promo2_since_year'].fillna(0, inplace=True)
        df1['promo_interval'].fillna(0, inplace=True) 

        # Change Data Types
        df1['competition_open_since_month'] = df1['competition_open_since_month'].astype('int64') 
        df1['competition_open_since_year'] = df1['competition_open_since_year'].astype('int64') 
        df1['promo2_since_week'] = df1['promo2_since_week'].astype('int64') 
        df1['promo2_since_year'] = df1['promo2_since_year'].astype('int64') 

        return df1

    def feature_engineering(self, df2):
        
        # Feature Engineering
        df2['day'] = df2['date'].dt.day
        df2['month'] = df2['date'].dt.month
        df2['year'] = df2['date'].dt.year
        df2['week_of_year'] = df2['date'].dt.isocalendar().week.astype('int64')
        df2['year_week'] = df2['date'].dt.strftime('%Y-%W')

        month_map = {1: 'Jan', 2: 'Feb', 3: 'Mar', 4: 'Apr', 5: 'May', 6: 'Jun', 7: 'Jul', 8: 'Aug', 9: 'Sep', 10: 'Oct', 11: 'Nov', 12: 'Dec'}
        df2['month_map'] = df2['date'].dt.month.map(month_map)
        df2['is_promo2'] = df2[['month_map', 'promo_interval']].apply(lambda x: 0 if x['promo_interval'] == 0 else 1 if x['month_map'] in x['promo_interval'].split(',') else 0, axis=1)

        df2['competition_since'] = pd.to_datetime(df2['competition_open_since_year'].astype(str) + '-' + df2['competition_open_since_month'].astype(str) + '-1')
        df2['competition_time_month'] = ((df2['date'] - df2['competition_since']) / 30).dt.days

        df2['promo2_since'] = df2['promo2_since_year'].astype(str) + '-' + df2['promo2_since_week'].astype(str) + '-1'
        df2['promo2_since'] = df2['promo2_since'].apply(lambda x: 0 if x == '0-0-1' else (datetime.strptime(x, '%Y-%W-%w')) - timedelta(days=7))
        df2['promo2_time_week'] = df2.apply(lambda x: 0 if x['promo2_since'] == 0 else ((x['date'] - x['promo2_since']) / 7).days, axis=1)

        df2['assortment'] = df2['assortment'].map({'a': 'basic' , 'b': 'extra', 'c': 'extended'})

        df2['state_holiday'] = df2['state_holiday'].map({'0': 'regular_day', 'a': 'public_holiday' , 'b': 'easter_holiday', 'c': 'christmas'})
            
        # Variable Filtering
        df2 = df2[df2['open'] != 0]

        cols_drop = ['open','promo_interval','month_map']
        df2 = df2.drop(cols_drop, axis=1)

        return df2

    def data_preparation(self, df5):

        # Rescaling
        df5['competition_distance'] = self.competition_distance_scaler.fit_transform(df5[['competition_distance']].values )
        
        df5['competition_time_month'] = self.competition_time_month_scaler.fit_transform(df5[['competition_time_month']].values )
        
        df5['promo2_time_week'] = self.promo_time_week_scaler.fit_transform(df5[['promo2_time_week']].values )
        
        df5['year'] = self.year_scaler.fit_transform(df5[['year']].values ) 

        # Encoding
        df5 = pd.get_dummies(df5, prefix=['state_holiday'], columns=['state_holiday'])

        df5['store_type'] = self.store_type_encoding.fit_transform(df5['store_type'])
       
        assortment_dict = {'basic': 1, 'extra': 2, 'extended': 3}
        df5['assortment'] = df5['assortment'].map(assortment_dict)

        # Nature Transformation
        df5['day_sin'] = df5['day'].apply(lambda x: np.sin(x * (2. * np.pi/30)))
        df5['day_cos'] = df5['day'].apply(lambda x: np.cos(x * (2. * np.pi/30)))

        df5['month_sin'] = df5['month'].apply(lambda x: np.sin(x * (2. * np.pi/12)))
        df5['month_cos'] = df5['month'].apply(lambda x: np.cos(x * (2. * np.pi/12)))

        df5['day_of_week_sin'] = df5['day_of_week'].apply(lambda x: np.sin(x * (2. * np.pi/7)))
        df5['day_of_week_cos'] = df5['day_of_week'].apply(lambda x: np.cos(x * (2. * np.pi/7)))

        df5['week_of_year_sin'] = df5['week_of_year'].apply(lambda x: np.sin(x * (2. * np.pi/52)))
        df5['week_of_year_cos'] = df5['week_of_year'].apply(lambda x: np.cos(x * (2. * np.pi/52)))

        # Colunas Selecionadas
        cols_selected = ['store', 'promo', 'store_type', 'assortment', 'competition_distance', 'competition_open_since_month', 'competition_open_since_year', 'promo2_since_week', 'promo2_since_year', 
                         'competition_time_month', 'promo2_time_week', 'day_sin', 'day_cos', 'month_sin', 'month_cos', 'day_of_week_sin', 'day_of_week_cos', 'week_of_year_sin', 'week_of_year_cos']
     
        return df5[cols_selected]

    # Create function to predict
    def get_prediction(self, model, original_data, test_data):
        
        # perform prediction
        pred = model.predict(test_data)

        # join pred into the original data
        original_data['prediction'] = np.expm1(pred)

        # transform from dataframe to json to return via API
        return original_data.to_json(orient='records', date_format='iso')