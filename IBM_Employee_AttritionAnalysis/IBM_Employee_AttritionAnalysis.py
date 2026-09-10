# 1 --------> Business Problem

# Objective:
# Identify patterns related to employee attrition and provide
# business recommendations that may help reduce employee turnover.


# 2 --------> Loading Data

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("WA_Fn-UseC_-HR-Employee-Attrition.csv")


# 3 --------> Data Understanding

df.head()
df.info()
df.shape
df.columns


print("----------------------------------------------------------------------------")

# 4 --------> Data Cleaning

# 5 --------> Exploratory Data Analysis

   # Univariate Analysis

         # Age                                         # To see all the values
                                                       # Most of employees are between 30-40 y.o 
sns.histplot(df["Age"], bins = 20)
plt.title("Age Distribution")
plt.show()

         # Monthly Income                               # Box Plot to see outliers, mean values, dispersion values
                                                        # 
sns.boxplot(x=df["MonthlyIncome"])
plt.title("Monthly Income Distribution")
plt.show()











   # What is the overall attrition rate?

print(df["Attrition"].value_counts(normalize = True) * 100)           # Approximatly 16% of employees left the company || This indicates that employee attrition is a significant business issue
print("----------------------------------------------------------------------------")

   # Which department has the highest attrition                       # Sales ---> because has more % of "Yes" (20.63%), 
   #                                                                               folloewd by HR (19.05%), R&D has (13.84%).
print(pd.crosstab(df["Department"],df["Attrition"], normalize = "index")*100)
print("----------------------------------------------------------------------------")

   # Does overtime affect attrition                                    # In the cases that employees do overtime 54% of them get attrition
   #                                                                     and in the cases that employees do not overtime 23% of them get attrition
print(pd.crosstab(df["Attrition"],df["OverTime"], normalize = "index")*100)
print("----------------------------------------------------------------------------")


   # Do employees who leave earn less money?                            # Relate the mean value for monthly income, the employees who left 
   #                                                                     the company earn less money 
print(df.groupby("Attrition")["MonthlyIncome"].mean())
print("----------------------------------------------------------------------------")

   #Are younger employees more likely to leave?                          # Yes, the mean age value that is associated to the "Yes" is lower than 
   #                                                                       the "No" mean age value
print(df.groupby("Attrition")["Age"].mean())
print("----------------------------------------------------------------------------")


   #Does job satisfaction affect attrition?                              #  
   #                                                                       
print(df.groupby("Attrition")["JobSatisfaction"].mean())
print("----------------------------------------------------------------------------")

   # Which role as the highest attrition?                                # Sales Executive
   #
print(pd.crosstab(df["Attrition"],df["JobRole"]))
print("----------------------------------------------------------------------------")

   # Does distance from home affect attrition?                           #
   #
print(df.groupby("Attrition")["DistanceFromHome"].mean())
print("----------------------------------------------------------------------------")


# 6 --------> Attrition Analysis Visualizations

   # Attrition vs Salary
sns.boxplot(data=df, x="Attrition", y ="MonthlyIncome")
plt.show()

   # Attrition vs Age
sns.boxplot(data=df,x="Attrition",y="Age")
plt.show()

   # Attrition vs OverTime
sns.countplot(data=df, x="OverTime", hue="Attrition")
plt.show()

   # Heatmap
df["Attrition_Flag"] = df["Attrition"].map({"No":0,"Yes":1})

corr = df.corr(numeric_only=True)
corr["Attrition_Flag"].sort_values()

plt.figure(figsize=(15,10))

sns.heatmap(df.corr(numeric_only=True),cmap="RdYlGn")
plt.show()



# Correlation Findings:

# OverTime shows one of the strongest positive
# relationships with Attrition.

# Age shows a negative relationship with Attrition,
# suggesting younger employees are more likely to leave.


# 7 --------> Visualizations


# 8 --------> Key Findings

      # 1. Attrition rate is approximately 16%.

      # 2. Sales department shows the highest attrition rate.

      # 3. Employees working overtime are significantly more likely to leave.

      # 4. Employees who leave tend to be younger.

      # 5. Employees who leave generally earn lower salaries.

      # 6. Research & Development has the lowest attrition rate.



# 9 --------> Business Recommendations


      # 1. Review overtime policies.

      # 2. Improve retention efforts in Sales.

      # 3. Create development plans for younger employees.

      # 4. Review compensation for lower salary groups.

      # 5. Monitor employee satisfaction regularly.