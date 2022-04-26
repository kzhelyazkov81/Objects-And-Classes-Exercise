class Catalogue:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name: str):
        self.products.append(product_name)

    def get_by_letter(self, first_letter: str):
        list_by_letter = []
        for product in self.products:
            if product[0] == first_letter:
                list_by_letter.append(product)
        return list_by_letter

    def __repr__(self):
        joined_products = '\n'.join(sorted(self.products))
        return f"Items in the {self.name} catalogue:\n{joined_products}"


catalogue = Catalogue("Furniture")
catalogue.add_product("Sofa")
catalogue.add_product("Mirror")
catalogue.add_product("Desk")
catalogue.add_product("Chair")
catalogue.add_product("Carpet")
print(catalogue.get_by_letter("C"))
print(catalogue)
