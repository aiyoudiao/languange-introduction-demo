
arr = [1 2 3 4 5]; % 一维数组
matrix = [1 2; 3 4]; % 二维数组

disp(arr);
disp(matrix);

A = [1 2; 3 4];
disp(A);
B = [5 6; 7 8];
disp(B);
C1 = A * B; % 矩阵乘法
C2 = A .*B; % 逐元素乘法
C3 = A^2; % 矩阵平方
C4 = A.^2; % 元素平方
disp(C1);
disp(C2);
disp(C3);
disp(C4);