def my_abs(b):
    if b < 0:
        return -b
    else:
        return b
def main():
    a = input("please print a num:")
    b = int(a)
    print(my_abs(b))
main()