from random import randint
import matplotlib.pyplot as plt

numbers = [0] * 99

x = [_ for _ in range (2,101)]

for _ in range(20000000):
    a = randint(1,20)
    b = randint(1,20)
    d = randint(1,20)
    e = randint(1,20)
    f = randint(1,20)

    c = a + b + d + e + f

    numbers[c-2] += 1

plt.plot(x, numbers)
plt.show()

print(x)
print("fdfd")
