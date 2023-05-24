import pandas as pd

# List of CSV filenames for each day
csv_files = ['Day1_od.csv', 'Day2_od.csv', 'Day3_od.csv', 'Day4_od.csv', 'Day5_od.csv', 'Day6_od.csv']

start_date = "May 9th"
end_date = "May 16th"

# Initialize an empty dictionary to store the volunteer attendance
volunteer_attendance = {}
# Iterate over the CSV files starting from day1
for i, csv_file in enumerate(csv_files, start=1):
    # Read the CSV file
    df = pd.read_csv(csv_file)
    
    # Iterate over each row in the DataFrame
    for _, row in df.iterrows():
        roll_number = row.iloc[0].strip()  # First column (index 0) with trailing spaces removed
        name = row.iloc[1].strip()  # Second column (index 1) with trailing spaces removed
        
        # Update the attendance days for the volunteer
        if name in volunteer_attendance:
            volunteer_attendance[name].append(i)
        else:
            volunteer_attendance[name] = [i]

# Create a DataFrame from the volunteer attendance dictionary
attendance_df = pd.DataFrame(volunteer_attendance.items(), columns=['Name', 'Days Present'])

# Convert the days to a readable format
attendance_df['Days Present'] = attendance_df['Days Present'].apply(lambda x: sorted(x))
attendance_df['Days Present'] = attendance_df['Days Present'].apply(lambda x: f"{start_date} - {end_date}" if len(x) == 6 else ", ".join([f"{start_date[:2]}{int(start_date[2:4]) + i}th {start_date[5:]}" for i in x]))

# Save the attendance DataFrame to a CSV file
attendance_df.to_csv('volunteer_attendance.csv', index=False)