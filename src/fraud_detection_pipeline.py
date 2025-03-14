import faiss
import numpy as np
import pandas as pd
import smtplib
from sentence_transformers import SentenceTransformer

np.random.seed(42)

# Load FAISS index and dataset
index = faiss.read_index("faiss_index.bin")
df = pd.read_csv("indexed_transactions.csv")

# Set FAISS parameters for deterministic search
index.nprobe = 10
faiss.omp_set_num_threads(1)  # Single-threaded for stability

# Load the embedding model
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Set similarity threshold
SIMILARITY_THRESHOLD = 1.05  # Adjust based on testing

# Fraud-related keywords
FRAUD_KEYWORDS = ["unauthorized", "fraud", "scam", "suspicious", "lottery", "hacked"]
SAFE_KEYWORDS = ["salary", "deposit", "credit card", "bill payment"]


# 🚨 Email Alert Function
def send_email_alert(fraud_case):
    sender = "vriti.garg2021@vitstudent.ac.in"
    receiver = "kanhapyasi2@gmail.com"
    password = "toby cxta melc evtu"  # Use App Password, not actual password

    subject = "Fraud Alert - Suspicious Transaction"
    body = f"Suspicious transaction detected:\n{fraud_case}"

    message = f"Subject: {subject}\nMIME-Version: 1.0\nContent-Type: text/plain; charset=utf-8\n\n{body}"

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(sender, receiver, message)
        print("📩 Fraud alert email sent!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")


# Fraud detection functions
def is_fraudulent_by_keyword(transaction):
    """Check if transaction contains high-risk fraud keywords."""
    transaction_text = transaction.get("description", "").lower()
    return any(word in transaction.lower() for word in FRAUD_KEYWORDS)

def is_safe_transaction(transaction):
    """Check if transaction contains trusted words and should not be flagged."""
    transaction_text = str(transaction).lower()  # Ensure it's a string
    return any(word in transaction.lower() for word in SAFE_KEYWORDS)

def detect_fraud(new_transaction, top_n=5):
    """Detects fraud by checking similarity with past transactions + keyword check."""
    print(f"✅ Running fraud detection for: {new_transaction}")

    # Step 1: Keyword-Based Fraud Detection
    keyword_flag = is_fraudulent_by_keyword(new_transaction)

    # Step 2: Skip FAISS if Transaction is Safe
    if is_safe_transaction(new_transaction):
        print(f"✅ SAFE TRANSACTION: {new_transaction}")
        return pd.DataFrame(
            {"Transaction_Description": [new_transaction], "Similarity_Score": [None], "Anomalous": [False]})

    # Step 3: FAISS-Based Similarity Detection
    transaction_embedding = np.array([model.encode(new_transaction)]).astype("float32")
    faiss.normalize_L2(transaction_embedding)  # Normalize embedding

    distances, indices = index.search(transaction_embedding, top_n)

    # Step 4: Retrieve matching transactions
    similar_transactions = df.iloc[indices[0]].copy()
    similar_transactions["Similarity_Score"] = distances[0]

    # Step 5: Flag anomalies based on similarity score
    similar_transactions["Anomalous"] = similar_transactions["Similarity_Score"] > SIMILARITY_THRESHOLD

    # Final Decision
    if similar_transactions["Anomalous"].any() or keyword_flag:
        print(f"⚠️ FRAUD ALERT: {new_transaction} detected as high-risk!")

        # 🚨 Send Email Alert
        send_email_alert(new_transaction)

    return similar_transactions


# Load **real dataset**
real_df = pd.read_csv("realistic_transactions.csv")  # Update filename if needed

# List of transactions to check
transactions_to_check = real_df["Transaction_Description"].head(5).tolist()

# Store flagged transactions
flagged_transactions = []

for transaction in transactions_to_check:
    results = detect_fraud(transaction)
    flagged = results[results["Anomalous"]]  # Filter fraudulent transactions

    if not flagged.empty:
        flagged_transactions.append(flagged)

# Save flagged transactions to CSV
if flagged_transactions:
    flagged_df = pd.concat(flagged_transactions, ignore_index=True)
    flagged_df.to_csv("flagged_transactions_test.csv", index=False)
    print("🚨 Flagged transactions saved to 'flagged_transactions_test.csv'!")
else:
    print("✅ No fraudulent transactions detected.")




