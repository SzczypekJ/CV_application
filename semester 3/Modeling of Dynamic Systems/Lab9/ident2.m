function blad = ident2(X0)
load obiekt;
k = X0(1);
T1 = X0(2);
T2 = X0(3);
theta = X0(4);
t = 1:60;

model = tf([0 0 k ], conv([T1 1], [T2 1]));
set(model, 'outputdelay', theta);
y_sym = step(model, t);
plot(t, y, t, y_sym);
legend('Odpowiedź skokowa rzeczywista', 'Odpowiedź skokowa przybliżona')

e = y - y_sym;
blad = sum(e.^2) / length(e);
end
