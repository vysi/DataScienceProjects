li = ['apple', 'banana', 'cherry']

# i nimmt die tatsächlichen Werte der Elemente der Liste an
for i in li:
    print(i, end=' ')
print()

print(len(li))

# for i in range(3):
for i in range(len(li)):
    # Zugriff über Index i auf Elemente der Liste 'li'
    print(li[i])
    li[i] = i

print(li)

print('######## Range funktionen: ')

print("""
for i in range(5):
    print(i)
""")
for i in range(5):
    print(i)
print("""

for i in range(5, 11):
    print(i)
""")

for i in range(5, 11):
    print(i)

print("""

for i in range(5, 11, 2):
    print(i)
""")
for i in range(5, 11, 2):
    print(i)

print()
print()
# Erstellen von Liste mit Zahlen 0 - 4
print(list(range(5)))
