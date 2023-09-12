def multiplo_5_3():
    num = int(input("Digite um número: "))
    if num % 5 and num % 3:
        return True
    else:
        return False
print(multiplo_5_3())