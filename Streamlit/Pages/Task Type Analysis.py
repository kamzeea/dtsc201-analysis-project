# ==================== PAGE 3: TASK TYPE ANALYSIS ====================
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

st.title("Task Type Analysis")

mean_by_task = df.groupby('TaskType').mean(numeric_only=True)[['SatisfactionRating', 'TotalPrompts']]
#groupby tasktype, includes columnwith numbers,checks avg, selects column

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Task Types", df['TaskType'].nunique())
with col2:
    st.metric("Most Common", df['TaskType'].mode()[0])
with col3:
    st.metric("Least Common", df['TaskType'].value_counts().index[-1])
               
st.markdown("---")
        
# Visualizations
col1, col2 = st.columns(2)
        
with col1:
    st.subheader("Satisfaction Rating by Task Type")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='TaskType', y='SatisfactionRating', errorbar=None, color='#3498db', ax=ax1)
    ax1.set_title('Mean Satisfaction Rating by Task Type', fontweight='bold')
    ax1.set_xlabel('Task Type')
    ax1.set_ylabel('Mean Satisfaction Rating')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig1)
        
with col2:
    st.subheader("Total Prompts by Task Type")
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    sns.barplot(data=df, x='TaskType', y='TotalPrompts', errorbar=None, color='#e74c3c', ax=ax2)
    ax2.set_title('Mean Total Prompts by Task Type', fontweight='bold')
    ax2.set_xlabel('Task Type')
    ax2.set_ylabel('Mean Total Prompts')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    st.pyplot(fig2)
        
st.markdown("---")
        
st.subheader("Mean Statistics by Task Type")
st.dataframe(mean_by_task
.style
.highlight_max(axis=0, color='yellow')
.highlight_min(axis=0, color='red')
)
 