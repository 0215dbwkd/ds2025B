def duplicate_city(cities):
    result = list()
    s = set()

    for city in cities:
        l1 = len(s)
        s.add(city)
        l2 = len(s)
        if l1 == l2: #중복값이 들어왔으면
            result.append(city)
    return result


cities = ['Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul']
#city = {'Incheon', 'Incheon', 'Incheon', 'Gimpo', 'Seoul', 'Seoul'} # set 중복안됨.

cities.append('Anyang')
cities.append('Seoul')

print(cities)
print(set(duplicate_city(cities)))