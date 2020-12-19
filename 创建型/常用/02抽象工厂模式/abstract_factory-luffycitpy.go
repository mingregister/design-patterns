package main

import (
	"fmt"
)

// Abstract Product
type PhoneShell interface {
	Show_shell()
}

type CPU interface {
	Show_cpu()
}

type OS interface {
	Show_os()
}

// Abstract Factory
type PhoneFactory interface {
	Make_shell() PhoneShell
	Make_cpu() CPU
	Make_os() OS
}



// Concreate Product
type SmallShell struct{}

func (ss *SmallShell) Show_shell() {
	fmt.Println("普通手机小手机壳")
}

type SnapDragonCPU struct{}

func (sc *SnapDragonCPU) Show_cpu() {
	fmt.Println("骁龙CPU")
}

type Android struct{}

func (so *Android) Show_os() {
	fmt.Println("Android OS")
}

// Concreate factory
type MiFactory struct{}

func (mf *MiFactory) Make_cpu() CPU {
	// return &SnapDragonCPU{}
	return new(SnapDragonCPU)
}

func (mf *MiFactory) Make_os() OS {
	// return &Android{}
	return new(Android)
}

func (mf *MiFactory) Make_shell() PhoneShell {
	// return &BigShell{}
	return new(BigShell)
}

// 下面的属于扩展

type BigShell struct{}

func (ss *BigShell) Show_shell() {
	fmt.Println("普通手机大手机壳")
}

type AppleShell struct{}

func (ss *AppleShell) Show_shell() {
	fmt.Println("苹果手机壳")
}

type MediaTekCPU struct{}

func (sc *MediaTekCPU) Show_cpu() {
	fmt.Println("联发科CPU")
}

type AppleCPU struct{}

func (sc *AppleCPU) Show_cpu() {
	fmt.Println("苹果CPU")
}

type IOS struct{}

func (so *IOS) Show_os() {
	fmt.Println("IOS")
}

type HuaweiFactory struct{}

func (mf *HuaweiFactory) Make_cpu() CPU {
	return new(MediaTekCPU)
}

func (mf *HuaweiFactory) Make_os() OS {
	return new(Android)
}

func (mf *HuaweiFactory) Make_shell() PhoneShell {
	return new(SmallShell)
}

type IPhoneFactory struct{}

func (mf *IPhoneFactory) Make_cpu() CPU {
	return new(AppleCPU)
}

func (mf *IPhoneFactory) Make_os() OS {
	return new(IOS)
}

func (mf *IPhoneFactory) Make_shell() PhoneShell {
	return new(AppleShell)
}

// client
type Phone struct {
	cpu   CPU
	os    OS
	shell PhoneShell
}

// func(p *Phone)Show_info(shell PhoneShell, cpu CPU, os OS){
func (p *Phone) Show_info() {
	p.cpu.Show_cpu()
	p.os.Show_os()
	p.shell.Show_shell()
}

func Make_phone(factory PhoneFactory) Phone {
	cpu := factory.Make_cpu()
	os := factory.Make_os()
	shell := factory.Make_shell()
	return Phone{cpu, os, shell}
	// return Phone()
}

func main() {
	p1 := Make_phone(&MiFactory{})
	p1.Show_info()
}
