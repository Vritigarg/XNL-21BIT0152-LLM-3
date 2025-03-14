import time
from sklearn.metrics import accuracy_score

def detect_fraud(transaction):
    """
    Placeholder function for LLM-based fraud detection.
    Replace this with the actual fraud detection logic.
    """
    return 1 if transaction["amount"] > 7000 else 0

# Step 2.2: Measure Accuracy

# Actual Labels (1 = Fraud, 0 = Safe)
y_true = [1, 0, 0, 1, 1]

# Predictions from LLM-Based Model
y_pred_llm = [1, 0, 0, 1, 1]

# Calculate Accuracy
accuracy_llm = accuracy_score(y_true, y_pred_llm)
print(f"LLM-Based Fraud Detection Accuracy: {accuracy_llm:.2f}")

# Step 3.1: Compare Accuracy & Speed

# Predictions from Rule-Based Model
y_pred_rule_based = [1, 0, 1, 1, 0]

# Calculate Accuracy for Rule-Based Model
accuracy_rule_based = accuracy_score(y_true, y_pred_rule_based)
print(f"Rule-Based Accuracy: {accuracy_rule_based:.2f}")
print(f"LLM-Based Accuracy: {accuracy_llm:.2f}")

# Speed Comparison
start_rule = time.time()
for txn in range(1000000):
    _ = 1 if txn > 5000 else 0
end_rule = time.time()

start_llm = time.time()
for txn in range(1000000):
    detect_fraud({"description": "random", "amount": txn})
end_llm = time.time()

print(f"Rule-Based Time: {end_rule - start_rule:.6f} sec")
print(f"LLM-Based Time: {end_llm - start_llm:.6f} sec")
