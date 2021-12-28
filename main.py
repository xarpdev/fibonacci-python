# Program to generate fibonacci sequence using dynamic programming approach

def fib_dp(num):
    arr = [0,1]
    print("Fibonacci Sequence: ")
    if num == 1:
        print(0)
    elif num == 2:
        print('[0,','1]')
    else:
        while(len(arr) < num): # length of list should be less then num
            arr.append(0)
        if (num == 0 or num == 1):
            return 1
        else:
            arr[0] = 0
            arr[1] = 1
            for i in range(2, num):
                arr[i] = arr[i - 1] + arr[i - 2] # New term is equal to sum of two previous terms.
            print(arr)
            return arr[num - 2]
n = int(input("Enter the value of 'n': "))
fib_dp(n)