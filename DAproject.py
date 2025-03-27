import pandas as pd
data = pd.read_csv('Coffee_company.csv')
data.columns = data.columns.str.strip()#去除 data 这个 DataFrame 所有列名（columns）的前后空格，确保列名的格式干净整洁
print(data.head())

data['Units Sold'] = data['Units Sold'].astype(int)
print(data.head())

print(data.columns) # to check the exact name of each column
data.rename(columns={'Month Name':'Month'}, inplace = True)
print(data.head())

#这行代码的作用是 将 data['Sales'] 列的字符串数据转换为数值型（float），同时去掉 "$" 和 "," 符号，以便进行数学运算。
data['Sales'] = pd.to_numeric(data['Sales'].str.replace(',', '', regex=False).str.replace('$', '', regex=False), errors='coerce')
data['Sales'] = data['Sales'].astype(float)
total_sales = data['Sales'].sum()
print("Total Sales: $", total_sales)


# Convert 'Date' to datetime format
data['Date'] = pd.to_datetime(data['Date'], format='%d/%m/%Y')

# Set 'Date' as the index
data.set_index('Date', inplace=True)

# Calculate quarterly sales
quarterly_sales = data['Sales'].resample('Q').sum().reset_index() #这行代码的作用是 按季度（Q）对 Sales 进行重采样并求和，即计算每个季度的总销售额。
quarterly_sales.columns = ['Quarter', 'Total Sales']#重命名列名

print(quarterly_sales)