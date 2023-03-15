function [A,B] = getMatrixAB( x1r, x2r, x3r, ur, c1, c2, c3, a1, a2, a3)

a = 10.5;
b = 35.8;
c = 25;
w = 3.4;
H = 25;
R = 36.5;

%pola powierzchni 

S1 = c*w;
S2 = @(x2) w*(((b-a)/H)*x2 + a);
S3 = @(x3) w*sqrt(2*R*x3 - x3^2);


%inicjalizacja macierzy A i B        
A = [0 0 0; 0 0 0; 0 0 0];
B = [0; 0; 0];


% funkcje symboliczne zmian przepływu 
syms f1(x1)
syms f2(x1,x2)
syms f3(x2,x3)
syms q(u)

% funkcja przepływu pompy
ap =  470.7022;
bp = -1.4617e+03;
cp =  1.6882e+03;
dp =  -543.2470;
q = ap*(u^3) + bp*(u^2) + cp*u +dp;


%wiersz 1 macierzy A
q = q(ur);
f1(x1) = (q-c1*x1^(a1))/S1;
g(x1) = diff(f1);
A(1,1) = g(x1r);

% wiersz 2 macierzy A
f2(x1,x2) = ( c1 * x1^a1 - c2*x2^a2) / S2(x2);
f2_dx1(x1,x2) = diff(f2,x1);
A(2,1) = f2_dx1(x1r,x2r);
f2_dx2(x1,x2) = diff(f2,x2);
A(2,2)= f2_dx2(x1r,x2r);

% wiersz 3 macierzy A
f3(x2,x3) = ( c2  * x2^a2 - c3*x3^a3) / S3(x3);
f3_dx1(x2,x3) = diff(f3,x2);
A(3,2) = f3_dx1(x2r,x3r);
f3_dx2(x2,x3) = diff(f3,x3);
A(3,3) = f3_dx2(x2r,x3r);

% wiersz 1 macierzy B

q_du(u) = diff(q)/S1;
B(1) = q_du(ur);



end

