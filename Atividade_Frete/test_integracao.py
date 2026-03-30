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