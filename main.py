import requests

def compare_institutions(name_1, name_2):
    '''Compare 2 institutions given their display names'''
    r_1 = requests.get(f'https://api.openalex.org/institutions?filter=display_name.search:{name_1}').json()['results'][0]
    r_2 = requests.get(f'https://api.openalex.org/institutions?filter=display_name.search:{name_2}').json()['results'][0]

    keys_1 = list(r_1.keys())
    keys_1.remove('international')
    keys_1.remove('associated_institutions')
    keys_1.remove('counts_by_year')
    keys_1.remove('x_concepts')

    keys_2 = list(r_2.keys())
    keys_2.remove('international')
    keys_2.remove('associated_institutions')
    keys_2.remove('counts_by_year')
    keys_2.remove('x_concepts')

    print(f'=== {name_1} ===')
    for key in keys_1:
        print(key, '->',r_1[key])
    print('\n')

    print(f'=== {name_2} ===')
    for key in keys_2:
        print(key, '->',r_2[key])

first_name = input('Institution #1: ')
second_name = input('Institution #2: ')

# Run func
compare_institutions(first_name, second_name)