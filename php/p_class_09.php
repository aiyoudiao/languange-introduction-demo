<!-- PHP 类 -->

<!-- 构造函数 Constructor -->
<?php

class Person {

    public $name;
    public function __construct($name) {
        $this->name = $name;
    }

    public function sayHi () {
        echo "Hi, my name is " . $this->name . "\n";
    }
}

$tom = new Person('Tom');
$tom->sayHi();

?>

<!-- 继承 Inheritance -->
<?php

class SimpleClass {
    public function write () {
        echo "I'm a simple class\n";
    }
}

class ExtendClass extends SimpleClass {
    // 重写
    public function write () {
        parent::write();
        echo "I'm an extended class\n";
    }
}

$job = new ExtendClass();
$job->write();

?>

<!-- 魔术方法 -->
<?php

class MagicClass {

    // 获取对象信息
    public function __toString () {
        return "I'm a magic class\n";;
    }

    // 析构方法
    public function __destruct() {
        echo "I'm destructing\n";
    }
}

echo new MagicClass();

?>

<!-- 接口 -->
<?php

interface Write {
    public function write();
}

interface Read {
    public function read();
}

class IO implements Write, Read {
    public function write() {
        echo "I'm writing\n";
    }

    public function read() {
        echo "I'm reading\n";
    }
}

$io = new IO();
$io->write();
$io->read();

?>

<!-- 类变量 -->
<?php

class MyClass {
    const MY_CONST = 'I\'m a constant'. "\n";
    static $staticVar = 'I\'m a static variable'. "\n";
    // 公开的静态变量
    public static $publicStaticVar = 'I\'m a public static variable'. "\n";
    // 私有的静态变量，当前类内可用
    private static $privateStaticVar = 'I\'m a private static variable';
    // 受保护的静态变量，当前类与子类中可用
    protected static $protectedStaticVar = 'I\'m a protected static variable';
    // 受保护的变量，当前类与子类可用
    protected $protectedVar = 'I\'m a protected variable';
    // 私有的变量，当前类可用
    private $privateVar = 'I\'m a private variable';
}

echo MyClass::MY_CONST;
echo MyClass::$staticVar;
echo MyClass::$publicStaticVar;

?>
