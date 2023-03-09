%Wywołanie eq_poziet - wylicza punkty pracy
[ x1r, x2r, x3r, ur ] = eq_poziet(15, 41.0862, 36.7398 , 25.9394, 0.2787, 0.3289, 0.4045)

%Wywołanie getMatrix - wylicza macierze A i B
[ A, B] = getMatrixAB(x1r, x2r, x3r, ur, 41.0862, 36.7398 , 25.9394, 0.2787, 0.3289, 0.4045)


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