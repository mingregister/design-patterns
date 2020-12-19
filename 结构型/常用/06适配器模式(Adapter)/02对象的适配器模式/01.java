/*
核心思想就是：
    只需要修改Adapter类的源码即可：
*/

public class Source {  
  
    public void method1() {  
        System.out.println("this is original method!");  
    }  
}  

public interface Targetable {  
  
    /* 与原类中的方法相同 */  
    public void method1();  
  
    /* 新类的方法 */  
    public void method2();  
}  

public class Wrapper implements Targetable {  
  
    private Source source;  
      
    public Wrapper(Source source){  
        super();  
        this.source = source;  
    }  

    @Override  
    public void method2() {  
        System.out.println("this is the targetable method!");  
    }  
  
    @Override  
    public void method1() {  
        source.method1();  
    }  
}  


// 测试类
public class AdapterTest {  
  
    public static void main(String[] args) {  
        Source source = new Source();  
        Targetable target = new Wrapper(source);  
        target.method1();  
        target.method2();  
    }  
}  


/*
输出：
    this is original method!
    this is the targetable method!

输出与第一种一样，只是适配的方法不同而已。
*/