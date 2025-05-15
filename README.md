# gene2protein: Gene-Protein Relationship Analysis

## Overview

This project involves the analysis of biological data, specifically looking at the relationship between gene expression levels and protein abundance. The goal is to understand how gene expression levels correlate with protein production in cells, and to build a predictive model for protein expression based on gene expression data.

# Gene2Protein: Gene-Protein Relationship Analysis Toolkit

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A bioinformatics toolkit for analyzing relationships between gene expression levels and protein abundance.

## Features

- **数据预处理**
  - 基因表达数据标准化 (log2转换)
  - 低表达基因过滤 (可配置阈值)
  - 自动化数据验证 (格式/完整性检查)

- **预测建模**
  - 多项式特征工程 (支持非线性关系)
  - 正则化回归 (RidgeCV自动调参)
  - 端到端预测Pipeline

- **分析工具**
  - 多维度相关性分析 (Pearson/Spearman/Kendall)
  - 差异表达分析 (分组统计)
  - 内存优化处理 (HDF5格式支持)

## Installation

```bash
# 克隆项目
git clone https://github.com/jlchen5/gene2protein.git

# 安装依赖
cd gene2protein
pip install -r requirements.txt

# 验证安装
python -c "from src.data_processor import DataProcessor; print('Installation successful!')"
```

## Quick Start
### 数据预处理
~~~
from src.data_processor import DataProcessor

processor = DataProcessor()
raw_data = processor.load_raw_data("data/raw/gene_expression_data.csv")
normalized_data = processor.normalize_expression(raw_data)
filtered_data = processor.filter_low_expression(normalized_data, threshold=5.0)
~~~

### 模型训练
~~~
from src.modeling import build_regression_model
import numpy as np

# 准备数据
X = np.array(filtered_data['Normalized']).reshape(-1, 1)
y = protein_abundance_values  # 从protein_data.csv加载

# 构建模型
model = build_regression_model(degree=2)
model.fit(X, y)
~~~

### 结果分析
~~~
from src.analysis import calculate_correlation

corr_results = calculate_correlation(filtered_data['Normalized'], y)
print(f"Pearson Correlation: {corr_results['pearson']:.3f}")
~~~

## Advanced Usage
### 配置管理
- 修改config.yaml自定义参数：
~~~
model_params:
  polynomial_degree: 3       # 多项式次数
  regularization: [0.1, 1, 10] # 正则化强度

analysis:
  expression_threshold: 5.0  # 表达量过滤阈值
~~~

### 批量处理
~~~
# 使用HDF5存储优化大数据
filtered_data.to_hdf('data/processed/normalized.h5', key='gene_exp', mode='w')
~~~

## License
This project is available under the MIT License. See the LICENSE file in the repository for full details.


