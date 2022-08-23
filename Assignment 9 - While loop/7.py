'''Write a python script to print first N even natural numbers in reverse order.'''
n = int(input("Enter a natural numbers :"))
i = n
while i>=1:
    print(i,end=' ')
    i-=2
    