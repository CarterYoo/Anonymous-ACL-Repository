import matplotlib.pyplot as plt
import numpy as np

# 데이터를 분 단위로 변환하는 함수
def convert_to_minutes(time_str):
    if not time_str or time_str.strip() == '':
        return 0
    time_str = time_str.strip()
    if '초' in time_str and '분' in time_str:
        minutes = int(time_str.split('분')[0].strip())
        seconds = int(time_str.split('분')[1].replace('초', '').strip())
        return minutes + (seconds / 60)
    elif '분' in time_str:
        return float(time_str.replace('분', '').strip())
    elif ':' in time_str:
        minutes, seconds = map(int, time_str.split(':'))
        return minutes + (seconds / 60)
    return 0

# 각 퍼즐의 해결 시간 데이터
times = {
    'Role Injected': [
        '4 minutes', '10분', '10분', '1분 43초', '3분 48초', '3분 33초', '5:30'
    ],
    'Zero Prompt': [
        '', '1분', '5분', '1분 25초', '1분 20초', '1분 36초', '0:42'
    ],
    'Real Game': [
        '', '5분', '5분', '2분 27초', '1분 56초', '2분 32초', '6:42'
    ]
}

# 데이터를 분 단위로 변환
converted_times = {
    puzzle: [convert_to_minutes(t) for t in times[puzzle]] 
    for puzzle in times
}

# 평균 시간 계산
average_times = {
    puzzle: np.mean([t for t in times if t > 0]) 
    for puzzle, times in converted_times.items()
}

# 시각화
plt.figure(figsize=(10, 6))
puzzles = list(average_times.keys())
avg_values = list(average_times.values())

bars = plt.bar(puzzles, avg_values, color=['#FF9999', '#66B2FF', '#99FF99'])
plt.title('Average Puzzle Solving Time', fontsize=14, pad=15)
plt.xlabel('Puzzle Type', fontsize=12)
plt.ylabel('Average Time (minutes)', fontsize=12)
plt.grid(axis='y', alpha=0.75)

# 막대 위에 값 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{height:.2f}',
             ha='center', va='bottom')

plt.tight_layout()
plt.show()
