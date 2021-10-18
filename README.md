## ROSSMANN: A SALES FORECAST PROJECT
![Rossmann_Logo](https://user-images.githubusercontent.com/85720162/137200378-8aea0b70-b41a-451e-a255-d2f21333904f.png)

------------------------------------------------------------------
## About the Project
For the development of this project, public data available by the company Dirk Rossmann GmbH in a Kaggle competition in 2015 was used. From this data, a business context was created in which the company's CFO needs a forecast of the next six weeks of sales of each store. Based on this, this project was developed in order to get as close as possible to a solution to a real demand of the company, executing all the necessary steps, generating insights and building a really usable data product that generates value for the stakeholder and the company.

The methodology used to carry out this project was CRISP-DM which works through cyclical development with the objective of delivering value quickly. **This project refers to the first cycle of CRISP-DM**.

<p align="center">
	The CRISP-DM Cycle
</p>

<p align="center">
	<img width="450" alt="drawing" src="img/crisp.png">
</p>


**For the execution of this project the following tools were used:**
<p align="left">
 <table>
  <tbody>
    <tr valign="top">
      <td width="5%" align="center">
        <span>Python</span><br><br>
        <img height="40px" src="https://cdn.svgporn.com/logos/python.svg">
      </td>
      <td width="5%" align="center">
        <span>pandas</span><br><br>
        <img height="40px" src="https://pandas.pydata.org/static/img/pandas.svg">
      </td>
      <td width="5%" align="center">
        <span>NumPy</span><br><br>
        <img height="40px" src="https://numpy.org/images/logos/numpy.svg">
      </td>
      <td width="5%" align="center">
        <span>Matplotlib</span><br><br>
        <img height="40px" src="https://matplotlib.org/_images/sphx_glr_logos2_001.png">
      </td>
      <td width="5%" align="center">
        <span>seaborn</span><br><br>
        <img height="40px" src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg">
      </td>
      <td width="10%" align="center">
        <span>scikit-learn</span><br><br>
        <img height="40px" src="https://scikit-learn.org/stable/_images/scikit-learn-logo-notext.png">
      </td>
      <td width="5%" align="center">
        <span>XGBoost</span><br><br>
        <img height="40px" src="https://upload.wikimedia.org/wikipedia/commons/6/69/XGBoost_logo.png">	    
      </td>
      <td width="5%" align="center">
        <span>Flask</span><br><br>
        <img height="40px" src="https://flask.palletsprojects.com/en/1.1.x/_images/flask-logo.png">
      </td>
      <td width="5%" align="center">
        <span>Heroku</span><br><br>
        <img height="40px" src="https://blog.4linux.com.br/wp-content/uploads/2018/01/Heroku.png">
       </td>
  </tbody>
</table>
</p>

## About the Company
Dirk Rossmann GmbH is one of the largest drug store chains in Europe with around 56.300 employees and a total of 4.244 stores, including 2.233 in Germany. In 2020, the Rossmann Group achieved sales of €10,35 billion turnover in Germany, Poland, Hungary, the Czech Republic, Turkey, Albania, Kosovo and Spain.

The company was founded by Dirk Rossmann with its headquarters in Burgwedel near Hanover in Germany. The Rossmann family owns 60%, and the Hong Kong-based A.S. Watson Group 40% of the company.

The product range includes up to 21,700 items and can vary depending on the size of the shop and the location.

## Project Structure
### Business Understanding
1. **Business Problem:** Rossmann's CFO recently asked store managers for a projection of the next six weeks of sales, as based on this information, he intends to define the investment that will be made in the renovation of each store. Given the requested information and the lack of accurate response from store managers, the data science team suggested the development of a solution to this problem, prioritizing the quality of information and ease of access by the stakeholder.

  	For this project, a dataset with sales information for the years 2013 until mid-2015 was made available, with data referring to 1,115 Rossmann stores.
	
  	**Features available in the dataset:**	  
	
   | Feature                          | Description |
   | ---                              | --- |
   | Store                            | A unique Id for each store |
   | DayOfWeek                        | Day of the week (1 = Monday, 7 = Sunday)  |
   | Date                             | Date of each sale  |
   | Sales                            | The turnover for any given day (this is what you are predicting) |
   | Customers                        | The number of customers on a given day |
   | Open                             | An indicator for whether the store was open: 0 = closed, 1 = open |
   | StateHoliday                     | Indicates a state holiday. Normally all stores, with few exceptions, are closed on state holidays. Note that all schools are closed on public holidays and weekends. a = public holiday, b = Easter holiday, c = Christmas, 0 = None |
   | SchoolHoliday                    | Indicates if the (Store, Date) was affected by the closure of public schools |
   | StoreType                        | Differentiates between 4 different store models: a, b, c, d |
   | Assortment                       | Describes an assortment level: a = basic, b = extra, c = extended |
   | CompetitionDistance              | Distance in meters to the nearest competitor store |
   | CompetitionOpenSinceMonth        | Gives the approximate month of the time the nearest competitor was opened |
   | CompetitionOpenSinceYear         | Gives the approximate year the nearest competitor was opened |
   | Promo                            | Indicates whether a store is running a promo on that day |
   | Promo2                           | Promo2 is a continuing and consecutive promotion for some stores: 0 = store is not participating, 1 = store is participating |
   | Promo2Since[Year/Week]           | Describes the year and calendar week when the store started participating in Promo2 |
   | PromoInterval                    | Describes the consecutive intervals Promo2 is started, naming the months the promotion is started anew. E.g. "Feb,May,Aug,Nov" means each round starts in February, May, August, November of any given year for that store |
		
2. **Solution Plan:** After understanding the reason for the CFO to request the accumulated revenue per store for the next 6 weeks, an end-to-end sales forecast project was agreed to be carried out in order to understand the behavior of the features provided, obtain future sales of the stores through a regression machine learning model and display the results in a simple and fast way through a messaging application, where the stakeholder provides the store id and the application returns the estimated sales prediction of the store for the next 6 weeks.

### Data Understanding & Data Preparation

3. **Data Cleaning & Data Description:** At this stage, the dimensions of the data were verified; data cleaning was performed: renaming columns, changing types to the correct format, analyzing and replacing missing data. A descriptive statistical analysis is also carried out to get an initial idea of the data and identify possible errors.

4. **Feature Engineering:** At this stage, a mind-map was created to model the phenomenon(sales) and 12 business hypotheses were generated to be validated in the future. Based on the generated hypotheses, features from the original dataset were derived to support the analysis and learning of the model, which will be carried out in the next phases.

5. **Variable Filtering:** At this stage, the data referring to the days that the stores were closed and/or had no sales were removed; and also removed the columns that are not relevant because we have derived other features from them and the column 'customers' which contains information that we won't have in the production environment.

6. **Exploratory Data Analysis (EDA):** At this stage, three types of analysis were performed in order to better understand the available data.
	* **Univariate analysis:** carried out in order to understand the individual behavior of each variable.
	* **Bivariate analysis:** carried out in order to understand the relationship between the independent variables with the dependent variable which is 'sales' and to validate the business hypotheses raised in the previous step.
	* **Multivariate Analysis:** carried out in order to understand the correlation between all dataset variables.
	
7. **Data Preprocessing:** At this stage, the preparation of data for future application in machine learning algorithms was performed. The objective is to adjust the data without losing the information content in order to facilitate its understanding by machine learning algorithms.
	* **Numerical variables:**
		* **Transformation:** applied the logarithmic transformation on the response variable(sales) to bring its distribution closer to a Gaussian distribution.	
		* **Rescaling:** MinMax Scaler and Robust Scaler was applied to time-related variables that do not follow a cyclical nature and a variable that contains a distance in meters.
		* **Nature Transformation:** the sine and cosine of the variables with information related to the passage of time were extracted, so that their cyclical nature can be better interpreted by the model.

	* **Categorical variables:**
		 * **Encoding:** Ordinal Encoding is applied to variables that follow an order; Label Encoding on variables that don't follow an order; and One Hot Encoding on variables that represent a state and affect all other variables in the dataset.
		 
8. **Feature Selection:** In this step, a feature selection algorithm called Boruta was applied, along with a random forest, and which uses the selection by subset (Wrapper method) as a criterion, which adds feature by feature, training the model and applying it to check if the accuracy increases or decreases, selecting only features that have an increase in model accuracy. 


### Modeling
9. **Machine Learning Algorithms:** In this step, we train five Machine Learning models to compare the results. The first was an averaging model to be used as a baseline; the second and third were a linear regression and a regularized linear regression(lasso) with the objective of measuring the complexity of the phenomenon we are modeling (the worse the result, the more complex the phenomenon); the fourth and fifth model were a Random Forest Regressor and a XGBoost Regressor, which are more sophisticated models and obtain better results in more complex phenomena.
	
	**ML Results:**
	
	![RossmannCVPerformance](https://user-images.githubusercontent.com/85720162/137336387-d584f99e-b5d7-4a43-afd0-b36be1047fb5.png)


	* **Cross-Validation:** technique applied to the training dataset to verify if the results initially obtained are in fact the real ones, or if the validation data were positively or negatively biased. The technique consists of dividing several parts of the dataset between training and validation (following the chronological order of the data) and performing the prediction several times in order to find the average of the predictions that would be the real result of the model.
	**Cross-Validation Results:**
	
		![RossmannCVPerformance](https://user-images.githubusercontent.com/85720162/137337535-ba393661-0449-43a6-b185-ca3b3ba187d9.png)
		
		Although random forest initially presented a better result, the model chosen to be used was xgboost because it presented a very similar performance after the HP fine tuning step, in addition to training the model faster and having a much smaller final size compared to random forest.
	
10. **Hyperparameter Fine Tuning:** In this step, we look for the best parameters to obtain an even better performance from the model that was chosen in the previous step. To obtain these parameters, an optimization method called Random Search was applied, which randomly tested a set of parameters that were passed to it and returned the set of parameters that presented the best result.
	
	**Final Results:**
	
	![RFR](https://user-images.githubusercontent.com/85720162/137791145-cbbb4f7d-eb92-4382-97c3-ba467c490233.png)

	
###	Evaluation

11. **Performance:**
	* **Financial Results:** At this stage, the transformation of the model result to a business result was carried out. For a better understanding of the model's financial results, the sum of the total predictions of all stores was performed and the best and worst scenarios were created according to the mean absolute percentage error(MAPE) of 10% displayed in the model results of the Hyperparameter Fine Tuning step.
	
		![RossmannPredictionScenarios](https://user-images.githubusercontent.com/85720162/137360461-44e22044-65ad-4252-a872-bbb94e174c7a.png)
	
	* **Machine Learning Performance:** As can be seen from the image below, the model predictions are very close to the real data, which shows us a very accurate result of the algorithm. Further analysis of the model's performance is available on the notebook in the Translation and Error Interpretation section.

		![ModelPerformance](https://user-images.githubusercontent.com/85720162/137546021-b1ee6264-e5a4-4dfe-b26b-23286d504452.png)


###	Deploy
12. **Deploy Model to Production:** To publish the model in production following the initial objective of being an application with easy and quick access, a bot was developed in the telegram that the user informs the ID of the store that wants to view the sales forecast and a cloud in Heroku is loaded containing the APIs that will receive this information and load the necessary data to carry out the application of the machine learning model and return the result to the user. Below is a flowchart of the operation with the steps of this process:


	![Flowchart - Frame 1 (2)](https://user-images.githubusercontent.com/85720162/137370090-71ec9e36-cb3f-48ed-ab81-ef7b5c82b7b3.jpg)

<p align="center">
Rossmann Bot
</p>

<p align="center">
 	<img width="350" alt="drawing" src="img/telegram_bot.gif">
</p>

<p align="center">
To access a store's sales forecast, start a Telegram conversation with RossmanBot @rossmann_sales_prediction_bot and enter the store id.
</p>

* **Next Steps:** For the next CRISP cycle, we can make several improvements to the project:

	- Develop a secondary project to forecast the number of customers in the store in the next six weeks and use the model output as input in this sales forecast project.
	- Map more features that impact the business through a more accurate mental map and raise and validate more business hypothesis to generate actionable insights for the business team. 
	- Test different machine learning algorithms to get more accurate results.
	- Use a more sophisticated hyperparameter fine tuning technique.
	- Optimize the bot on the telegram to provide more information to the user.

* **Learns:** This was the first data science project I did and I can say that the lessons learned were immense. The development of all stages of the project in an organized and structured way, from the initial understanding of the problem to training the model, interpreting the results and publishing it in production, added a lot to my knowledge in the area and in my ability to develop projects in such a way structured. All the analyzes carried out contributed a lot to my understanding of the sales phenomenon in a chain of stores, which can be very useful in future analyzes in several areas. 
