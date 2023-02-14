# Calc the cost for one trip and add the values to lists
def trip_calc():
    minutes = int(input("How long did the trip take? (minutes) "))
    cost = 10 + minutes * 2
    print(f"Cost for that trip is ${cost}")

    trip_times.append(minutes)
    trip_costs.append(cost)
    return cost


# Setting variables
average_time = 0
average_profit = 0
total_profit = 0
total_time = 0

trip_times = []
trip_costs = []

new_trip = ""


# Main
driver = input("What is the driver's name? ").title()

# Input loop
while new_trip != "n":
    new_trip = input("\nCalculate trip cost? (y or n) ").lower()
    if new_trip == "y":
        trip_calc()


# Time calculations
for time in trip_times:
    total_time += time

    average_time = total_time / len(trip_times)

# Money calculations
for money in trip_costs:
    total_profit += money

    average_profit = total_profit / len(trip_costs)


# Print summary
print(f"\n\nDAILY SUMMARY for {driver}:"
      f"\n\nTotal trip time: {total_time}m"
      f"\nAverage trip time: {average_time}m"
      f"\n\nTotal trip profits: ${total_profit}"
      f"\nAverage trip profits: ${average_profit}")
