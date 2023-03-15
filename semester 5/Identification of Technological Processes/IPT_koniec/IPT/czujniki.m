clear all;
close all;

czujnik1 = [3601.5,
            3515.2,
            3401.5,
            3274.8,
            3162.3,
            3045.9,
            2921.8,
            2793.2,
            2679.3,
            2559.9,
            2441.4,
            2326.9,
            2271.9,
            2210.1,
            2158.1];
czujnik2 = [3707.5,
            3588.0,
            3460.9,
            3335.4,
            3216.5,
            3082.1,
            2976.5,
            2845.9,
            2719.4,
            2609.3,
            2476.9,
            2357.2,
            2291.8,
            2238.7,
            2202.8];
czujnik3 = [3710.9,
            3589,
            3470.5,
            3348.2,
            3218.3,
            3103.3,
            2981.4,
            2854.3,
            2737.1,
            2614.2,
            2485.5,
            2365.4,
            2309.1,
            2247.8,
            2206.9];
h = [25,
    23,
    21,
    19,
    17,
    15,
    13,
    11,
    9,
    7,
    5,
    3,
    2,
    1,
    0];

p1 = polyfit(czujnik1, h, 1);


a1 = p1(1)
b1 = p1(2)
f1 = @(x) a1*x + b1;    % Funkcja dla czujnika 1

p2 = polyfit(czujnik2, h, 1);
a2 = p2(1)
b2 = p2(2)
f2 = @(x) a2*x + b2;    % Funkcja dla czujnika 2

p3 = polyfit(czujnik3, h, 1);
a3 = p3(1)
b3 = p3(2)
f3 = @(x) a3*x + b3;     % Funkcja dla czujnika 3

x1 = linspace(2100,3700,10000);
L_b1 = x1(find(f1(x1) >= 0, 1));
H_b1 = x1(find(f1(x1) >= 25, 1));
% new x1  -- > range 0 - 25 cm
x1 = linspace(L_b1, H_b1,10000);

%-------------------------------------------
x2 = linspace(2100,3800,10000);
L_b2 = x2(find(f2(x2) >= 0, 1));
H_b2 = x2(find(f2(x2) >= 25, 1));
% new x2  -- > range 0 - 25 cm
x2 = linspace(L_b2, H_b2,10000);

%-------------------------------------------
x3 = linspace(2100, 3800,10000);
L_b3 = x3(find(f3(x3) >= 0, 1));
H_b3 = x3(find(f3(x3) >= 25, 1));
% new x3  -- > range 0 - 25 cm
x3 = linspace(L_b3, H_b3,10000);

%-------------------------------------------

figure(1)
hold on
grid on
plot(x1, f1(x1),'blue');
plot(x2, f2(x2),'red');
plot(x3, f3(x3),'yellow');
legend('Sensor1', 'Sensor2', 'Sensor3','Location','southeast');
title('Sensor Scale')
xlabel('Sensor Value')
ylabel('Height h (0-25)[cm]')
xlim([2100, 3750])
ylim([-1, 27])
hold off




