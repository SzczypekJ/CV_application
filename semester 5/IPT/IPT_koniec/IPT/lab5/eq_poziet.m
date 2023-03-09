function [ x1r, x2r, x3r, ur ] = eq_poziet( x3r, c1, c2, c3, a1, a2, a3 )
    % funkcja q
    a =  470.7022;
    b = -1.4617e+03;
    c = 1.6882e+03;
    d =  -543.2470;
    %q = a*(u^3) + b*(u^2) + c* u + d;
    % koniec funkcji q
    %równania dla pochodnych stanu ustalonego
    x2r = ((c3*(x3r^(a3)))/c2)^(1/a2);
    x1r = ((c2*(x2r^(a2)))/c1)^(1/a1);
    qr=c3*(x3r^a3);
    u=roots([a b c (d-qr)]);
    if u(1)<1 && u(1)>0
      ur = u(1);
    end
    if u(2)<1 && u(2)>0
       ur = u(2);
    end
    if u(3)<1 && u(3)>0
       ur = u(3);
    end
end