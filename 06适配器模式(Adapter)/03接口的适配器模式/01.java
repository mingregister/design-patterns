public interface Sourceable {  
      
    public void method1();  
    public void method2();  
}  

// Wrapper2 实现了接口Sourceable的所有方法
public abstract class Wrapper2 implements Sourceable{  
      
    public void method1(){}  
    public void method2(){}  
}  

/*
这里我们不直接和接口打交道，我们直接使用Wrapper2,
因为Wrapper2已经实现了接口的所有方法，所以我们这里只重写我们需要的方法则可。
*/
public class SourceSub1 extends Wrapper2 {  
    public void method1(){  
        System.out.println("the sourceable interface's first Sub1!");  
    }  
}  

public class SourceSub2 extends Wrapper2 {  
    public void method2(){  
        System.out.println("the sourceable interface's second Sub2!");  
    }  
}  

// 测试类
public class WrapperTest {  
  
    public static void main(String[] args) {  
        Sourceable source1 = new SourceSub1();  
        Sourceable source2 = new SourceSub2();  
          
        source1.method1();  
        source1.method2();  
        source2.method1();  
        source2.method2();  
    }  
}  


/*
测试输出：

the sourceable interface's first Sub1!
the sourceable interface's second Sub2!

达到了我们的效果！
*/