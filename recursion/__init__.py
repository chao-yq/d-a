def foo(n):
    if n < 1:
        return
    else:
        print("push foo(", n, ")")
        foo(n - 1)
        print("pop foo(", n, ")")


if __name__ == '__main__':
    print("push main: ")
    foo(3)
    print("pop main: ")