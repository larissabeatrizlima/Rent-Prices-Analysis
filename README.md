# Rent Prices Analysis

This Python script explores a dataset of rent prices, performs data preprocessing, and creates visualizations to gain insights into the data. The script is intended to prepare the data for further analysis and prediction using machine learning.

## Getting Started

### Prerequisites

Before running this code, make sure you have the following libraries installed:

- Pandas
- NumPy
- Matplotlib
- Seaborn
- Geopandas

You can install these libraries using `pip`:
```shell
pip install pandas numpy matplotlib seaborn geopandas
```

## Exploring Data
The script starts by loading a CSV file containing data about rental properties. It explores the dataset to understand its structure and properties.

### Data Preprocessing
Conversion of data types

Handling missing values in 'condominio' and 'qtd_vagas'

Calculation of 'Total Value' as the sum of 'valor' and 'condominio'

Exploration of the top 10 most announced neighborhoods

Visualization: Bar chart showing the top 10 neighborhoods with the most property listings.

Correlation Matrix
:Heatmap displaying the correlation between numerical variables.

## Next Steps

The next steps for this project include building a predictive analysis using Scikit-Learn to make predictions about rent prices based on the provided data.

## Acknowledgements

This project was created with inspiration from the following sources:

Cauê Marchionatti Ausec (github.com/strangercacaus).
