def sumsquares(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + pow(i,2)
    return sum
n = int(input('Enter n value:'))
print('sum of squares of',n,'is',sumsquares(n))
