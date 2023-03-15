load matrix_A;
load matrix_B;

w1 = 1;
w2 = 1;
w3 = 1;
H_1 = 10;
H_2 = 10;
H_3 = 10;
s1 = 3.5*25;
s2 = 3.45*H_2 + 35;
s3 = 3.5*sqrt(72.8*H_3 - H_3 ^ 2);


Q = [w1, 0, 0; 0, w2, 0; 0, 0, w3];
R = 5;
[K, P, eig] = lqr(A, B, Q, R)

W = ((c3/c1) ^ (1/alpha1)) * 10 ^ (alpha3/alpha1);
p = [-308, 762, -305-W];
u_r = roots(p)