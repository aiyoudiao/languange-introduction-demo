<!-- PHP 数组 -->

<!-- 定义 -->
<?php
$a1 = ['hello', 'world', '!'];
var_dump($a1);
$a2 = array('hello', 'world', '!');
var_dump($a2);
$a3 = explode(',', 'apple,pear,orange');
var_dump($a3);

// 混合 int 和 string 键
$array = array(
    "foo" => "bar",
    "bar" => "foo",
    100 => -100,
    -100 => 100,
);
var_dump($array);

// 短数组语法
$array = [
    "foo" => "bar",
    "bar" => "foo",
];

var_dump($array);
?>

<!-- 索引迭代 -->
<?php
$array = array('a', 'b', 'c');
$count = count($array);
for ($i = 0; $i < $count; $i++) {
    var_dump("i:{$i}, value:{$array[$i]}");
}
?>

<!-- 串联阵列 -->
<?php 
$a = [1, 2];
$b = [3, 4];

// PHP 7.4 以后
$result = [...$a, ...$b];
var_dump($result);
?>

<!-- 多阵列 -->
<?php 
$multiArray = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];
print_r($multiArray[0][0]);
print_r($multiArray[0][1]);
print_r($multiArray[0][2]);
?>

<!-- 操作 -->
<?php 
$arr = array(5 => 1, 12 => 2)
?>

