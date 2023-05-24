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


# Example usage
numbers = ["1", "2","3", "4", "5", "6","7", "9", "8"]
formatted = format_numbers(numbers)
print(formatted)  # Output: 1-3,5,7,9
