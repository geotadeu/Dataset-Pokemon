import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('All_Pokemon_edit.csv')

# Teste de valores
df.shape
df.columns
df.describe()
df.dtypes

# Lendários
print(df['Legendary'].value_counts())
plt.figure(figsize=(8, 4))
sns.countplot(data=df, y='Legendary')
plt.show()

# Porcentagem dos lendarios e dos Normais
fig = plt.figure(figsize=(5, 5))
ax = fig.add_axes([0, 0, 1, 1])
ax.axis('equal')
Survived = df.Legendary.value_counts()
labels = ['Normal', 'Legendary']
ax.pie(Survived, labels=labels, autopct='%1.2f%%', colors=['skyblue', 'red'])
plt.show()

# Numeros de tipos usando nunique()
print('Numeros de Tipos: ', df.Type_1.nunique())
# Tipos usando unique()
print('Tipos: ', df.Type_1.unique())


# Plotar o Type_1 (Tipos 1 principais)
plt.figure(figsize=(12, 6))
sns.countplot(data=df, x='Type_1')
plt.show()
