# Medical_Insurance.mi
Predicting medical insurance charges using Linear Regression. This project cleans and analyzes the Insurance dataset, visualizes trends, and builds a Linear Regression model to estimate healthcare costs based on age, BMI, and smoking habits.
📁 Dataset

The dataset used is insurance.csv, which contains:

age — Age of the individual

sex — Gender

bmi — Body Mass Index

children — Number of children/dependents

smoker — Smoking status

region — Residential region

charges — Medical insurance cost

⚙️ Project Workflow

Data Loading & Exploration

Load dataset using Pandas

Check info, summary statistics, and correlations

Data Visualization

Visualized distributions and outliers using Seaborn and Matplotlib

Data Cleaning

Removed outliers in BMI using IQR method

Encoded categorical variables using pd.get_dummies()

Model Building

Selected key features (age, bmi, smoker_yes)

Trained a Linear Regression model

Model Evaluation

Evaluated using R² Score and Mean Squared Error (MSE)
