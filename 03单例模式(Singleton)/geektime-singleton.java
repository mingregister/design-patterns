// 饿汉式 03:12
public class Singleton {

    private static Singleton singleton = new Singleton();

    private Singleton(){}

    public static Singleton getInstance(){
        return singleton;
    }
}

// 饿汉式变种-静态代码块形式 03:48
public class Singleton {

    private static Singleton singleton;

    static {
        singleton = new Singleton();
    }

    private Singleton(){}

    public static Singleton getInstance(){
        return singleton;
    }
}


// 懒汉式
public class Singleton {

    private static Singleton singleton;

    private Singleton()

    public static Singleton getInstance() {
        if (singleton == null) {
            synchronized (Singleton.class) {
                singleton = new Singleton();
            }
        }
        return singleton;
    }
}

// 双重检查模式 5:51, 线程安全，延时加载
public class Singleton {

    private static volatile Singleton singleton;

    private Singleton() {}

    public static Singleton getInstance() {
        if (singleton == null) {
            synchronized (Singleton.class){
                if (singleton == null) {
                    singleton = new Singleton();
                }
            }
        }
        return singleton;
    }
}


// 静态内部类 9:12 线程安全，延时加载
public class Singleton {

    private Singleton(){}

    private static class SingletonInstance {
        private static finale Singleton singleton = new Singleton();
    }

    public static Singleton getInstance () {
        return SingletonInstance.singleton;
    }
}

// 枚举式 10:14 线程安全，延时加载, 防止反序列化
public enum Singleton{
    INSTANCE;

    public void whateverMethod(){

    }
}