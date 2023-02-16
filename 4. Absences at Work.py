names = []
absences = []

# Information loop
while True:
    name_input = input("\nEnter employee name ($ to quit): ")
    if name_input == "$":
        break

    names.append(name_input)
    absences_input = int(input("Number days absent: "))
    absences.append(absences_input)

total_absences = sum(absences)
num_employees = len(names)


# Printing results
avg_absences = total_absences / num_employees

print(f"\nAverage number of days absent per year: {avg_absences:.2f}")

max_absences_index = absences.index(max(absences))
max_absences_name = names[max_absences_index]

print(f"\nPerson with most absences: {max_absences_name}, {max(absences)} days")

not_absent_names = [name for name, absences in zip(names, absences) if absences == 0]
not_absent_names.sort()

print("\nPeople who were never absent:")
for name in not_absent_names:
    print(name)


above_avg_names = [name for name, absences in zip(names, absences) if absences > avg_absences]
above_avg_names.sort()

print("\nPeople whose absences was above average:")
for name in above_avg_names:
    print(f"{name.title()}: {absences[names.index(name)]} days")






