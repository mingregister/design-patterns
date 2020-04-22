和代理模式感觉又有点像。

### 作用：


### 角色：
* Prototype
* ConcretePrototype


### 总结：
#### 优点：
1. 性能优化。       *每NEW一次，都需要执行一次构造函数，如果构造函数的执行时间很长，那么多次的执行这个初始化操作就实在是太低效了。一般在初始化的信息不发生变化的情况下，克隆是最好的办法。这既隐藏了对象创建的细节，又对性能是大大的提高，何乐而不为呢？*
2. You can clone objects without coupling to their concrete classes.
3. You can get rid of repeated initialization code in favor of cloning pre-built prototypes.
4. You can produce complex objects more conveniently.
5. You get an alternative to inheritance when dealing with configuration presets for complex objects.

#### 缺点：
1. Cloning complex objects that have circular references might be very tricky.


### Rules of thumb
* Sometimes creational patterns are competitors: there are cases when either Prototype or Abstract Factory could be used properly. At other times they are complementary: Abstract Factory might store a set of Prototypes from which to clone and return product objects. Abstract Factory, Builder, and Prototype can use Singleton in their implementations.
* Abstract Factory classes are often implemented with Factory Methods, but they can be implemented using Prototype.
* Factory Method: creation through inheritance. Prototype: creation through delegation.
* Often, designs start out using Factory Method (less complicated, more customizable, subclasses proliferate) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, more complex) as the designer discovers where more flexibility is needed.
* Prototype doesn't require subclassing, but it does require an "initialize" operation. Factory Method requires subclassing, but doesn't require Initialize.
Designs that make heavy use of the Composite and Decorator patterns often can benefit from Prototype as well.
* Prototype co-opts one instance of a class for use as a breeder of all future instances.
* Prototypes are useful when object initialization is expensive, and you anticipate few variations on the initialization parameters. In this context, Prototype can avoid expensive "creation from scratch", and support cheap cloning of a pre-initialized prototype.
* Prototype is unique among the other creational patterns in that it doesn't require a class – only an object. Object-oriented languages like Self and Omega that do away with classes completely rely on prototypes for creating new objects.

### Relations with Other Patterns:
* Many designs start by using Factory Method (less complicated and more customizable via subclasses) and evolve toward Abstract Factory, Prototype, or Builder (more flexible, but more complicated).
* Abstract Factory classes are often based on a set of Factory Methods, but you can also use Prototype to compose the methods on these classes.
* Prototype can help when you need to save copies of Commands into history.
* Designs that make heavy use of Composite and Decorator can often benefit from using Prototype. Applying the pattern lets you clone complex structures instead of re-constructing them from scratch.
* Prototype isn’t based on inheritance, so it doesn’t have its drawbacks. On the other hand, Prototype requires a complicated initialization of the cloned object. Factory Method is based on inheritance but doesn’t require an initialization step.
* Sometimes Prototype can be a simpler alternative to Memento. This works if the object, the state of which you want to store in the history, is fairly straightforward and doesn’t have links to external resources, or the links are easy to re-establish.
* Abstract Factories, Builders and Prototypes can all be implemented as Singletons.