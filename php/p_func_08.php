<!-- PHP 函数 -->

<!-- 函数 返回值 -->
<?php
function square($number) {
    return $number**2;
}
echo "square(5) = ".square(5)."\n";

?>



<!-- 函数 返回类型 -->
<?php
function sum($one, $two): float {
    return $one + $two + "0.5";
}

echo "sum(1, 2) = ".sum(1, 2)."\n";

function getStr (): string {
    return "hello world";
}

echo "getStr() = ".getStr()."\n";

class Component {};
function getComponent (): Component {
    return new Component;
}

var_dump(getComponent());

?>



<!-- 函数 可空返回类型 -->
<?php

function nullOrString (int $val): ?string {
    return $val % 2 ? "odd": null;
}
echo "nullOrString(1) = ".nullOrString(1)."\n";
var_dump(nullOrString(2));

?>



<!-- 无返回值函数-->
<?php

function voidFunction (): void {
    echo "voidFunction()\n";
    return;
}

voidFunction();

?>



<!-- 变量函数 -->
<?php

function bar ($args = '') {
    echo "bar($args) \n";
}
$func = 'bar';
$func('hello');
$func2 = "bar";
$func2('world');
?>



<!-- 匿名函数 -->
<?php

$func = function ($args = '') {
    echo "function ($args) \n";
};

$func('hello');
$func('world');

?>


<!-- 递归函数 -->
<?php

// 自己调自己，必须得有中止条件
function recursion ($x) {
    if ($x < 5) {
        echo "recursion($x) \n";
        recursion($x + 1);
    }
}

recursion(1);

?>


<!-- 默认参数 -->
<?php

function eat($food = 'apple') {
    echo "eat $food \n";
}

eat();
eat('banana');
eat('orange');

?>


<!-- 箭头函数 -->
<?php

$two = 1;

$fn1 = fn($one) => $one + $two;
$fn2 = function ($one) use ($two) {
    return $one + $two;
};

echo $fn1(1000) . "\n";
echo $fn2(100) . "\n";

?>
