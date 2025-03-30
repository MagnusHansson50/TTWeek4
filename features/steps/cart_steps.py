from behave import given, when, then
from src.cart import Cart

@given("varukorgen är tom")
def step_given_empty_cart(context):
    context.cart = Cart()

@given('varukorgen innehåller en bok "{title}" med priset {price:d}')
def step_given_cart_with_book(context, title, price):
    context.cart = Cart()
    context.cart.add_book(title, price)

@given("varukorgen innehåller flera böcker")
def step_given_cart_with_multiple_books(context):
    context.cart = Cart()
    context.cart.add_book("Python Crash Course", 300)
    context.cart.add_book("Clean Code", 200)

@when('användaren lägger till en bok "{title}" med priset {price:d}')
def step_when_add_book(context, title, price):
    context.cart.add_book(title, price)

@when('användaren tar bort boken "{title}"')
def step_when_remove_book(context, title):
    context.cart.remove_book(title)

@when("användaren tömmer varukorgen")
def step_when_clear_cart(context):
    context.cart.clear_cart()

@when("användaren slutför köpet")
def step_when_checkout(context):
    context.checkout_message = context.cart.checkout()

@then("varukorgen ska vara tom")
def step_then_cart_should_be_empty(context):
    assert context.cart.total_books() == 0
    assert context.cart.total_price() == 0

@then("varukorgen ska innehålla {count:d} bok")
@then("varukorgen ska innehålla {count:d} böcker")
def step_then_cart_should_contain_books(context, count):
    assert context.cart.total_books() == count

@then("den totala summan ska vara {total_price:d}")
def step_then_total_price_should_be(context, total_price):
    assert context.cart.total_price() == total_price

@then("varukorgen ska innehålla {count:d} unik bok")
def step_then_cart_should_contain_unique_books(context, count):
    assert context.cart.unique_books() == count

@then('antalet av "{title}" ska vara {quantity:d}')
def step_then_book_quantity_should_be(context, title, quantity):
    assert context.cart.get_book_quantity(title) == quantity

@then("den totala summan ska vara {total_price:d} efter rabatt")
def step_then_total_price_with_discount(context, total_price):
    assert context.cart.total_price() == total_price

@given("varukorgen innehåller {count:d} böcker \"{title}\" med totalt pris {total_price:d}")
def step_given_cart_with_books_for_discount(context, count, title,  total_price):
    context.cart = Cart()
    price = total_price / count
    context.cart.add_book(title, price, count)

@given("en bok \"{title}\" finns i lager med {stock:d} exemplar")
def step_given_book_in_stock(context, title, stock):
    context.cart = Cart()
    context.cart.stock[title] = stock

@when("användaren försöker köpa {quantity:d} exemplar av \"{title}\"")
def step_when_try_to_buy_more_than_stock(context, quantity, title):
    context.purchase_message = context.cart.add_book(title, 100, quantity)

@then("ett meddelande visas \"{message}\"")
def step_then_stock_limit_message(context, message):
    assert context.purchase_message == message, f"Förväntade meddelande {message}, fick meddelande {context.purchase_message}"

@then("varukorgen innehåller {quantity:d} exemplar av \"{title}\"")
def step_then_cart_contains_limited_stock(context, quantity, title):
    assert context.cart.get_book_quantity(title) == quantity

@given("användaren försöker logga in med användarnamn \"{username}\" och lösenord \"{password}\"")
def step_given_user_tries_to_login(context, username, password):
    context.cart = Cart()
    context.login_result = context.cart.login(username, password)

@when("inloggning behandlas")
def step_when_login_processed(context):
    pass  # Inloggning skedde redan i Given

@then("inloggningen ska vara \"{result}\"")
def step_then_login_result(context, result):
    assert context.login_result == result

@given("en användare har tidigare beställningar")
def step_given_user_has_order_history(context):
    context.cart = Cart()
    context.cart.order_history.append({"Clean Code": 2, "Python Crash Course": 1})

@when("användaren tittar på sin orderhistorik")
def step_when_user_views_order_history(context):
    context.viewed_history = context.cart.order_history

@then("beställningarna ska visas korrekt")
def step_then_order_history_displayed_correctly(context):
    assert len(context.viewed_history) > 0

@given("en användare slutför ett köp")
def step_given_user_completes_purchase(context):
    context.cart = Cart()
    context.cart.logged_in = True  # Simulerar inloggning
    context.receipt_message = context.cart.checkout()

@when("systemet behandlar beställningen")
def step_when_system_processes_order(context):
    pass  # Behandlingen skedde redan i Given

@then("ett kvitto ska skapas")
@then("ett kvitto ska skickas till användaren")
def step_then_receipt_sent(context):
    assert context.receipt_message == "Kvitto skickat"
