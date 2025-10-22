import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file (update the file path to your actual file location)
file_path = r'C:\Users\Kishl\OneDrive\Documents\Streaming Wars An Analytical Study of Age Restrictions and Ratings on Netflix vs. Disney+\data\processed\age_analysis_v22.csv'  # Replace this with your actual file path

df = pd.read_csv(file_path)

# Count the frequency of each minimum age
score_counts = df['min_age'].value_counts().sort_index()

# Create a scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(score_counts.index, score_counts.values, color='skyblue', edgecolors='black')

# Adding labels and title
plt.xlabel('Minimum age absolute')
plt.ylabel('Count of Number of Movies')
plt.title('Scatter Plot of Minimum age frequency Frequency')

# Show the plot
plt.tight_layout()
plt.show()
