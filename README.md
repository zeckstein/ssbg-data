# SSBG Data Analysis Project

Analysis of publicly available SSBG data using Python, Jupyter notebooks, and custom data cleaning functions.

## Project Structure

```
ssbg-data/
├── data/
│   ├── raw/              # Raw data files (manually add your SSBG data here)
│   └── processed/        # Cleaned and processed data files
├── notebooks/            # Jupyter notebooks for analysis
│   └── 01_exploratory_data_analysis.ipynb
├── src/                  # Python modules with helper functions
│   ├── __init__.py
│   ├── cleaning.py       # Data cleaning utilities
│   ├── data_loader.py    # Data loading and saving utilities
│   └── analysis.py       # Analysis and statistics utilities
├── requirements.txt      # Python dependencies
└── README.md
```

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/zeckstein/ssbg-data.git
cd ssbg-data
```

2. Install required Python packages:
```bash
pip install -r requirements.txt
```

### Adding Data

1. Manually download your SSBG data files
2. Place them in the `data/raw/` directory
3. The raw data files are gitignored to prevent accidentally committing large datasets

### Usage

#### Using Jupyter Notebooks

1. Start Jupyter Notebook:
```bash
jupyter notebook
```

2. Open `notebooks/01_exploratory_data_analysis.ipynb`
3. Follow the template to load, clean, analyze, and visualize your data

#### Using Helper Functions

The `src/` directory contains several utility modules:

**Data Loading (`src/data_loader.py`)**:
- `load_csv()`: Load data from CSV files
- `load_excel()`: Load data from Excel files
- `save_csv()`: Save DataFrame to CSV
- `save_excel()`: Save DataFrame to Excel
- `get_data_path()`: Get full path to data files

**Data Cleaning (`src/cleaning.py`)**:
- `remove_duplicates()`: Remove duplicate rows
- `handle_missing_values()`: Handle missing data with various strategies
- `standardize_column_names()`: Standardize column names
- `convert_to_datetime()`: Convert columns to datetime format
- `filter_outliers()`: Remove outliers based on standard deviation

**Analysis (`src/analysis.py`)**:
- `get_summary_statistics()`: Get descriptive statistics
- `calculate_correlation()`: Calculate correlation matrix
- `group_and_aggregate()`: Group and aggregate data
- `find_missing_data()`: Identify missing data
- `get_unique_counts()`: Count unique values

#### Example Usage

```python
from src.data_loader import load_csv, get_data_path
from src.cleaning import standardize_column_names, remove_duplicates
from src.analysis import get_summary_statistics

# Load data
df = load_csv(get_data_path('your_data.csv', data_type='raw'))

# Clean data
df = standardize_column_names(df)
df = remove_duplicates(df)

# Analyze
summary = get_summary_statistics(df)
print(summary)
```

## Contributing

Feel free to open issues or submit pull requests with improvements.

## License

See LICENSE file for details.
