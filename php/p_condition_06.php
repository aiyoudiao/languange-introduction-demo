<!-- PHP 条件 -->

<!-- if elseif else -->
<?php

$a = 10;
if ($a > 20) {
    echo "a 大于 20";
} elseif ($a > 10) {
    echo "a 大于 10";
} else {
    echo "a 小于 10";
}

?>

<!-- switch -->
<?php
$a = 10;
switch ($a) {
    case 10:
        echo "a 等于 10";
        break;
    case 20:
        echo "a 等于 20";
        break;
    default:
        echo "a 不等于 10 和 20";
        break;
}
?>

<!-- 三元运算符 -->
<?php
$a = 10;
echo ($a > 20 ? "a 大于 20" : "a 小于 20") . "\n";

$x = false;
print($x ?: "x 为 false \n"); // 三元运算符缩写  x ? x : "x 为 false"

$a = null;
print($a ?? "a 为 null \n"); // 空合并运算符, 获取变量的值, 如果变量为 null, 则返回后面的值

$b = "hello";
print($b ?? "b 为 null \n");
?>

<!-- 匹配 php 8 开始可用 https://www.php.net/manual/zh/control-structures.match.php -->
<?php
$code = 201;
$message = match ($code) {
    200, 201 => "OK",
    404 => "Not Found",
    500 => "Internal Server Error",
    default => "Unknown Error"
};
echo $message . "\n";
?>

<!-- 匹配表达式 -->
<?php
$age = 18;
$result = match (true) {
    $age >= 35 => "Senior",
    $age >= 18 => "Adult",
    $age >= 16 => "Minor",
    default => "Child"
};
echo $result . "\n";
?>
