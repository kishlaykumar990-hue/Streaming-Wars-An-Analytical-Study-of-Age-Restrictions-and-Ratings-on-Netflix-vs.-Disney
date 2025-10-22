import pandas as pd
from scipy import stats
data = pd.read_csv(r'C:\Users\Kishl\OneDrive\Documents\Streaming Wars An Analytical Study of Age Restrictions and Ratings on Netflix vs. Disney+\data\processed\rating_analysis.csv') #Reading the data set in Python format
# Step 2: Extract Sample 1 (where Netflix = 1) and Sample 2 (where Disney+ = 1)
S1 = data[data['Netflix'] == 1]['Rotten_Tomatoes_Absolute']
S2 = data[data['Disney+'] == 1]['Rotten_Tomatoes_Absolute']


# Calculate mean and standard deviation for group1 (Disney+)
mean_Netflix = S1.mean()
var_Netflix = S1.var()

# Calculate mean and standard deviation for group2 (Netflix)
mean_Disney = S2.mean()
var_Disney = S2.var()

# Printing the mean and standard deviation
print("Group 1 (Netflix):")
print("Mean:", mean_Netflix)
print("Variance:", var_Netflix)

print("\nGroup 2 (Disney+):")
print("Mean:", mean_Disney)
print("Variance:", var_Disney)
print("\n")


t_stat, p_value = stats.ttest_ind(S1, S2)
if t_stat <0:
    p_value /=2
    print(f"T-statistic: {t_stat}")
    print(f"P-value (one-tailed): {p_value}")
    alpha = 0.05 #Setting the significance level at 95%
    if p_value < alpha:
           print("Reject the null hypothesis: The mean of Rotten_Tomatoes_Absolute for Netflix is significantly less than that for Disney+.")
    else:
           print("Fail to reject the null hypothesis: No significant difference between the means of Rotten_Tomatoes_Absolute for Netflix and Disney+.")

else:
    p_value /=2
    print(f"T-statistic: {t_stat}")
    print(f"P-value (one-tailed): {p_value}")
    alpha = 0.05 #Setting the significance level at 95%
    if p_value < alpha:
        print("Reject the null hypothesis: The mean of Rotten_Tomatoes_Absolute for Disney+ is significantly less than that for Netflix.")
    else:
        print("Fail to reject the null hypothesis: No significant difference between the means of Rotten_Tomatoes_Absolute for Netflix and Disney+.")
