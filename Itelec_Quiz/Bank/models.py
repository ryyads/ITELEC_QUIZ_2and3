from django.db import models

class Account(models.Model):
    name = models.CharField(max_length=100)
    _balance = models.FloatField(default=0)

    def display_info(self):
        return f"The Account of {self.name} has balance {self._balance}"

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.save()
            return "Deposit is successful!!!"
        return "Invalid deposit amount"

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            self.save()
            return "Withdrawal is successful!!!"
        return "Insufficient balance"


    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount >= 0:
            self._balance = amount
            self.save()
            return "Balance updated"
        return "Negative balance not allowed"