class Shelf:
    def __init__(self) -> None:
        self.price_map = dict()

    def set_product_price(self, product: str, price: float) -> None:
        self.price_map[product] = price

    def get_product_price(self, product: str) -> float:
        return self.price_map[product]
