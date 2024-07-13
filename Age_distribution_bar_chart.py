import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Sample data: Age distribution
data = {
    'Age': [23, 25, 31, 35, 42, 23, 25, 31, 35, 42, 50, 60, 30, 25, 23, 23, 35, 42, 42, 23, 25, 31, 35, 42]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Create a histogram using Seaborn
sns.histplot(df['Age'], bins=10, kde=False, color="pink")

# Add titles and labels
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')

# Show the plot
plt.show()
