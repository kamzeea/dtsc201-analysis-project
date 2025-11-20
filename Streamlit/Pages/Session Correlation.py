import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# Page config & styling
st.set_page_config(page_title="Student Satisfaction Analysis Dashboard", layout="wide")
sns.set_style("whitegrid")

# Cache the data
@st.cache_data(show_spinner="Loading dataset...")
def load_data():
    df = pd.read_csv('updated_cleaned_dataset1.csv')
    return df

df = load_data()

# Title
st.title("Session Length & Correlation Analysis")

# Correlation calculation
correlation = df['SessionLengthMin'].corr(df['SatisfactionRating'])

# Key metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Avg Session Length", f"{df['SessionLengthMin'].mean():.2f} min")

with col2:
    st.metric("Correlation (Session vs Satisfaction)", f"{correlation:.3f}")

with col3:
    correlation_strength = "Strong" if abs(correlation) > 0.7 else "Moderate" if abs(correlation) > 0.4 else "Weak"
    st.metric("Correlation Strength", correlation_strength)

st.info(
    f"**Correlation Coefficient:** {correlation:.2f} - "
    f"This indicates a {correlation_strength.lower()} "
    f"{'positive' if correlation > 0 else 'negative'} "
    f"relationship between session length and satisfaction rating."
)

st.markdown("---")

# Two-column layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Session Length vs Satisfaction")
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    
    ax1.scatter(df['SessionLengthMin'], df['SatisfactionRating'], 
                alpha=0.5, color='#36A2EB')
    
    # Trend line
    z = np.polyfit(df['SessionLengthMin'].dropna(), df['SatisfactionRating'].dropna(), 1)
    p = np.poly1d(z)
    ax1.plot(df['SessionLengthMin'].sort_values(), 
             p(df['SessionLengthMin'].sort_values()), 
             "r--", linewidth=2, 
             label=f'Trend line (r={correlation:.2f})')
    
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
    
    ax2.hist(df['SessionLengthMin'], bins=30, color='#FF6384', 
             edgecolor='black', alpha=0.7)
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

st.markdown("### Key Insight")
if correlation > 0.3:
    st.success("Students who spend more time in sessions tend to report higher satisfaction — consider encouraging deeper engagement!")
elif correlation < -0.3:
    st.warning("Very long sessions are associated with lower satisfaction — possible fatigue? Consider optimal session duration.")
else:
    st.info("Session length has little impact on satisfaction — other factors like course material, instructor may matter more.")