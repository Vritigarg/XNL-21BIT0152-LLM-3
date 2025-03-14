from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np

# Load the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Load cleaned dataset
df = pd.read_csv("cleaned_fake_transactions.csv")

# Generate embeddings for transaction descriptions
df["Embeddings"] = df["Transaction_Description"].apply(lambda x: model.encode(x).tolist())

# Save dataset with embeddings
df.to_csv("transactions_with_embeddings.csv", index=False)

print("Embeddings generated and saved successfully!")
