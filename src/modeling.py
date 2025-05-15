from sklearn.pipeline import Pipeline
from sklearn.linear_model import RidgeCV
from sklearn.preprocessing import PolynomialFeatures, StandardScaler

def build_regression_model(degree: int = 2) -> Pipeline:
    """构建基因-蛋白表达预测模型"""
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('scaler', StandardScaler()),
        ('regressor', RidgeCV(alphas=np.logspace(-3, 3, 20)))
    ])

class ProteinPredictor:
    """蛋白质表达预测器"""
    
    def __init__(self, model):
        self.model = model
        
    def train(self, X, y):
        """模型训练"""
        self.model.fit(X, y)
        
    def predict(self, X):
        """表达量预测"""
        return self.model.predict(X)
