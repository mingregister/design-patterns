package main

import "fmt"

//from abc import ABCMeta, abstractclassmethod

// // 相当于抽象类
// class API(metaclass=ABCMeta):
//     @abstractclassmethod
//     def Say(self, name):
//         pass
type API interface {
	Say(name string) string
}

// class Chinese(API):
//     def Say(self, name):
//         print("你好, %s" % name)

type Chinese struct{}

func (*Chinese) Say(name string) string {
	return "你好" + " " + name
}

// class English(API)
type English struct{}

func (*English) Say(name string) string {
	return "hello" + " " + name
}

// 如果你要扩展，
// step 1
type Japanese struct{}

// step 2
func (*Japanese) Say(name string) string {
	return "日本人你好" + " " + name
}

// class NewAPI():
//     def create_api(self, str):
//         if str == "en":
//             return English()
//         elif str == "cn":
//             return Chinese()
//         elif str == "jp":
//             return Japanese()
//         else:
//             return None

func NewAPI(str string) API {
	if str == "en" {
		return &English{}
	} else if str == "cn" {
		return &Chinese{}
		// step 3
	} else if str == "jp" {
		return &Japanese{}
	} else {
		return nil
	}
}

// str1 = "en"
// name = "Trump"
// api = NewAPI()
// lang = api.create_api(str1)
// lang.Say(name)
func main() {
	str := "en"
	name := "Trump"
	api := NewAPI(str)
	server := api.Say(name)
	fmt.Println(server)
}
