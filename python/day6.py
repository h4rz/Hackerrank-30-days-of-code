# Enter your code here. Read input from STDIN. Print output to STDOUT
# Day 6: Let's Review
try:
    t = int(input())
    for i in range(0, t):
        s = input()
        print(s[::2] + " " +s[1::2])
except:
    print("Error - Data-type mismatch.")
