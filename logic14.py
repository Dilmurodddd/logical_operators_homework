def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (((a%10)+1)%2)==0 and (((a//10)+1)%2)==0
print(main(55))