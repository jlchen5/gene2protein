import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def load_dataset(filename):
    """Load and return the dataset from a CSV file."""
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def split_dataset(data, feature_col, target_col, test_size=0.2, random_state=None):
    """Split the dataset into training and testing sets."""
    X = data[feature_col].values.reshape(-1, 1)
    y = data[target_col].values
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_and_evaluate(X_train, X_test, y_train, y_test):
    """Train a linear regression model and evaluate it using mean squared error."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    return model, mse

# Main script
if __name__ == "__main__":
    # Load the dataset
    data = load_dataset('gene_protein_data.csv')
    if data is not None:
        # Split the dataset
        X_train, X_test, y_train, y_test = split_dataset(data, 'Gene_Expression', 'Protein_Expression', 0.2, 42)

        # Train the model and evaluate its performance
        model, mse = train_and_evaluate(X_train, X_test, y_train, y_test)
        print("Mean Squared Error:", mse)


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
