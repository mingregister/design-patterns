[01、普通]
// 共同接口/基类
public interface Sender {  
    public void Send();  
}  

// 实现类
public class MailSender implements Sender {  
    @Override  
    public void Send() {  
        System.out.println("this is mailsender!");  
    }  
}  

public class SmsSender implements Sender {  
  
    @Override  
    public void Send() {  
        System.out.println("this is sms sender!");  
    }  
}  

// 工厂类
public class SendFactory {  
  
    public Sender produce(String type) {  
        if ("mail".equals(type)) {  
            return new MailSender();  
        } else if ("sms".equals(type)) {  
            return new SmsSender();  
        } else {  
            System.out.println("请输入正确的类型!");  
            return null;  
        }  
    }  
}  

// 测试类
public class FactoryTest {  
  
    public static void main(String[] args) {  
        SendFactory factory = new SendFactory();  
		// 在普通工厂方法模式中，如果传递的字符串出错，则不能正确创建对象，
		// 而多个工厂方法模式是提供多个工厂方法，分别创建对象。
        Sender sender = factory.produce("sms");  
        sender.Send();  
    }  
}  



