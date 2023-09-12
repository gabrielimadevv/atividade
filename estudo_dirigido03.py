def palavra():
    p = input("Digite uma palavra: ")
    m = p[::-1]
    if p == m:
        print("Sim. {} é palindrome".format(p))
    else:
        print("{} não é palindrome".format(p))
print(palavra())