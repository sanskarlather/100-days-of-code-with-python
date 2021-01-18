from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
item=Menu.get_items(Menu())
cho=input(f"What would you like? ({item}): ")
while cho!='off':
    if cho=='report':
        coffee_maker.report()
        money_machine.report()
    else:
        espr=menu.find_drink(cho)
        if coffee_maker.is_resource_sufficient(espr):
            if money_machine.make_payment(menu.find_drink(cho).cost):
                coffee_maker.make_coffee(espr)
    cho=input(f"What would you like? ({item}): ")
