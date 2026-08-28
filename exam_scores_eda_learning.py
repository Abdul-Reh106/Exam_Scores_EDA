import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("Libraries imported successfully!")

df = pd.read_csv("07_exam_scores.csv")

print(df)
print("Shape of dataset:", df.shape)
print("\nColumn names:")
print(df.columns)
print("\nData types:")
print(df.dtypes)

print("\nBasic statistics:")
print(df.describe())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nRows with missing values:")
print(df[df.isnull().any(axis=1)])

print("\nMedian values:")
print(df.median(numeric_only=True))

df["math_score"] = df["math_score"].fillna(df["math_score"].median())
df["science_score"] = df["science_score"].fillna(df["science_score"].median())
df["english_score"] = df["english_score"].fillna(df["english_score"].median())
df["study_hours"] = df["study_hours"].fillna(df["study_hours"].median())

print("\nMissing values after cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df[df.duplicated()])

df = df.drop_duplicates()

print("\nDuplicate rows after cleaning:")
print(df.duplicated().sum())
print("\nMinimum values:")
print(df[["math_score", "science_score", "english_score", "final_score"]].min())

print("\nMaximum values:")
print(df[["math_score", "science_score", "english_score", "final_score"]].max())

print("\nInvalid math scores:")
print(df[(df["math_score"] < 0) | (df["math_score"] > 100)])

print("\nInvalid science scores:")
print(df[(df["science_score"] < 0) | (df["science_score"] > 100)])

print("\nInvalid english scores:")
print(df[(df["english_score"] < 0) | (df["english_score"] > 100)])

print("\nInvalid final scores:")
print(df[(df["final_score"] < 0) | (df["final_score"] > 100)])

print("\nInvalid study hours:")
print(df[df["study_hours"] < 0])

df.loc[(df["math_score"] < 0) | (df["math_score"] > 100), "math_score"] = df["math_score"].median()

df.loc[(df["science_score"] < 0) | (df["science_score"] > 100), "science_score"] = df["science_score"].median()

df.loc[(df["english_score"] < 0) | (df["english_score"] > 100), "english_score"] = df["english_score"].median()

df.loc[(df["final_score"] < 0) | (df["final_score"] > 100), "final_score"] = df["final_score"].median()

df.loc[df["study_hours"] < 0, "study_hours"] = df["study_hours"].median()

print("\nMinimum values after cleaning:")
print(df[["math_score", "science_score", "english_score", "final_score", "study_hours"]].min())

print("\nMaximum values after cleaning:")
print(df[["math_score", "science_score", "english_score", "final_score", "study_hours"]].max())

print("\nFinal dataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nAverage scores:")
print(df[["math_score", "science_score", "english_score", "final_score"]].mean())

plt.figure(figsize=(8, 5))

sns.histplot(df["final_score"], bins=10, kde=True)

plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")

plt.show()

subject_means = df[["math_score", "science_score", "english_score"]].mean()

plt.figure(figsize=(8, 5))

sns.barplot(x=subject_means.index, y=subject_means.values)

plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")

plt.show()

plt.figure(figsize=(8, 5))

sns.scatterplot(x=df["study_hours"], y=df["final_score"])

plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")

plt.show()

correlation = df["study_hours"].corr(df["final_score"])

print("\nCorrelation between study hours and final score:")
print(correlation)

print("\nCorrelation matrix:")
print(df.corr(numeric_only=True))

plt.figure(figsize=(8, 6))

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Correlation Heatmap")

plt.show()

print("\nLowest final score:")
print(df["final_score"].min())

print("\nHighest final score:")
print(df["final_score"].max())

print("\nStudent with lowest final score:")
print(df.loc[df["final_score"].idxmin()])

print("\nStudent with highest final score:")
print(df.loc[df["final_score"].idxmax()])

df["study_group"] = pd.cut(
    df["study_hours"],
    bins=[0, 4, 8, 12],
    labels=["Low", "Medium", "High"]
)

print("\nAverage final score by study group:")
print(df.groupby("study_group", observed=True)["final_score"].mean())

study_group_means = df.groupby(
    "study_group", observed=True
)["final_score"].mean()

plt.figure(figsize=(8, 5))

sns.barplot(
    x=study_group_means.index,
    y=study_group_means.values
)

plt.title("Average Final Score by Study Group")
plt.xlabel("Study Group")
plt.ylabel("Average Final Score")

plt.show()

plt.figure(figsize=(8, 5))

sns.scatterplot(x=df["math_score"], y=df["final_score"])

plt.title("Math Score vs Final Score")
plt.xlabel("Math Score")
plt.ylabel("Final Score")

plt.show()

plt.figure(figsize=(8, 5))

sns.scatterplot(x=df["science_score"], y=df["final_score"])

plt.title("Science Score vs Final Score")
plt.xlabel("Science Score")
plt.ylabel("Final Score")

plt.show()

plt.figure(figsize=(8, 5))

sns.scatterplot(x=df["english_score"], y=df["final_score"])

plt.title("English Score vs Final Score")
plt.xlabel("English Score")
plt.ylabel("Final Score")

plt.show()

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df[["math_score", "science_score", "english_score", "final_score"]]
)

plt.title("Score Distribution")
plt.xlabel("Score Type")
plt.ylabel("Score")

plt.show()

print("\nStandard deviation:")
print(df[["math_score", "science_score", "english_score", "final_score"]].std())

Q1 = df["final_score"].quantile(0.25)
Q3 = df["final_score"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print("\nFinal Score IQR:")
print(IQR)

print("\nLower bound:")
print(lower_bound)

print("\nUpper bound:")
print(upper_bound)

outliers = df[
    (df["final_score"] < lower_bound) |
    (df["final_score"] > upper_bound)
]

print("\nFinal score outliers:")
print(outliers)

df["performance_level"] = pd.cut(
    df["final_score"],
    bins=[0, 40, 60, 80, 100],
    labels=["Poor", "Average", "Good", "Excellent"],
    include_lowest=True
)

print("\nPerformance level counts:")
print(df["performance_level"].value_counts().sort_index())

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="performance_level",
    order=["Poor", "Average", "Good", "Excellent"]
)

plt.title("Student Performance Levels")
plt.xlabel("Performance Level")
plt.ylabel("Number of Students")

plt.show()

performance_by_study = pd.crosstab(
    df["study_group"],
    df["performance_level"]
)

print("\nPerformance level by study group:")
print(performance_by_study)

performance_percentage = pd.crosstab(
    df["study_group"],
    df["performance_level"],
    normalize="index"
) * 100

print("\nPerformance percentage by study group:")
print(performance_percentage.round(2))

performance_percentage.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 6)
)

plt.title("Performance Levels by Study Group")
plt.xlabel("Study Group")
plt.ylabel("Percentage of Students")
plt.legend(title="Performance Level")

plt.show()