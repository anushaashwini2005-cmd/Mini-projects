n = int(input("Enter number of Subjects: "))

marks = []
total = 0

for i in range(n):
    m = int(input(f"Enter marks of Subject {i+1}: "))
    marks.append(m)
    total += m

average = total / n

highest = marks[0]
lowest = marks[0]

for m in marks:
    if m > highest:
        highest = m
    if m < lowest:
        lowest = m

print("\n--- Result ---")
print("Total marks:", total)
print("Average marks:", average)
print("Highest marks:", highest)
print("Lowest marks:", lowest)
