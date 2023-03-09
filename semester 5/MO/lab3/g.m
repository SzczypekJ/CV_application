function g=g(x)
    px = [-10 -5 0 5 10];
    py = [0.0001 -0.1 0 0.1 -0.0001];
    stopien = 5;
    W = polyfit(px, py, stopien);
    g = (0.05*sin(1*x)+W(1)*x.^stopien+W(2)*x.^(stopien-1)+W(3)*x.^(stopien-2)+W(4)*x.^(stopien-3)+W(5)*x.^(stopien-4)+W(6)*x.^(stopien-5))*(0.001*sin(x/10))+0.000001*x;
end