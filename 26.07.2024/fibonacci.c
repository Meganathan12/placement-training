t = int(input("Enter the number of terms: "))

a, b = 0, 1
c = 0

while c < t:
    print(a, end=' ')
    n = a + b
    a = b
    b = n
    c += 1
