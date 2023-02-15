function blad = ident3(X0)
load obiekt;
k = X0(1);
T = X0(2);
t = 1:60;

model = zpk([], [-T, -T, -T], k);   %dla kolejnych n zwiększam o jedno -T
y_sym = step(model, t);
plot(t, y, t, y_sym);
legend('Odpowiedź skokowa rzeczywista', 'Odpowiedź skokowa przybliżona')

e = y - y_sym;
blad = sum(e.^2) / length(e);
end