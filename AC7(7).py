def ordenar_strings_por_tamanho(strings):
    return sorted(strings, key=lambda x: (len(x), strings.index(x)))

def main():
    casos_teste = int(input())

    for _ in range(casos_teste):
        conjunto_strings = input().split()
        conjunto_strings_ordenado = ordenar_strings_por_tamanho(conjunto_strings)
        print(' '.join(conjunto_strings_ordenado))

if __name__ == "__main__":
    main()
