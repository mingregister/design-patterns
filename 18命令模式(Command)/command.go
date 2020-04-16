package main

import (
	"fmt"
)

var s_cmd make([]Command,3,5)

type Invoker struct {
	cmds s_cmd
}

type Ireceiver interface{
	action()
}

func(i *Invoker)Store_command(command Command){
	// p.cmds(command)
	append(command, p.cmds)
}

func(i *Invoker)Execute_commands(){
    for _, cmd := range p.cmds {  
        cmd.Execute()
    }  
}

type Command interface{
	Execute()
}

type ConcreteCommand struct{
	receiver Ireceiver
}

func(c *ConcreteCommand)Execute(){
	c.receiver.action()
}

type Receiver struct{}

func(r *Receiver)action(){
	fmt.Println("haha")
}

func main(){

	receiver := &Receiver{}

	concrete_command := &ConcreteCommand{receiver}

	i = &Invoker{s}
	i.Store_command(concrete_command)
	i.Execute_commands()


}
