clear all;
close all;

% Wartość zadana "Set_motor" - początkowa 0.55 ponieważ dopiero od takiego
% ustawienia pompa zaczynała nalewać wodę do zbiornika.
Set_motor = [0.55
            0.6
            0.65
            0.7
            0.75
            0.8
            0.85
            0.9 
            0.95
            1];
czas = [112.7
        50.62
        37.68
        28.35
        23.55
        21.14
        18.92
        17.77
        16.35
        15.42];

% Wymiary pierwszego zbiornika: a = 3.5, b = 25, c = 25
% Stąd całkowita objętość  Volume = 3.5*25*25 = 2375 [cm^3] 
Volume = 2188 %cm^3

% Policzona prędkość napełnienia policzonej objętości dla czasu przy której zadana wartość na pompę go napełniła
% valocity [cm^3/s]
velocity = Volume./czas;

% Dopasowanie funkcji wielomianowej do uzyskanych wyników
parametry_motor = polyfit(Set_motor, velocity,3)
a1_motor = parametry_motor(1)
a2_motor = parametry_motor(2)
a3_motor = parametry_motor(3)
a4_motor = parametry_motor(4)


f_motor = @(x) a1_motor * x.^3 + a2_motor * x.^2 + a3_motor * x + a4_motor;

set = linspace(0.5, 1);

figure(2)

hold on 
%plot(czas,Set_motor)
plot(Set_motor, velocity, 'b-*', 'LineWidth', 3)
plot(set, f_motor(set), 'r', 'LineWidth', 2)

legend('Measure', 'Function','Location','southeast');
title('Motor Efficiency')
xlabel('Control value')
ylabel('Velocity [m^3/s]')
hold off