# test_integraçao.py
import pytest
from carrinho import fechar_compra

def test_integracao_carrinho_com_frete_padrao():
    print("\n" + "="*50)
    print("[TESTE 1] Iniciando integração: Carrinho + Frete Padrão (SP)")

    produtos = [50.0, 50.0]
    print(f"[TESTE 1] Produtos inseridos no carrinho: {produtos}")

    resultado = fechar_compra(produtos, 'SP')

    print(f"[TESTE 1] Resultado retornado pela integração: R$ {resultado: .2f}")
    print("[TESTE 1] O teste espera que o valor seja R$ 120.00. Verificando (assert)...")

    assert resultado == 120.0

    print("TESTE 1 Sucesso! Os módulos se comunicam perfeitamente")
    print("="*50)

# --- Teste 2: Regra de Exceção

def test_integracao_carrinho_frete_sc():
    print("\n" + "="*50)
    print("[TESTE 2] Iniciando Integração: Carrinho + Frete Exceção (SC)")

    produtos = [40.0, 60.0]
    print(f"[TESTE 2] Produtos inseridos no carrinho: {produtos}")

    resultado = fechar_compra(produtos, 'SC')

    print(f"[TESTE 2] Resultado retornado pela integração: R$ {resultado: .2f}")
    print("[TESTE 2] O teste espera que o valor seja R$ 110.00. Verificando (assert)...")

    assert resultado == 110.0

    print("[TESTE 2] Sucesso! A regra de exceção do estado de SC funcionou na integração")
    print("="*50 + "\n")

# --- Avaliar a saída ---

if __name__ == "__main__":
    pytest.main(["-s", "-v", __file__])