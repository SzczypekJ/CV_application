clear all

%zmienne
A = 0.32345;
B = -0.78743;
C = 0.56532;

sign = 1;
prec_f = 1;
prec_i = 1;


res = zeros(1,17);
for prec_f=0:16
    word = 1 + prec_i + prec_f;
    A_fix = fi(A, sign, word, prec_f)
    B_fix = fi(B, sign, word, prec_f)
    C_fix = fi(C, sign, word, prec_f)
    
    Y_fix = (A_fix+B_fix)*C_fix; %wynik przybliżony
    Y = (A+B)*C; %wynik dokładny

    res(prec_f + 1) = abs(Y-double(Y_fix)); %popełniany błąd

end


%rysowanie wykresu
figure
plot(res, '*-');
xlabel("precyzja")
ylabel("błąd")
title('Błąd w zależności od precyzji')

A = 0.32345;
B = -0.78743;
C = 0.56532;
sign = 1;
prec_f = 10;
prec_i = 1;
word = 1 + prec_i + prec_f;
A_fix = fi(A, sign, word, prec_f)
B_fix = fi(B, sign, word, prec_f)
C_fix = fi(C, sign, word, prec_f)
A_bin = bin(A_fix)
B_bin = bin(B_fix)
C_bin = bin(C_fix)

% Y_bin = (A_bin+B_bin)*C_bin



