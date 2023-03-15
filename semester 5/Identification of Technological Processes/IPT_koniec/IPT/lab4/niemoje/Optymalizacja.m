clear all
load Sliced_Tank_Vectors.mat

a = 10;
b = 44.5;
c = 25;
w = 3.5;
H = 35;
R = 36.4;

aa = a;
bb = b;
cc = c;
ww = w;
HH = H;
RR = R;

options = optimset('PlotFcns','optimplotresnorm')

f1 = @(param) Func1(param(1),param(2),param(3), Tank1slicedt, Tank1slicedx, cc, ww);
init_cond = [40,  0.3, 24];
lw_bound = [1, 0.01, 23];
up_bound = [100, 0.5, 26];

[sol1, res1] = lsqnonlin(f1, init_cond, lw_bound, up_bound)
[t_ode,x_ode] = ode45(@(t,x) -sol1(1)*(x^sol1(2))/(cc*ww), Tank1slicedt, sol1(3));

figure
plot(Tank1slicedt,Tank1slicedx), hold on
plot(t_ode,x_ode)

f2 = @(param) Func2(param(1),param(2),param(3), Tank2slicedt, Tank2slicedx, aa, bb, ww, HH);
init_cond = [38,  0.3, 24];
lw_bound = [1, 0.01, 23];
up_bound = [100, 0.5, 26];

[sol2, res2] = lsqnonlin(f2, init_cond, lw_bound, up_bound)
[t_ode,x_ode] = ode45(@(t,x) -sol2(1)*(x^sol2(2))/(ww*(((bb-aa)/HH)*x + aa)), Tank2slicedt, sol2(3));

figure
plot(Tank2slicedt,Tank2slicedx), hold on
plot(t_ode,x_ode)

f3 = @(param) Func3(param(1),param(2),param(3), Tank3slicedt, Tank3slicedx, ww, RR);
init_cond = [25,  0.4, 24];
lw_bound = [1, 0.01, 23];
up_bound = [100, 0.5, 26];

[sol3, res3] = lsqnonlin(f3, init_cond, lw_bound, up_bound)
[t_ode,x_ode] = ode45(@(t,x) -sol3(1)*(x^sol3(2))/(ww*sqrt(2*RR*x - x^2)), Tank3slicedt, sol3(3));

figure
plot(Tank3slicedt,Tank3slicedx), hold on
plot(t_ode,x_ode)
