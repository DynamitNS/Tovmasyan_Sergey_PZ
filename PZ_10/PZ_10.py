# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных
# некоторые из стран и какие не доставлены ни в одну страну.
# Данные о марках машин, экспортируемых в разные страны

exports = {
    'Страна1': {'Toyota', 'Lamborghini', 'Ford'},
    'Страна2': {'Toyota', 'BMW', 'Ford'},
    'Страна3': {'Lamborghini', 'BMW', 'Ford'},
}

all_brands = {'Toyota', 'Lamborghini', 'Ford', 'BMW', 'Nissan', 'Chevrolet', 'Mercedes'}

all_countries = set(exports.keys())

brands_in_all_countries = None
for country in all_countries:
    if brands_in_all_countries is None:
        brands_in_all_countries = exports[country]
    else:
        brands_in_all_countries &= exports[country]

brands_in_some_countries = set()
for country in all_countries:
    brands_in_some_countries = brands_in_some_countries.union(exports[country])

brands_not_delivered = all_brands - brands_in_some_countries

print(f'Марки машин, доставленные во все указанные страны: {brands_in_all_countries}')
print(f'Марки машин, доставленные в некоторые из стран: {brands_in_some_countries}')
print(f'Марки машин, не доставленные ни в одну страну: {brands_not_delivered}')
