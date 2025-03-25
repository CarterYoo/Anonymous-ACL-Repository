import matplotlib.pyplot as plt

# Data input (scores for "How difficult was it?" for each puzzle)
data = {
    "Role Injected": [8, 10, 10, 8, 9, 10, 6],
    "Zero Prompt": [3, 6, 5, 2, 1, 3, 2],
    "Real Game": [6, 5, 9, 9, 10, 10, 7]
}

# Calculate average difficulty for each puzzle
averages = {puzzle: sum(scores) / len(scores) for puzzle, scores in data.items()}

# Visualization
puzzles = list(averages.keys())
avg_scores = list(averages.values())

plt.figure(figsize=(10, 6))
plt.bar(puzzles, avg_scores, color=['#FF9999', '#66B2FF', '#99FF99'])
plt.title('Average Difficulty per Puzzle (Out of 10)', fontsize=14)
plt.xlabel('Puzzle Type', fontsize=12)
plt.ylabel('Average Difficulty Score', fontsize=12)
plt.ylim(0, 10)  # Set y-axis range from 0 to 10
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Display average values above each bar
for i, v in enumerate(avg_scores):
    plt.text(i, v + 0.2, f'{v:.2f}', ha='center', fontsize=12)

plt.show()
