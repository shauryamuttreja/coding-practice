def digitsManipulations(n):
    if n==0:
        return 0
    product=1
    total=0
    while n>0:
        digit = n%10
        product*=digit
        total+=digit
        n=n//10
    return product-total