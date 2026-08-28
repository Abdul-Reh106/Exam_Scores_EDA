import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. LOAD DATASET
df = pd.read_csv("07_exam_scores.csv")

# 2. BASIC DATASET INFORMATION
print("Dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nData types:")
print(df.dtypes)
print("\nBasic statistics:")
print(df.describe())

# 3. DATA CLEANING
# Check missing values
print("\nMissing values before cleaning:")
print(df.isnull().sum())

# Handle missing values using median
missing_value_columns = [
    "math_score",
    "science_score",
    "english_score",
    "study_hours"
]
for column in missing_value_columns:
    df[column] = df[column].fillna(df[column].median())

# Remove duplicate rows
df = df.drop_duplicates()

# Handle invalid score values
score_columns = [
    "math_score",
    "science_score",
    "english_score",
    "final_score"
]
for column in score_columns:
    invalid = (df[column] < 0) | (df[column] > 100)
    df.loc[invalid, column] = df[column].median()
    
# Replace negative study hours with median
df.loc[df["study_hours"] < 0, "study_hours"] = (
    df["study_hours"].median()
)

# 4. VERIFY DATA CLEANING
print("\nDataset after cleaning:")
print("Shape:", df.shape)
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
print("\nMinimum values:")
print(df.min())
print("\nMaximum values:")
print(df.max())

# 5. EXPLORATORY DATA ANALYSIS
print("\nAverage scores:")
print(
    df[
        [
            "math_score",
            "science_score",
            "english_score",
            "final_score"
        ]
    ].mean()
)

# 6. FINAL SCORE DISTRIBUTION
plt.figure(figsize=(8, 5))
sns.histplot(
    df["final_score"],
    bins=10,
    kde=True
)
plt.title("Distribution of Final Scores")
plt.xlabel("Final Score")
plt.ylabel("Number of Students")
plt.savefig(
    "screenshots/final_score_distribution.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# 7. AVERAGE SCORE BY SUBJECT
subject_means = df[
    ["math_score", "science_score", "english_score"]
].mean()
plt.figure(figsize=(8, 5))
sns.barplot(
    x=subject_means.index,
    y=subject_means.values
)
plt.title("Average Score by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.savefig(
    "screenshots/average_score_by_subject.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# 8. STUDY HOURS VS FINAL SCORE
plt.figure(figsize=(8, 5))
sns.scatterplot(
    x=df["study_hours"],
    y=df["final_score"]
)
plt.title("Study Hours vs Final Score")
plt.xlabel("Study Hours")
plt.ylabel("Final Score")
plt.savefig(
    "screenshots/study_hours_vs_final_score.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# Correlation between study hours and final score
correlation = df["study_hours"].corr(
    df["final_score"]
)
print("\nCorrelation between study hours and final score:")
print(round(correlation, 3))

# 9. CORRELATION ANALYSIS
correlation_matrix = df.corr(
    numeric_only=True
)
print("\nCorrelation matrix:")
print(correlation_matrix)

# Correlation heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.savefig(
    "screenshots/correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# 10. HIGHEST AND LOWEST PERFORMERS
print("\nLowest final score:")
print(df["final_score"].min())
print("\nHighest final score:")
print(df["final_score"].max())
print("\nStudent with lowest final score:")
print(
    df.loc[df["final_score"].idxmin()]
)
print("\nStudent with highest final score:")
print(
    df.loc[df["final_score"].idxmax()]
)

# 11. STUDY GROUPS
df["study_group"] = pd.cut(
    df["study_hours"],
    bins=[0, 4, 8, 12],
    labels=["Low", "Medium", "High"]
)
print("\nAverage final score by study group:")
study_group_means = df.groupby(
    "study_group",
    observed=True
)["final_score"].mean()
print(study_group_means)

# Average final score by study group
plt.figure(figsize=(8, 5))
sns.barplot(
    x=study_group_means.index,
    y=study_group_means.values
)
plt.title("Average Final Score by Study Group")
plt.xlabel("Study Group")
plt.ylabel("Average Final Score")
plt.savefig(
    "screenshots/average_final_score_by_study_group.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# 12. PERFORMANCE LEVELS
df["performance_level"] = pd.cut(
    df["final_score"],
    bins=[0, 40, 60, 80, 100],
    labels=[
        "Poor",
        "Average",
        "Good",
        "Excellent"
    ],
    include_lowest=True
)
print("\nPerformance level counts:")
print(
    df["performance_level"]
    .value_counts()
    .sort_index()
)

# Performance level distribution
plt.figure(figsize=(8, 5))
sns.countplot(
    data=df,
    x="performance_level",
    order=[
        "Poor",
        "Average",
        "Good",
        "Excellent"
    ]
)
plt.title("Student Performance Levels")
plt.xlabel("Performance Level")
plt.ylabel("Number of Students")
plt.savefig(
    "screenshots/performance_levels.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# 13. PERFORMANCE VS STUDY GROUP
performance_by_study = pd.crosstab(
    df["study_group"],
    df["performance_level"]
)
print("\nPerformance level by study group:")
print(performance_by_study)

# Calculate percentages
performance_percentage = pd.crosstab(
    df["study_group"],
    df["performance_level"],
    normalize="index"
) * 100
print("\nPerformance percentage by study group:")
print(
    performance_percentage.round(2)
)

# Performance levels by study group
performance_percentage.plot(
    kind="bar",
    stacked=True,
    figsize=(9, 6)
)
plt.title("Performance Levels by Study Group")
plt.xlabel("Study Group")
plt.ylabel("Percentage of Students")
plt.legend(
    title="Performance Level"
)
plt.savefig(
    "screenshots/performance_levels_by_study_group.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

# 14. SAVE CLEANED DATASET
df.to_csv(
    "07_exam_scores_cleaned.csv",
    index=False
)
print("\nCleaned dataset saved successfully.")