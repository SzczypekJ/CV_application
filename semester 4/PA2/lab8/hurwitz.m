function [] = hurwitz(k, Ti, Td, T)
    liczO = 10;
    mianO = [1 2 2 1];

    liczR = [k*(Ti*T + Td*Ti) k*(Ti + T), k];
    mianR = [Ti*T Ti 0];

    [lo, mo] = series(liczO, mianO, liczR, mianR);
    [lz, mz] = cloop(lo, mo, -1);

    h1 = [mz(2)];
    h2 = [mz(2) mz(4) ; mz(1) mz(3)];
    h3 = [mz(2) mz(4) mz(6) ; mz(1) mz(3) mz(5) ; 0 mz(2) mz(4)];
    h4 = [mz(2) mz(4) mz(6) 0 ; mz(1) mz(3) mz(5) 0 ; 0 mz(2) mz(4) mz(6) ; 0 mz(1) mz(3) mz(5)];

    if(sign(det(h1)) > 0 && sign(det(h2)) > 0 && sign(det(h3)) > 0 && sign(det(h4)) > 0)
        h = msgbox(sprintf('k=%2.2f, T_i=%2.2f, T_d=%2.2f', k, Ti, Td), 'Układ stabilny', 'warn');
    else
        h = msgbox(sprintf('k=%2.2f, T_i=%2.2f, T_d=%2.2f', k, Ti, Td), 'Układ niestabilny', 'error');
    end
    
    set(h, 'position', [600 440 200 80])
end