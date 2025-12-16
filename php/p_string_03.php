<!-- PHP 字符串 -->
<?php
$sql_quotes = '$String';
var_dump($sql_quotes);
$dbl_quotes = "this is a $sql_quotes.";
var_dump($dbl_quotes);
$escaped = "a \t tab character.";
var_dump($escaped);
$unescaped = 'a slash and a t: \t';
var_dump($unescaped);
?>

<!-- 多行字符串 -->
<?php 
// 未插值的多行
$str = "aaaaa";
$nowdoc = <<<'END'
Multi line string
$str
END;
var_dump($nowdoc);

// 插值多行
$str = "aaaaa";
$doc = <<<END
Multi line string
$str
END;
var_dump($doc)
?>

<!-- 操作 Manipulation https://www.php.net/manual/zh/ref.strings.php -->
<?php
$s = "hello phper";
var_dump(strlen($s));
var_dump(substr($s, 0, 3));
var_dump(substr($s, 1));
var_dump(substr($s, -4, 3));
var_dump(strtoupper($s));
var_dump(strtolower($s));
var_dump(strpos($s, 'l'));
var_dump(strpos($s, 'L'));
?>
