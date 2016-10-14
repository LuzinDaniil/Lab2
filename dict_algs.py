def dict(arr):
    res = []
    for i in arr:
        for child in i['children']:
            if child['age'] > 18:
                res.append(i['name'])
    return res


if __name__ == "__main__":

    ivan = {
        "name": "ivan",
        "age": 34,
        "children": [{
            "name": "vasja",
            "age": 12,
        }, {
            "name": "petja",
            "age": 10,
        }],
    }

    darja = {
        "name": "darja",
        "age": 41,
        "children": [{
            "name": "kirill",
            "age": 21,
        }, {
            "name": "pavel",
            "age": 15,
        }],
    }
    emps = [ivan, darja]
    print(dict(emps))
