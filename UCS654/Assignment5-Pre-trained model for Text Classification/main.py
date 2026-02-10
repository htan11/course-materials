import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from topsis import Topsis

# Models: DistilBERT, RoBERTa, BERT, XLNet, ALBERT
# Metrics: 
# - Accuracy (Higher better)
# - Inference Time (ms) (Lower better)
# - Model Size (Params in M) (Lower better)
# - F1 Score (Higher better)

data = {
    'Model': ['DistilBERT', 'RoBERTa', 'BERT', 'XLNet', 'ALBERT'],
    'Accuracy': [0.88, 0.92, 0.90, 0.93, 0.89],
    'Inference Time (ms)': [40, 90, 80, 120, 50],
    'Model Size (M Params)': [66, 125, 110, 110, 12],
    'F1 Score': [0.87, 0.91, 0.89, 0.92, 0.88]
}

df = pd.DataFrame(data)

# Columns to use for analysis (excluding Model name)
numeric_data = df.iloc[:, 1:].values

# Weights (Assume equal importance or customize)
# Acc: 1, Time: 1, Size: 1, F1: 1
weights = [1, 1, 1, 1] 

# Impacts 
# Acc (+), Time (-), Size (-), F1 (+)
impacts = ['+', '-', '-', '+']

topsis = Topsis(numeric_data, weights, impacts)
scores = topsis.run()

df['Topsis Score'] = scores
df['Rank'] = df['Topsis Score'].rank(ascending=False).astype(int)

# Sort by Rank
df_sorted = df.sort_values(by='Rank')

print("Final Rankings:")
print(df_sorted)

# Save to CSV
df_sorted.to_csv('topsis_results.csv', index=False)
print("\nResults saved to 'topsis_results.csv'")

# Bar Plot for Rankings
plt.figure(figsize=(10, 6))
sns.barplot(x='Topsis Score', y='Model', data=df_sorted, palette='viridis')
plt.title('TOPSIS Ranking of Text Classification Models')
plt.xlabel('TOPSIS Score')
plt.ylabel('Model')
plt.xlim(0, 1)
plt.tight_layout()
plt.savefig('rankings_graph.png')
print("Graph saved to 'rankings_graph.png'")

# Comparison Charts (Subplots)
fig, axes = plt.subplots(2, 2, figsize=(12, 10))
fig.suptitle('Model Metrics Comparison', fontsize=16)

sns.barplot(ax=axes[0, 0], x='Model', y='Accuracy', data=df, palette='Blues')
axes[0, 0].set_title('Accuracy')
axes[0, 0].set_ylim(0.8, 1.0) # Zoom in for text classification acc

sns.barplot(ax=axes[0, 1], x='Model', y='Inference Time (ms)', data=df, palette='Reds')
axes[0, 1].set_title('Inference Time (Lower is Better)')

sns.barplot(ax=axes[1, 0], x='Model', y='Model Size (M Params)', data=df, palette='Greens')
axes[1, 0].set_title('Model Size (Lower is Better)')

sns.barplot(ax=axes[1, 1], x='Model', y='F1 Score', data=df, palette='Purples')
axes[1, 1].set_title('F1 Score')
axes[1, 1].set_ylim(0.8, 1.0)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.savefig('metrics_comparison.png')
print("Comparison charts saved to 'metrics_comparison.png'")
