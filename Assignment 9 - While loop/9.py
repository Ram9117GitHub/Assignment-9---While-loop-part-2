'''Write a python script to print cubes of first N natural numbers.'''
n = int(input("Enter a natural number :"))
i = 1
while i<=n:
    print(i*i*i,end=' ')
    i+=1