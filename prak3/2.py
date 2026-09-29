numbers = [10, 20, 30]
print("spisok:", numbers)

numbers.append(40)
print("1. after append(40):", numbers)

numbers.extend([50, 60])
print("2. after extend([50, 60]):", numbers)

numbers.insert(1, 15)
print("3. after insert(1, 15):", numbers)

numbers.remove(30)
print("4. after remove(30):", numbers)

numbers.reverse()
print("5. after reverse():", numbers)

numbers.sort()
print("6. after sort():", numbers)

numbers_copy = numbers.copy()
print("7. copy spisok:", numbers_copy)

numbers.clear()
print("8. afterclear():", numbers)
print("copy dont have been touch:", numbers_copy)