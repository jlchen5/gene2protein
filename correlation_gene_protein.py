import pandas as pd

def load_data(file_name, column_name):
    """Load and return a specific column from a CSV file."""
    try:
        data = pd.read_csv(file_name)
        return data[column_name]
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def calculate_correlation(series1, series2):
    """Calculate and return the correlation between two data series."""
    return series1.corr(series2)

# Main script
if __name__ == "__main__":
    # Load data
    gene_expression_levels = load_data('gene_expression_data.csv', 'Expression')
    protein_abundance = load_data('protein_data.csv', 'Abundance')

    if gene_expression_levels is not None and protein_abundance is not None:
        # Perform analysis
        correlation = calculate_correlation(gene_expression_levels, protein_abundance)
        print("Correlation between gene expression and protein translation efficiency:", correlation)


# 读取基因表达量数据
gene_expression_data = pd.read_csv('gene_expression_data.csv')

# 读取蛋白质谱数据
protein_data = pd.read_csv('protein_data.csv')

# 基因表达量分析
gene_expression_levels = gene_expression_data['Expression']

# 蛋白质谱分析
protein_abundance = protein_data['Abundance']

# 进行进一步的分析和评估

# 例如，计算基因表达和蛋白质翻译效率的相关性
correlation = gene_expression_levels.corr(protein_abundance)
print("Correlation between gene expression and protein translation efficiency:", correlation)
