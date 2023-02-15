function Euler(W_i, V)
N = 1000;
h = 0.1;
W_ust = 0.4;
T_i = 293;
T_ust = 303;
V_ust = 0.04;
C = 1820;
ro = 1000;

Q_ust = -W_ust*(T_i-T_ust)/(V_ust*ro) * C * V_ust*ro;

x = 1:h:N;
y = zeros(size(x));
y(1) = 293;
n = numel(y);
X = ones(1,2000);
Q = [Q_ust*X, 0.5 * Q_ust * X,Q_ust*X, 1.5 * Q_ust * X, Q_ust * X];

T_i = y(1);
for i = 1:n-1
    f = (1/(V*ro))*(W_i*(T_i - y(i)) + Q(i)/C);
    y(i+1) = y(i) + h * f;
end
plot(x,y)
grid on

end