def show():
    for j in "divyansh":
        if (j == "s"):
            break
        print(j, end="")
show()

def main():
    x = int(input("\nenter your subject"))
    sum = 0
    for i in range(0, x):
        y = int(input("enter your marks"))
        sum += y

    print(sum // 3)
main()

def display():
    print("\n")
    a = 0
    while (a <= 15):
        a = a + 1
        if (a % 2 == 0):
            continue
        print(a)
    print("end of loop")
display()
def hello():
    x = int(input("enter how many rows you want"))
    n = 1
    for i in range(1, x + 1):
        for j in range(1, i + 1):
            print(n, "\t", end="")
            n = n + 1
        print("")
hello()