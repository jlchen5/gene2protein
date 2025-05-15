from typing import Optional, Tuple
import pandas as pd
import numpy as np

class DataProcessor:
    """基因表达数据预处理模块"""
    
    @staticmethod
    def load_raw_data(path: str) -> Optional[pd.DataFrame]:
        """加载原始数据并验证格式"""
        try:
            df = pd.read_csv(path, usecols=['GeneID', 'Expression'])
            if not {'GeneID', 'Expression'}.issubset(df.columns):
                raise ValueError("Missing required columns")
            return df
        except FileNotFoundError:
            print(f"数据文件 {path} 未找到")
            return None

    def normalize_expression(self, df: pd.DataFrame) -> pd.DataFrame:
        """应用log2归一化处理"""
        df['Normalized'] = np.log2(df['Expression'] + 1)
        return df.dropna()

    def filter_low_expression(self, df: pd.DataFrame, threshold: float = 5.0) -> pd.DataFrame:
        """过滤低表达基因"""
        return df[df['Normalized'] >= threshold]
