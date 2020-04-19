### 作用：
迭代器模式提供一种方法 顺序访问一个聚合对象中各个元素，而不是暴露该对象的内部表示。

### 角色：
* AbstractAggregate(抽象聚集类)
* ConcreateAggregate
* AbstractIterator: 定义开始、下一个、是否结尾、当前是那一项 等方法.
* ConcreateIterator

### 应用场景：
1. 当你需要访问一个聚集对象，而且不管这些对象是什么都需要遍历的时候，你就应该考虑用迭代器模式。
2. 你需要对聚集有多种方式遍历时，可以考虑用迭代器模式。


###  Relations with Other Patterns
* You can use **Iterators** to traverse Composite trees.
* You can use **Factory Method** along with Iterator to let collection subclasses return different types of iterators that are compatible with the collections.
* You can use **Memento** along with Iterator to capture the current iteration state and roll it back if necessary.
* You can use **Visitor** along with Iterator to traverse a complex data structure and execute some operation over its elements, even if they all have different classes

###　Rules of thumb
* The abstract syntax tree of Interpreter is a Composite (therefore Iterator and Visitor are also applicable).
* Iterator can traverse a Composite. Visitor can apply an operation over a Composite.
* Polymorphic Iterators rely on Factory Methods to instantiate the appropriate Iterator subclass.
* Memento is often used in conjunction with Iterator. An Iterator can use a Memento to capture the state of an iteration. The Iterator stores the Memento internally.