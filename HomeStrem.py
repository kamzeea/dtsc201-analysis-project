import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Set page config
st.set_page_config(page_title="Dataset Analysis Dashboard")

# Set seaborn style
sns.set(style="whitegrid")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv('updated_cleaned_dataset1.csv')  # Fixed indentation
    df1 = pd.read_csv('ai_assistant_usage_student_life.csv')
    return df, df1  # Fixed indentation

df, df1 = load_data()

# Initialize session state for page navigation
if 'page' not in st.session_state:
    st.session_state.page = 'Overview'

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("### Select a Page:")

pages = [
    "Overview",
    "Prompts by Discipline", 
    "Task Type Analysis",
    "Student Level Analysis",
    "Outcome & Usage Analysis",
    "Satisfaction Analysis",
    "Session & Correlations"
]

for page in pages:
    if st.sidebar.button(page, use_container_width=True, type="primary" if st.session_state.page == page else "secondary"):
        st.session_state.page = page

st.sidebar.markdown("---")
st.sidebar.info(f"Total Records: {len(df)}")

# ==================== PAGE 1: OVERVIEW ====================
if st.session_state.page == "Overview":

    st.title("Dataset Overview")
    st.subheader("Uncleaned Dataset")
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    with col1:
        st.metric("Total Records", len(df1))
    with col2:
        if 'Discipline' in df.columns:
            st.metric("Disciplines", df1['Discipline'].nunique())
    with col3:
        if 'TotalPrompts' in df.columns:
            st.metric("Avg Prompts", f"{df1['TotalPrompts'].mean():.2f}")
    with col4:
        if 'SatisfactionRating' in df.columns:
            st.metric("Avg Satisfaction", f"{df1['SatisfactionRating'].mean():.2f}")
    with col5:
        if 'TaskType' in df.columns:
            st.metric("TaskType", f"{df1['TaskType'].nunique()}")
    with col6:
        if 'StudentLevel' in df.columns:
            st.metric("StudentLevel", f"{df1['StudentLevel'].nunique()}")  # Fixed typo
    with col7:
        if 'FinalOutcome' in df.columns:
            st.metric('FinalOutcome', f"{df1['FinalOutcome'].nunique()}")
    
    st.markdown("---")
    
    st.subheader("Dataset Preview")
    st.dataframe(df1.head(10))
    
    st.markdown("---")
    
    st.subheader("Column Information")
    col_info = pd.DataFrame({
        'Column': df1.columns,
        'Type': df1.dtypes.values,
        'Non-Null': df1.count().values,
        'Null Count': df1.isnull().sum().values
    })
    st.dataframe(col_info)
    
    st.markdown("---")
    
    st.subheader("Quick Statistics")
    st.dataframe(df1.describe())






    #cleaned dataset
    st.title("Cleaned Dataset")
    
    col1, col2, col3, col4, col5, col6, col7 = st.columns(7)
    
    with col1:
        st.metric("Total Records", len(df))
    with col2:
        if 'Discipline' in df.columns:
            st.metric("Disciplines", df['Discipline'].nunique())
    with col3:
        if 'TotalPrompts' in df.columns:
            st.metric("Avg Prompts", f"{df['TotalPrompts'].mean():.2f}")
    with col4:
        if 'SatisfactionRating' in df.columns:
            st.metric("Avg Satisfaction", f"{df['SatisfactionRating'].mean():.2f}")
    with col5:
        if 'TaskType' in df.columns:
            st.metric("TaskType", f"{df['TaskType'].nunique()}")
    with col6:
        if 'StudentLevel' in df.columns:
            st.metric("StudentLevel", f"{df['StudentLevel'].nunique()}")  # Fixed typo
    with col7:
        if 'FinalOutcome' in df.columns:
            st.metric('FinalOutcome', f"{df['FinalOutcome'].nunique()}")
    
    st.markdown("---")
    
    st.subheader("Dataset Preview")
    st.dataframe(df.head(15), use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("Column Information")
    col_info = pd.DataFrame({
        'Column': df.columns,
        'Type': df.dtypes.values,
        'Non-Null': df.count().values,
        'Null Count': df.isnull().sum().values
    })
    st.dataframe(col_info, use_container_width=True)
    
    st.markdown("---")
    
    st.subheader("Quick Statistics")
    st.dataframe(df.describe(), use_container_width=True)

# ==================== PAGE 2: PROMPTS BY DISCIPLINE ====================
elif st.session_state.page == "Prompts by Discipline":
    st.title("Average Prompts Used by Discipline")
    
    if 'Discipline' in df.columns and 'TotalPrompts' in df.columns:
        prompts_by_discipline = df.groupby('Discipline')['TotalPrompts'].mean()
        max_prompts_discipline = prompts_by_discipline.idxmax()
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
        
        with col1:
            st.subheader("Distribution - Pie Chart")
            explode = [0.1 if discipline == max_prompts_discipline else 0 
                      for discipline in prompts_by_discipline.index]
            
            fig1, ax1 = plt.subplots(figsize=(8, 6))
            colors = ["#36A2EB", "#FF6384", "#FFCE56", "#4BC0C0", "#9966FF"]
            
            ax1.pie(prompts_by_discipline, 
                   labels=prompts_by_discipline.index, 
                   autopct='%1.2f%%', 
                   explode=explode,
                   colors=colors[:len(prompts_by_discipline)], 
                   startangle=90, 
                   textprops={'fontsize': 10})
            
            ax1.set_title('Distribution of Prompts by Discipline', fontweight='bold')
            plt.tight_layout()
            st.pyplot(fig1)
        
        with col2:
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
        })#.sort_values('Average Prompts', ascending=False)
        
        st.dataframe(
    stats_df
    .style
    .highlight_max(subset=['Average Prompts'], color='yellow')
    .highlight_min(subset=['Average Prompts'], color='#ffcccc')
        )
    else:
        st.error("Required columns not found in dataset!")

    st.markdown("---")
    st.header("Insight")
    st.write("What we learnded from this analysis was:")

# ==================== PAGE 3: TASK TYPE ANALYSIS ====================
elif st.session_state.page == "Task Type Analysis":
    st.title("Task Type Analysis")
    
    if 'TaskType' in df.columns:
        # Calculate means
        mean_by_task = df.groupby('TaskType').mean(numeric_only=True)[['SatisfactionRating', 'TotalPrompts']]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Task Types", df['TaskType'].nunique())
        with col2:
            st.metric("Most Common", df['TaskType'].mode()[0])
        with col3:
            st.metric("Least Common", df['TaskType'].value_counts().index[-1])

        
        st.markdown("---")
        
        st.subheader("Mean Statistics by Task Type")
        st.dataframe(mean_by_task.style.highlight_max(axis=0))
        
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
    else:
        st.error("Required columns not found in dataset!")

# ==================== PAGE 4: STUDENT LEVEL ANALYSIS ====================
elif st.session_state.page == "Student Level Analysis":
    st.title("Student Level Analysis")
    
    if 'StudentLevel' in df.columns:
        # Calculate statistics
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
                ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.05, f'{yval:.2f}', 
                        ha='center', va='bottom', fontsize=10)
            
            ax2.set_title("Satisfaction Rating by Student Level", fontweight='bold')
            ax2.set_xlabel("Student Level")
            ax2.set_ylabel("Satisfaction Rating")
            plt.tight_layout()
            st.pyplot(fig2)
    else:
        st.error("Required columns not found in dataset!")

# ==================== PAGE 5: OUTCOME & USAGE ANALYSIS ====================
elif st.session_state.page == "Outcome & Usage Analysis":
    st.title("Final Outcome & AI Usage Analysis")
    
    if 'FinalOutcome' in df.columns and 'UsedAgain' in df.columns:
        # Calculate percentages
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
            
            sns.barplot(x='FinalOutcome', y='UsedAgain', data=df, estimator='mean', errorbar=None, 
                       palette=["#36A2EB", "#FF6384", "#FFCE56", "#4BC0C0"], ax=ax2)
            
            for bar in ax2.patches:
                yval = bar.get_height()
                ax2.text(bar.get_x() + bar.get_width()/2, yval + 0.02, f'{yval:.2f}', 
                        ha='center', va='bottom', fontsize=10)
            
            ax2.set_title('Likelihood of Using AI Tool Again by Session Outcome', fontweight='bold')
            ax2.set_ylabel('Proportion who would use again')
            ax2.set_xlabel('Session Outcome')
            ax2.set_ylim(0, 1.1)
            plt.tight_layout()
            st.pyplot(fig2)
    else:
        st.error("Required columns not found in dataset!")

# ==================== PAGE 6: SATISFACTION ANALYSIS ====================
elif st.session_state.page == "Satisfaction Analysis":
    st.title("Satisfaction Rating Analysis")
    
    if 'SatisfactionRating' in df.columns:
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.metric("Mean Rating", f"{df['SatisfactionRating'].mean():.2f}")
        with col2:
            st.metric("Median Rating", f"{df['SatisfactionRating'].median():.2f}")
        with col3:
            st.metric("Std Dev", f"{df['SatisfactionRating'].std():.2f}")
        with col4:
            st.metric("Max Rating", f"{df['SatisfactionRating'].max():.2f}")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Distribution of Satisfaction Ratings")
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            ax1.hist(df["SatisfactionRating"], bins=20, color='red', edgecolor='black', alpha=0.7)
            ax1.axvline(df["SatisfactionRating"].mean(), color='blue', linestyle='--', 
                       linewidth=2, label=f'Mean: {df["SatisfactionRating"].mean():.2f}')
            ax1.set_title("Distribution of Satisfaction Rating", fontweight='bold')
            ax1.set_xlabel("Satisfaction Rating")
            ax1.set_ylabel("Frequency")
            ax1.legend()
            plt.tight_layout()
            st.pyplot(fig1)
        
        with col2:
            st.subheader("Satisfaction by Student Level")
            satisfaction_by_level = df.groupby("StudentLevel")["SatisfactionRating"].mean().sort_values(ascending=False)
            
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            bars = ax2.barh(satisfaction_by_level.index, satisfaction_by_level.values, 
                           color=["#36A2EB", "#FF6384", "#FFCE56"])
            
            for bar in bars:
                xval = bar.get_width()
                ax2.text(xval + 0.05, bar.get_y() + bar.get_height()/2, f'{xval:.2f}', 
                        ha='left', va='center', fontsize=10)
            
            ax2.set_title("Average Satisfaction by Student Level", fontweight='bold')
            ax2.set_xlabel("Satisfaction Rating")
            ax2.set_ylabel("Student Level")
            plt.tight_layout()
            st.pyplot(fig2)
        
        st.markdown("---")
        
        # Satisfaction by Task Type
        if 'TaskType' in df.columns:
            st.subheader("Satisfaction Rating Distribution by Task Type")
            fig3, ax3 = plt.subplots(figsize=(12, 6))
            df.boxplot(column='SatisfactionRating', by='TaskType', ax=ax3)
            ax3.set_title('Satisfaction Rating by Task Type', fontweight='bold')
            ax3.set_xlabel('Task Type')
            ax3.set_ylabel('Satisfaction Rating')
            plt.xticks(rotation=45, ha='right')
            plt.suptitle('')
            plt.tight_layout()
            st.pyplot(fig3)
    else:
        st.error("Required columns not found in dataset!")

# ==================== PAGE 7: SESSION & CORRELATIONS ====================
elif st.session_state.page == "Session & Correlations":
    st.title("Session Length & Correlation Analysis")
    
    if 'SessionLengthMin' in df.columns and 'SatisfactionRating' in df.columns:
        # Calculate correlation
        correlation = df['SessionLengthMin'].corr(df['SatisfactionRating'])
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Avg Session Length", f"{df['SessionLengthMin'].mean():.2f} min")
        with col2:
            st.metric("Correlation (Session vs Satisfaction)", f"{correlation:.3f}")
        with col3:
            correlation_strength = "Strong" if abs(correlation) > 0.7 else "Moderate" if abs(correlation) > 0.4 else "Weak"
            st.metric("Correlation Strength", correlation_strength)
        
        st.info(f"**Correlation Coefficient:** {correlation:.2f} - This indicates a {correlation_strength.lower()} {'positive' if correlation > 0 else 'negative'} relationship between session length and satisfaction rating.")
        
        st.markdown("---")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Session Length vs Satisfaction")
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            ax1.scatter(df['SessionLengthMin'], df['SatisfactionRating'], alpha=0.5, color='#36A2EB')
            
            # Add trend line
            z = np.polyfit(df['SessionLengthMin'].dropna(), df['SatisfactionRating'].dropna(), 1)
            p = np.poly1d(z)
            ax1.plot(df['SessionLengthMin'].sort_values(), p(df['SessionLengthMin'].sort_values()), 
                    "r--", linewidth=2, label=f'Trend line (r={correlation:.2f})')
            
            ax1.set_xlabel('Session Length (minutes)', fontweight='bold')
            ax1.set_ylabel('Satisfaction Rating', fontweight='bold')
            ax1.set_title('Session Length vs Satisfaction Rating', fontweight='bold')
            ax1.legend()
            ax1.grid(alpha=0.3)
            plt.tight_layout()
            st.pyplot(fig1)
        
        with col2:
            st.subheader("Session Length Distribution")
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            ax2.hist(df['SessionLengthMin'], bins=30, color='#FF6384', edgecolor='black', alpha=0.7)
            ax2.axvline(df['SessionLengthMin'].mean(), color='red', linestyle='--', 
                       linewidth=2, label=f'Mean: {df["SessionLengthMin"].mean():.1f} min')
            ax2.set_xlabel('Session Length (minutes)', fontweight='bold')
            ax2.set_ylabel('Frequency', fontweight='bold')
            ax2.set_title('Distribution of Session Lengths', fontweight='bold')
            ax2.legend()
            plt.tight_layout()
            st.pyplot(fig2)
        
        st.markdown("---")
        
        # Session length by Discipline
        if 'Discipline' in df.columns:
            st.subheader("Session Length by Discipline")
            session_by_discipline = df.groupby('Discipline')['SessionLengthMin'].mean().sort_values(ascending=False)
            
            fig3, ax3 = plt.subplots(figsize=(12, 6))
            bars = ax3.bar(session_by_discipline.index, session_by_discipline.values, color='#FFCE56')
            
            for bar in bars:
                yval = bar.get_height()
                ax3.text(bar.get_x() + bar.get_width()/2, yval + 1, f'{yval:.1f}', 
                        ha='center', va='bottom', fontsize=9)
            
            ax3.set_xlabel('Discipline', fontweight='bold')
            ax3.set_ylabel('Average Session Length (minutes)', fontweight='bold')
            ax3.set_title('Average Session Length by Discipline', fontweight='bold')
            plt.xticks(rotation=45, ha='right')
            plt.tight_layout()
            st.pyplot(fig3)
    else:
        st.error("Required columns not found in dataset!")
