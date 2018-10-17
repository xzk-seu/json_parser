import json


def json_parse(name, temp_dict):
    # "dfn": "Blockchain"
    # if temp_dict.get("dfn") == "Blockchain":
    #     print('find in', name)
    #     return True
    for k, v in temp_dict.items():
        if v == "Blockchain":
            print('\nfind in', k)
            print(name)
            return True
        if isinstance(v, dict):
            if json_parse(k, v):
                print(k)
        if isinstance(v, list):
            for n, i in enumerate(v):
                if isinstance(i, dict):
                    if json_parse('%s[%d]' % (k, n), i):
                        print(name)
    return False


if __name__ == '__main__':
    with open('cs.json', 'r', encoding='UTF-8') as fr:
        js_dict = json.load(fr)

    if json_parse('root', js_dict):
        print('T')
    else:
        print('F')

    with open('cs.json', 'w', encoding='UTF-8') as fw:
        json.dump(js_dict, fw, indent=4)
