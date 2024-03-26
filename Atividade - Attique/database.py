class Database:
    def __init__(self):
        self.products = {}
        self.categories = {}

    def add_product(self, product_id, name, category):
        self.products[product_id] = {"name": name, "category": category}

    def update_product_category(self, product_id, new_category):
        if product_id in self.products:
            self.products[product_id]["category"] = new_category

    def delete_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    def add_category(self, category_id, name):
        self.categories[category_id] = name

    def get_products_by_category(self, category):
        return [product for product in self.products.values() if product["category"] == category]

    def get_all_products(self):
        return self.products.values()

    def get_all_categories(self):
        return self.categories.values()
