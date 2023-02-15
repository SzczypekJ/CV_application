function zadanie8(m)

syms t w
N = 10; % liczba próbek
fp = 1000;%Hz
Tp = 1/fp;
A1 = 10;
f1 = 100; %Hz
A2 = 5;
f2 = 200; %Hz
x1 = A1*sin(2*pi*f1*t)+A2*sin(2*pi*f2*t);
x = x1;
tn = [0:N-1]*Tp; % wsp. czasowe próbek
xn = double(subs(x,t,tn));
xn = [xn(end-m+1:end), xn(1:end-m)];
Xk = zeros(1,N);
wk = fp*[0:N/2-1]/N;
for k = 0:N-1 % impl. wzoru (8)
 for n = 0:N-1
 Xk(k+1) = Xk(k+1)+xn(n+1)*exp((-2*pi*1i*k*n)/N);
 end
end
Xk_fft = fft(xn,N); %funkcja wbudowana
dft_err = sum(abs(Xk_fft-Xk));
disp('DFT error:'); disp(dft_err);

Xk_1 = Xk(1:(N/2));
tol = 10e-5;
Xk_1(abs(Xk_1)<tol) = 0;
g_widm_amp = abs(Xk_1);
g_widm_faz = (180/pi)*angle(Xk_1);
figure;
subplot(2,1,1)
ezplot(x,[tn(1),tn(N)]); hold on; grid on
plot(tn, xn,'ob');
xlabel('t [s]'); ylabel('x(nT_p)');
subplot(2,1,2)
stem(wk, real(Xk_1),'ob'); grid on, hold on
stem(wk, imag(Xk_1),'*r');
title('Widmo'),
ylabel('X(k\Omega_p)'); %
figure;
subplot(2,1,1)
stem(wk, g_widm_amp)
title('Widmowa gęstość amplitudy')
xlabel('f[Hz]')
subplot(2,1,2)
stem(wk, g_widm_faz)
title('Widmowa gęstęść fazy')
xlabel('F[Hz)')
end