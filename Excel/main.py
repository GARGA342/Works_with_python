import pandas as p

#GENERATING
products = {
    'Limpeza' : ['sabão', 'àlcool', 'detergente'],
    'Alimento' : ['arroz', 'batata', 'ovo'],
    'Tecnologia' : ['celular', 'tablet', 'smartwatch']
}

data = p.DataFrame(products)
data.to_excel('products.xlsx')

#READING
data = p.read_excel('products.xlsx')
print(f"All data:\n{data}\n\nLimpeza Column:\n{data['Limpeza']}\n\nAlimento Column:\n{data['Alimento']}\n\nTecnologia Column:\n{data['Tecnologia']}")