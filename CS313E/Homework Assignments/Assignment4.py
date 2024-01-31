import matplotlib.pyplot as plt
def x_axis(len):
    # Function creates a list with the length of the x-axis.
    x_len = []
    for i in range(1, len+1):
        x_len.append(i)
    return x_len
def three_lines():
    # f1 in red, f2 in blue, f3 in green
    x = x_axis(50)
    y1 = []
    y2 = []
    y3 = []
    for n in x:
        func1 = (2 ** 10) * n + (2**6)
        y1.append(func1)
    plt.plot(x, y1, label = 'f1', color = 'red')
    for n in x:
        func2 = (n ** 3.3) - 100
        y2.append(func2)
    plt.plot(x, y2, label = 'f2', color = 'blue')
    for n in x:
        func3 = 100 *(n ** 2.1) + 2 ** 100
        y3.append(func3)
    plt.plot(x, y3, label = 'f3', color = 'green')
    plt.legend()
    plt.xlabel('n - values')
    plt.ylabel('f(n) - values')
    plt.title('Test 1 n = 50')
    plt.show()
three_lines()

