class Cart:
    def __init__(self):
        self.items = {}
        self.order_history = []
        self.logged_in = False
        self.users = {"admin": "korrekt", "user2": "felaktig"}  # Enkel inloggning
        self.stock = {"Clean Code": 2, "Refactoring": 3, "Python Crash Course": 5, "Design Patterns": 2}

    def add_book(self, title, price, quantity=1):
        stock = self.stock[title]
        # Kontrollera om det finns tillräckligt med lager
        if title in self.stock and self.stock[title] == 0:
            return f"Tyvärr, boken \"{title}\" finns inte i lager."

        while quantity > 0:
            if title in self.stock and self.stock[title] > 0:
                # Om det finns lager, ta bort en bok från lagret och lägg till i varukorgen
                self.stock[title] -= 1
                if title in self.items:
                    self.items[title]['quantity'] += 1
                else:
                    self.items[title] = {'price': price, 'quantity': 1}
                quantity -= 1
            else:
                # Om det inte finns fler böcker i lager, ge ett meddelande
                return f"Endast {stock} exemplar finns i lager"

        # Om vi här har lagt till alla böcker i varukorgen, avsluta och returnera
        return f"{quantity} böcker har lagts till i varukorgen"

    def remove_book(self, title):
        if title in self.items:
            self.stock[title] += self.items[title]['quantity']  # Returnera till lager
            del self.items[title]

    def clear_cart(self):
        for title in self.items:
            self.stock[title] += self.items[title]['quantity']  # Returnera allt till lager
        self.items = {}

    def total_books(self):
        return sum(item['quantity'] for item in self.items.values())

    def unique_books(self):
        return len(self.items)

    def total_price(self):
        total = sum(item['price'] * item['quantity'] for item in self.items.values())
        return total * 0.9 if self.total_books() > 3 else total  # 10% rabatt om fler än 3 böcker

    def get_book_quantity(self, title):
        return self.items[title]['quantity'] if title in self.items else 0

    def login(self, username, password):
        if username in self.users:
            self.logged_in = self.users.get(username) == password
        return "lyckad" if self.logged_in else "misslyckad"

    def checkout(self):
        if not self.logged_in:
            return "Inloggning krävs"
        self.order_history.append(self.items.copy())
        self.clear_cart()
        return "Kvitto skickat"

