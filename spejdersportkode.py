filepath = 'C:\\Users\\username\\Desktop\\oplysninger.txt'

with open(filepath, 'x') as f:
    f.write(input('Tast dine oplysninger ind   '))

f = open("C:\\Users\\username\\Desktop\\oplysninger.txt")
print(f.read())