function e = Func1(c, alpha, x0, t, x, cc, ww)
%     tspan = [0 t(end)]
    [t_ode,x_ode] = ode45(@(t,x) -c*(x^alpha)/(cc*ww), t, x0);
%     figure
%     plot(t_ode,x_ode)
%     e = sum((x_ode - x).^2)
    e = x_ode - x;
    e = real(e);
end