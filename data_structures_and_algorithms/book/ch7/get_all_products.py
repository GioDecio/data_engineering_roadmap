def get_all_products(array):

    products = []
    for i, n in enumerate(array):
        for j, m in enumerate(array[i + 1 :]):
            product = n * m
            products.append(product)

    return products


array = [1, 2, 3, 4, 5]

products = get_all_products(array)

print(products)
