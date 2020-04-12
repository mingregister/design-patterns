package main

import _ "fmt"

type Payment interface {
	Pay(money string) string
}

type Alipay struct{}

func (*Alipay) Pay(money string) string {
	return "支付宝余额支付元:" + " " + money
}

type WechatPay struct{}

func (*WechatPay) Pay(money string) string {
	return "微信余额支付元:" + " " + money
}

type PaymentFactory interface {
	Create_payment() Payment
}

type AlipayFactory struct{}

func (ap *AlipayFactory) Create_payment() Payment {
	return &Alipay{}
}

type WechatPayFactory struct{}

func (ap *WechatPayFactory) Create_payment() Payment {
	return &WechatPay{}
}

func main() {
	money := "100"
	pay := AlipayFactory()
	p := pay.Create_payment()
	m := p.Pay(money)
}

// func main() {
// 	method := "alipay"
// 	money := "100"
// 	pay := PaymentFactory(method)
// 	m := pay.Pay(money)
// 	fmt.Println(m)
// }
