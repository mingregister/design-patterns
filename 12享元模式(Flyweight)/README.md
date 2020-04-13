### 作用：
1. 享元模式(Flyweight): 运用共享技术有效地支持大量细粒度的对象
2. 享元模式的主要目的是实现对象的共享，即共享池，当系统中对象多的时候可以减少内存的开销，通常与工厂模式一起使用。

**感觉和单例模式很象，我看flyweight.py的实现，就是：一个key仅允许创建一个实例，如果key不同，那就可以创建不同的实例**

### 优缺点：
The Flyweight pattern has a single purpose: minimizing memory intake. If your program doesn’t struggle with a shortage of RAM, then you might just ignore this pattern for a while.


### 角色：
