import pandas as pd
from sentence_transformers import SentenceTransformer
import numpy as np

df = pd.read_csv('output/analytics_vidhya_courses_with_ratings.csv')

model = SentenceTransformer('all-MiniLM-L6-v2')

course_descriptions = df['Description'].tolist()
description_embeddings = model.encode(course_descriptions)

# Store the embeddings into the DataFrame
df['Embeddings'] = list(description_embeddings)

# Save the DataFrame with embeddings for later use
df.to_pickle('output/courses_with_embeddings.pkl')
print("Embeddings generated and saved successfully!")
