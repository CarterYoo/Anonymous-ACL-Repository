import matplotlib.pyplot as plt
import numpy as np

# Data Preparation
puzzles = ['Role Injected', 'Zero Prompt', 'Real Game']
/* This is just example, change it to importing your json file
correct_counts = [
    [0, 0, 0, 2, 2, 2, 4],  # Role Injected
    [4, 4, 0, 4, 4, 4, 4],  # Zero Prompt
    [1, 1, 1, 1, 0, 1, 2]   # Real Game
]
*/

# Calculating Correctness
correct_rates = [
    (sum(correct_counts[0]) / (len(correct_counts[0]) * 4)) * 100,
    (sum(correct_counts[1]) / (len(correct_counts[1]) * 4)) * 100,
    (sum(correct_counts[2]) / (len(correct_counts[2]) * 4)) * 100
]

# Graph
plt.figure(figsize=(10, 6))
bars = plt.bar(puzzles, correct_rates, color=['#FF9999', '#66B2FF', '#99FF99'])

#  Customizing Graph
plt.title('Puzzle Correct Rate Comparison', fontsize=14, pad=15)
plt.xlabel('Puzzle Type', fontsize=12)
plt.ylabel('Correct Rate (%)', fontsize=12)
plt.ylim(0, 100)

# Adding Percentages
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%',
             ha='center', va='bottom')

# Adding Grids 
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()

#Additional Info
print("\nPuzzle Statistics:")
for puzzle, rate in zip(puzzles, correct_rates):
    print(f"{puzzle}: {rate:.1f}% correct rate")
