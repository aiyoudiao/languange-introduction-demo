% 函数
function y = add(a,b)
y = a + b;
end

sum=add(3,5);
disp(['Sum is: ', num2str(sum)]);

disp('--- 分割线 ---');

% 条件语句
x = 10;
if x > 5
    disp('x is greater than 5');
elseif x < 5
    disp('x is less than 5');
else
    disp('x is equal to 5');
end

% 循环语句
for i=1:5
    disp(['for: ', num2str(i)]);
end

i = 1;
while i <= 5
    disp(['while: ', num2str(i)]);
    i = i + 1;
end

% 用 for 循环计算 1~10 的平方和。
sum_squares = 0;
for n = 1:10
    sum_squares = sum_squares + n^2;
end
disp(['Sum of squares: ', num2str(sum_squares)]);

disp('--- 分割线 ---');
