[02、多个工厂]
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

// 工厂类  # 相对01修改：step1
public class SendFactory {  
   public Sender produceMail(){  
		return new MailSender();  
    }  
      
    public Sender produceSms(){  
        return new SmsSender();  
    }  
}  

// 测试类 # 相对01修改：step2
public class FactoryTest {  
  
    public static void main(String[] args) {  
        SendFactory factory = new SendFactory();  
        Sender sender = factory.produceMail();  
        sender.Send();  
    }  
}  



