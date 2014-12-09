# coding=utf-8
#P(0, 0) = 0.5
#P(i, 0) = 0.0 dla i > 0
#P(0, j) = 1.0 dla j > 0
#P(i, j) = 0.5 * (P(i-1,j) + P(i,j-1)) dla i > 0, j > 0

"""Za pomocą techniki programowania dynamicznego napisać program
obliczający wartości funkcji P(i, j). Porównać z wersją
rekurencyjną programu. Wskazówka: Wykorzystać tablicę dwuwymiarową
(np. słownik) do przechowywania wartości funkcji. Wartości w tablicy
wypełniać kolejno wierszami."""


def function(i, j):
    if i > j:
        table = [[0 for x in range(i)] for x in range(i)]
    else:
        table = [[0 for y in range(j)] for y in range(j)]

    table[0][0] = 0.5
    for x in range(1, i):
        table[x][0] = 0.
    for y in range(1, j):
        table[0][y] = 1.0

    for x in range(1, i):
        for y in range(1, j):
            table[x][y] = 0.5 * (table[x-1][y] + table[x][y-1])

    print table[i-1][j-1]


function(10, 7)
function(5, 5)