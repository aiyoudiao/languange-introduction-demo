<!-- 以 PHP 开放标签开头 hello.php -->
<?php
    echo "Hello World\n";
    print("Hello World 2");
?>


<!-- Arrays 数组 -->
<?php
$num = [1, 3, 5, 7, 9];
$num[5] = 11;
unset($num[2]); // 删除数组元素
print_r($num);
echo count($num);
?>

<!-- Functions 功能 -->
<?php
function add($a, $b) {
    return $a + $b;
}
echo add(1, 2);
echo add(2, 3);
?>

<!-- Constants 常数 -->
<?php
const MY_CONST = "hello";
echo MY_CONST;

echo 'MY_CONST is: '.MY_CONST;
?>

<!-- Variables 变量 -->
<?php
$boolean1=true;
$boolean2=True;
$int=12;
$float=3.1415926;
unset($float);
$str1="how are you?";
$str2='fine, thank you!';
echo "$boolean1\n";
echo "$boolean2\n";
echo "$int\n";
echo "$float\n";
echo "$str1\n";
echo "$str2\n";
?>

<!-- Operators 运算符 -->
<?php
$x = 1;
$y = 2;
$sum = $x + $y;
echo $sum;
?>

<!-- Comments 注释 -->
<?php
# 单行 shell 样式的注释
// 单行 C 样式的注释
/* 多行 C 样式的注释 */
?>

<!-- Classes 类 -->
<?php 
class Student {
    public $name;
    public function __construct($name) {
        $this->name = $name;
    }
}
$alex = new Student("Alex");
echo "my name is {$alex->name}";
?>

<!-- Strings 字符串 -->
<?php
$url = "www.baidu.com";
echo "i am going to {$url}\n";
// 字符串连接
echo "I am going to ". $url."\n";
$hello = "hello, ";
$hello .= "world!";
echo $hello;
?>
