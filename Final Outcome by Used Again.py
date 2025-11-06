import pandas as pd
import matplotlib.pyplot as plt

# Load updated cleaned dataset
data_set = pd.read_csv("updated_cleaned_dataset1.csv")

# Calculate percentages
outcome_by_used_pct = pd.crosstab(data_set['FinalOutcome'], data_set['UsedAgain'], normalize='index') * 100

print("\n=== FinalOutcome by UsedAgain (Percentages) ===")
print(outcome_by_used_pct.round(2))

# Create chart
fig, ax = plt.subplots(figsize=(10, 6))

outcome_by_used_pct.plot(
    kind='bar', stacked=True, ax=ax, color=['#e74c3c', '#2ecc71']
)
ax.set_title('Final Outcome by Used Again', fontsize=14, fontweight='bold')
ax.set_xlabel('Final Outcome')
ax.set_ylabel('Percentage (%)')
ax.legend(title='Used Again', labels=['No', 'Yes'])
ax.tick_params(axis='x', rotation=45)
ax.set_ylim(0, 100)
ax.grid(axis='y', alpha=0.3)

plt.tight_layout()
plt.savefig('outcome_by_used_again.png', dpi=300, bbox_inches='tight')
print("\nChart saved to outcome_by_used_again.png")
plt.show()
