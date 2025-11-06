import matplotlib.pyplot as plt
import pandas as pd

# Load dataset and limit to 500 rows
df = pd.read_csv('updated_cleaned_dataset1.csv').head(500)

# Group by Discipline and calculate mean SessionLengthMin
#session_length_by_discipline = df.groupby('Discipline')['SessionLengthMin'].mean()
#max_discipline = session_length_by_discipline.idxmax()
#max_session_length = session_length_by_discipline.max()

# Print the discipline with the highest average session length
#print(f"The discipline with the highest average session length is '{max_discipline}' "
      #f"with an average of {max_session_length:.2f} minutes.")

# Calculate mean TotalPromptsUsed by Discipline for the pie chart
prompts_by_discipline = df.groupby('Discipline')['TotalPrompts'].mean()

# Find the discipline with the highest average prompts (highest percentage)
max_prompts_discipline = prompts_by_discipline.idxmax()

# Create explode array - explode only the highest value
explode = [0.1 if discipline == max_prompts_discipline else 0 for discipline in prompts_by_discipline.index]

# Create pie chart
plt.figure(figsize=(8, 6))
plt.pie(prompts_by_discipline, labels=prompts_by_discipline.index, 
        autopct='%1.2f%%', 
        explode=explode,  # Add explode parameter
        colors=["#36A2EB", "#FF6384", "#FFCE56", "#4BC0C0", "#9966FF"], 
        startangle=90, textprops={'fontsize': 10})
plt.title('Average Number of Prompts Used by Discipline')
plt.tight_layout()  # Adjust layout to prevent label cutoff
plt.savefig('prompts_by_discipline_piechart.png')  # Save the plot
plt.show()
