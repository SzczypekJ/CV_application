


a = -231.6274;
b = 625.0864;
c = -254.4828;
q =@(u) a*(u.^2) + b*u + c;

vect = linspace(0.5,1);
plot(vect, q(vect))