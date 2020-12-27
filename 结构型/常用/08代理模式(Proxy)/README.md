### 对比区分：
1. 和装饰模式有什么不同？应用场景都有那些？   感觉功能上，两者都可以实现。
2. 和原型模式有什么不同？
    原型模式是为了解决构建一些需要很多*资源*才能创建好的对象的创建。而代理模式是为了在不侵入业务的代码的同时，增加一些*辅助*功能

为其他对象提供一种代理以控制对这个对象的访问 


### 优缺点
#### 优点：
1. You can control the service object without clients knowing about it.
2. You can manage the lifecycle of the service object when clients don’t care about it.
3. The proxy works even if the service object isn’t ready or is not available.
4. Open/Closed Principle. You can introduce new proxies without changing the service or clients.


#### 缺点：
* The code may become more complicated since you need to introduce a lot of new classes.
* The response from the service might get delayed.

* Relations with Other Patterns
1. Adapter provides a different interface to the wrapped object, Proxy provides it with the same interface, and Decorator provides it with an enhanced interface.
2. Facade is similar to Proxy in that both buffer a complex entity and initialize it on its own. Unlike Facade, Proxy has the same interface as its service object, which makes them interchangeable.
3. Decorator and Proxy have similar structures, but very different intents. Both patterns are built on the composition principle, where one object is supposed to delegate some of the work to another. The difference is that a Proxy usually manages the life cycle of its service object on its own, whereas the composition of Decorators is always controlled by the client.

### 应用场景, 说法一：
1. 远程代理，也就是为一个对象在不同的地址空间提供局部代表。这样可以隐藏一个对象存在于不同地址空间的事实[DP].
2. 虚拟代理，是根据需要创建开销很大的对象。通过它来存放实例化需要很长时间的真实对象[DP]。这样就可以达到性能的最优化，*比如说你打开一个很大的HTML网页时，里面可能有很多的文字和图片，但你还是可以很快打开它，此时你所看到的是所有的文字，但图片却是一张一张地下载后才能看到。那些未打开的图片框，就是通过虚拟代理来替代了真实的图片，此时代理存储了真实图片的路径和尺寸。*
3. 安全代理(保护代理)，用来控制真实对象访问时的权限[DP]。一般用于对象应该有不同的访问权限的时候。
4. 智能指引，是指当调用真实的对象时，代理处理另外一些事[DP]。*如计算真实对象的引用次数，这样当该对象没有引用时，可以自动释放它；或当第一次引用一个持久对象时，将它装入内存；或在访问一个实际对象前，检查是否已经锁定它，以确保其他对象不能改变它。它们都是通过代理在访问一个对象时附加一些内务处理。*

### 应用场景，说法二：
如果已有的方法在使用的时候需要对原有的方法进行改进，此时有两种办法：
1. 修改原有的方法来适应。这样违反了“对扩展开放，对修改关闭”的原则。
2. 就是采用一个代理类调用原有的方法，且对产生的结果进行控制。这种方法就是代理模式。

使用代理模式，可以将功能划分的更加清晰，有助于后期维护！


### 应用场景：具体案例
* Lazy initialization (virtual proxy). This is when you have a heavyweight service object that wastes system resources by being always up, even though you only need it from time to time.
    Instead of creating the object when the app launches, you can delay the object’s initialization to a time when it’s really needed.

* Access control (protection proxy). This is when you want only specific clients to be able to use the service object; for instance, when your objects are crucial parts of an operating system and clients are various launched applications (including malicious ones).
    The proxy can pass the request to the service object only if the client’s credentials match some criteria.

* Local execution of a remote service (remote proxy). This is when the service object is located on a remote server.
    In this case, the proxy passes the client request over the network, handling all of the nasty details of working with the network.

* Logging requests (logging proxy). This is when you want to keep a history of requests to the service object.
    The proxy can log each request before passing it to the service.

* Caching request results (caching proxy). This is when you need to cache results of client requests and manage the life cycle of this cache, especially if results are quite large.
    The proxy can implement caching for recurring requests that always yield the same results. The proxy may use the parameters of requests as the cache keys.

* Smart reference. This is when you need to be able to dismiss a heavyweight object once there are no clients that use it.
    The proxy can keep track of clients that obtained a reference to the service object or its results. From time to time, the proxy may go over the clients and check whether they are still active. If the client list gets empty, the proxy might dismiss the service object and free the underlying system resources.

    The proxy can also track whether the client had modified the service object. Then the unchanged objects may be reused by other clients.