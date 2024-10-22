import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Base URL for the courses page
url = 'https://courses.analyticsvidhya.com/collections/courses'

# Function to scrape curriculum from an individual course page
def scrape_curriculum(course_url):
    course_response = requests.get(course_url)
    course_soup = BeautifulSoup(course_response.text, 'html.parser')
    
    curriculum_section = course_soup.find('div', class_='course-curriculum')
    if curriculum_section:
        curriculum_items = curriculum_section.find_all('li')
        curriculum = [item.text.strip() for item in curriculum_items]
        return ', '.join(curriculum)  # Join all curriculum items into a string
    return 'Not available'

# Make an HTTP request to fetch the main course page
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Lists to store scraped data
course_titles = []
course_descriptions = []
course_curriculums = []
course_links = []

# Scrape course data from the main page
for course in soup.find_all('div', class_='course-block'):
    # Scrape the course title
    title = course.find('h4', class_='course-title').text.strip()
    course_titles.append(title)
    
    # Scrape the course description
    description = course.find('p', class_='course-description').text.strip()
    course_descriptions.append(description)
    
    # Scrape the course link
    link = course.find('a', class_='course-link')['href']
    full_link = f'https://courses.analyticsvidhya.com{link}'
    course_links.append(full_link)
    
    # Scrape the curriculum from each course's individual page
    curriculum = scrape_curriculum(full_link)
    course_curriculums.append(curriculum)

# Create output directory if it doesn't exist
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Store data in a pandas DataFrame
courses_df = pd.DataFrame({
    'Course Title': course_titles,
    'Description': course_descriptions,
    'Curriculum': course_curriculums,
    'Link': course_links
})

# Save the DataFrame to a CSV file
output_file = os.path.join(output_dir, 'analytics_vidhya_courses_with_curriculum.csv')
courses_df.to_csv(output_file, index=False)

print("Data scraped and saved to CSV successfully!")
