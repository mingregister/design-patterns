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

func PaymentFactory(method string) Payment {
	if method == "alipay" {
		return &Alipay{}
	} else if method == "wechat" {
		return &WechatPay{}
	} else {
		return nil
	}
}

func main() {
	method := "alipay"
	money := "100"
	pay := PaymentFactory(method)
	m := pay.Pay(money)
	fmt.Println(m)
}
