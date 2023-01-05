matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = mai = somt = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f"Digite um valor para [{l}, {c}]:  "))
print("--" * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}]", end='')
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]

        if c == 2:
            somt += matriz[l][c]

        if l == 1:
            mai = matriz[l][c]
            if matriz[l][c] > mai:
                mai = matriz[l][c]
    print()

print("--" * 30)
print("A soma dos valores pares é", somap)
print("A soma dos valores da 3ª coluna é", somt)
print("O maior valor da 2ª linha é", mai)