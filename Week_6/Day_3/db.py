import json
# json.dump - takes a string formatted like javascript and outputs json notation
# json.dumps - does similar but slightly different
# json.load - takes json and formats it back to python
def create_database(dst_file='my_file.json'):
    data = [
        {
            'name': 'iphone 9',
            'price': 799,
            'instock': True
        },

        {
            'name': 'Macbook Pro',
            'price': 4799,
            'instock': False
        },

        {
            'name': 'Apple Watch',
            'price': 10799,
            'instock': True
        },

        {
            'name': 'Apple stand pro',
            'price': 99999,
            'instock': True
        },
    ]
    with open(dst_file, 'w') as file_obj:
        json.dump(data, file_obj, indent=4)

def load_database(src_file='my_file.json'):
    with open(src_file, 'r') as f:
        data = json.load(f)
    return data

def update_database(products, src_file='my_file.json'):
    with open(src_file, 'w') as f:
        json.dump(products, f, indent=4)
        print("database updated...")
