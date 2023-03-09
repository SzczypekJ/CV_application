% x1 = [3601.5
%     3515.2 
%     3401.5 
%     3274.8 
%     3162.3 
%     3045.9 
%     2921.8 
%     2793.2
%     2679.3
%     2559.9 
%     2441.4
%     2326.9 
%     2271.9 
%     2210.1 
%     2158.1];
% 
% x2 = [3707.5
%     3588.0
%     3460.9
%     3335.4 
%     3216.5 
%     3082.1
%     2976.5 
%     2845.9
%     2719.4 
%     2609.3 
%     2476.9
%     2357.2
%     2291.8
%     2238.7
%     2202.8];
% 
% x3 = [3710.9
%     3589
%     3470.5
%     3348.2
%     3218.3
%     3103.3
%     2981.4
%     2854.3
%     2737.1
%     2614.2
%     2485.5
%     2365.4
%     2309.1
%     2247.8
%     2206.9];
% 
% y = [25 
%     23
%     21 
%     19 
%     17 
%     15 
%     13 
%     11 
%     9 
%     7 
%     5
%     3 
%     2 
%     1
%     0];
% 
% 
% vect = linspace(2000,3800);
% 
% p1 = polyfit(x1,y,1);
% a1 = p1(1)
% b1 = p1(2)
% f1 = @(x) x*p1(1) + p1(2);
% 
%  
% 
% 
% p2 = polyfit(x2,y,1);
% a2 = p2(1)
% b2 = p2(2)
% f2 = @(x) x*p2(1) + p2(2);
% 
% p3 = polyfit(x3,y,1);
% a3 = p3(1)
% b3 = p3(2)
% f3 = @(x) x*p3(1) + p3(2);
% 
% %figure(1)
% %hold on
% %grid on
% %plot(vect, f1(vect));
% 
% %plot(vect, f2(vect)); 
% %plot(vect, f3(vect));
% %hold off
% 
% 
% V = 2375 %cm^3
% 
% Set_motor = [
%     0.55
%     0.6
%     0.65
%     0.7
%     0.75
%     0.8
%     0.85
%     0.9 
%     0.95
%     1];
% czas = [
%     112.7
%     50.62
%     37.68
%     28.35
%     23.55
%     21.14
%     18.92
%     17.77
%     16.35
%     15.42];
% 
% v = V./czas  % velocity motor [cm^3/s]
% 

% figure(1)
% hold on 
% plot(Set_motor, v)
% 
% p_motor = polyfit(Set_motor, v,3);
% a_motor = p_motor(1)
% b_motor = p_motor(2)
% f_motor = @(x) x*a_motor + b_motor;
% 
% vect_motor = linspace(0,25);
% plot(Set_motor, v, 'O');
% plot(f_motor(v),v)
% hold off

%--------------------------------------------------------------




c = 10;
alfa = 0.4;
x0 = 25;

%y = linspace(0,25);
%t = linspace(0,25);

errorr = my_error(c, alfa, x0, y, t);

figure(1)
hold on
plot(t, errorr,'-')
hold off




