import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Load data
data = pd.read_csv('iris/iris.data', header=None, 
                   names=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species'])

print("=" * 70)
print("IRIS DATASET ANALYSIS REPORT")
print("=" * 70)

# Basic Info
print("\n1. DATASET OVERVIEW")
print("-" * 70)
print(f"Total Samples: {len(data)}")
print(f"Features: {data.shape[1] - 1}")
print(f"Species: {data['species'].nunique()}")

# Species Distribution
print("\n2. SPECIES DISTRIBUTION")
print("-" * 70)
print(data['species'].value_counts())

# Statistical Summary
print("\n3. STATISTICAL SUMMARY")
print("-" * 70)
print(data.describe())

# Correlation
print("\n4. FEATURE CORRELATIONS")
print("-" * 70)
numeric_data = data.drop('species', axis=1)
print(numeric_data.corr())

# Species-wise Statistics
print("\n5. SPECIES-WISE STATISTICS")
print("-" * 70)
for species in data['species'].unique():
    print(f"\n{species}:")
    print(data[data['species'] == species].describe().loc['mean'])

# Create visualizations
sns.set_style("whitegrid")
fig = plt.figure(figsize=(16, 12))

# 1. Species Distribution
plt.subplot(3, 3, 1)
data['species'].value_counts().plot(kind='bar', color=['#667eea', '#764ba2', '#f093fb'])
plt.title('Species Distribution', fontsize=12, fontweight='bold')
plt.ylabel('Count')
plt.xticks(rotation=45)

# 2. Pairplot features
plt.subplot(3, 3, 2)
for species in data['species'].unique():
    subset = data[data['species'] == species]
    plt.scatter(subset['sepal_length'], subset['sepal_width'], label=species, alpha=0.6)
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Width', fontsize=12, fontweight='bold')
plt.legend()

plt.subplot(3, 3, 3)
for species in data['species'].unique():
    subset = data[data['species'] == species]
    plt.scatter(subset['petal_length'], subset['petal_width'], label=species, alpha=0.6)
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')
plt.title('Petal Length vs Width', fontsize=12, fontweight='bold')
plt.legend()

# 3. Box plots
plt.subplot(3, 3, 4)
data.boxplot(column='sepal_length', by='species', ax=plt.gca())
plt.title('Sepal Length by Species')
plt.suptitle('')

plt.subplot(3, 3, 5)
data.boxplot(column='sepal_width', by='species', ax=plt.gca())
plt.title('Sepal Width by Species')
plt.suptitle('')

plt.subplot(3, 3, 6)
data.boxplot(column='petal_length', by='species', ax=plt.gca())
plt.title('Petal Length by Species')
plt.suptitle('')

plt.subplot(3, 3, 7)
data.boxplot(column='petal_width', by='species', ax=plt.gca())
plt.title('Petal Width by Species')
plt.suptitle('')

# 4. Correlation Heatmap
plt.subplot(3, 3, 8)
sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Feature Correlation Heatmap', fontsize=12, fontweight='bold')

# 5. Distribution plots
plt.subplot(3, 3, 9)
for col in numeric_data.columns:
    plt.hist(data[col], alpha=0.5, label=col, bins=20)
plt.xlabel('Measurement (cm)')
plt.ylabel('Frequency')
plt.title('Feature Distributions', fontsize=12, fontweight='bold')
plt.legend()

plt.tight_layout()
plt.savefig('iris_analysis.png', dpi=300, bbox_inches='tight')
print("\n" + "=" * 70)
print("Analysis complete! Visualization saved as 'iris_analysis.png'")
print("=" * 70)
