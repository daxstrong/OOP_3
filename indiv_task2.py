from datetime import datetime


class Goods:
    def __init__(self, code, name, unit_price, quantity):
        self._code = code
        self._name = name
        self._unit_price = unit_price
        self._quantity = quantity

    # Property for code
    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, value):
        self._code = value

    # Property for name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    # Property for unit_price
    @property
    def unit_price(self):
        return self._unit_price

    @unit_price.setter
    def unit_price(self, value):
        self._unit_price = value

    # Property for quantity
    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    # Calculate total price for the goods
    def total_price(self):
        return self.unit_price * self.quantity

    def __str__(self):
        return (f"Goods(code={self.code}, name={self.name}, "
                f"unit_price={self.unit_price}, quantity={self.quantity})")


class Receipt:
    def __init__(self, number):
        self.number = number
        self.datetime = datetime.now()
        self.goods_list = []

    # Add a Goods object to the receipt
    def add_goods(self, goods):
        self.goods_list.append(goods)

    # Edit an existing Goods object identified by code
    def edit_goods(self, goods):
        for idx, g in enumerate(self.goods_list):
            if g.code == goods.code:
                self.goods_list[idx] = goods
                return True
        return False

    # Delete a Goods object by code
    def delete_goods(self, code):
        for g in self.goods_list:
            if g.code == code:
                self.goods_list.remove(g)
                return True
        return False

    # Search for a Goods object by code
    def search_goods(self, code):
        for g in self.goods_list:
            if g.code == code:
                return g
        return None

    # Calculate the total amount for the receipt
    def total_amount(self):
        return sum(g.total_price() for g in self.goods_list)

    def __str__(self):
        goods_str = "\n".join(str(g) for g in self.goods_list)
        return (f"Receipt Number: {self.number}\nDateTime: {self.datetime}\n"
                f"Goods:\n{goods_str}\nTotal Amount: {self.total_amount()}")


if __name__ == '__main__':
    # Create a receipt
    receipt = Receipt(number=1)

    # Create some goods
    apple = Goods(code=101, name="Apple", unit_price=0.5, quantity=10)
    bread = Goods(code=102, name="Bread", unit_price=1.5, quantity=2)
    milk = Goods(code=103, name="Milk", unit_price=0.99, quantity=5)

    # Add goods to receipt
    receipt.add_goods(apple)
    receipt.add_goods(bread)
    receipt.add_goods(milk)

    print("After adding goods:")
    print(receipt)

    # Edit quantity of bread
    bread.quantity = 3
    receipt.edit_goods(bread)

    print("\nAfter editing bread quantity:")
    print(receipt)

    # Delete milk from receipt
    receipt.delete_goods(103)

    print("\nAfter deleting milk:")
    print(receipt)

    # Search for apple
    searched_goods = receipt.search_goods(101)
    print("\nSearched Goods:")
    print(searched_goods if searched_goods else "Goods not found.")

    # Total amount
    total = receipt.total_amount()
    print(f"\nTotal Amount: {total}")