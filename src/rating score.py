import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the dataset in Python format
data = pd.read_csv(r'C:\Users\Kishl\OneDrive\Documents\Streaming Wars An Analytical Study of Age Restrictions and Ratings on Netflix vs. Disney+\data\processed\rating_analysis.csv')

# Step 2: Extract Sample 1 (where Netflix = 1) and Sample 2 (where Disney+ = 1)
S1 = data[data['Netflix'] == 1]['Rotten_Tomatoes_Absolute']
S2 = data[data['Disney+'] == 1]['Rotten_Tomatoes_Absolute']

# Perform t-test
t_stat, p_value = stats.ttest_ind(S1, S2)

# Adjust p-value for one-tailed test
if t_stat < 0:
    p_value /= 2

# Print t-statistic and p-value
print(f"T-statistic: {t_stat}")
print(f"P-value (one-tailed): {p_value}")

# Set the significance level at 0.05 (95% confidence)
alpha = 0.05

# Hypothesis testing
if p_value < alpha:
    print("Reject the null hypothesis: The mean of Rotten_Tomatoes_Absolute for Netflix is significantly less than that for Disney+.")
else:
    print("Fail to reject the null hypothesis: The mean of Rotten_Tomatoes_Absolute for Netflix is not significantly less than that for Disney+.")


  

# Boxplot visualization of Rotten Tomatoes ratings for Netflix vs Disney+
# Reshaping the data for seaborn
data_combined = pd.DataFrame({
    'Platform': ['Netflix'] * len(S1) + ['Disney+'] * len(S2),
    'Rotten_Tomatoes_Absolute': list(S1) + list(S2)
})

# Plotting boxplot
plt.figure(figsize=(10, 6))
sns.boxplot(x='Platform', y='Rotten_Tomatoes_Absolute', data=data_combined)
plt.title('Comparison of Rotten Tomatoes Ratings for Netflix vs. Disney+')
plt.xlabel('Platform')
plt.ylabel('Rotten Tomatoes Absolute Rating')
plt.show()
