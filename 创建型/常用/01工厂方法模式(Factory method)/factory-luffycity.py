# -*- coding:utf-8 -*-  

from abc import ABCMeta, abstractclassmethod 

class Payment(metaclass=ABCMeta):
    @abstractclassmethod
    def pay(self, money):
        pass

class Alipay(Payment):
    def __init__(self, use_huabei=False):
        self.use_huabei = use_huabei

    def pay(self, money):
        if self.use_huabei:
            print("花呗支付%d元" % money)
        else:
            print("支付宝余额支付%d元" % money)

class WechatPay(Payment):
    def pay(self, money):
        print("微信支付%d元" % money)



# # simple factory
# class PaymentFactory:
#     def create_payment(self, method):
#         if method == 'alipay':
#             return Alipay()
#         elif method == 'wechat':
#             return WechatPay()
#         elif method == 'huabei':
#             return Alipay(use_huabei=True)
#         else:
#             return TypeError("No such payment named %s" % method)
# # client
# pf = PaymentFactory()
# # p = pf.create_payment('huabei')
# p = pf.create_payment('alipay')
# p.pay(100)

# factory
class PaymentFactory(metaclass=ABCMeta):
    @abstractclassmethod 
    def create_payment(self):
        pass


class AlipayFactory(PaymentFactory):
    def create_payment(self):
        return Alipay()

class WechatPayFactory(PaymentFactory):
    def create_payment(self):
        return WechatPay()

class HuabeiFactory(PaymentFactory):
    def create_payment(self):
        return Alipay(use_huabei=True)
    
# 在工厂模式下，如果人有新需求，做如下两步
# step 1
class BankPay(Payment):
    def pay(self, money):
        print("银联支付%d元" % money)
# step 2
class BankPayFactory(PaymentFactory):
    def create_payment(self):
        return BankPay()


pf = BankPayFactory()
p = pf.create_payment()
p.pay(100)
