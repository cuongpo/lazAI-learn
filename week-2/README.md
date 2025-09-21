# LazAI/Alith Data Upload and Inference

This project demonstrates how to upload encrypted data to IPFS using LazAI/Alith framework and then use the uploaded data for inference.

## Prerequisites

- Python 3.8 or higher
- A LazAI wallet with private key
- Pinata IPFS JWT token
- Testnet tokens for gas fees (get from https://t.me/lazai_testnet_bot)

## Setup Instructions

### 1. Python Environment Setup

First, create and activate a Python virtual environment:

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### 2. Install Alith

Install the Alith framework and required dependencies:

```bash
# Install alith
python3 -m pip install alith -U

```

### 3. Environment Configuration

Set up your environment variables for authentication:

```bash
# Export your LazAI private key
export PRIVATE_KEY=""

# Export your Pinata IPFS JWT token
export IPFS_JWT=""
```

**Note:** Replace `your_lazai_private_key_here` and `your_pinata_jwt_token_here` with your actual credentials.

### 4. Run Data Upload (Dat.py)

Execute the data upload script to encrypt and upload your privacy data to IPFS and mint DAT:

```bash
python Dat.py
```

This script will:
1. Encrypt your privacy data using your wallet signature
2. Upload the encrypted data to IPFS via Pinata
3. Register the file with LazAI
4. Print the **File ID** which you'll need for inference

**Expected Output:**
```
File ID: [some_number]
```

**Important:** Save the File ID that is printed - you'll need it for the next step.

### 5. Run Inference (inference.py)

Use the File ID from the previous step to run inference on your uploaded data:

```bash
python inference.py
```

Replace `[FILE_ID]` with the actual File ID you received from the previous step.

## Troubleshooting

### Common Issues

1. **Environment Variables Not Set**
   - Make sure you've exported both `PRIVATE_KEY` and `IPFS_JWT`
   - You can verify by running: `echo $PRIVATE_KEY` and `echo $IPFS_JWT`

2. **Virtual Environment Not Activated**
   - Ensure your virtual environment is activated (you should see `(venv)` in your terminal prompt)
   - If not activated, run: `source venv/bin/activate`

### Getting Your Credentials

1. **LazAI Private Key**:
   - This is your wallet's private key from the your EVM wallet
   - Keep this secure and never share it

2. **Pinata IPFS JWT Token**:
   - Sign up at [Pinata](https://pinata.cloud/)
   - Go to your API keys section
   - Create a new JWT token
   - Copy the token and use it as your `IPFS_JWT`

## Project Structure

```
laztest/
├── venv/                 # Python virtual environment
├── Dat.py               # Data upload script
├── inference.py         # Inference script (you'll create this)
├── README.md           # This file
└── requirements.txt    # Dependencies (optional)
```


## Assignment Deliverables

### FileID + DAT Transaction Hash

- **FileID**: 2038
- **DAT Transaction Hash**: 9417248c8d155f1d8f56c777235e37ea8f5fec194b07087a923f19a3163fc357

### Inference Queries and Responses

Two inference queries were attempted against the dataset. However, the inference server was unresponsive and returned a "Not Found" error for all attempted models. The full error log has been saved to `inference_log.txt`.

### Dataset Description and Agent Potential

The dataset is a brief document outlining the fundamental concepts of cryptocurrency and blockchain technology. It covers topics such as decentralization, transactions, mining, and key terms like public/private keys.

This dataset could power a simple educational chatbot or a question-answering agent. The agent would be able to answer basic questions about cryptocurrency, explain technical concepts in simple terms, and provide a high-level overview of how blockchain technology works, making it a useful tool for individuals new to the crypto space.