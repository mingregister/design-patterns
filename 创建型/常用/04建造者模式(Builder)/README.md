### 作用：
将一个复杂对象的构建与它的表示分离，使得同样的构建过程可以创建不同的表示。
--
构造函数、set方法、建造者模式三种对象创建方式

### 角色：
1. 抽象建造者(Builder)
2. 具体建造者(Concrete Builder): 每一个方法*都应该*能建造Product的一部分属性。
3. 指挥者(Director)
4. 产品(Product)
*The "director" invokes "builder" services as it interprets the external format. The "builder" creates part of the complex object each time it is called and maintains all intermediate state. When the product is finished, the client retrieves the result from the "builder".*

### 对比工厂模式
建造者模式与抽象工厂模式相似，也用来创建复杂对象。
主要区别在于建行者模式着重一步步构造**一个复杂对象**，而抽象工厂模式着重于**多个系列的(一组)产品的对象**。--对应现实场景中有什么么?

顾客走进一家餐馆点餐，我们利用工厂模式，根据用户不同的选择，来制作不同的食物，比如披萨、汉堡、沙拉。
对于披萨来说，用户又有各种配料可以定制，比如奶酪、西红柿、起司，我们通过建造者模式根据用户选择的不同配料来制作披萨。


### 优缺点
#### 优点
1. 隐藏了一个产品的内部结构和装配过程
2. 将构造代码与表示代码分开 
3. 可以对构造过程进行更精细的控制

#### 缺点