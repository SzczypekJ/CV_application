function [] = testNyqusit(k, Ti, Td, T)

    liczO = 10;
    mianO = [1 2 2 1];
    
    liczR = [k*(Ti*T + Td*Ti) k*(Ti + T), k];
    mianR = [Ti*T Ti 0];
    
    [lo, mo] = series(liczO, mianO, liczR, mianR);
    
    figure
    nyquist(lo, mo);
    legend(sprintf('k=%2.2f, T_{i}=%2.2f, T_d=%2.2f', k, Ti, Td))
    xlabel("Część rzeczywista")
    ylabel("Część urojona")
    title("Charakterystyka Nyquista")
end