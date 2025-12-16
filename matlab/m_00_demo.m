% 数组遍历
% A = [1, 2, 3];
% A.map(x => x * 2);  // [2,4,6]

A = [1 2 3];
B = A * 2;
disp(['A: ', num2str(A)]);
disp(['B: ', num2str(B)]);

% 过滤（filter）
% A.filter(x => x > 2);
C = A(A > 2);
disp(['C (elements > 2): ', num2str(C)]);

% 查找元素（find / findIndex）
% A.find(x => x > 2);  // 3
% A.findIndex(x => x > 2);  // 2
v = A(A > 2); % 查找元素值
i = find(A > 2); % 获取元素索引
disp(['v (first element > 2): ', num2str(v(1))]);
disp(['i (index of first element > 2): ', num2str(i(1))]);

% 排序（sort）
% A.sort((a,b)=>a-b);
D = sort(A);% 默认升序
E = sort(A, 'descend'); % 降序
disp(['D (sorted A ascending): ', num2str(D)]);
disp(['E (sorted A descending): ', num2str(E)]);

% 去重（Set）
% [...new Set([1,2,2,3])]
F = unique([1 2 2 3]);
disp(['F (unique elements): ', num2str(F)]);

% reduce（求和、累加）
% A.reduce((a,b)=>a+b);
sumA = sum(A);
disp(['A: ', num2str(A)]);
disp(['Sum of A: ', num2str(sumA)]);
disp(['mean(平均) of A: ', num2str(mean(A))]);
disp(['prod(求积) of A: ', num2str(prod(A))]);
disp(['median(中位数) of A: ', num2str(median(A))]);
disp(['cumsum(累积和) of A: ', num2str(cumsum(A))]);
disp(['std(标准差) of A: ', num2str(std(A))]);
disp(['var(方差) of A: ', num2str(var(A))]);
disp(['norm(范数) of A: ', num2str(norm(A))]);

% 最大最小值
% Math.max(...A)
% Math.min(...A)
disp(['max of A: ', num2str(max(A))]);
disp(['min of A: ', num2str(min(A))]);

% 数组切片（slice）
% A.slice(1,3)  // 第 1~2 个元素
G = A(2:3); % 由于MATLAB 索引从 1 开始
disp(['G (A slice from index 2 to 3): ', num2str(G)]);

% concat 合并数组
% A.concat(B);
H = [A B]; % 水平合并
disp(['H (A horizontally concatenated with B): ', num2str(H)]);
% I = [A; B]; % 垂直合并
disp(['I (A vertically concatenated with B): ']);
disp([A; B]);

% 字符串处理
% "hello".toUpperCase()
% "hello world".split(" ")
disp(['Uppercase of "hello": ', upper('hello')]);
disp(['Split "hello world": ', strjoin(split('hello world', ' '), ', ')]);

% 随机数
% Math.random(); // 0~1
disp(['Random number between 0 and 1: ', num2str(rand())]);
disp(['Random array of 10 elements between 0 and 1: ', num2str(rand(1,10))]);
disp(['Random integer between 1 and 10: ', num2str(randi([1,10]))]);

% 二维数组 / 矩阵操作
% A = [
%   [1,2],
%   [3,4]
% ];
M = [1 2; 3 4];
disp('Matrix M:');
disp(M);

% 矩阵乘法（JS 要手写，但 MATLAB 内置）
disp('Matrix M * M:');
N = M * M;
disp(N);

% 逐元素运算
disp('Element-wise M .* M:');
O = M .* M;
disp(O);

% 常见数学函数 JS → MATLAB
% JS	MATLAB
% Math.sin(x)	sin(x)
% Math.cos(x)	cos(x)
% Math.sqrt(x)	sqrt(x)
% Math.pow(x,2)	x^2（矩阵） / x.^2（逐元素）
% Math.abs(x)	abs(x)
% Math.log(x)	log(x)
% Math.exp(x)	exp(x)

% Bonus：MATLAB 版「JS 数组方法」全集映射表
% JS Array Method	MATLAB 对应
% map	向量化运算（不需写 map）
% filter	逻辑索引：A(A > x)
% reduce	sum, max, min, mean, prod
% find	find(condition)
% findIndex	find(condition)
% sort	sort(A)
% every	all(condition)
% some	any(condition)
% includes	ismember()
% indexOf	find(A==x,1)
% concat	[A B]
% slice	A(a:b)
% push	[A newItem]
% pop	A(end) & A(1:end-1)
% shift	A(1) & A(2:end)
% unshift	[newItem A]
