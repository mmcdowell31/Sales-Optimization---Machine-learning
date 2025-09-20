import pandas as pd

# def encode_non_numeric(df, drop_first=True):
#     """
#     Encodes all non-numeric columns in the DataFrame using one-hot encoding.

#     Parameters:
#     - df: pandas DataFrame
#     - drop_first: whether to drop the first level to avoid multicollinearity (default: True)

#     Returns:
#     - df_encoded: DataFrame with only numeric columns
#     """
#     non_numeric_cols = df.select_dtypes(include=['object', 'category']).columns
#     df_encoded = pd.get_dummies(df, columns=non_numeric_cols, drop_first=drop_first)
#     return df_encoded



def encode_non_numeric(df, drop_first=True):
    """
    Encodes all non-numeric columns in the DataFrame using one-hot encoding and assigns day of week columns
    numeric values (1 for Monday, 2 for Tuesday, etc.), case-insensitively.

    Parameters:
    - df: pandas DataFrame
    - drop_first: whether to drop the first level to avoid multicollinearity (default: True)

    Returns:
    - df_encoded: DataFrame with encoded columns, including numeric day of week columns
    """
    # Check for columns that represent days of the week and replace them with numeric values
    for col in df.select_dtypes(include=['object', 'category']).columns:
        if df[col].str.lower().isin(['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']).all():  # Check if it's a day of the week (case-insensitive)
            df[col] = df[col].str.lower().map({'mon': 1, 'tue': 2, 'wed': 3, 'thu': 4, 'fri': 5, 'sat': 6, 'sun': 7})
    
    # Now apply one-hot encoding to other non-numeric columns
    non_numeric_cols = df.select_dtypes(include=['object', 'category']).columns
    df_encoded = pd.get_dummies(df, columns=non_numeric_cols, drop_first=drop_first)
    
    return df_encoded