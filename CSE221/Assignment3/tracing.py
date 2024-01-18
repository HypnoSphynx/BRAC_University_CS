class Human:
    def __init__(self):
        self.age = 0
        self.height = 0.0


h1 = Human()
h2 = Human()
h1.age = 21
h1.height = 5.5
print(h1.age)
print(h1.height)
h2.height = h1.height - 3
print(h2.height)
h2.age = h1.age
h1.age += h1.age
print(h1.age)
h2 = h1
print(h2.age)
print(h2.height)
h1.age += h1.age
h2.height += h2.height
print(h1.age)
print(h1.height)
h2.age += h2.age
h1.age = h2.age
print(h2.age)

