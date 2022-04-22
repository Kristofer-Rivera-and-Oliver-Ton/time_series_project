# TIME SERIES PROJECT - SUPERSTORE -
Team Members: Kristofer Rivera & Oliver Ton -- April 2022
 
===
 
Table of Contents
---
 
* I. [Project Overview](#i-project-overview)<br>
[1. Goals](#1-goal)<br>
[2. Description](#2-description)<br>
[3. Initial Questions](#3initial-questions)<br>
[4. Deliverables](#4-deliverables)<br>
* II. [Project Data Context](#ii-project-data-context)<br>
[1. Data Dictionary](#1-data-dictionary)<br>
* III. [Project Plan - Data Science Pipeline](#iii-project-plan---using-the-data-science-pipeline)<br>
[1. Project Planning](#1-plan)<br>
[2. Data Acquisition](#2-acquire)<br>
[3. Data Preparation](#3-prepare)<br>
[4. Data Exploration](#4explore)<br>
[5. Modeling & Evaluation](#5-model--evaluate)<br>
[6. Product Delivery](#6-delivery)<br>
* IV. [Project Modules](#iv-project-modules)<br>
* V. [Project Reproduction](#v-project-reproduction)<br>
 
 
 
## I. PROJECT OVERVIEW
 
 
#### 1.  GOAL:
The goal of this project is to provide the SuperStore VP of Product with a data-backed recommendation for which product line to expand on.  
 
 
#### 2. DESCRIPTION:
Superstore's mission is to be the preferred supplier of workspace solutions; from home-office to cooperate office, we aspire to be the leading expert in workplace solutions for everyone! For this reason, it is important to know whether we are reaching everyone with our products and services. 
This project will use exploratory analysis, time-series analysis and modeling to identify the best product category for Superstore to expand on. Based on sales and profitability, we will provide recommendations on where to shift our company focus in order to maintain happy loyal customers while continuing to grow our customer base.
 

#### 3.INITIAL QUESTIONS:
The focus of the project is identifying the best product category to expand on. Below are some of the initial questions this project looks to answer throughout the Data Science Pipeline.
 
#### Data-Focused Questions
1. Which product category is the most profitable?

2. Is there a category that stands out in terms of sales volume?

3. Does profitability and sales vary by customer segment?

4. How does the sales and volume and profit change over time? Are there specific times of the year where we see more profits or sales?

  
#### 4. DELIVERABLES:
- [x] README file - provides an overview of the project and steps for project reproduction
- [x] Draft Jupyter Notebook - provides all steps taken to produce the project
- [x] Report Jupyter Notebook - provides final presentation-ready wrangle, exploration and modeling
- [x] Slide Deck - 5-minute presentation to stakeholders (VP of Product)
 
 
## II. PROJECT DATA CONTEXT
 
#### 1. DATA DICTIONARY:
The final DataFrame used to explore the data for this project contains the following variables (columns).  The variables, along with their data types, are defined below:
 
 
|  Variables               |    Definition                                                |    DataType        |
| :--------------------:   | :----------------------------------------:                   | :---------------:  |
order_date (index)         |  Date order was placed                                       |  datetime64[ns]    |
ship_date                  |  Date order was shipped                                      |  datetime64[ns]    |
ship_mode                  |  Type of shipping                                            |  object            |
segment                    |  Type of customer                                            |  object            |
country                    |  Country to which shipment was delivered                     |  object            |
city                       |  City to which shipment was delivered                        |  object            |
state                      |  State to which shipment was delivered                       |  object            |
postal_code                |  Postal code to which shipment was delivered                 |  float64           |
sales                      |  Sale total for product id * quantity in given order ($USD)  |  float64           |
quantity                   |  Total number of specified product ordered                   |  float64           |
discount                   |  Percentage of discount applied to order in decimal form     |  float64           |
profit                     |  Sales Minus Product Cost                                    |  float64           |
customer_name              |  Name of customer                                            |  object            |
product_name               |  Name of product                                             |  object            |
category                   |  Category the product belongs to                             |  object            |
sub-category               |  Subcategory the product belongs to                          |  object            |
region_name                |  General area of US where order was placed                   |  object            |

* feature engineered
 
## III. PROJECT PLAN - USING THE DATA SCIENCE PIPELINE:
The following outlines the process taken through the Data Science Pipeline to complete this project. 
 
Plan➜ Acquire ➜ Prepare ➜ Explore ➜ Model & Evaluate ➜ Deliver
 
#### 1. PLAN
- [x]  Review project expectations
- [x]  Draft project goal to include measures of success
- [x]  Create questions related to the project
- [x]  Create questions related to the data
- [x]  Create a plan for completing the project using the data science pipeline
- [x]  Create a data dictionary to define variables and data context
 
#### 2. ACQUIRE
- [x]  Create .gitignore to store files and ensure the security of sensitive data
- [x]  Create env file with log-in credentials
- [x]  Create wrangle.py to store functions needed to acquire the Superstore dataset from Codeup database
- [x]  Ensure all imports needed to run the functions are inside the wrangle.py document
- [x]  Using Jupyter Notebook
     - [x]  Run all required imports
     - [x]  Import functions from wrangle.py module
     - [x]  Summarize dataset using methods and document observations
 
#### 3. PREPARE
Using Jupyter Notebook
- [x]  Import functions from wrangle.py module
- [x]  Summarize dataset using methods and document observations
- [x]  Clean data, rename columns, change datatypes
- [x]  Categorical features or discrete features need to be numbers that represent those categories
- [x]  Continuous features may need to be standardized to compare like datatypes
- [x]  Address missing values, data errors, unnecessary data
- [x]  Split data into train, validate, and test samples
Using Python Scripting Program (Jupyter Notebook)
- [x]  Create prepare function within wrangle.py
- [x]  Store functions needed to prepare the Superstore data such as:
   - [x]  Cleaning Function: to clean data for exploration
   - [x]  Encoding Function: to create datetime columns for order date and ship date columns and set order date as an index
   - [x]  Split Function: to split data into train, validate, and test
- [x]  Ensure all imports needed to run the functions are inside the wrangle.py document
 
#### 4.EXPLORE
Using Jupyter Notebook:
- [x]  Answer key questions and find the best category in regards to sales
     - [x]  Document findings
- [x]  Create visualizations with the intent to discover variable relationships
     - [x]  Identify variables related to catgory and sales
     - [x]  Identify any potential data integrity issues
- [x]  Summarize conclusions, provide clear answers, and summarize takeaways
     - [x] Explain plan of action as deduced from work to this point
 
#### 5. MODEL & EVALUATE
Using Jupyter Notebook:
- [x]  Train and fit multiple models with varying algorithms and/or hyperparameters
- [x]  Remove unnecessary features
- [x]  Evaluate best performing models using validate set
- [x]  Choose best performing validation model for use on test set
- [x]  Test final model on out-of-sample testing dataset
- [x]  Summarize performance
- [x]  Interpret and document findings
 
#### 6. DELIVERY
- [x]  Prepare a five-minute presentation 
     - [x]  Include an introduction of the project and goals
     - [x]  Provide an executive summary of findings, key takeaways, recommendations, and rationale
     - [x]  Create a walkthrough of the analysis 
     - [x]  Include presentation-worthy visualizations that support the problem and recommendation
     - [x]  Provide final takeaways, recommend a course of action, and next steps
     - [x]  Be prepared to answer questions following the presentation
- [x]  Prepare final notebook in Jupyter Notebook
     - [x]  Create clear walk-though of the Data Science Pipeline using headings and dividers
     - [x]  Explicitly define questions asked during the initial analysis
     - [x]  Visualize relationships
     - [x]  Document takeaways
     - [x]  Comment code thoroughly


## IV. PROJECT MODULES:
- [x] wrangle.py - provides reproducible python code to automate acquiring, preparing, and splitting the data
- [x] model.py - provides reproducible python code to automate create prophet machine learning algorithm
 
  
## V. PROJECT REPRODUCTION:
### Steps to Reproduce
 - [x] You will need an env.py file that contains the hostname, username, and password of the database that contains the superstore_db dataset
- [x] Store that env file locally in the repository
- [x] Make .gitignore and confirm .gitignore is hiding your env.py file
- [x] Clone our repo (including the wrangle.py, model.py)
- [x] Import python libraries:  pandas, matplotlib, seaborn, numpy, and prophet
- [x] Follow steps as outlined in the README.md. and draft notebooks
- [x] Run Final_Report.ipynb to view the final product
