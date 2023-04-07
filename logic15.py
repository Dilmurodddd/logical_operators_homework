def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    b = ((a//100)+((a//10)%10)+(a%10)) 
    return ((b+1)%2)==0
print(main(456))