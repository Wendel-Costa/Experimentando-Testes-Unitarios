def conversorTemperatura(opcao, graus):
    """
    Converte temperaturas entre Celsius e Fahrenheit.

    Testes:
    >>> conversorTemperatura(1, 0)
    32.0
    >>> conversorTemperatura(1, 25)
    77.0
    >>> conversorTemperatura(2, 32)
    0.0
    >>> conversorTemperatura(2, 77)
    25.0
    >>> conversorTemperatura(3, 10)
    'Opção inválida'
    """

    if opcao == 1:
        f = graus * 1.8 + 32
        return f
    
    elif opcao == 2:
        c = (graus - 32) / 1.8
        return c
        
    else:
        return "Opção inválida"

import doctest
doctest.testmod(verbose=True)