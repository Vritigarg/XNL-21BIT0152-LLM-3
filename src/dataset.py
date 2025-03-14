import pandas as pd
import random
import faker

fake = faker.Faker()

# Transaction categories
transaction_types = [
    "Amazon Purchase", "Walmart Shopping", "Gas Station Payment",
    "PayPal Transfer", "Suspicious Wire Transfer", "Credit Card Payment"
]


# Function to generate random transactions
def generate_transaction(transaction_id):
    user_id = random.randint(1000, 5000)
    transaction_type = random.choice(transaction_types)
    amount = round(random.uniform(5, 10000), 2)  # Amounts between $5 and $10,000
    location = fake.city() + ", " + fake.country()
    timestamp = fake.date_time_this_year().strftime("%Y-%m-%d %H:%M:%S")
    description = f"{transaction_type} ${amount}"

    return {
        "Transaction_ID": transaction_id,
        "User_ID": user_id,
        "Transaction_Description": description,
        "Amount": amount,
        "Location": location,
        "Timestamp": timestamp
    }


# Generate 1 million transactions
num_records = 10000
data = [generate_transaction(i) for i in range(num_records)]

# Create DataFrame
df = pd.DataFrame(data)

# Save dataset to CSV
df.to_csv("fake_transactions.csv", index=False)

print("Dataset generated successfully!")
