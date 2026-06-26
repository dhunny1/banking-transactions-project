# %%
# 2. Cleaned data → data/processed/
# This is the cleaned version after fixing:

# dates

# amounts

# categories

# duplicates


# %%
import pandas as pd
import boto3

path = "s3://ds-learning-hunny/aws-practice-data/banking/data/raw-data/fake_bank_transactions.csv"

df = pd.read_csv(path)
df.head()

# %%
df.info()

# %%
# 1. convert date column
df['date'] = pd.to_datetime(df['date'])
df['date'].info()

# %%
# 2 check for duplicates
df.drop_duplicates()

# %%
# 3 check for missing values
df.isnull().sum()

df = df.dropna(subset=[
    'date',
    'amount',
    'balance',
    'transaction_type',
    'description',
    'category'
    ])
# These are optional metadata fields:
# account_name
# bank_name
# month

df = df.drop(columns=['account_name','bank_name'])

# make sures that moenth columns are filled 
df['month']= df['date'].dt.strftime('%Y-%m')
df.head()

# %%
# 4 Ensure amount and balance is numeric
df['amount'] = pd.to_numeric(df['amount'])
df['balance'] = pd.to_numeric(df['balance'])


# %%
# 5 Validate balance
validation_df = df[['amount','balance']]
validation_df['expected_balance'] = (validation_df['balance'].shift(1)+ validation_df['amount'])
validation_df.loc[0,'expected_balance'] = validation_df.loc[0,'balance']
validation_df.head()

# %%
# NOW VALIDATE
validation_df['is_valid'] = (validation_df['balance'] - validation_df['expected_balance']).abs()<0.01

print("Not Valid Balance") if (validation_df['is_valid'] == False).any() else print("Valid Balance!")


# %%
df.reset_index()

# %%
df.to_csv('s3://ds-learning-hunny/aws-practice-data/banking/data/processed/bank_transactions_cleaned.csv',index=False)

# %%
df.to_csv('C:/Users/hunny/OneDrive/Documents/Resume/JOBSTUDY/Data_Science_Projects/AWS_PROJECT/banking-project/data/processed/bank_transactions_cleaned.csv', index=False)



