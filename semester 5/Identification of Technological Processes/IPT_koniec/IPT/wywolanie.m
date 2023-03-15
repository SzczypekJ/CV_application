%Wywołanie eq_poziet - wylicza punkty pracy
[ x1r, x2r, x3r, ur ] = eq_poziet(15, c1, c2, c3, alpha1, alpha2, alpha3)

%Wywołanie getMatrix - wylicza macierze A i B
[ A, B] = getMatrixAB(x1r, x2r, x3r, ur, c1, c2, c3, alpha1, alpha2, alpha3)

C=eye(3);

%KF
Q=0.1^2 .* eye(3);
R=0.01^2 .* eye(3);
G=eye(3);
L=lqe(A,G,C,Q,R)

%LQ
Q = eye(3);
R = 10;
K=lqr(A, B, Q, R)
