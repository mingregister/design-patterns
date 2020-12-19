策略模式定义了一系列算法，并将每个算法封装起来，使他们可以相互替换，且算法的变化不会影响到使用算法的客户。需要设计一个接口，为一系列实现类提供统一的方法，多个实现类实现该接口，设计一个抽象类（可有可无，属于辅助类），提供辅助函数，关系图如下: 


  ![image](https://github.com/mingregister/design-patterns/blob/master/13%E7%AD%96%E7%95%A5%E6%A8%A1%E5%BC%8F/%E7%B1%BB%E5%9B%BE.jpg)


### 角色
1. Context
2. AbstractStrategy
3. ConcreateStrategy


### Relations with Other Patterns
* Bridge, State, Strategy (and to some degree Adapter) have very similar structures. Indeed, all of these patterns are based on composition, which is delegating work to other objects. However, they all solve different problems. A pattern isn’t just a recipe for structuring your code in a specific way. It can also communicate to other developers the problem the pattern solves.
* Command and Strategy may look similar because you can use both to parameterize an object with some action. However, they have very different intents.
* You can use Command to convert any operation into an object. The operation’s parameters become fields of that object. The conversion lets you defer execution of the operation, queue it, store the history of commands, send commands to remote services, etc.
* On the other hand, Strategy usually describes different ways of doing the same thing, letting you swap these algorithms within a single context class.
* Decorator lets you change the skin of an object, while Strategy lets you change the guts.
* Template Method is based on inheritance: it lets you alter parts of an algorithm by extending those parts in subclasses. Strategy is based on composition: you can alter parts of the object’s behavior by supplying it with different strategies that correspond to that behavior. Template Method works at the class level, so it’s static. Strategy works on the object level, letting you switch behaviors at runtime.
* State can be considered as an extension of Strategy. Both patterns are based on composition: they change the behavior of the context by delegating some work to helper objects. Strategy makes these objects completely independent and unaware of each other. However, State doesn’t restrict dependencies between concrete states, letting them alter the state of the context at will.