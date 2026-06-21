marks = []

for i in range(5):
    mark = int(input(f"Enter marks of student {i+1}: "))
    marks.append(mark)

print("Highest Marks:", max(marks))
print("Lowest Marks:", min(marks))
print("Average Marks:", sum(marks) / len(marks))