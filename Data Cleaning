# Data cleaning and transformation
# Remove rows with missing Customer ID or InvoiceDate
cleaned_df = df.dropna(subset=['Customer ID', 'InvoiceDate'])

# Convert InvoiceDate to datetime
cleaned_df['InvoiceDate'] = pd.to_datetime(cleaned_df['InvoiceDate'])

# Calculate total purchase amount for each transaction
cleaned_df['TotalAmount'] = cleaned_df['Quantity'] * cleaned_df['Price']

# Display the cleaned dataframe head
print(cleaned_df.head())
