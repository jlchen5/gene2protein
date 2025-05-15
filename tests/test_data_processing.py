import pytest
from src.data_processor import DataProcessor

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'GeneID': ['ENSG000001', 'ENSG000002'],
        'Expression': [10.5, 3.2]
    })

def test_normalization(sample_data):
    processor = DataProcessor()
    normalized = processor.normalize_expression(sample_data)
    assert 'Normalized' in normalized.columns
    assert normalized['Normalized'].min() >= 3.0
