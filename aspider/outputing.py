'''
define some default output method
'''
import json


def write_csv(item_dict, file=None):
    pass


def write_json(item_dict, file=None):
    json_txt = json.dumps(item_dict, ensure_ascii=False)
    print(json_txt, file=file)
    file.close()


def write_txt(item_dict, file=None):
    for key, value in item_dict.items():
        print(f'**{key} - {value}\n', file=file)

    print('*' * 10, file=file)
    file.close()


def write_stream(item_dict, file=None):
    for key, value in item_dict.items():
        print(f'{key} - {value}\n')

    print('')


OUT_FUNCS = {
    'csv': write_csv,
    'json': write_json,
    'stream': write_stream,
    'txt': write_txt
}


def do_write(method, item_dict, file=None):
    func = OUT_FUNCS.get(method)
    if isinstance(file, str):
        file = open(file, 'a')
    if func:
        func(item_dict, file)
