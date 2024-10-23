import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

# Base URL for the courses page
url = 'https://courses.analyticsvidhya.com/collections/courses?page='

# Make an HTTP request to fetch the main course page

# Lists to store scraped data
course_titles = []
course_descriptions = []
course_ratings = []
level = []
duration = []
course_links = []

# Scrape course data from the main page
for page in range(1,9):
    response = requests.get(url+str(page))
    soup = BeautifulSoup(response.text, 'html.parser')
    for course in soup.find_all('a', class_='course-card'):
        try:
            # Scrape the course title
            title = course.find('h3').text.strip()
            course_titles.append(title)
            
            # Scrape the course description
            # description = course.find('p', class_='course-description').text.strip()
            # course_descriptions.append(description)

            # Scrape the course link
            link = course['href']
            full_link = f'https://courses.analyticsvidhya.com{link}'
            course_links.append(full_link)
            
            # Scrape the rating from each course's individual page
            course_page = requests.get(full_link)
            course_soup = BeautifulSoup(course_page.text, 'html.parser')
            icon_par = course_soup.find('ul', class_="text-icon__list")
            if not icon_par:
                duration.append("")
                course_ratings.append("")
                level.append("")
            else:
                values = icon_par.find_all("h4")
                try:
                    duration.append(values[0].text)
                except:
                    duration.append("NA")

                try:
                    course_ratings.append(values[1].text)
                except:
                    course_ratings.append("NA")
                
                try:
                    level.append(values[2].text)
                except:
                    level.append("Beginner")


            # description scrapper
            try:
                desc_par = course_soup.find('section', class_='rich-text')
                desc = desc_par.find('article').text
                course_descriptions.append(desc[2:-2])
            except:
                course_descriptions.append("title")

        except Exception as e:
            print(f"Error scraping course data: {e}")

# Debugging: Print the lists to check if they have data 
# print("Course Titles:", course_titles)
# print("Course Descriptions:", course_descriptions)
# print("Course Ratings:", course_ratings)
# print("Course Links:", course_links)
# print("Course Duration:", duration)
# print("Course Level:", level)

# # Print the length of each list to check if they have the same number of elements
# print("Length of Course Titles:", len(course_titles))
# print("Length of Course Descriptions:", len(course_descriptions))
# print("Length of Course Ratings:", len(course_ratings))
# print("Length of Course Links:", len(course_links))
# print("Length of Course Duration:", len(duration))
# print("Length of Course Level:", len(level))

# Create output directory if it doesn't exist
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Store data in a pandas DataFrame
courses_df = pd.DataFrame({
    'Course Title': course_titles,
    'Description': course_descriptions,
    'Rating': course_ratings,
    'Link': course_links,
    'Duration': duration,
    'Level': level

})

# # Debugging: Print the DataFrame to check if it has data
# print(courses_df)

# # Save the DataFrame to a CSV file
output_file = os.path.join(output_dir, 'analytics_vidhya_courses_with_ratings.csv')
try:
    courses_df.to_csv(output_file, index=False)
    print("Data scraped and saved to CSV successfully!")
except Exception as e:
    print(f"Error saving DataFrame to CSV: {e}")