<!-- PHP 类型 -->

<!-- 布尔类型 Boolean 值不区分大小写 -->
<?php
$boolean1 = true;
$boolean2 = TRUE;
$boolean3 = false;
$boolean4 = FALSE;
$boolean5 = (bool) 1; # true
$boolean6 = (bool) 0; # false
var_dump($boolean1);
var_dump($boolean2);
var_dump($boolean3);
var_dump($boolean4);
var_dump($boolean5);
var_dump($boolean6);
?>

<!-- 浮点数 Float / Double -->
<?php
$float1 = 1.234;
$float2 = 1.2e7;
$float3 = 7E-10;
$float4 = 1_234.567; # 7.4.0 以上
var_dump($float4);
$float5 = 1 + "10.5";
var_dump($float5);
$float6 = 1 + "-1.3e3";
var_dump($float6);
?>

<!-- 整数 Integer -->
<?php
$int1 = 28;
$int2 = -32;
$int3 = 012; # 8进制
$int4 = 0x15; # 16进制
$int5 = 0b1010; # 2进制
$int6 = 1_234_567; # 7.4.0 以上
var_dump($int1);
var_dump($int2);
var_dump($int3);
var_dump($int4);
var_dump($int5);
var_dump($int6);
?>

<!-- Null 类型 -->
<?php
$a = null;
$b = 'Hello php!';
var_dump($a ?? 'a is unset'); # a is unset
var_dump($b ?? 'b is unset'); # Hello php!

$a = array();
var_dump('$a == null ', $a == null); # bool(true)
var_dump('$a === null ', $a === null); # bool(false)
var_dump('is_null($a) ', is_null($a)); # bool(false)
?>

<!-- 字符串 String -->
<?php
echo 'this is a simple string';
?>

<!-- 数组 Array -->
<?php
$arr = array("hello", 'world', '!');
var_dump($arr);
?>

<!-- 可迭代对象 Iterable -->
<?php
function bar(): iterable {
    return [1, 2, 3];
}

function gen(): iterable {
    yield 1;
    yield 2;
    yield 3;
}

foreach (bar() as $value) {
    var_dump($value);
}

foreach (gen() as $value) {
    var_dump($value);
}
?>
