function [] = wyswietl_zapas_modulu_i_fazy(Gm, Pm)

zapas_modulu = 10 ^ (Gm/20);
zapas_fazy = deg2rad(Pm);
disp("Zapas modułu: " + zapas_modulu + newline + "Zapas fazy: " + zapas_fazy + "[rad]")

end