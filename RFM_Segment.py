# Segmenting customers based on RFM scores
import numpy as np

# Define RFM segmentation function
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

# Display the segmented RFM dataframe head
print(rfm_df.head())
