### 角色
1. 主题(subject)
2. 观察者(Observer): 它为关注主题的对象定义了一个接口。
3. 具体观察者(ConcreteObserver)

### 模式类型：
1. Subject **push** to Observer
2. Observer **pull** from Subject
*The protocol described above specifies a "pull" interaction model. Instead of the Subject "pushing" what has changed to all Observers, each Observer is responsible for "pulling" its particular "window of interest" from the Subject. The "push" model compromises reuse, while the "pull" model is less efficient.*

### 应用场景 
1. 广播或者 发布订阅系统中。
2. 分布式系统中的事件服务


### 优缺点


### 类似模式对比：
* Chain of Responsibility, Command, Mediator, and Observer, address how you can decouple senders and receivers, but with different trade-offs. Chain of Responsibility passes a sender request along a chain of potential receivers. Command normally specifies a sender-receiver connection with a subclass. Mediator has senders and receivers reference each other indirectly. Observer defines a very decoupled interface that allows for multiple receivers to be configured at run-time.
* Mediator and Observer are competing patterns. The difference between them is that Observer distributes communication by introducing "observer" and "subject" objects, whereas a Mediator object encapsulates the communication between other objects. We've found it easier to make reusable Observers and Subjects than to make reusable Mediators.
* On the other hand, Mediator can leverage Observer for dynamically registering colleagues and communicating with them.