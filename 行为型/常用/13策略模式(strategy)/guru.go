package main

// 尚未完成

import (
	"fmt"
)

type IStrategy interface {
	DoAlgorithm()
}

type Context struct {
	strategy IStrategy
}

func (c *Context) DoSomeBusinessLogic() {
	c.strategy.DoAlgorithm()
}

func initContext(s IStrategy) *Context {
	return &Context{
		strategy: s,
	}
}

// set strategy
func (c *Context) SetStrategy(s IStrategy) {
	// 我可以通过结构体中的参数来传递*类实例*的参数，相当于python中的self.strategy=s
	c.strategy = s
}

type ConcreteStrategyA struct {
}

func (s *ConcreteStrategyA) DoAlgorithm() {
	fmt.Println("ConcreteStrategyA")
}

type ConcreteStrategyB struct {
}

func (s *ConcreteStrategyB) DoAlgorithm() {
	fmt.Println("ConcreteStrategyB")
}

func main() {
	csa := &ConcreteStrategyA{}
	context := initContext(csa)
	context.DoSomeBusinessLogic()

	csb := &ConcreteStrategyB{}
	context.SetStrategy(csb)
	context.DoSomeBusinessLogic()
}
