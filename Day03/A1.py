import random


w1 = random.randint(1, 6)
w2 = random.randint(1, 6)

# Use a while loop to create a script that
# rolls two dice until a double (same number)
# was thrown.

# The dice can be simulated with random.randint().

# w1 = 1
# w2 = 2
# while w1 != w2:
#     w1 = random.randint(1, 6)
#     w2 = random.randint(1, 6)
#     print(w1, w2)
# print('PASCH!!!')

while True:
    w1 = random.randint(1, 6)
    w2 = random.randint(1, 6)
    if w1 == w2:
        print('PASCH!!!', w1, w2)
        break
    else:
        print(w1, w2)
