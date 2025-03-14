import pytest
import numpy as np
import faiss
import pandas as pd
from sentence_transformers import SentenceTransformer
from fraud_detection_pipeline import detect_fraud, is_fraudulent_by_keyword, is_safe_transaction

# Sample test transactions
TEST_TRANSACTIONS = [
    ("hacked $5000", True),  # Fraudulent
    ("lottery winnings $10000", True),  # Fraudulent
    ("salary $2500", False),  # Safe
    ("bill payment $1200", False),  # Safe
    ("unauthorized withdrawal $3000", True),  # Fraudulent
]


def test_keyword_based_detection():
    """Test if keyword-based fraud detection works correctly."""
    for transaction, expected in TEST_TRANSACTIONS:
        assert is_fraudulent_by_keyword(transaction) == expected


def test_safe_transaction_detection():
    """Test if safe transactions are correctly identified."""
    for transaction, expected in TEST_TRANSACTIONS:
        assert is_safe_transaction(transaction) == (not expected)


@pytest.fixture(scope="module")
def setup_faiss():
    """Setup FAISS index and embedding model for testing."""
    index = faiss.read_index("faiss_index.bin")
    model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
    return index, model


def test_faiss_similarity_search(setup_faiss):
    """Test if FAISS-based similarity search works correctly."""
    index, model = setup_faiss

    test_transaction = "suspicious transfer $4500"
    transaction_embedding = np.array([model.encode(test_transaction)]).astype("float32")
    faiss.normalize_L2(transaction_embedding)

    distances, indices = index.search(transaction_embedding, 5)
    assert len(distances[0]) == 5  # Should return top 5 results
    assert all(d >= 0 for d in distances[0])  # Distances should be non-negative
