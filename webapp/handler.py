import os
import pickle
import pandas as pd
from flask             import Flask, request, Response
from rossmann.Rossmann import Rossmann

# load the trained model into memory
model = pickle.load(open('model/model_rossmann.pkl', 'rb'))

# instantiate Flask/Start API
app = Flask(__name__)

# create the endpoint that will receive the requests
@app.route('/rossmann/predict', methods=['POST'])

# create the first function that will run on the endpoint
def rossmann_predict():
   
    # get the request data sent via API
    test_json = request.get_json()
    
    # check if the data really came
    if test_json: 
        # create a single json dataframe
        if isinstance(test_json, dict): 
            test_raw = pd.DataFrame(test_json, index=[0])

        # create a multiple json dataframe
        else: 
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        # Instantiate the Rossmann class
        pipeline = Rossmann()

        # apply changes to data
        df1 = pipeline.data_cleaning(test_raw)
        df2 = pipeline.feature_engineering(df1)
        df3 = pipeline.data_preparation(df2)
        
        # perform prediction and save original data with the predictions
        df_response = pipeline.get_prediction(model, test_raw, df3)

        # return predictions to requestor
        return df_response

    else:
        # if there is no data, return a response stating that the request was successful but the execution was wrong
        return Response('{}', status=200, mimetype='application/json')

# run flask initially
if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)	
    app.run(host='0.0.0.0', port=port)