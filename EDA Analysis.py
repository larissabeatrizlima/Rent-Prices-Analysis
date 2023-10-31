import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import geopandas

############# EXPLORING DATA ################

# Load CSV
data = pd.read_csv('/Users/larissalima/Developer/Github/Rent Prices/archive/data/dataset.csv',index_col=0)
print(data.head())

dtypes = {
        'data': 'datetime64[s]',
        'fonte':'str',
        'descricao': 'str',
        'endereco':'str',
        'rua': 'str',
        'numero': 'float',
        'bairro':'category',
        'cidade': 'category',
        'valor':'float',
        'periodicidade': 'category',
        'condominio': 'float',
        'area':'float',
        'qtd_banheiros': 'float',
        'qtd_quartos':'float',
        'qtd_vagas':'float',
        'url':'str'
        }

# Convert data types
for column, dtype in dtypes.items():
    if dtype == 'datetime64[s]':
        data[column] = pd.to_datetime(data[column])
    elif dtype == 'str':
        data[column] = data[column].astype(str)
    elif dtype == 'float':
        data[column] = pd.to_numeric(data[column], errors='coerce')
    elif dtype == 'category':
        data[column] = data[column].astype('category')

# Knowledge data
print(data.info())

data = data.drop('fonte', axis=1)

# Replacing null values with 0 -> assuming that the null don't charge for condo and don't have garage
data['condominio'].fillna(0, inplace=True)
data['qtd_vagas'].fillna(0, inplace=True)

# Getting total value = Rent + Condo
data['Total Value'] = data['valor'] + data['condominio']

# Knowing the neighborhoods more announced

# Count the occurrences of each 'bairro' and select the top 10
top_10_bairros = data['bairro'].value_counts().head(10)

# Create a bar chart
plt.figure(figsize=(15, 8))
ax = top_10_bairros.plot(kind='bar', color='skyblue')
plt.title('Top 10 More Announced Neigborhoods')
plt.xlabel('Neigborhoods')
plt.ylabel('Count of announces')
plt.xticks(rotation=45)

# Add labels to the bars
for i, count in enumerate(top_10_bairros):
    ax.text(i, count + 1, str(count), ha='center', va='bottom')

plt.show()

# Print the correlation matrix for variables
plt.figure(figsize=(15,8))
correlation_matrix = sns.heatmap(data.select_dtypes(include=[np.number]).corr(), annot=True, cmap='YlGnBu')
