def conversorTemperatura(opcao, graus):
    if opcao == 1:
        f = graus * 1.8 + 32
        print(f)
        return f
    
    elif opcao == 2:
        c = (graus - 32) / 1.8
        print(c)
        return c
        
    else:
        print("Opção inválida")
        return 0
