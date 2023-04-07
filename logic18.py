def main(a):
    """Given a five-digit integer a, check the following statement "All digits of the number are in descending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
        Besh xonali tamsayı a berilgan bo'lsa, quyidagi "Raqamning barcha raqamlari kamayish tartibida" ni tekshiring.
    """
    return  (a%10)<((a%100)//10)<((a%1000)//100)<((a%10000)//1000)<((a%100000)//10000) and ((a//100000)<1)
print(main(54321))
