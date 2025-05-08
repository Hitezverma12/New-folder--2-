num = int(input("you want odd and even under which value:"))

odd_list = [i for i in range(num) if i % 2 != 0]
print("list of odd numbers are:", odd_list, "\n")

even_list = [i for i in range(num) if i % 2 == 0]
print("list of even numbers are:", even_list, "\n")

fruits = ['apple', 'banana', 'mango','papaya','grapes']
Fruits = [x[0].upper() + x[1:] for x in fruits]

print(("Fruits with proper nouns:", Fruits ))