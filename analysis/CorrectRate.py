import matplotlib.pyplot as plt
import numpy as np

# 데이터 준비
puzzles = ['Role Injected', 'Zero Prompt', 'Real Game']
# 각 퍼즐별 정답 그룹 수 (4개 기준)를 모든 응답에서 평균냄
correct_counts = [
    [0, 0, 0, 2, 2, 2, 4],  # Role Injected
    [4, 4, 0, 4, 4, 4, 4],  # Zero Prompt
    [1, 1, 1, 1, 0, 1, 2]   # Real Game
]

# 정답률 계산 (4가 최대이므로 %로 변환)
correct_rates = [
    (sum(correct_counts[0]) / (len(correct_counts[0]) * 4)) * 100,
    (sum(correct_counts[1]) / (len(correct_counts[1]) * 4)) * 100,
    (sum(correct_counts[2]) / (len(correct_counts[2]) * 4)) * 100
]

# 막대그래프 생성
plt.figure(figsize=(10, 6))
bars = plt.bar(puzzles, correct_rates, color=['#FF9999', '#66B2FF', '#99FF99'])

# 그래프 꾸미기
plt.title('Puzzle Correct Rate Comparison', fontsize=14, pad=15)
plt.xlabel('Puzzle Type', fontsize=12)
plt.ylabel('Correct Rate (%)', fontsize=12)
plt.ylim(0, 100)

# 각 막대 위에 백분율 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.1f}%',
             ha='center', va='bottom')

# 그리드 추가
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 그래프 표시
plt.tight_layout()
plt.show()

# 추가 통계 출력
print("\nPuzzle Statistics:")
for puzzle, rate in zip(puzzles, correct_rates):
    print(f"{puzzle}: {rate:.1f}% correct rate")
