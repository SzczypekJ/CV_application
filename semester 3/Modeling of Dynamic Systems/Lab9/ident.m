function blad = ident(X0)
load obiekt;
k = X0(1);
T = X0(2);
theta = X0(3);
t = 1:60;

model = tf([0 k], [T 1]);
set(model, 'outputdelay', theta);
y_sym = step(model, t);
plot(t, y, t, y_sym);
legend('Odpowiedź skokowa rzeczywista', 'Odpowiedź skokowa przybliżona')

e = y - y_sym;
blad = sum(e.^2) / length(e);
end