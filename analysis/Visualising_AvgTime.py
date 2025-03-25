import matplotlib.pyplot as plt
import numpy as np

# Function to convert time data into minutes
def convert_to_minutes(time_str):
    if not time_str or time_str.strip() == '':
        return 0
    time_str = time_str.strip()
    if 'seconds' in time_str and 'minutes' in time_str:
        minutes = int(time_str.split('minutes')[0].strip())
        seconds = int(time_str.split('minutes')[1].replace('seconds', '').strip())
        return minutes + (seconds / 60)
    elif 'minutes' in time_str:
        return float(time_str.replace('minutes', '').strip())
    elif ':' in time_str:
        minutes, seconds = map(int, time_str.split(':'))
        return minutes + (seconds / 60)
    return 0

# Puzzle solving time data
times = {
    'Role Injected': [
        '4 minutes', '10 minutes', '10 minutes', '1 minute 43 seconds', '3 minutes 48 seconds', '3 minutes 33 seconds', '5:30'
    ],
    'Zero Prompt': [
        '', '1 minute', '5 minutes', '1 minute 25 seconds', '1 minute 20 seconds', '1 minute 36 seconds', '0:42'
    ],
    'Real Game': [
        '', '5 minutes', '5 minutes', '2 minutes 27 seconds', '1 minute 56 seconds', '2 minutes 32 seconds', '6:42'
    ]
}

# Convert data to minutes
converted_times = {
    puzzle: [convert_to_minutes(t) for t in times[puzzle]] 
    for puzzle in times
}

# Calculate average times
average_times = {
    puzzle: np.mean([t for t in times if t > 0]) 
    for puzzle, times in converted_times.items()
}

# Visualization
plt.figure(figsize=(10, 6))
puzzles = list(average_times.keys())
avg_values = list(average_times.values())

bars = plt.bar(puzzles, avg_values, color=['#FF9999', '#66B2FF', '#99FF99'])
plt.title('Average Puzzle Solving Time', fontsize=14, pad=15)
plt.xlabel('Puzzle Type', fontsize=12)
plt.ylabel('Average Time (minutes)', fontsize=12)
plt.grid(axis='y', alpha=0.75)

# Display values on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom')

plt.tight
