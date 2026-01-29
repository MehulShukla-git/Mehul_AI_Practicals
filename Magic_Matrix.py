def generate_square(n):
    mat = [[0] * n for _ in range(n)]

    i = n // 2
    j = n - 1

    for num in range(1, n * n + 1):

        if i == -1 and j == n:
            j = n - 2
            i = 0
        else:

            if j == n:
                j = 0


            if i < 0:
                i = n - 1

        if mat[i][j]:
            j -= 2
            i += 1
            continue
        else:
            mat[i][j] = num

        j += 1
        i -= 1

    return mat

n = 5
magic_square = generate_square(n)
for row in magic_square:
    print(" ".join(map(str, row)))