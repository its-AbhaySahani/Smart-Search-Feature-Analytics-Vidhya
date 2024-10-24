import pandas as pd
import gradio as gr
from SmartSearchEngine import search_courses

# Load the DataFrame with embeddings
df = pd.read_pickle('output/courses_with_embeddings.pkl')

# Define the search function to be used in the Gradio interface
def gradio_search(query):
    results = search_courses(query, top_n=5)
    return results.to_dict(orient='records')

# Create a Gradio interface
iface = gr.Interface(
    fn=gradio_search,
    inputs=gr.Textbox(lines=2, placeholder="Enter your search query here...", label="Search Query"),
    outputs=gr.Dataframe(headers=["Course Title", "Description", "Rating", "Link", "Duration", "Level"], label="Search Results"),
    title="Smart Course Search Tool",
    description="Search for the most relevant courses on Analytics Vidhya",
    theme="default",
    layout="vertical",
    live=True
)

# Add a logo and some styling
iface.launch(
    share=True,
    favicon_path="path/to/logo.png",  # Replace with the path to your logo
    show_error=True
)