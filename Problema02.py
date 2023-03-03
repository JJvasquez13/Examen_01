def encontrar_matriz(matriz_grande, matriz_pequeña):
    m_grande = len(matriz_grande)
    n_grande = len(matriz_grande[0])
    m_pequeña = len(matriz_pequeña)
    n_pequeña = len(matriz_pequeña[0])

    for i in range(m_grande - m_pequeña + 1):
        for j in range(n_grande - n_pequeña + 1):
            encontrada = True
            for k in range(m_pequeña):
                for l in range(n_pequeña):
                    if matriz_grande[i+k][j+l] != matriz_pequeña[k][l]:
                        encontrada = False
                        break
                if not encontrada:
                    break
            if encontrada:
                return True
    return False

matriz_grande = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
matriz_pequeña = [[6, 7], [10, 11]]

print(encontrar_matriz(matriz_grande, matriz_pequeña))
