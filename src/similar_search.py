import faiss
import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer

# Load FAISS index and dataset
index = faiss.read_index("faiss_index.bin")
df = pd.read_csv("indexed_transactions.csv")

# Load the same embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Define a similarity threshold (adjust based on dataset analysis)
SIMILARITY_THRESHOLD = 0.85  # Adjust as needed (0.7 means 70% similarity)

def find_similar_transactions(query_text, top_n=5):
    # Generate embedding for the query
    query_embedding = np.array([model.encode(query_text)]).astype("float32")

    # Search for top N similar transactions
    distances, indices = index.search(query_embedding, top_n)

    # Convert FAISS distances to similarity scores
    similarity_scores = 1 / (1 + distances)  # Normalize distance to similarity

    # Get similar transactions
    similar_transactions = df.iloc[indices[0]].copy()
    similar_transactions["Similarity_Score"] = similarity_scores[0]

    # Flag anomalies (low similarity score)
    similar_transactions["Anomalous"] = similar_transactions["Similarity_Score"] < SIMILARITY_THRESHOLD

    return similar_transactions

# Example usage
query = "suspicious wire transfer 5000"
results = find_similar_transactions(query)

print("Similar Transactions Found:")
print(results[["Transaction_Description", "Amount", "Similarity_Score", "Anomalous"]])

