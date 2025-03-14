# XNL-21BIT0152-LLM-3
## LLM-Powered Fraud Detection & Anomaly Analysis
### 📌 Project Overview
## This project leverages LLM embeddings and transformer models to analyze transaction descriptions, detect anomalies, and flag potential fraudulent activities.The system integrates with a vector database to enable rapid anomaly identification through similarity search.
###  📌Part 1: DATA PREPARATION AND FEATURE ENGINEERING
### 1.1 Simulate a Transaction Dataset
##### Generated synthetic transaction data with metadata (e.g., transaction descriptions, amount, timestamp, merchant category, etc.).
##### Preprocessing Steps:
##### Text cleaning (removing special characters, lowercasing)
##### Tokenization for LLM input
##### Handling missing values and outliers
### 1.2 Generate Embeddings
#### A pretrained transformer model, here I have used "sentence-transformers/all-MiniLM-L6-v2"
##### Steps:
##### Convert transaction descriptions into vector embeddings.
##### Batch process and store embeddings in a database for efficient retrieval.

###  📌PART 2: INTEGRATION WITH A VECTOR DATABASE
### 2.1 Set Up a Vector Database, here I have used FAISS
##### Steps:
##### Configure vector database and upload embeddings.
##### Index the data for optimized similarity search.
### 2.2 Implement Similarity Search for Anomaly Detection
##### Query mechanism retrieves similar transactions based on embeddings.
##### Defined similarity thresholds to differentiate between normal and anomalous clusters., like in this case I have defined threshold value as 1.05 to maintain a balance
##### In this Project I have used FAISS for similarity Search plus I have manually also used keyword Search (like words like "unauthorized","hacked") are also detected as fraud
##### Flag transactions that deviate significantly from known pattern

###  📌PART 3: DEVELOP THE FRAUD DETECTION PIPELINE
### 3.1 Build a Processing Pipeline
#### Workflow:
#### Ingest new transactions
#### Compute embeddings
#### Perform similarity search
#### Flag anomalies
#### Implement robust error handling to ensure reliability.
### 3.2 Implement Alert Generation
#### Generated an Email System where if the Transaction is detected Anamolous, the person is alerted via Email, this is only done for the sole purpose of Testing
![Image](https://github.com/user-attachments/assets/d74108b3-7a98-4174-99a1-e78efcb3c51b)

![Image](https://github.com/user-attachments/assets/d455b4c8-e4df-4228-9164-41153e2132e3)

This is the alert system That I Made that if any transaction is detected fraud it will send an email to that person
![Image](https://github.com/user-attachments/assets/aaadbbc9-869e-4261-993d-63acb99dc70b)

###  📌PART 4: TESTING & PERFORMANCE EVALUATION
### 4.1 Develop a Comprehensive Test Suite
#### Unit and integration tests to simulate normal and fraudulent transactions.
### 4.2 Conduct Comparative Analysis
#### Compare detection performance of LLM-based approach vs. rule-based/statistical methods.
