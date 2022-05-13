a = []

b = []

a = [int(item) for item in input("Enter the list items : ").split()]

b = [int(item) for item in input("Enter the list items : ").split()]


def subsetSums(a, n, b, n1):
    bs = []
    total1 = 1 << n1

    for i1 in range(total1):
        Sum1 = 0
        for j1 in range(n1):
            if ((i1 & (1 << j1)) != 0):
                Sum1 += b[j1]
        bs.append(Sum1)

    total = 1 << n
    for i in range(1, total):
        Sum = 0

        for j in range(n):
            if ((i & (1 << j)) != 0):
                Sum += a[j]

        for x in range(1, total1):
            if bs[x] == Sum:
                return i, x;
    return -1, -1;


n = len(a)

n1 = len(b)

a_ind, b_ind = subsetSums(a, n, b, n1);

a_nums = []
b_nums = []

if a_ind != -1:
    for j in range(n):
        if ((a_ind & (1 << j)) != 0):
            a_nums.append(a[j])

    for j in range(n1):
        if ((b_ind & (1 << j)) != 0):
            b_nums.append(b[j])

    print(a_nums)
    print(b_nums)

else:
    print("0")