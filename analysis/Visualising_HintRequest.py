import matplotlib.pyplot as plt

# Data input (number of hint requests)
data = {
    'Role Injected': [0, 3, 0, 0, 0, 0, 1],  # Role Injected
    'Zero Prompt': [0, 0, 2, 0, 0, 0, 0],    # Zero Prompt
    'Real Game': [0, 1, 2, 1, 0, 0, 1]       # Real Game
}

# Calculate average number of hint requests per puzzle
hints_avg = {
    'Role Injected': sum(data['Role Injected']) / len(data['Role Injected']),
    'Zero Prompt': sum(data['Zero Prompt']) / len(data['Zero Prompt']),
    'Real Game': sum(data['Real Game']) / len(data['Real Game'])
}

# Visualization
puzzles = list(hints_avg.keys())  # ['Role Injected', 'Zero Prompt', 'Real Game']
avg_values = list(hints_avg.values())

plt.figure(figsize=(8, 6))
plt.bar(puzzles, avg_values, color=['#FF9999', '#66B2FF', '#99FF99'])
plt.title('Average Hint Requests per Puzzle', fontsize=14)
plt.xlabel('Puzzle Type', fontsize=12)
plt.ylabel('Average Number of Hint Requests', fontsize=12)
plt.ylim(0, max(avg_values) + 0.5)  # Set y-axis range
for i, v in enumerate(avg_values):
    plt.text(i, v + 0.05, f'{v:.2f}', ha='center', fontsize=10)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
