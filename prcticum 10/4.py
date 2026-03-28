def make_payment(P):
    CREDIT_LIMIT = 1000
    MIN_PAYMENT = 20

    if not isinstance(P, (int, float)):
        print("Повторить попытку")
        return

    if P < MIN_PAYMENT:
        print("Повторить попытку")
        return

    if P > CREDIT_LIMIT:
        print("Повторить попытку")
        return

    print("Успех")


make_payment(15)
