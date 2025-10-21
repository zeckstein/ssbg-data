"""
Data loading utilities for SSBG data analysis.

This module provides functions to load data from various file formats.
"""

import pandas as pd
from pathlib import Path
from typing import Optional, Union


def load_csv(filepath: Union[str, Path], **kwargs) -> pd.DataFrame:
    """
    Load data from a CSV file.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the CSV file
    **kwargs
        Additional arguments to pass to pd.read_csv()
        
    Returns
    -------
    pd.DataFrame
        Loaded data
    """
    return pd.read_csv(filepath, **kwargs)


def load_excel(filepath: Union[str, Path], sheet_name: Optional[str] = None, **kwargs) -> pd.DataFrame:
    """
    Load data from an Excel file.
    
    Parameters
    ----------
    filepath : str or Path
        Path to the Excel file
    sheet_name : str, optional
        Name of the sheet to load (default: first sheet)
    **kwargs
        Additional arguments to pass to pd.read_excel()
        
    Returns
    -------
    pd.DataFrame
        Loaded data
    """
    return pd.read_excel(filepath, sheet_name=sheet_name, **kwargs)


def save_csv(df: pd.DataFrame, filepath: Union[str, Path], **kwargs) -> None:
    """
    Save DataFrame to a CSV file.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to save
    filepath : str or Path
        Path to save the CSV file
    **kwargs
        Additional arguments to pass to df.to_csv()
    """
    df.to_csv(filepath, index=False, **kwargs)


def save_excel(df: pd.DataFrame, filepath: Union[str, Path], sheet_name: str = 'Sheet1', **kwargs) -> None:
    """
    Save DataFrame to an Excel file.
    
    Parameters
    ----------
    df : pd.DataFrame
        DataFrame to save
    filepath : str or Path
        Path to save the Excel file
    sheet_name : str, default 'Sheet1'
        Name of the sheet
    **kwargs
        Additional arguments to pass to df.to_excel()
    """
    df.to_excel(filepath, sheet_name=sheet_name, index=False, **kwargs)


def get_data_path(filename: str, data_type: str = 'raw') -> Path:
    """
    Get the full path to a data file.
    
    Parameters
    ----------
    filename : str
        Name of the data file
    data_type : str, default 'raw'
        Type of data directory: 'raw' or 'processed'
        
    Returns
    -------
    Path
        Full path to the data file
    """
    base_path = Path(__file__).parent.parent / 'data'
    
    if data_type == 'raw':
        return base_path / 'raw' / filename
    elif data_type == 'processed':
        return base_path / 'processed' / filename
    else:
        raise ValueError(f"Unknown data_type: {data_type}. Use 'raw' or 'processed'")
