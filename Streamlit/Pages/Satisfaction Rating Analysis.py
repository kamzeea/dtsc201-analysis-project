import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Page config & styling
st.set_page_config(page_title="Student Satisfaction Analysis Dashboard", layout="wide")
sns.set_style("whitegrid")
#plt.rcParams['figure.facecolor'] = 'white'

# Cache the data
@st.cache_data(show_spinner="Loading dataset...")
def load_data():
    df = pd.read_csv('updated_cleaned_dataset1.csv')
    return df

df = load_data()

# Title & description
st.title("Student Satisfaction Rating Analysis Dashboard")
st.markdown("### Exploring satisfaction patterns across student levels and task types")

# Key Metrics Row
st.markdown("Key Statistics")
col1, col2, col3, col4, col5 = st.columns(5)

mean_val = df['SatisfactionRating'].mean()
median_val = df['SatisfactionRating'].median()
std_val = df['SatisfactionRating'].std()
max_val = df['SatisfactionRating'].max()
min_val = df['SatisfactionRating'].min()

with col1:
    st.metric("Mean Rating", f"{mean_val:.2f}", delta=None)
with col2:
    st.metric("Median Rating", f"{median_val:.2f}")
with col3:
    st.metric("Standard Deviation", f"{std_val:.2f}")
with col4:
    st.metric("Highest Rating", f"{max_val:.2f}")
with col5:
    st.metric("Lowest Rating", f"{min_val:.2f}")

st.markdown("---")

# Two-column layout
col1, col2 = st.columns([2, 1.5])

with col1:
    st.subheader("Distribution of Satisfaction Ratings")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    counts, bins, patches = ax1.hist(df["SatisfactionRating"], bins=20, 
                                     color='#4e79a7', edgecolor='black', alpha=0.8, rwidth=0.9)
    
    # Add mean and median lines
    ax1.axvline(mean_val, color='#e15759', linestyle='--', linewidth=2.5, label=f'Mean: {mean_val:.2f}')
    ax1.axvline(median_val, color='#f28e2b', linestyle='-.', linewidth=2, label=f'Median: {median_val:.2f}')
    
    ax1.set_title("Distribution of Satisfaction Ratings", fontsize=16, fontweight='bold', pad=20)
    ax1.set_xlabel("Satisfaction Rating", fontsize=12)
    ax1.set_ylabel("Number of Responses", fontsize=12)
    ax1.legend(frameon=True, fancybox=True, shadow=True)
    ax1.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig1)

with col2:
    st.subheader("Avg. Satisfaction by Student Level")
    satisfaction_by_level = df.groupby("StudentLevel")["SatisfactionRating"].mean().round(2).sort_values(ascending=False)
    
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    colors = ['#59a14f' if x == satisfaction_by_level.max() else '#4e79a7' for x in satisfaction_by_level.values]
    bars = ax2.barh(satisfaction_by_level.index, satisfaction_by_level.values, color=colors, edgecolor='black', linewidth=0.8)
    
    # Add value labels
    for i, (level, value) in enumerate(satisfaction_by_level.items()):
        ax2.text(value + 0.05, i, f'{value:.2f}', va='center', fontsize=11, fontweight='bold')
    
    ax2.set_title("Average Satisfaction by Student Level", fontsize=14, fontweight='bold', pad=20)
    ax2.set_xlabel("Average Satisfaction Rating")
    ax2.invert_yaxis()  # Highest on top
    ax2.grid(axis='x', alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig2)

st.markdown("---")

# Boxplot by Task Type with better aesthetics
st.subheader("Satisfaction Rating Distribution by Task Type")

# Interactive filter (optional enhancement)
task_options = st.multiselect(
    "Filter Task Types (optional):",
    options=sorted(df['TaskType'].unique()),
    default=sorted(df['TaskType'].unique())
)

filtered_df = df[df['TaskType'].isin(task_options)] if task_options else df

fig3, ax3 = plt.subplots(figsize=(14, 7))
boxprops = dict(linestyle='-', linewidth=2, color='darkblue')
medianprops = dict(linestyle='-', linewidth=2.5, color='firebrick')

filtered_df.boxplot(column='SatisfactionRating', by='TaskType', ax=ax3,
                    grid=False, patch_artist=True,
                    boxprops=boxprops, medianprops=medianprops,
                    whiskerprops=dict(linewidth=2),
                    capprops=dict(linewidth=2),
                    flierprops=dict(marker='o', markersize=5, alpha=0.5))

ax3.set_title('Satisfaction Rating Distribution by Task Type', fontsize=16, fontweight='bold', pad=20)
ax3.set_xlabel('Task Type', fontsize=12)
ax3.set_ylabel('Satisfaction Rating', fontsize=12)
plt.suptitle('')  # Remove default title
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
st.pyplot(fig3)