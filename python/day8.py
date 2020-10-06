# Enter your code here. Read input from STDIN. Print output to STDOUT
# Day 8: Dictionaries and Maps
try:
    n = int(input())
    myDict = {}
    for i in range(n):
        args = list(map(str, input().rstrip().split()))
        myDict[args[0]] = args[1]
    while True:
        x = input()
        if not x:
            exit()
        output = x+"="+myDict[x] if x in myDict else "Not found"
        print(output)
except:
    exit()