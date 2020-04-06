public interface Sourceable {  
    public void method();  
}  


public class Source implements Sourceable {  
  
    @Override  
    public void method() {  
        System.out.println("the original method!");  
    }  
}  

public class Proxy implements Sourceable {  
  
    private Source source;  
    public Proxy(){  
        super();  
        this.source = new Source();  
    }  

    @Override  
    public void method() {  
        before();  
        source.method();  
        atfer();  
    }  

    private void atfer() {  
        System.out.println("after proxy!");  
    }  

    private void before() {  
        System.out.println("before proxy!");  
    }  
}  

// 测试类
public class ProxyTest {  
  
    public static void main(String[] args) {  
        Sourceable source = new Proxy();  
        source.method();  
    }  
  
}  


/*
输出：

before proxy!
the original method!
after proxy!
*/