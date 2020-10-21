myNumbers = [23,234,345,4356234,243,43,56,2]

#Your code go here:
def increment_by_one(number):
    return number * 3

new_list = map(increment_by_one, myNumbers)
result = list(map(increment_by_one, myNumbers))

print(result)

# print(new_list)