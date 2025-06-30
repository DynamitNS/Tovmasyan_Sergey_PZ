# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных
# некоторые из стран и какие не доставлены ни в одну страну.
# Данные о марках машин, экспортируемых в разные страны

country1_brands = {'Toyota', 'Lamborghini', 'Ford'}
country2_brands = {'Toyota', 'BMW', 'Ford'}
country3_brands = {'Lamborghini', 'BMW', 'Ford'}

all_brands = {'Toyota', 'Lamborghini', 'Ford', 'BMW', 'Nissan', 'Chevrolet', 'Mercedes'}

brands_in_all_countries = country1_brands & country2_brands & country3_brands

brands_in_some_countries = country1_brands | country2_brands | country3_brands

brands_not_delivered = all_brands - brands_in_some_countries

print(f'Марки машин, доставленные во все указанные страны: {brands_in_all_countries}')
print(f'Марки машин, доставленные в некоторые из стран: {brands_in_some_countries}')
print(f'Марки машин, не доставленные ни в одну страну: {brands_not_delivered}')