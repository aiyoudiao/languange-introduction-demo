% 3D 波动动画
[X,Y] = meshgrid(0:0.5:10, 0:0.5:10);
for t = 0:0.2:10
    Z = sin(X + t).*cos(Y + t);
    surf(X,Y,Z)
    zlim([-1 1])
    pause(0.05)
end
