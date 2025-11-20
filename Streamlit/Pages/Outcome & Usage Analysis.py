# ==================== PAGE 5: OUTCOME & USAGE ANALYSIS ====================

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

st.title("Final Outcome & AI Usage Analysis")

outcome_by_used_pct = pd.crosstab(df['FinalOutcome'], df['UsedAgain'], normalize='index') * 100
        
st.subheader("Final Outcome by Used Again (Percentages)")
st.dataframe(outcome_by_used_pct.round(2).style.highlight_max(axis=1), use_container_width=True)
        
st.markdown("---")
        
col1, col2 = st.columns(2)
        
with col1:
    st.subheader("Stacked Bar Chart")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    outcome_by_used_pct.plot(kind='bar', stacked=True, ax=ax1, color=['#e74c3c', '#2ecc71'])
    ax1.set_title('Final Outcome by Used Again', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Final Outcome')
    ax1.set_ylabel('Percentage (%)')
    ax1.legend(title='Used Again', labels=['No', 'Yes'])
    ax1.tick_params(axis='x', rotation=45)
    ax1.set_ylim(0, 100)
    ax1.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig1)
        
with col2:
    st.subheader("Likelihood of Using AI Again")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
            
    sns.barplot(x='FinalOutcome', y='UsedAgain', data=df, estimator='mean', errorbar=None, palette=["#36A2EB", "#FF6384", "#FFCE56", "#4BC0C0"], ax=ax2)
            
    for bar in ax2.patches:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f'{yval:.2f}', ha='center', va='bottom', fontsize=10)
            
    ax2.set_title('Likelihood of Using AI Tool Again by Session Outcome', fontweight='bold')
    ax2.set_ylabel('Proportion who would use again')
    ax2.set_xlabel('Session Outcome')
    ax2.set_ylim(0, 1.1)
    plt.tight_layout()
    st.pyplot(fig2)