def main(n):
    """
    A number consisting of one and zero is given (the number starts at once). 
    If the number of ones is greater than zero, true, otherwise False is returned.
    
    Args:
        n(int): parameter n
    Returns:
        bool: answer
    Bir va noldan iborat raqam berilgan (raqam birdan boshlanadi).
    Agar birliklar soni noldan katta bo'lsa, rost, aks holda False qaytariladi.       9 < n < 10000
    """
    
    return (((n%10)==0) and ((n//10)==1) and ((n//100)<1)) or ((((n%10))>=0) and (((n%100)//10)==0) and ((n//100)==1) and ((n//1000)<1)) or (((n%10)>=0) and (((n%100)//10)>=0) and (((n%1000)//100)==0) and ((n//1000)==1) and ((n//10000)<1)) or ((((n%10)>=0) and (((n%100)//10)>=0) and (((n%1000)//100)>=0) and (((n%10000)//1000)==0) and ((n//10000)==1) and ((n//100000)<1)))

print(main(10555))