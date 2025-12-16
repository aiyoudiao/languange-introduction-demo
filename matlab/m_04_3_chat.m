[X,Y]=meshgrid(1:0.5:10);
Z=sin(X).*cos(Y);
surf(X,Y,Z);
