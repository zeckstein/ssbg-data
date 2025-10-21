"""
Data cleaning utilities for SSBG data analysis.

This module provides functions to clean and preprocess raw SSBG data.
"""

import pandas as pd
import numpy as np
from typing import List, Optional


def remove_duplicates(df: pd.DataFrame, subset: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Remove duplicate rows from a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    subset : List[str], optional
        Column labels to consider for identifying duplicates
        
    Returns
    -------
    pd.DataFrame
        DataFrame with duplicates removed
    """
    return df.drop_duplicates(subset=subset, keep='first').reset_index(drop=True)


def handle_missing_values(df: pd.DataFrame, strategy: str = 'drop', fill_value=None) -> pd.DataFrame:
    """
    Handle missing values in a DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    strategy : str, default 'drop'
        Strategy for handling missing values: 'drop', 'fill', or 'interpolate'
    fill_value : any, optional
        Value to use when strategy is 'fill'
        
    Returns
    -------
    pd.DataFrame
        DataFrame with missing values handled
    """
    df_clean = df.copy()
    
    if strategy == 'drop':
        df_clean = df_clean.dropna()
    elif strategy == 'fill':
        df_clean = df_clean.fillna(fill_value if fill_value is not None else 0)
    elif strategy == 'interpolate':
        df_clean = df_clean.interpolate(method='linear')
    else:
        raise ValueError(f"Unknown strategy: {strategy}. Use 'drop', 'fill', or 'interpolate'")
    
    return df_clean.reset_index(drop=True)


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize column names by converting to lowercase and replacing spaces with underscores.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
        
    Returns
    -------
    pd.DataFrame
        DataFrame with standardized column names
    """
    df_clean = df.copy()
    df_clean.columns = df_clean.columns.str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)
    return df_clean


def convert_to_datetime(df: pd.DataFrame, columns: List[str], format: Optional[str] = None) -> pd.DataFrame:
    """
    Convert specified columns to datetime format.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str]
        List of column names to convert
    format : str, optional
        Datetime format string
        
    Returns
    -------
    pd.DataFrame
        DataFrame with converted datetime columns
    """
    df_clean = df.copy()
    
    for col in columns:
        if col in df_clean.columns:
            df_clean[col] = pd.to_datetime(df_clean[col], format=format, errors='coerce')
    
    return df_clean


def filter_outliers(df: pd.DataFrame, column: str, n_std: float = 3) -> pd.DataFrame:
    """
    Filter outliers from a DataFrame based on standard deviation.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    column : str
        Column name to use for outlier detection
    n_std : float, default 3
        Number of standard deviations to use as threshold
        
    Returns
    -------
    pd.DataFrame
        DataFrame with outliers removed
    """
    df_clean = df.copy()
    
    if column in df_clean.columns and pd.api.types.is_numeric_dtype(df_clean[column]):
        mean = df_clean[column].mean()
        std = df_clean[column].std()
        df_clean = df_clean[
            (df_clean[column] >= mean - n_std * std) & 
            (df_clean[column] <= mean + n_std * std)
        ]
    
    return df_clean.reset_index(drop=True)
