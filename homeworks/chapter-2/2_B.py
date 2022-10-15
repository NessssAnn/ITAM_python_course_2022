def comparison(a = dict(), b = dict()):
    dict3=dict()
    for key1 in a.keys():
        if not b.get(key1):
            dict3[key1] = 'deleted'
    for key2 in b.keys():
        if a.get(key2):
            if b.get(key2)==a.get(key2):
                dict3[key2] ='equal'
            else:
                dict3[key2] ='changed'
        else:
            dict3[key2] = 'added'
    return dict3

dict1 = {"a":"b", "b":"a",  "c": "a"}
dict2 = {"a":"b", "b":"a"}

print(comparison(dict1,dict2))

