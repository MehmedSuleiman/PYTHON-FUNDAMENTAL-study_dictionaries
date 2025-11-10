#Write a program that keeps the information about students and their grades.
#On the first line, you will receive an integer number representing the next pair of rows.
#On the next lines, you will be receiving each student's name and their grade.
#Keep track of all grades for each student and keep only the students with an
#average grade higher than or equal to 4.50.
#Print the final dictionary with students and their average grade in the following format:
#"{name} -> {averageGrade}"
#Format the average grade to the 2nd decimal place.

n = int(input())

names_grade= {}

for i in range(n):
    name = input()
    g = float(input())
    if name in names_grade:
        names_grade[name] += [g]
        continue
    else:
        names_grade[name] = [g]

for name, grade in names_grade.items():
    averageGrade =sum(grade) / len(grade)
    if averageGrade >= 4.50:
        print(f"{name} -> {averageGrade:.2f}")
    else:
        continue


