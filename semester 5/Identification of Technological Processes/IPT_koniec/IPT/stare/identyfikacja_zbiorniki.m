clear all
close all

%=========================================================zbiornik1
load('zbiornik1111.mat');
time1 = zbiornik1.time((118:2674),1);
Zbiornik1 = zbiornik1.signals.values((118:2674),1);
% figure(1)
% hold on 
% %plot(time1,Zbiornik1)
% hold off
%=========================================================zbiornik2
load('zbiornik222.mat');
time2 = zbiornik2.time((180:2322),1);
Zbiornik2 = zbiornik2.signals.values((180:2322),1);
% figure(2)
% hold on
% %plot(time2,Zbiornik2)
% hold off
%=========================================================zbiornik3
load('zbior3.mat');
time3 = zbiornik3.time((123:3053),1);
Zbiornik3 = zbiornik3.signals.values((123:3053),1);
% figure(3)
% hold on
% %plot(time3,Zbiornik3)
% hold off
%==================================================================


p = [60; 0.5; 25];
S1 = 3.8 * 25;

wynik = fun1(p, Zbiornik1, time1)

plot(wynik, time1)

























