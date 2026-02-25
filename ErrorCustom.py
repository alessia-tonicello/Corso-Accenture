class ErroreCustom(Exception):
    pass  #significa: continua a fare quello che devi fare


def dividi(a, b):
    if b == 0:
        raise ErroreCustom
    return a / b


try:
    print(dividi(a, b))
except ErroreCustom as e:
    print("Il 7 non mi piace, prova un altro numero")

b