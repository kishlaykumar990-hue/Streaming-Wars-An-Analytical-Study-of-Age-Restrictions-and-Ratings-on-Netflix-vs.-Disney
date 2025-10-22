import pandas as pd
from scipy import stats
data = pd.read_csv(r'C:\Users\Kishl\OneDrive\Documents\Streaming Wars An Analytical Study of Age Restrictions and Ratings on Netflix vs. Disney+\data\processed\age_analysis_v22.csv') #reading the dataset for analysis
print(data.head()) #printing the geaders to confirm file is read successfully
group1 = data[data['Disney+'] == 1]['min_age'] #Creating the group 1 which has the minimum age data for Disney+ hotstar
group2 = data[data['Netflix'] == 1]['min_age'] #Creating the group 2 which has the minimum age data for Netflix

# Calculate mean and standard deviation for group1 (Disney+)
mean_group1 = group1.mean()
var_group1 = group1.var()

# Calculate mean and standard deviation for group2 (Netflix)
mean_group2 = group2.mean()
var_group2 = group2.var()

# Printing the mean and standard deviation
print("Group 1 (Disney+):")
print("Mean:", mean_group1)
print("Variance:", var_group1)

print("\nGroup 2 (Netflix):")
print("Mean:", mean_group2)
print("Variance:", var_group2)
print("\n")


statistic, p_value = stats.mannwhitneyu(group1, group2, alternative='less') #Running the Mann-Whitney U test with the alternate Hypothesis that minimum age values is Disney+ is smaller than those in Netflix
print("U-statistic:", statistic) #Printing the U statistics
print("p-value:", p_value) # Printing the p-value
alpha = 0.05 #Setting the confidence level at 95%
if p_value < alpha:
       print("Reject the null hypothesis: The distribution of Hotstar minimum age is significantly shifted towards smaller values than the minimum age of Netflix.")
else:
       print("Fail to reject the null hypothesis: No significant difference between the minimum age of Netflix and Disney Hotstar.")
