from . import Shelf


class Basket:
    def __init__(self, shelf: Shelf) -> None:
        self.shelf = shelf
        self.products = []
        self.products_price = 0.0

    def add_product(self, product: str) -> None:
        self.products.append(product)
        self.products_price += self.shelf.get_product_price(product)

    def get_total_price(self) -> float:
        return (
            self.products_price
            + (self.products_price * 0.2)
            + (2.0 if self.products_price > 10 else 3.0)
        )

    def __len__(self) -> int:
        return len(self.products)
