from behave import given, when, then


@given("there is a {product}, which costs £{price}")
def step_impl(context, product, price):
    context.shelf.set_product_price(product, float(price))


@when("I add the {product} to the basket")
def step_impl(context, product):
    context.basket.add_product(product)


@then("I should have 1 product in the basket")
def step_impl(context):
    assert 1 == len(context.basket), \
        f"The product quantity should be 1, but the value returned was {len(context.basket)}"


@then("I should have {count} products in the basket")
def step_impl(context, count):
    assert int(count) == len(context.basket), \
        f"The product quantity should be {int(count)}, but the value returned was {len(context.basket)}"


@then("the overall basket price should be £{price}")
def step_impl(context, price):
    assert (float(price) == context.basket.get_total_price()), \
        f"The basket price should be {float(price)}, but the value returned was {context.basket.get_total_price()}"
