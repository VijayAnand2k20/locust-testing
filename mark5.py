def format_numbers(numbers):
    numbers = sorted(set(map(int, numbers)))  # Convert to sorted unique integers
    
    ranges = []
    start = end = numbers[0]
    
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] == 1:
            end = numbers[i]
        else:
            ranges.append((start, end))
            start = end = numbers[i]
    
    ranges.append((start, end))
    
    formatted_numbers = []
    for range_start, range_end in ranges:
        if range_end - range_start == 0:
            formatted_numbers.append(str(range_start))
        elif range_end - range_start == 1:
            formatted_numbers.extend([str(range_start), str(range_end)])
        else:
            formatted_numbers.append(f"{range_start}-{range_end}")
    
    return ",".join(formatted_numbers)

def format_dates(days_present, start_date):
    replacement_dates = {
        'day1': '09th May',
        'day2': '10th May',
        'day3': '11th May',
        'day4': '12th May',
        'day5': '15th May',
        'day6': '16th May'
    }

    day_numbers = [int(day[3:]) for day in days_present]
    formatted_numbers = format_numbers(day_numbers)
    formatted_dates = []

    date_ranges = []
    current_range = []

    for number in formatted_numbers.split(','):
        if '-' in number:
            if current_range:
                date_ranges.append(current_range)
                current_range = []

            start, end = number.split('-')
            current_range.append(start)
            current_range.append(end)
        else:
            current_range.append(number)

    if current_range:
        date_ranges.append(current_range)

    for date_range in date_ranges:
        start = int(date_range[0])
        end = int(date_range[-1])

        formatted_range = []
        for i in range(start, end + 1):
            formatted_range.append(replacement_dates[f'day{i}'])

        formatted_dates.append(f"day{start}-{formatted_range[0]} to day{end}-{formatted_range[-1]}")

    return ', '.join(formatted_dates)


# Example usage
days_present = ['day1', 'day2', 'day3', 'day4', 'day5', 'day6']
start_date = 'May09'

formatted_dates = format_dates(days_present, start_date)
print(formatted_dates)  # Output: day1-09th May to day6-16th May
