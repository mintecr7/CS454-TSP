import requests
# import tsplib95


url = "http://elib.zib.de/pub/mp-testdata/tsp/tsplib/tsp/a280.tsp"
r = requests.get(url)
cities = r.content.splitlines()

k = [str(i).strip("b'") for i in cities]
k.pop()
city_dic = {}
for i in range(6, len(k)):
    # h = k[i].split
    city = int(k[i].split()[0])
    x_cor = k[i].split()[1]
    y_cor = k[i].split()[2]
    city_dic[city] = (float(x_cor), float(y_cor))
# print(city_dic)
