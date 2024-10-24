# Smart-Search-Feature-Analytics-Vidhya



### Live Demo:

**Link to Hugging Face Spaces**: Included the link to the live demo: [SmartSearchEngine-AnalyticsVidhya](https://huggingface.co/spaces/its-abhay777/SmartSearchEngine-AnalyticsVidhya).

This should make it easy for users to access and try out the live demo of your Smart Search Engine.
## Overview

The Smart Search Feature for Analytics Vidhya is a tool designed to help users find the most relevant free courses on the Analytics Vidhya platform. This project leverages web scraping, natural language processing, and machine learning to provide an efficient and user-friendly search experience.

## Features

- **Web Scraping**: Collects data from the Analytics Vidhya free courses page.
- **Data Cleaning**: Handles missing values and ensures data consistency.
- **Vector Embeddings**: Uses Sentence Transformers to generate embeddings for course descriptions.
- **Search Engine**: Implements a smart search engine using cosine similarity and the Gemmini API for enhanced search results.
- **User Interface**: Provides a user-friendly interface using Gradio for easy interaction.


## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/Smart-Search-Feature-Analytics-Vidhya.git
    cd Smart-Search-Feature-Analytics-Vidhya
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Data Scraping

1. **Run the scraper**:
    ```sh
    python DataScrapping/scrapper.py
    ```

2. **Handle missing values**:
    ```sh
    python DataScrapping/hsndlingMissingValues.py
    ```

### Generating Vector Embeddings

1. **Generate embeddings**:
    ```sh
    python Search\ Engine/VectorEmbedding.py
    ```

### Deploying the Search Engine

1. **Deploy the search engine**:
    ```sh
    python Search\ Engine/deployment.py
    ```

## Example

To perform a search query, simply enter your query in the Gradio interface and get the most relevant courses displayed.

### Example Search Query

```sh
data science beginner course
