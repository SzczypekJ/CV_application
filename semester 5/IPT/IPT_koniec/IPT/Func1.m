function error = Func1(p, t, x)
    
    c = p(1);
    alpha = p(2);
    x0 = p(3);
    S = 3.5 * 25;

    dx = @(t,x) -(c * x^alpha)/S;
    
    [~,x_ode] = ode45(dx, t, x0);
    x_ode = real(x_ode);

    error = (x_ode - x);
    error = real(error);
end
