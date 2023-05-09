import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# 读取数据集，其中features是基因表达量，target是对应的蛋白表达量
data = pd.read_csv('gene_protein_data.csv')

# 分割数据集为训练集和测试集
X = data['Gene_Expression'].values.reshape(-1, 1)  # 特征值（基因表达量）
y = data['Protein_Expression'].values  # 目标值（蛋白表达量）
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 创建线性回归模型
model = LinearRegression()

# 训练模型
model.fit(X_train, y_train)

# 在测试集上进行预测
y_pred = model.predict(X_test)

# 评估模型性能
mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)
