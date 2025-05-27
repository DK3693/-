grades = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grades_scores = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
subjects = []

score = 0.0
rate = 0.0

for _ in range(20):
    subjects.append(list(input().split()))

for i in range(20):
    if subjects[i][2] in grades:
        score += float(subjects[i][1]) * grades_scores[grades.index(subjects[i][2])]
        rate += float(subjects[i][1])
        
total_score = score / rate
print(total_score)