function error = fun1(p, wartosc, time)

%c = p(1);
%alfa = p(2);
x0 = p(3);

dx= @(t,x) test_fun1(t,x,p);

[~,x] = ode45(dx, time, x0);

error = x-wartosc;
end

