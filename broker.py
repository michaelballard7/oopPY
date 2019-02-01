from bank import Account
from queue import LifoQueue


class Executor(Account):
    """ An account to execute buying and selling of an asset """

    def __init__(self, uni):
        self.client = Account('balance.txt')
        self.universe = uni
        self.available_cash = self.client.get_balance()  # update for leverage
        self.number_units_sought = 20  # base  on execution threads or pipes
        self.current_transaction_amount = 0
        self.commission_rate = 0.01
        self.order_type = ["limit", "market"]
        self.last_transactions = LifoQueue()  # provides me a put and get method

    def set_buy_price(self):
        selection = str(input("Enter asset: "))
        for asset in self.universe:
            for k, v in asset.items():
                if k == selection:
                    ask = v.get("ask")
                    if self.number_units_sought < v.get("shares_available"):
                        return int(ask * self.number_units_sought)

    def set_buy_order(self):
        order_value = self.set_buy_price()
        commission_value = self.commission_rate * order_value
        order = order_value + commission_value
        return order

    def execute_buy_order(self):
        buy_order = self.set_buy_order()
        print("Your current value inside execute order is ${}".format(client1.available_cash))
        self.client.withdraw(buy_order)
        self.last_transaction.put(("order value", buy_order))
        # complete the txn with client server interaction

    def set_sell_price(self):
        pass

    def execute_sell_order(self):
        pass

    def order_metrics(self):
        pass

    def fetch_universe(self):
        """ calls the fetcher class to get the investible universe" """
        pass


# eventuall fetch this information from portfolio or fetcher
fetched_uni = [{"abc": {'ask': 40, "shares_available": 3000}}, {"team": {'ask': 99.00, "shares_available": 200}}]

client1 = Executor(fetched_uni)
print("Your current value is ${}".format(client1.available_cash))
client1.execute_buy_order()
