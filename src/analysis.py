from scipy import stats
import pandas as pd

def calculate_correlation(gene_exp: pd.Series, protein_abun: pd.Series) -> dict:
    """多维度相关性分析"""
    return {
        'pearson': gene_exp.corr(protein_abun),
        'spearman': gene_exp.corr(protein_abun, method='spearman'),
        'kendall': stats.kendalltau(gene_exp, protein_abun)[0]
    }

def differential_analysis(df: pd.DataFrame, group_col: str) -> pd.DataFrame:
    """差异表达分析"""
    return df.groupby(group_col).agg({
        'Expression': ['mean', 'std'],
        'Normalized': ['median', 'quantile']
    })
