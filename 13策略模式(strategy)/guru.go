package main 

// 尚未完成

type IStrategy interface {
	DoAlgorithm
}

// type IContext interface {
// 	Strategy
// 	SetStrategy
// 	DoSomeBusinessLogic
// }

type Context struct {
	strategy: IContext
}
 
// set strategy
func(c *Context) NewStrategy(strategy Strategy){
	return &strategy{}
}

func(c *Context) SetStrategy


type ConcreteStrategyA struct {

}

func(s *ConcreteStrategyA)DoAlgorithm(){
	
}
