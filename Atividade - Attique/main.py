from database import Database
from lib.funcoes import validate_product_id, validate_category, print_products, print_categories

def add_product(db):
    product_id = input("ID do produto: ")
    if not validate_product_id(product_id):
        return
    name = input("Nome do produto: ")
    category = input("Categoria do produto: ")
    db.add_product(product_id, name, category)
    print("Produto cadastrado com sucesso!")

def get_products_by_category(db):
    category = input("Digite a categoria: ")
    products = db.get_products_by_category(category)
    print("Produtos na categoria '{}':".format(category))
    print_products(products)

def list_all_products(db):
    products = db.get_all_products()
    print("Lista de todos os produtos:")
    print_products(products)

def list_all_categories(db):
    categories = db.get_all_categories()
    print("Lista de todas as categorias:")
    print_categories(categories)

def update_product_category(db):
    product_id = input("ID do produto: ")
    if not validate_product_id(product_id):
        return
    new_category = input("Nova categoria: ")
    if not validate_category(new_category):
        return
    db.update_product_category(product_id, new_category)
    print("Categoria do produto atualizada com sucesso!")

def main():
    db = Database()
    while True:
        print("\n=== Menu ===")
        print("1. Cadastrar novo produto")
        print("2. Consultar produtos por categoria")
        print("3. Listar todos os produtos")
        print("4. Listar todas as categorias")
        print("5. Atualizar categoria de um produto")
        print("6. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            add_product(db)

        elif choice == "2":
            get_products_by_category(db)

        elif choice == "3":
            list_all_products(db)

        elif choice == "4":
            list_all_categories(db)

        elif choice == "5":
            update_product_category(db)

        elif choice == "6":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
