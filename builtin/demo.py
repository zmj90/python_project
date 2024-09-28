class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def play(self):
        print("方法play")

    def f1(self, n):
        # return sum([2 * i - 1 for i in range(1, n + 1)])
        return sum((2 * i - 1 for i in range(1, n + 1)))

    def f2(self, n):
        return (1 + 2 * n - 1) * n / 2


if __name__ == '__main__':
    p = Person("中码", "26")
    p.play()
    print(p.f1(10))
    print(p.f2(10))
    print(Person.__dict__)
    print(dir(Person))
    print(p.__dict__)
    print(p.__dir__())
    print(Person.__name__)
