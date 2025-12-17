<!-- 其它 -->

<!-- 基本错误处理 -->
<?php
try {
    // action
    echo "start try ... \n";
    throw new Exception("error");
} catch (Exception $e) {
    echo "handle error: {$e} \n";
    // handle error
} finally {
    // 必定执行
    echo "finally end \n";

}
?>

<!-- 自定义异常 -->
<?php

class MyException extends Exception {}

try {
    $isError = true;
    if ($isError) {
        throw new MyException("error");
    }
} catch(MyException $e) {
    echo "handle error: {$e} \n";
}
?>

<!-- 运行时定义的常量 -->
<?php

define("CURRENT_DATE", date("Y-m-d H:i:s"));

echo "today is: " . CURRENT_DATE;

?>

<!-- PHP 8.0 中异常 -->
<?php

$nullableValue = null;

try {
    $value = $nullableValue ?? throw new InvalidArgumentException();
} catch(InvalidArgumentException) { // 捕获异常， 变量是可选参数
    echo "handle error \n";
}

?>

<!-- Nullsafe  短路运算符 8.0 新增 https://wiki.php.net/rfc/nullsafe_operator -->
<?php

$repo = null;
$result = null;

$result = $repo?->getUser(5)?->name;
echo $result ." === \n";

// 等价于下方代码
if (is_null($repo)){
    $result = null;
} else {
    $user = $repo->getUser(5);
    if (is_null($user)) {
        $result = null;
    } else {
        $result = $user->name;
    }
}

echo $result ." --- \n";

?>

<!-- 正则表达式 https://www.javasoho.com/reference/docs/regex.html#php%E4%B8%AD%E7%9A%84%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F -->
<?php
$str = "hello world";
echo preg_match('/ai/i', $str); // 0 表示匹配失败，1 表示匹配成功
?>

<!-- 文件读写 -->
<?php

/**
* r	    读
* r+	读写，前置
* w	    写入，截断
* w+	读写，截断
* a	    写，追加
* a+	读写，追加
 */
$txt = fopen("./file/my_file.txt", "r");
// 循环读取文件
while(!feof($txt)) {
    echo fgets($txt);
}
?>
