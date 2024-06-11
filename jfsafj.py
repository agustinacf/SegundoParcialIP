def ap_antes_corte(c: chr, s: str) -> int:
    contador_apariciones: int = 0

    for i in range(len(s)):
        if s[i] == c:
            contador_apariciones += 1
        elif s[i] == "x":
            return contador_apariciones
    return contador_apariciones

def verificar_transacciones(s: str) -> int:
    saldo: int = 0

    for i in range(len(s)):
        if s[i] == "x":
            return (350 * ap_antes_corte("r", s)-(56*ap_antes_corte("v", s)))
        elif s[i] == "v":
            saldo -= 56
            if saldo < 0:
                saldo += 56
                return saldo
        elif s[i] == "r":
            saldo += 350

print(verificar_transacciones("ssrvvrrvvsvvsxrvvv"))
print(verificar_transacciones("ssrvvvvsvvsvvv"))
