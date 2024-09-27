# Calculate RFM values
import datetime as dt

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

# Display the RFM dataframe head
print(rfm_df.head())
