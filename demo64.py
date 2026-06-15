'''
Encapsulation: It wraps up states& behaviours of entity in a container & accessing using public data handler method
'''
class BankAccount:
    def __init__(self,name,acc_no,pin):
        self._name=name
        self._acc_no=acc_no
        self._pin=pin
        print('Bank Account is Created')
    def get_name(self):
        print(self._name)
    def get_accno(self):
        print(self._acc_no)
    def get_pin(self):
        print(self._pin)
b1=BankAccount('scott',1234567890,1234)
b1.get_name()
b1.get_accno()
b1.get_pin()