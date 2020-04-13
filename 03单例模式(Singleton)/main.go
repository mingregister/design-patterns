package main

import (
	"factory/singleton" // 导入本地包的时候，前面的factory是包的名称，后面那个是package--通常与目录名称相同
)

func main() {
	mSingleton, nSingleton := singleton.NewSingleton("hello"), singleton.NewSingleton("hi")
	mSingleton.SaySomething()
	nSingleton.SaySomething()
}
