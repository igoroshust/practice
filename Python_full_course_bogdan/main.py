# name, surname, city = input("Enter your name: "),  input("Enter your surname: "),  input("Enter your city: ")
# print(name, surname, city)

text = 'tutorial'
table = str.maketrans('aeiou', '43105')
result = text.translate(table)
print(result)