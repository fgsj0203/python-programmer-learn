number_one = int(input("number one: "))
number_two = int(input("number two: "))
number_three = int(input("number three: "))
average_weighted = ((number_one * 2) + (number_two * 3) + (number_three * 5)) / (
    2 + 3 + 5
)

print("\n*** Solution ***")
print("\nThe average weighted is: %d" % average_weighted)
