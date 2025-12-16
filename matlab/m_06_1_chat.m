% 动态正弦波
x=0:0.1:10;
for t=0:0.1:10
y = sin(x + t);
plot(x,y);
ylim([-1 1]);
pause(0.05); % 暂停 0.05 秒以显示动画效果
end
