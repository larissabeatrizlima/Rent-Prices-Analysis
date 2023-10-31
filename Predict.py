import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

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

# Splitting train data
X = data.drop(['Total Value'], axis=1)
y = data['Total Value']

# 80/20 splitting for training
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2)

train_data = X_train.join(y_train)

# Print the correlation matrix
plt.figure(figsize=(15,8))
correlation_matrix = sns.heatmap(train_data.select_dtypes(include=[np.number]).corr(), annot=True, cmap='YlGnBu')

plt.show()

######## Data Preprocessing
train_data['qtd_quartos'] = np.log(train_data['qtd_quartos'] + 1)
train_data['qtd_banheiros'] = np.log(train_data['qtd_quartos'] + 1)
train_data['qtd_vagas'] = np.log(train_data['qtd_quartos'] + 1)