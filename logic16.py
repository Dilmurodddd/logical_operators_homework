def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (a%10)>=0 and ((a%100)//10)>=0 and ((a%1000)//100)>=0 and ((a%10000)//1000)>=0 and ((a%100000)//10000)>=0 and (a//100000)<1
print(main(12345))