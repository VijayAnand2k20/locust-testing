import pandas as pd

# List of CSV filenames for each day
csv_files = ['Day1_od.csv', 'Day2_od.csv', 'Day3_od.csv', 'Day4_od.csv', 'Day5_od.csv', 'Day6_od.csv']

# Initialize an empty dictionary to store the volunteer attendance
volunteer_attendance = {}

# Iterate over the CSV files
for i, csv_file in enumerate(csv_files):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Iterate over each row in the DataFrame
    for _, row in df.iterrows():
        roll_number = row.iloc[0].strip()  # First column (index 0)
        name = row.iloc[1].strip()  # Second column (index 1)
        
        # Update the attendance days for the volunteer
        if name in volunteer_attendance:
            volunteer_attendance[name].append(f"day{i+1}")
        else:
            volunteer_attendance[name] = [f"day{i+1}"]

# Create a DataFrame from the volunteer attendance dictionary
attendance_df = pd.DataFrame(volunteer_attendance.items(), columns=['Name', 'Days Present'])

# Save the attendance DataFrame to a CSV file
attendance_df.to_csv('volunteer_attendance.csv', index=False)
