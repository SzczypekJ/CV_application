function e = Func3(c, alpha, x0, t, x, ww, RR)
%     tspan = [0 t(end)]
    [t_ode,x_ode] = ode45(@(t,x) -c*(x^alpha)/(ww*sqrt(2*RR*x - x^2)), t, x0);
%     figure
%     plot(t_ode,x_ode)
%     e = sum((x_ode - x).^2)
    e = x_ode - x;
    e = real(e);
end