def user(*args):
    print(args)
    print(type(args))


ls1 = ["qwe", 123, "asd"]
user(*ls1)
user(ls1)
