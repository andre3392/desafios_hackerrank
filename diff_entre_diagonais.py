def diagonalDifference(arr):
    limite = len(arr)
    i = 0
    j = 0
    diagonal_principal = []
    diagonal_secundaria = []

    while i < limite and j < limite:
        diagonal_principal.append(arr[i][i])
        diagonal_secundaria.append(arr[i][limite - 1 - i])
        i += 1
        j += 1

    print("Diagonal Principal:", sum(diagonal_principal))
    print("Diagonal Secundária:", sum(diagonal_secundaria))
    resultado = sum(diagonal_principal) - sum(diagonal_secundaria)
    return print(resultado)
