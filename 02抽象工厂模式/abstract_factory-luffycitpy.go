package main

import (
    "fmt"
)

type PhoneShell interface {
    Show_shell()
}

type CPU interface {
    Show_cpu()
}

type OS interface {
    show_CPU()
}


type PhoneFactory interface {
    Make_shell()
    Make_cpu()
    Make_os()
}

type SmallShell struct{}
func(ss *SmallShell)Show_shell(){
    fmt.Println("普通手机小手机壳")
}

type BigShell struct{}
func(ss *BigShell)Show_shell(){
    fmt.Println("普通手机大手机壳")
}

type AppleShell struct{}
func(ss *AppleShell)Show_shell(){
    fmt.Println("苹果手机壳")
}

type SnapDragonCPU struct{}
func (sc *SnapDragonCPU)Show_cpu(){
    fmt.Println("骁龙CPU")
}

type MediaTekCPU struct{}
func (sc *MediaTekCPU)Show_cpu(){
    fmt.Println("联发科CPU")
}


type AppleCPU struct{}
func (sc *AppleCPU)Show_cpu(){
    fmt.Println("苹果CPU")
}


type Android struct{}
func(so *Android)Show_os(){
    fmt.Println("Android OS")
}

type IOS struct{}
func(so *IOS)Show_os(){
    fmt.Println("Android OS")
}

type MiFactory struct {}
func (mf *MiFactory)Make_cpu()PhoneFactory{
    return &SnapDragonCPU{}
}


func (mf *MiFactory)Make_os()PhoneFactory{
    return &Android{}
}

func (mf *MiFactory)Make_shell()PhoneFactory{
    return &BigShell{}
}

// type HuaweiFactory struct {}
// type IPhoneFactory struct {}

// client
type Phone struct{}
func(p *Phone)Show_info(shell PhoneShell, cpu CPU, os OS){
    fmt.Println("aa")
}


