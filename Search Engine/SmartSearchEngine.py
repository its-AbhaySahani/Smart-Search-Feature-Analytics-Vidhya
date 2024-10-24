import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from sentence_transformers import SentenceTransformer

# Load the DataFrame with embeddings
df = pd.read_pickle('output/courses_with_embeddings.pkl')

# Load the model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Function to perform a search query
def search_courses(query, top_n=5):
    # Generate the embedding for the query
    query_embedding = model.encode([query])
    
    # Calculate cosine similarity between the query and course descriptions
    similarities = cosine_similarity(query_embedding, np.array(df['Embeddings'].tolist()))
    
    # Sort courses based on similarity score
    sorted_indices = np.argsort(similarities[0])[::-1]
    
    # Retrieve the top N most relevant courses
    top_courses = df.iloc[sorted_indices[:top_n]]
    
    return top_courses[['Course Title', 'Description', 'Rating', 'Link', 'Duration', 'Level']]

# Example search
query = "data science beginner course"
results = search_courses(query)
print(results)