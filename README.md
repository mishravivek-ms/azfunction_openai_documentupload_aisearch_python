# Azure Function for Resume Processing

This Azure Function is designed to process resumes uploaded to Azure Blob Storage. It uses AI Document Intelligence to read the content, OpenAI for text classification, and an embedding model to generate vector data, which is then loaded into Azure Search Service.

## Table of Contents
- Prerequisites
- Architecture
- Setup
- Function Code
- Deployment
- Usage
- Contributing
- License

## Prerequisites
- Azure Subscription
- Python 3.8 or later
- Azure CLI
- Azure Functions Core Tools
- Azure Storage Account
- Azure Cognitive Services (Document Intelligence)
- OpenAI API Key
- Azure Search Service

## Architecture
1. **Trigger**: The function is triggered when a resume is uploaded to Azure Blob Storage.
2. **Document Intelligence**: The content of the resume is read using Azure Document Intelligence.
3. **Text Classification**: The text is classified using OpenAI's API.
4. **Embedding Model**: The classified text is converted into vector data using an embedding model.
5. **Azure Search**: The vector data is loaded into Azure Search Service for indexing and searching.

![Architecture](image/image.bmp)
## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/azure-function-resume-processing.git
cd azure-function-resume-processing
