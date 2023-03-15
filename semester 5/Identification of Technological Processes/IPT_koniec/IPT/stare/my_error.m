function e = my_error(c, alfa, x0, y, t)

    s = 87.5; %cm^2
        
    fun = @(x) (x0.^(1-alfa) - ((c * t)/s) *(1-alfa)) * (1/(1-alfa));
    
    x = lsqnonlin(fun, x0);
    e = x-y;
    
end
