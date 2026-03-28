import frete

def fechar_compra(produtos_preco, estado_cliente):
    valor_produtos = sum(produtos_preco)
    print(f"[Carrinho] Somando Produtos... Total: R$ {valor_produtos:.2f}")

    valor_frete = frete.calcular_frete(valor_produtos, estado_cliente)
    print(f"[Integração] O frete retornando para {estado_cliente} foi de: R$ {valor_frete:.2f}")

    total = valor_produtos + valor_frete
    print(f"[Carrinho] Fechando a conta... Valor final: {total:.2f}")

    return total

if __name__ == "__main__":
    print("- - - Teste  Manual do Carrinho - - -")
    fechar_compra([50.0, 50.0], 'SP')