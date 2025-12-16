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
$arr = array(5 => 1, 12 => 2);
print_r($arr);
$arr[] = 16; // 添加元素
print_r($arr);
$arr['x'] = 19; // 用键添加元素
print_r($arr);
unset($arr[5]); // 消除元素
print_r($arr);
sort($arr); // 排序，会改变数组的索引，从 0 开始
print_r($arr);
unset($arr); // 删除数组
print_r($arr);
?>

<!-- 数组迭代 -->
<?php
$colors = array('red', 'green', 'blue');
foreach($colors as $color) {
    echo "do something with {$color}\n";
}
?>

<!-- Into 函数，将参数解构  -->
<?php
$array = [1, 2, 3];
function func($a, $b, $c) {
    echo $a . ' ' . $b . ' ' . $c . "\n";
}
func(...$array);
?>

<!-- Splat运算符，将参数聚合 -->
<?php
function func2($one, ...$others) {
    var_dump($one);
    printf("others: %s\n", var_export($others, true));
}
func2(1, 2, 3, 4, 5);

function func3($one, string ...$others) {}
?>

<!-- 多类型 -->
<?php
$array = array(
    'a' => 'apple',
    36 => 63,
    "list" => array(
        "items" => array(
            "item1" => "item1",
            "item2" => "item2"

        )
    )
);

var_dump($array["a"]);
var_dump($array[36]);
var_dump($array["list"]["items"]["item1"]);
?>

<!-- 迭代键值对 -->
<?php
    $arr = ["a" => "apple", "b" => "banana"];
    foreach($arr as $key => $value) {
        echo $key . ":" . $value . "\n";
    }
?>
