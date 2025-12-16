<?php
// 引入本地文件
include 'p_introduction_01__vars.php';
echo "\n".$fruit."\n";
// 与 include 相同，如果不存在则报错
require 'p_introduction_01__vars.php';

// 效果相同
include('p_introduction_01__vars.php');
require('p_introduction_01__vars.php');

// 引入远程文件
include "http://x.com/file.php";

$result = include 'p_introduction_01__vars.php';
echo "\n".$result."\n";
?>
