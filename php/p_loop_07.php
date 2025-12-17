<!-- PHP 循环 -->

<?php

// while 循环
$i = 1;
while ($i < 5) {
    echo "while ". $i++."\n";
}

// do...while 循环
$i = 1;
do {
    echo "do...while ". $i++."\n";
} while ($i < 5);

// for 循环
for ($i = 1; $i < 5; $i ++) {
    echo "for ". $i . "\n";
}

// 循环控制
for ($i = 1; $i < 5; $i ++) {
    if($i == 4) {
        echo "for break ". $i . "\n";
        break;
    }

    if ($i == 2) {
        echo "for continue ". $i . "\n";
        continue;
    }

    echo "for ". $i . "\n";
}

// foreach 循环
$arr = array("a" => "apple", "b" => "banana");
$arr2 = ["a" => "apple", "b" => "banana"];
foreach ($arr as $key => $value) {
    echo "foreach key => value : ". $key. " => ". $value. "\n";
}

foreach ($arr2 as $value) {
    echo "foreach value : ". $value. "\n";
}

?>

