# Recalculate the RFM values to ensure rfm_df is defined
import pandas as pd
import datetime as dt

# Load the cleaned dataframe again to ensure we have the necessary data
cleaned_df = pd.read_csv('online_retail_II.csv', encoding='iso-8859-1')
cleaned_df = cleaned_df.dropna(subset=['Customer ID', 'InvoiceDate'])
cleaned_df['InvoiceDate'] = pd.to_datetime(cleaned_df['InvoiceDate'])
cleaned_df['TotalAmount'] = cleaned_df['Quantity'] * cleaned_df['Price']

# Set the reference date for recency calculation
reference_date = cleaned_df['InvoiceDate'].max() + dt.timedelta(days=1)

# Group by Customer ID and calculate RFM metrics
rfm_df = cleaned_df.groupby('Customer ID').agg({
    'InvoiceDate': lambda x: (reference_date - x.max()).days,  # Recency
    'Invoice': 'nunique',  # Frequency
    'TotalAmount': 'sum'  # Monetary
}).reset_index()

# Rename columns
rfm_df.columns = ['Customer ID', 'Recency', 'Frequency', 'Monetary']

# Segmenting customers based on RFM scores
def rfm_segment(row):
    if row['Recency'] <= 30 and row['Frequency'] > 5 and row['Monetary'] > 500:
        return 'High Value'
    elif row['Recency'] <= 60 and row['Frequency'] > 3:
        return 'Medium Value'
    elif row['Recency'] <= 90:
        return 'Low Value'
    else:
        return 'At Risk'

# Apply segmentation
rfm_df['Segment'] = rfm_df.apply(rfm_segment, axis=1)

# Redefine the segment_analysis dataframe
segment_analysis = rfm_df.groupby('Segment').agg({
    'Customer ID': 'count',  # Count of customers in each segment
    'Recency': 'mean',  # Average recency
    'Frequency': 'mean',  # Average frequency
    'Monetary': 'mean'  # Average monetary value
}).reset_index()

# Rename columns for clarity
segment_analysis.columns = ['Segment', 'Customer Count', 'Average Recency', 'Average Frequency', 'Average Monetary']

# Now we can create the visualizations
import matplotlib.pyplot as plt
import seaborn as sns

# Set the aesthetic style of the plots
sns.set(style='whitegrid')

# 1. Bar chart for Customer Count by Segment
plt.figure(figsize=(10, 6))
sns.barplot(x='Segment', y='Customer Count', data=segment_analysis, palette='viridis')
plt.title('Customer Count by Segment')
plt.xlabel('Segment')
plt.ylabel('Customer Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('customer_count_by_segment.png')
plt.show()

# 2. Box plot for Monetary Value by Segment
plt.figure(figsize=(10, 6))
sns.boxplot(x='Segment', y='Monetary', data=rfm_df, palette='viridis')
plt.title('Monetary Value Distribution by Segment')
plt.xlabel('Segment')
plt.ylabel('Monetary Value')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monetary_value_by_segment.png')
plt.show()

# 3. Heatmap for RFM metrics
plt.figure(figsize=(10, 6))
sns.heatmap(segment_analysis[['Average Recency', 'Average Frequency', 'Average Monetary']].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of RFM Metrics')
plt.tight_layout()
plt.savefig('rfm_correlation_heatmap.png')
plt.show()
