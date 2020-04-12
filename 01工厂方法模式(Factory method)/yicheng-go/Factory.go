package main

import "fmt"


type Operator interface {
	Setleft(int)
	SetRight(int)
	Result()int
}

// 工厂接口
type OperatorFactory interface {
    Creater() Operator
}

type OperatorBase struct{
    left,right int
}

// 赋值
func (op *OperatorBase)Setleft(left int){
    op.left = left
}
func (op *OperatorBase)SetRight(right int){
    op.right = right 
}


// 操作的抽象
type PlusOperatorFactory struct{}
type PlusOperator struct{
    *OperatorBase
}

// 实际运行
type (o *PlusOperator) Result() int {
    return o.right + o.left
}

func (PlusOperatorFactory)Create()Operator{
    return &PlusOperator{ OperatorBase:&OperatorBase{}}
}


func main(){
    var fac OperatorFactory
    fac = PlusOperatorFactory{}
    op := fac.Create()
    op.Setleft(20)
    op.SetRight(10)
    fmt.Println(op.Result())
}


[xxxx@alivm yicheng-go]$ go build
# Factory
./Factory.go:37:24: syntax error: unexpected Result after top level declaration]
