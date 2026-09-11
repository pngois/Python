import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
os.makedirs("images", exist_ok=True)


# 1. Importing data

df  = sns.load_dataset('titanic')
print(f"Loaded Dataset: {df.shape[0]} rows, {df.shape[1]} columns")



# 2. Initial Info
print(df.head())
df.info()
print(df.describe())
print("==========================================")

# Put all the columns without blank spaces, with lower case letters
df.columns = df.columns.str.strip().str.lower().str.replace(" ","_")

print("FIX APPLIED")
print(df.columns.tolist())


# 3.Univariable & Multivariable Analysis

    # Age Distribution                There are missing values bc total values are 891 and the age's value is 714
print(df["age"].describe())
print("==========================================")

    # Number of males & females on board
print(df["sex"].value_counts(normalize=True))
print("==========================================")

    # Passengers per class
print(df["class"].value_counts(normalize=True))
print("==========================================")

    # Average ticket price per class
print(df.groupby("class")["fare"].value_counts(normalize=True))
print("==========================================")


    # Survival Ratio 
print("Survive Ratio=",df["survived"].value_counts(normalize= True))
print("==========================================")

    # Survival Ratio per class 
print(df.groupby("class")["survived"].value_counts(normalize= True))
print("==========================================")

    # Survival Ratio per gender 
print(df.groupby("sex")["survived"].value_counts(normalize= True))
print("==========================================")

    # Survival Ratio per age 
                                                    
df["age_group"] = pd.cut(df["age"], bins = [0, 12, 18, 60, 100], labels=["child","teenager","adult","old"])
print(df.groupby("age_group", observed= True)["survived"].mean())
print("==========================================")

    # Survival Ratio "Alone vs w/ Family"
print(df.groupby("alone")["survived"].mean())
print("==========================================")

    # Survival Ratio per Class & Gender (avg)
print(df.groupby(["sex","class"], observed=True)["survived"].value_counts(normalize=True))
print("==========================================")

    # Embark Town
print(df.groupby("embark_town")["survived"].mean())
print("==========================================")

    # Ticket Price & survive correlation
print(df[["survived","age","fare","pclass"]].corr())
print("==========================================")

# 4.Visualization


    # Survive per class
df.groupby("class")["survived"].mean().plot(kind="bar", color=["gold","silver","brown"])
plt.title("Survival Ratio per Class")
plt.ylabel("Survival Ratio")
plt.xticks(rotation=0)
plt.savefig("images/survival_by_class.png")
plt.show()

    # Survival Ratio per Class & Gender (avg)
sns.barplot(data=df,x="class", y="survived",hue="sex")
plt.title("Survival Ratio per Class & Gender")
plt.ylabel("Survival Ratio")
plt.savefig("images/survival_by_class_gender.png")
plt.show()

    # Correlation heatmap                                   annot --> number in the cells; 
    #                                                       cmap --> red to positive correlation & blue to positive correlation
sns.heatmap(df[["survived","age","fare","pclass"]].corr(), annot=True, cmap="coolwarm")
plt.title("Correlação entre Variáveis")
plt.savefig("images/correlation_heatmap.png")
plt.show()