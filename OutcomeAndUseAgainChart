import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('updated_cleaned_dataset.csv')

outcome_labels = {
    0: "Gave up",
    1: "Confused",
    2: "Idea drafted",
    3: "Assignment completed"
}

df['OutcomeLabel'] = df['FinalOutcome'].map(outcome_labels)

df['OutcomeLabel'] = pd.Categorical(
    df['OutcomeLabel'],
    categories=["Gave up", "Confused", "Idea drafted", "Assignment completed"],
    ordered=True
)

plt.figure(figsize=(8, 6))
sns.barplot(x = 'OutcomeLabel', y = 'UsedAgain', data = df, estimator = 'mean', errorbar = None)
plt.title('Likelihood of Using AI Tool Again by Session Outcome')
plt.ylabel('Proportion who would use again')
plt.xlabel('Session Outcome')
plt.ylim(0, 1)
plt.show()
