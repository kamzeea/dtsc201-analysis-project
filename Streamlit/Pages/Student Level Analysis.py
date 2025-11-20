# ==================== PAGE 4: STUDENT LEVEL ANALYSIS ====================
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
st.title("Student Level Analysis")
    
mean_by_student_level = df.groupby('StudentLevel').mean(numeric_only=True)[['SessionLengthMin', 'SatisfactionRating']]
student_level_counts = df['StudentLevel'].value_counts()
        
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Student Levels", df['StudentLevel'].nunique())
with col2:
    st.metric("Most Common Level", student_level_counts.index[0])
with col3:
    st.metric("Students in Top Level", student_level_counts.iloc[0])
        
st.markdown("---")
        
st.subheader("Mean Statistics by Student Level")
st.dataframe(mean_by_student_level.style.highlight_max(axis=0), use_container_width=True)
        
st.markdown("---")
        
col1, col2 = st.columns(2)
        
with col1:
    st.subheader("Distribution of Students by Level")
    fig1, ax1 = plt.subplots(figsize=(8, 6))
    ax1.pie(student_level_counts, labels=student_level_counts.index,
            autopct='%1.1f%%', 
            colors=["#3498db", "#e74c3c", "#2ecc71"], 
            startangle=90, textprops={'fontsize': 11})
    ax1.set_title('Distribution of Students by Level', fontweight='bold')
    plt.tight_layout()
    st.pyplot(fig1)
        
with col2:
    st.subheader("Satisfaction Rating by Student Level")
    satisfaction_by_level = df.groupby("StudentLevel")["SatisfactionRating"].mean()
            
    fig2, ax2 = plt.subplots(figsize=(8, 6))
    bars = ax2.bar(satisfaction_by_level.index, satisfaction_by_level.values,
    color=["#36A2EB", "#FF6384", "#FFCE56", "#4BC0C0"])
            
    for bar in bars:
        yval = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'{yval:.2f}', ha='center', va='bottom', fontsize=10)
            
    ax2.set_title("Satisfaction Rating by Student Level", fontweight='bold')
    ax2.set_xlabel("Student Level")
    ax2.set_ylabel("Satisfaction Rating")
    plt.tight_layout()
    st.pyplot(fig2)
