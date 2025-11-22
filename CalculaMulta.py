def calculaMulta(velocidade):
    """
    Testes:
    >>> calculaMulta(50)
    0.0
    >>> calculaMulta(60)
    0.0
    >>> calculaMulta(61)
    203.0
    >>> calculaMulta(80)
    260.0
    >>> calculaMulta(60.5)
    201.5
    >>> calculaMulta(-5)
    'Entrada inválida'
    >>> calculaMulta('abc')
    'Entrada inválida'
    """
    
    if not isinstance(velocidade, (int, float)) or velocidade < 0:
        return 'Entrada inválida'
        
    limite = 60
    
    if velocidade <= limite:
        return 0.0
    else:
        excesso = velocidade - limite
        return 200.00 + excesso * 3.00

import doctest
doctest.testmod(verbose=True)