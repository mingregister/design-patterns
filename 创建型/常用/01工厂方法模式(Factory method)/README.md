

### 作用：
定义一个用于创建对象的接口(工厂接口)，让子类决定实例化哪一个产品类

### 角色
* 抽象工厂角色(Creator)
* 具体工厂角色(Concrete Creator)
* 抽象产品角色(Product)
* 具体产品角色(Concrete Product)

### 优缺点
#### 优点
1. 每个具体产品都对就一个具体工厂类，不需要修改工厂类代码
2. 隐藏了对象创建的实现细节

#### 缺点
1. 每增加一个具体产品类，都必须都加一个相应的具体工厂类


