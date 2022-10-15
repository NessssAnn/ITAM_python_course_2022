def greeting (name, surname):
    text = '''Доброго времени суток, '''+name+''' "Человек" '''+surname+'''!'''
    return text

str = input().split(" ")
print(greeting(str[0], str[1]))