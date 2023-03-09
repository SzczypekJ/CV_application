%Wywołanie eq_poziet - wylicza punkty pracy
[ x1r, x2r, x3r, ur ] = eq_poziet(15, 41.4343, 38.8705 , 26.2963, 0.2763, 0.3204, 0.4037)

%Wywołanie getMatrix - wylicza macierze A i B
[ A, B] = getMatrixAB(x1r, x2r, x3r, ur, 41.4343, 38.8705, 26.2963, 0.2763, 0.3204, 0.4037)
