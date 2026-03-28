def calcular_frete(valor_compra, estado):
    if valor_compra >= 200:
        return 0
    else:
        if estado == "SC":
            return 10
        else:
            return 20