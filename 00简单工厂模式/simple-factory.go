package main

import "fmt"

//
//

type API interface {
	Say(name string) string
}

func NewAPI(str string) API {
	if str == "en" {
		return &English{}
	} else if str == "cn" {
		return &Chinese{}
	} else if str == "jp" {
		return &Japanese{}
	} else {
		return nil
	}
}

type Chinese struct{}
func (*Chinese) Say(name string) string {
	return "你好" + name
}

type English struct{}

func (*English) Say(name string) string {
	return "hello" + name
}

// 如果你要扩展，
// step 1
type Japanese struct{}
// step 2
func (*Japanese) Say(name string) string {
	return "日本人你好" + name
}

func main() {
	str := "en"
	name := "Trump"
	api := NewAPI(str)
	server := api.Say(name)
	fmt.Println(server)
}
