# Semantic_Search
Semantic Search Engine Using the MIND Dataset


```markdown
# Semantic Search Engine Using the MIND Dataset

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-v3.7+-blue.svg)

## Overview

This repository contains a semantic search engine built using the [MIND Dataset](https://msnews.github.io/). The search engine leverages Elasticsearch for indexing and searching, BERT embeddings for vectorizing the titles, and Streamlit for an interactive user interface.

## Features

- **Elasticsearch Integration**: Efficient search and indexing using Elasticsearch.
- **BERT Embeddings**: Title column is vectorized using BERT model for semantic search.
- **Streamlit Interface**: User-friendly web interface to interact with the search engine.

## Installation

### Prerequisites

- Python 3.7 or higher
- Docker (for running Elasticsearch)
- Elasticsearch (can be run via Docker)
- Streamlit
- SentenceTransformers

### Step-by-Step Guide

1. **Clone the repository**:
    ```bash
    git clone https://github.com/andyzhangstat/semantic_search_engine.git
    cd semantic_search_engine
    ```

2. **Set up the environment**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run Elasticsearch using Docker**:
    ```bash
    docker run -d --name elasticsearch -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" elasticsearch:7.10.2
    ```

4. **Prepare the data**:
    Download the MIND dataset and place the `news.tsv` file in the root directory.

5. **Ingest data into Elasticsearch**:
    ```bash
    python ingest_data.py
    ```

6. **Run the Streamlit interface**:
    ```bash
    streamlit run app.py
    ```

## Usage

Once the Streamlit app is running, open your browser and navigate to `http://localhost:8501` to start using the semantic search engine. You can enter a search query in the search box, and the results will be displayed with the title and abstract of the news articles that match your query.

## Dataset

The [MIND Dataset](https://msnews.github.io/) is a large-scale dataset for news recommendation research. It contains news articles and user interactions, making it ideal for building and evaluating news recommendation and search systems.

## How It Works

1. **Data Preparation**:
    - The `news.tsv` file from the MIND dataset is loaded and the title column is vectorized using the BERT model.
    
2. **Elasticsearch Indexing**:
    - The vectorized titles are indexed in Elasticsearch to enable fast and efficient semantic search.
    
3. **Search**:
    - A search query is vectorized using the same BERT model, and Elasticsearch's KNN search is used to find the most relevant news articles based on the vector similarity.

4. **User Interface**:
    - The Streamlit app provides a simple interface to enter search queries and display the search results in real-time.

## Project Structure

```plaintext
.
├── app.py                # Streamlit app
├── ingest_data.py        # Script to ingest data into Elasticsearch
├── requirements.txt      # Python dependencies
├── news.tsv              # MIND dataset file (not included in the repo)
└── README.md             # Project documentation
```

## Screenshot

![Screenshot](screenshot.png)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- **MIND Dataset**: Microsoft for providing the MIND dataset.
- **SentenceTransformers**: Hugging Face for the BERT model used for embedding the titles.

## Contact

For any inquiries or issues, please reach out to me.

```
