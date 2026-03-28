from frete import calcular_frete

def test_frete_gratis():
    assert calcular_frete(250, "SP") == 0

def test_frete_padrao_fora_sc():
    assert calcular_frete(100, "PR") == 20

def test_frete_sc_abaixo_200():
    assert calcular_frete(150, "SC") == 10