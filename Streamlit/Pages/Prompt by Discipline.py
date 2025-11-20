# ==================== PAGE 2: PROMPTS BY DISCIPLINE ====================
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np


st.set_page_config(page_title="Dataset Analysis Dashboard") #page title

sns.set(style="whitegrid", context="talk") #seaborn - visual appearance of plots

#store dataset in cache, to prevent rerunning func
@st.cache_data
def load_data():
    df = pd.read_csv('updated_cleaned_dataset1.csv') #cleaned dataset
    return df

#calling function
df = load_data()

st.title("Average Prompts Used by Discipline")
    
prompts_by_discipline = df.groupby('Discipline')['TotalPrompts'].mean() #first group by discipline, selects totalprompt colum from each group, then calculage average of each
max_prompts_discipline = prompts_by_discipline.idxmax() #looks at previous table and index label that has the highest value - returns index i.e comp sci
max_prompts_value = prompts_by_discipline.max()
        
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Highest Discipline", max_prompts_discipline)
with col2:
    st.metric("Average Prompts", f"{max_prompts_value:.2f}")
with col3:
    st.metric("Lowest Prompts", f"{prompts_by_discipline.min():.2f}")
        
st.markdown("---")
        
col1, col2 = st.columns(2)
        
with col1: #created a pie chart
    st.subheader("Distribution - Pie Chart")
    explode = [0.1 if discipline == max_prompts_discipline else 0 
                      for discipline in prompts_by_discipline.index]
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    colors = ["#36A2EB","#FF6384", "#FFCE56", "#4BC0C0", "#9966FF"]
            
    ax1.pie(prompts_by_discipline,
            labels=prompts_by_discipline.index, 
            autopct='%1.2f%%', 
            explode=explode,
            colors=colors[:len(prompts_by_discipline)], 
            startangle=90, #rotates startin position to start at 12 o'clock (top)
            textprops={'fontsize': 11})
            
    ax1.set_title('Distribution of Prompts by Discipline', fontweight='bold')
    plt.tight_layout() # adjust subplot layout to avoid overlapping labels, title
    st.pyplot(fig1)
        
with col2: # create a bar chart
    st.subheader("Comparison - Bar Chart")
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    bars = ax2.bar(prompts_by_discipline.index, prompts_by_discipline.values,
                   color=colors[:len(prompts_by_discipline)])
    ax2.set_xlabel('Discipline', fontweight='bold')
    ax2.set_ylabel('Average Prompts', fontweight='bold')
    ax2.set_title('Average Prompts by Discipline', fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig2)
        
st.markdown("---")
        
st.subheader("Detailed Statistics")
stats_df = pd.DataFrame({
    'Discipline': prompts_by_discipline.index,
    'Average Prompts': prompts_by_discipline.values
})#create df that shows avg prompts of each display
        
st.dataframe(stats_df
             .style
             .highlight_max(subset=['Average Prompts'], color='yellow')
             .highlight_min(subset=['Average Prompts'], color='#ffcccc')
        )# highlights the max and min value

st.markdown("---")
st.header("Insight")
st.write("What we learned from this analysis was: People in the Computer Science discipline see the most used of prompts")
