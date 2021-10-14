## ROSSMANN: A SALES FORECAST PROJECT
![Rossmann_Logo](https://user-images.githubusercontent.com/85720162/137200378-8aea0b70-b41a-451e-a255-d2f21333904f.png)

------------------------------------------------------------------
## About the Project

## About the Company
Dirk Rossmann GmbH (usual: Rossmann) is one of the largest drug store chains in Europe with around 56.300 employees and a total of 4.244 stores, including 2.233 in Germany. In 2020, the Rossmann Group achieved sales of €10,35 billion turnover in Germany, Poland, Hungary, the Czech Republic, Turkey, Albania, Kosovo and Spain.

The company was founded by Dirk Rossmann[4] with its headquarters in Burgwedel near Hanover in Germany. The Rossmann family owns 60%, and the Hong Kong-based A.S. Watson Group 40% of the company.

The product range includes up to 21,700 items and can vary depending on the size of the shop and the location.

## Project Structure
### Business Understanding
* **Business Problem:** Rossmann's CFO recently asked store managers for a projection of the next six weeks of sales, as based on this information, he intends to define the investment that will be made in the renovation of each store. Given the requested information and the lack of accurate response from store managers, the data science team suggested the development of a solution to this problem, prioritizing the quality of information and ease of access by the stakeholder.

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
		
* **Solution Plan:** After understanding the reason for the CFO to request the accumulated revenue per store for the next 6 weeks, an end-to-end sales forecast project was agreed to be carried out in order to understand the behavior of the features provided, obtain future sales of the stores through a regression machine learning model and display the results in a simple and fast way through a messaging application, where the stakeholder provides the store id and the application returns the estimated sales prediction of the store for the next 6 weeks.

### Data Understanding & Data Preparation

* **Data Cleaning & Data Description:** At this stage, the dimensions of the data were verified; data cleaning was performed: renaming columns, changing types to the correct format, analyzing and replacing NAs. A descriptive statistical analysis is also carried out to get an initial idea of the data and identify possible errors.

* **Feature Engineering:** At this stage, a mind-map was created to model the phenomenon(sales) and business hypotheses were generated to be validated in the future. Based on the generated hypotheses, features from the original dataset were derived to support the analysis and learning of the model, which will be carried out in the next phases.

* **Exploratory Data Analysis (EDA):** At this stage, three types of analysis were performed in order to better understand the available data.
	* **Univariate analysis:** carried out in order to understand the individual behavior of each variable.
	* **Bivariate analysis:** carried out in order to understand the relationship between the independent variables with the dependent variable, which is 'sales' and to validate the business hypotheses raised in the previous step.
	* **Multivariate Analysis:** carried out in order to understand the correlation between all dataset variables.
	
* **Data Preprocessing:** At this stage, the preparation of data for future application in machine learning algorithms was performed. The objective is to adjust the data without losing the information content in order to facilitate its understanding by machine learning algorithms.
	* **Numerical variables:**
		* **Transformation:** applied the log on the response variable(sales) to bring its distribution closer to a Gaussian distribution.				
		* **Rescaling:** applied to time-related variables that do not follow a cyclical nature and a variable that contains a distance in meters.
		* **Nature Transformation:** the sine and cosine of the variables with information related to the passage of time were extracted, so that their cyclical nature can be better interpreted by the model.

	* **Categorical variables:**
		 * **Encoding:** Ordinal Encoding is applied to variables that follow an order; Label Encoding on variables that don't follow an order; and One Hot Encoding on variables that represent a state and affect all other variables in the dataset.
		 
* **Feature Selection:** In this step, a feature selection algorithm called Boruta was applied, along with a random forest, and which uses the selection by subset (Wrapper method) as a criterion, which adds feature by feature, training the model and applying it to check if the accuracy increases or decreases, selecting only features that have an increase in model accuracy. 


### Modeling
* **Machine Learning Algorithms**
* **Cross-Validation**
* **Hyperparameter Fine Tuning**

###	Evaluation
* **Error Interpretation**
* **Bussiness Performance**

###	Deploy
* **Deploy Model to Production**
* **Telegram Bot**
