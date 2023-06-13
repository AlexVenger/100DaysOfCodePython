from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


class CoffeeMachine:
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    resources = coffee_maker.resources

    def run_coffee_machine(self):
        todo = ""
        while todo != "off":
            todo = input(f"What would you like? {self.menu.get_items()}")
            if todo == "report":
                self.coffee_maker.report()
            elif todo == "off":
                return
            else:
                drink = self.menu.find_drink(todo)
                if self.coffee_maker.is_resource_sufficient(drink) and self.money_machine.make_payment(drink.cost):
                    self.coffee_maker.make_coffee(drink)


coffee_machine = CoffeeMachine()
coffee_machine.run_coffee_machine()
