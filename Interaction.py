import pandas as pd
def add_interaction_term(df, day_col='dayofweek', promo_col='total_promotions', new_col_name='interaction_term'):
    """
    Adds an interaction term between a numeric day-of-week column and total promotions.

    Parameters:
    - df: pandas DataFrame
    - day_col: name of the day-of-week column (numeric, 1=Mon to 7=Sun)
    - promo_col: name of the total promotions column (numeric)
    - new_col_name: name of the new interaction term column

    Returns:
    - df: DataFrame with the new interaction term added
    """
    if day_col not in df.columns or promo_col not in df.columns:
        raise ValueError(f"Columns '{day_col}' and/or '{promo_col}' not found in DataFrame.")
    
    if not pd.api.types.is_numeric_dtype(df[day_col]) or not pd.api.types.is_numeric_dtype(df[promo_col]):
        raise TypeError("Both columns must be numeric to compute interaction.")
    
    df[new_col_name] = df[day_col] * df[promo_col]
    return df
