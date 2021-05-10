# Задача 2

import json
# from copy import deepcopy


def sort_by_price_ascending(json_string):
    d_list = json.loads(json_string)
    for d in d_list:
        # use get for safety
        print(d.get('name'))
        print(d.get('price'))

    # sorted_obj = deepcopy(json_string)
    # sorted_obj = dict(sorted_obj)
    # print(sorted_obj)

    sorted_obj = sorted(d_list, key=lambda x: x['price'], reverse=True)
    #
    return sorted_obj


print(
    sort_by_price_ascending('[{"name":"eggs","price":1},{"name":"coffee","price":9.99},{"name":"rice","price":4.04}]'))
