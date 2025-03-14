import faiss
import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("transactions_with_embeddings.csv")

# Convert string embeddings to numpy arrays
df["Embeddings"] = df["Embeddings"].apply(eval)  # Convert string representation to list
embeddings = np.array(df["Embeddings"].tolist()).astype("float32")

# Initialize FAISS index (L2-based similarity search)
dimension = embeddings.shape[1]  # 384 for MiniLM
index = faiss.IndexFlatL2(dimension)

# Add embeddings to the FAISS index
index.add(embeddings)

# Save FAISS index for later use
faiss.write_index(index, "faiss_index.bin")
df.to_csv("indexed_transactions.csv", index=False)

print("FAISS index created and saved successfully!")
