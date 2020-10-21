def func():

    #input
    n,m = list(map(int, input().split()))
    x, y, s = list(map(int, input().split()))
    xi = list(map(int, input().split()))
    yi = list(map(int, input().split()))

    xi = [0] + xi + [n+1]
    yi = [0] + yi + [m+1]

    print(xi)
    print(yi)

    xi_diff = []
    yi_diff = []
    for i in range(1, len(xi)):
        xi_diff.append(xi[i] - x[i-1])
    for i in range(1, len(yi)):
        yi_diff.append(yi[i] - y[i-1])



if __name__ == "__main__":
    for _ in range(int(input())):
        func()



# 12 13
