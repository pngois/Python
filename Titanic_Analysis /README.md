# Titanic Survival Analysis

Exploratory data analysis (EDA) of the Titanic dataset, using pandas, seaborn and matplotlib.

## Objective
Explore the factors that influenced passenger survival — class, gender, age, and whether they traveled alone or with family.

## Data source
This project uses the [Titanic dataset from Kaggle](https://www.kaggle.com/datasets/yasserh/titanic-dataset), a classic dataset with passenger information from the RMS Titanic (891 records, 15 columns). 
In code, it's loaded via seaborn's built-in copy of the same dataset (`sns.load_dataset('titanic')`), so no manual download is required to run this project.

## Questions answered
- What was the overall survival rate, by class and by gender?
- Did age influence survival?
- Did traveling alone vs. with family make a difference?
- Is there a correlation between ticket fare and survival?

## Key findings
- *( "Women had a survival rate of 74%, men of 19%")*
- *( "1st class had 63% survival rate, 3rd class 24%")*
- *( "Even within the same gender, class made a difference of 47 percentage points")*

## Charts
![Survival by class](images/survival_by_class.png)
![Survival by class and gender](images/survival_by_class_gender.png)
![Correlation heatmap](images/correlation_heatmap.png)

## How to run
​```bash
pip install -r requirements.txt
python analysis_titanic.py
​```




