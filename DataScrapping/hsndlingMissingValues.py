import pandas as pd

# Load the existing CSV
output_file = 'output/analytics_vidhya_courses_with_ratings.csv'
courses_df = pd.read_csv(output_file)

# Fill empty levels with 'Beginner'
courses_df['Level'].fillna('Beginner', inplace=True)

# Fill empty durations with 'NA'
courses_df['Duration'].fillna('NA', inplace=True)

# Fill empty descriptions with the respective course title
courses_df['Description'].fillna(courses_df['course_titles'], inplace=True)

# Fill empty ratings with 'NA'
courses_df['Rating'].fillna('NA', inplace=True)

# Save the updated DataFrame back to the CSV file
courses_df.to_csv(output_file, index=False)

print("Missing values have been filled and CSV updated!")
