import pandas as pd

# Считываем данные из CSV файла
data = pd.read_csv('layerzero.csv')

# Записываем данные в XLSX файл
data.to_excel('layerzero.xlsx', index=False)