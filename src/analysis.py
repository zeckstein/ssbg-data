"""
Analysis utilities for SSBG data.

This module provides common analysis functions for data exploration and statistics.
"""

import pandas as pd
import numpy as np
from typing import List, Optional


def get_summary_statistics(df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Get summary statistics for DataFrame columns.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str], optional
        Specific columns to analyze (default: all numeric columns)
        
    Returns
    -------
    pd.DataFrame
        Summary statistics
    """
    if columns:
        return df[columns].describe()
    return df.describe()


def calculate_correlation(df: pd.DataFrame, columns: Optional[List[str]] = None, method: str = 'pearson') -> pd.DataFrame:
    """
    Calculate correlation matrix for DataFrame columns.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str], optional
        Specific columns to analyze (default: all numeric columns)
    method : str, default 'pearson'
        Correlation method: 'pearson', 'kendall', or 'spearman'
        
    Returns
    -------
    pd.DataFrame
        Correlation matrix
    """
    if columns:
        return df[columns].corr(method=method)
    return df.corr(method=method)


def group_and_aggregate(df: pd.DataFrame, group_by: List[str], agg_dict: dict) -> pd.DataFrame:
    """
    Group DataFrame by columns and apply aggregations.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    group_by : List[str]
        Columns to group by
    agg_dict : dict
        Dictionary mapping column names to aggregation functions
        
    Returns
    -------
    pd.DataFrame
        Aggregated DataFrame
    """
    return df.groupby(group_by).agg(agg_dict).reset_index()


def find_missing_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identify missing data in DataFrame.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
        
    Returns
    -------
    pd.DataFrame
        DataFrame with missing data counts and percentages
    """
    missing_count = df.isnull().sum()
    missing_percent = (missing_count / len(df)) * 100
    
    missing_df = pd.DataFrame({
        'column': missing_count.index,
        'missing_count': missing_count.values,
        'missing_percent': missing_percent.values
    })
    
    return missing_df[missing_df['missing_count'] > 0].sort_values('missing_count', ascending=False)


def get_unique_counts(df: pd.DataFrame, columns: Optional[List[str]] = None) -> pd.DataFrame:
    """
    Get count of unique values for DataFrame columns.
    
    Parameters
    ----------
    df : pd.DataFrame
        Input DataFrame
    columns : List[str], optional
        Specific columns to analyze (default: all columns)
        
    Returns
    -------
    pd.DataFrame
        DataFrame with unique value counts
    """
    cols_to_check = columns if columns else df.columns.tolist()
    
    unique_counts = pd.DataFrame({
        'column': cols_to_check,
        'unique_count': [df[col].nunique() for col in cols_to_check],
        'total_count': [df[col].count() for col in cols_to_check]
    })
    
    unique_counts['unique_percent'] = (unique_counts['unique_count'] / unique_counts['total_count']) * 100
    
    return unique_counts
