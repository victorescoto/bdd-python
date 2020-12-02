from src import Basket, Shelf


def before_scenario(context, scenario):
    context.shelf = Shelf()
    context.basket = Basket(context.shelf)
