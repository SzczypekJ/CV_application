clear all;
close all;

% Wczytane dane
load('Z1.mat');
T1 = zbiornik1.time((118:2674),1);
Z1 = zbiornik1.signals.values((118:2674),1);
load('Z2.mat');
T2 = zbiornik2.time((180:2322),1);
Z2 = zbiornik2.signals.values((180:2322),1);
load('Z3.mat');
T3 = zbiornik3.time((123:3053),1);
Z3 = zbiornik3.signals.values((123:3053),1);

p = [50; 0.5; 25];
LB = [10, 0, 20];
UB = [100, 0.5, 30];
error1 = @(p) Func1(p, T1, Z1);
error2 = @(p) Func2(p, T2, Z2);
error3 = @(p) Func3(p, T3, Z3);
[x1_val, resnorm1] = lsqnonlin(error1, p, LB, UB);
[x2_val, resnorm2] = lsqnonlin(error2, p, LB, UB);
[x3_val, resnorm3] = lsqnonlin(error3, p, LB, UB);

c1 = x1_val(1);
alpha1 = x1_val(2);
x0_1 = x1_val(3);

dx1 = @(t, x, p) -(p(1) * x^p(2))/(3.5 * 25);
fun_dx1 = @(t, x0) dx1(t, x0, x1_val);
[time1, x1_resoult] = ode45(fun_dx1, T1, x1_val(3));
figure(3)
hold on 
grid on
plot(T1, Z1, 'b', time1, x1_resoult,'r')
title('Zbiornik 1')
ylabel('Height h (0-25)[cm])')
legend('Pomiar', 'Funkcja')
hold off

c2 = x2_val(1);
alpha2 = x2_val(2);
x0_2 = x2_val(3);

S2 = @(x) 3.5*(((35-9.5)/25)*x + 9.5);
dx2 = @(t, x, p) -(p(1) * x^p(2)) / S2(x);
fun_dx2 = @(t, x0) dx2(t, x0, x2_val);
[time2, x2_resoult] = ode45(fun_dx2, T2, x2_val(3));
figure(4)
hold on 
grid on
plot(T2, Z2, 'b', time2, x2_resoult,'r')
title('Zbiornik 2')
ylabel('Height h (0-25)[cm])')
legend('Pomiar', 'Funkcja')
hold off



c3 = x3_val(1);
alpha3 = x3_val(2);
x0_3 = x3_val(3);

S3 = @(x) 3.5 * sqrt((35*2*x)-(x^2));
dx3 = @(t, x, p) -(p(1) * x^p(2)) / S3(x);
fun_dx3 = @(t, x0) dx3(t, x0, x3_val);
[time3, x3_resoult] = ode45(fun_dx3, T3, x0_3);

figure(5)
hold on 
grid on
plot(T3, Z3, 'b')
plot(time3, real(x3_resoult),'r')
title('Zbiornik 3')
ylabel('Height h (0-25)[cm])')
legend('Pomiar', 'Funkcja')
hold off





c_table = [c1, c2, c3]
alpha_table = [alpha1, alpha2, alpha3]
x0_table = [x0_1, x0_2, x0_3]

save('c_table')
save('alpha_table')
save('x0_table')















