def validate_product_id(product_id):
    # Verifica se o ID do produto possui um formato válido
    if not product_id:
        print("ID do produto não pode estar vazio.")
        return False
    return True

def validate_category(category):
    # Verifica se o nome da categoria não está vazio
    if not category:
        print("Nome da categoria não pode estar vazio.")
        return False
    return True

def print_products(products):
    # Imprime uma lista de produtos
    for product in products:
        print(product["name"])

def print_categories(categories):
    # Imprime uma lista de categorias
    for category in categories:
        print(category)
