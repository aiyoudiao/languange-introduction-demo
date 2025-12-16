% 求数组和
arr = 1:10;
sumArr = sum(arr);
disp(['数组和为: ', num2str(sumArr)]);

% 排序
arr=[5 2 8 1 9];
sortArr=sort(arr);
disp(['排序后: ', num2str(sortArr)]);

% 逻辑运算
A = [1 2 3 4];
B = A > 2;
disp(['逻辑运算结果:', num2str(B)]);

% 找到数组 [3 5 1 7 2] 中大于 4 的数字
arr2 = [3 5 1 7 2];
result = max(arr2);
disp(['数组中最大的数字: ', num2str(result)]);
result = find(arr2 > 4);
disp(['大于 4 的数字索引: ', num2str(result)]);
result = arr2(arr2 > 4);
disp(['大于 4 的数字: ', num2str(result)]);
