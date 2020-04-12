package main

import "fmt"

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
	return &Alipay{
		// money: string,  // remain here as an example.
	}
}

type WechatPayFactory struct{}

func (wp *WechatPayFactory) Create_payment() Payment {
	return &WechatPay{}
}

func main() {
	money := "100"
	pay := &AlipayFactory{}
	// // pay := AlipayFactory()   // 不是这样调用的，会报如下错误
	//      ./factory-luffycity.go:42:22: missing argument to conversion to AlipayFactory: AlipayFactory())
	p := pay.Create_payment()
	m := p.Pay(money)
	fmt.Println(m)
}

// func main() {
// 	method := "alipay"
// 	money := "100"
// 	pay := PaymentFactory(method)
// 	m := pay.Pay(money)
// 	fmt.Println(m)
// }
