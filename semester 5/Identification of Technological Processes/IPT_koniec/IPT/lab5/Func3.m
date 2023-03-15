function error = Func3(p, t, x)
    
    c = p(1);
    alpha = p(2);
    x0 = p(3);

    S = @(x) 3.5 * sqrt((35*2*x)-(x^2));

    dx = @(t,x) -(c * x^alpha) / S(x);
    
    [~,x_ode] = ode45(dx, t, x0);

    x_ode = real(x_ode);

    error = (x_ode - x);
    error = real(error);
end