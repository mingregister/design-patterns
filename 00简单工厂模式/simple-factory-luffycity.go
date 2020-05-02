package main

import "fmt"


// 相当于@abstractclassmethod
type Payment interface {
	Pay(money string) string
}

// 相当于抽象类：class Alipay(metaclass=ABCMeta)
type Alipay struct{}

// class Payment(metaclass=ABCMeta):
//     @abstractclassmethod
//     def pay(self, money):
//         pass


func (*Alipay) Pay(money string) string {
	return "支付宝余额支付元:" + " " + money
}

type WechatPay struct{}

func (*WechatPay) Pay(money string) string {
	return "微信余额支付元:" + " " + money
}

func PaymentFactory(method string) Payment {
	switch method {
	case "alipay":
		return &Alipay{}
	case "wechat":
		return &WechatPay{}
	}
	return nil
}

func main() {
	method := "alipay"
	money := "100"
	pay := PaymentFactory(method)
	m := pay.Pay(money)
	fmt.Println(m)
}
