## ROSSMANN: A SALES FORECAST PROJECT
![Rossmann_Logo](https://user-images.githubusercontent.com/85720162/137200378-8aea0b70-b41a-451e-a255-d2f21333904f.png)

------------------------------------------------------------------
## About the Project

## About the Company
Dirk Rossmann GmbH (usual: Rossmann) is one of the largest drug store chains in Europe with around 56.300 employees and a total of 4.244 stores, including 2.233 in Germany. In 2020, the Rossmann Group achieved sales of €10,35 billion turnover in Germany, Poland, Hungary, the Czech Republic, Turkey, Albania, Kosovo and Spain.

The company was founded by Dirk Rossmann[4] with its headquarters in Burgwedel near Hanover in Germany. The Rossmann family owns 60%, and the Hong Kong-based A.S. Watson Group 40% of the company.

The product range includes up to 21,700 items and can vary depending on the size of the shop and the location.

## Project Structure
### Bussiness Understanding
* **Bussiness Problem:** Rossmann's CFO recently asked store managers for a projection of the next six weeks of sales, as based on this information, he intends to define the investment that will be made in the renovation of each store. Given the requested information and the lack of accurate response from store managers, the data science team suggested the development of a solution to this problem, prioritizing the quality of information and ease of access by the stakeholder.

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
* **Data Cleaning & Data Description**
* **Feature Engineering**
* **Exploratory Data Analysis (EDA)**
* **Data Preprocessig**
* **Feature Selection**

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
