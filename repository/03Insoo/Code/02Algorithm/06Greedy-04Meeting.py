def max_meetings(meetings):
    meetings.sort(key=lambda x: x[2])
    
    selected_meetings=[meetings[0]]
    last_end_time=meetings[0][2]

    for i in range(1, len(meetings)):
        if meetings[i][1] >=last_end_time:
            selected_meetings.append(meetings[i])
            last_end_time=meetings[i][2]

    return selected_meetings

# 회의번호, 시작시간, 종료시간
meetings=[
    (1,1,4),
    (2,3,5),
    (3,0,6),
    (4,5,7),
    (5,3,8),
    (6,5,9),
    (7,6,10),
    (8,8,11),
    (9,8,12),
    (10,2,13)
]

selected_meetings=max_meetings(meetings)
print("선택된회의목록(회의번호,시작시간,종료시간):")
for meeting in selected_meetings:
    print(f"회의번호: {meeting[0]}, 시작시간: {meeting[1]}, 종료시간: {meeting[2]}")


