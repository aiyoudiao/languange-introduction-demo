<!-- PHP 运算符 -->

<!-- 算术 运算符 -->
<?php
echo "+ - * / % ** \n";
?>

<!-- 自增自减 运算符 -->
<?php
$one = 1;
echo '++$one '. ++$one . "\n";
echo '$one++ '. $one++ . "\n";
echo '$one '.$one . "\n";
?>

<!-- 比较 运算符 -->
<?php
echo "== === != <> !== < > <= >= \n";
?>

<!-- 复合赋值运算符 -->
<?php
echo "= += -= *= /= %= **= \n";
$one = 2;
$one **= 3;
echo $one;
?>

<!-- 逻辑运算符 -->
<?php
var_dump(true and true); // 逻辑与
var_dump(true or false); // 逻辑或
var_dump(false xor true); // 逻辑异或
var_dump(!true); // 逻辑非
var_dump(true && true); // 逻辑与
var_dump(true || false); // 逻辑或
?>

<!-- 按位运算符 -->
<?php
echo 1 & 1; // 与
echo "\n";
echo 1 ^ 1; // 异或
echo "\n";
echo ~1; // 非
echo "\n";
echo 1 << 1; // 左移
echo "\n";
echo 1 >> 1; // 右移
?>
