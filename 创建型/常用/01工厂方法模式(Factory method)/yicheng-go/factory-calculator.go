package main

import (
	"fmt"
)

// # from abc import ABCMeta, abstractclassmethod 

// # class Operation(metaclass=ABCMeta):
// # 	def __init__(self, a, b):
// # 		self.a = a
// # 		self.b = b

// # 	# @abstractclassmethod
// # 	def SetA(self, a):
// # 		self.a = a
// # 	# @abstractclassmethod
// # 	def SetB(self, b):
// # 		self.a = b 
// # 	@abstractclassmethod
// # 	def GetResult(self):
// # 		pass
type Operation struct {
	a float64
	b float64
}

func (op *Operation) SetA(a float64) {
	op.a = a
}

func (op *Operation) SetB(b float64) {
	op.b = b
}

// # class AddOperation(Operation):
// # 	def GetResult(self):
// # 		return self.a + self.b 
type AddOperation struct {
	Operation
}

func (this *AddOperation) GetResult() float64 {
	return this.a + this.b
}

// 作为具体工厂类的*返回值*，使它不仅仅限于基本类型 , 我个人觉得它和工厂模式是没有任何关系的，只是go的语法问题  // 那用结构体可以不?
type OperationI interface {
	GetResult() float64
	SetA(float64)
	SetB(float64)
}

// # class IFactory(metaclass=ABCMeta):
// # 	@abstractclassmethod
// # 	def CreateOperation() -> OperationI :
// # 		pass
type IFactory interface {
	CreateOperation() Operation
}

// # class AddFactory(IFactory):
// # 	def CreateOperation() -> OperationI:
// # 		return AddOperation()
type AddFactory struct {
}

func (this *AddFactory) CreateOperation() OperationI {
	return &(AddOperation{})
}

// 下面都是一样的结构，无需关注
type SubOperation struct {
	Operation
}

func (this *SubOperation) GetResult() float64 {
	return this.a - this.b
}

type MulOperation struct {
	Operation
}

func (this *MulOperation) GetResult() float64 {
	return this.a * this.b
}

type DivOperation struct {
	Operation
}

func (this *DivOperation) GetResult() float64 {
	return this.a / this.b
}

type SubFactory struct {
}

func (this *SubFactory) CreateOperation() OperationI {
	return &(SubOperation{})
}

type MulFactory struct {
}

func (this *MulFactory) CreateOperation() OperationI {
	return &(MulOperation{})
}

type DivFactory struct {
}

func (this *DivFactory) CreateOperation() OperationI {
	return &(DivOperation{})
}

func main() {
	fac := &AddFactory{} // 和 fac := &(AddFactory{})是一样的
	// fac := &(AddFactory{})
	// fac := &(SubFactory{})
	oper := fac.CreateOperation()
	oper.SetA(10)
	oper.SetB(20)
	fmt.Println(oper.GetResult())
}
