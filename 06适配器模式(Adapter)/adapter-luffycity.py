# -*- coding:utf-8 -*-

from abc import ABCMeta, abstractclassmethod

class Payment(metaclass=ABCMeta):
    @abstractclassmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def pay(self, money):
        print("支付宝支付%d元" % money)

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)

class BankPay():
    def cost(self, money):               # 注意这里的cose，和上面的pay是不同名的。
        print("银联支付 %d 元" % money)


class ApplePay():
    def cost(self, money):               # 注意这里的cose，和上面的pay是不同名的。
        print("苹果支付 %d 元" % money)



# # 类的适配器：使用多继承   # 当有多个类需要适配的时候，就不太好用了，所以就有了下面的PaymentAdapter
# class NewBankPay(Payment, BankPay):
#     def pay(self, money):
#         self.cost(money)

# p = NewBankPay()
# p.pay(100)


# 对象适配器
class PaymentAdapter(Payment):
    def __init__(self, payment):
        self.payment = payment

    def pay(self, money):
        self.payment.cost(money)

p = PaymentAdapter(ApplePay())
p.pay(100)
