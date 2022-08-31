from unittest import result


def collectStrings(obj):
    result = []
    for key in obj:
        if type(obj[key]) is str:
            result.append(obj[key])
        elif type(obj[key]) is dict:
           result= result+collectStrings(obj[key])
    return result


obj = {
    "stuff": 'fool',
    "data": {
        "val": {
            "thing": {
                "info": 'bar',
                "moreInfo": {
                    "evenMoreInfo": {
                        "weMadeIt": 'baz'
                    }
                }
            }
        }
    }
}

output = collectStrings(obj)  # ['foo', 'bar', 'baz']
print(output)

