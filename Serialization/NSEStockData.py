from Serialization import JsonSerialization


class JsonParser:
    ltp = 0
    count = 0
    pyobject = JsonSerialization.StockData()
    for x in range(9, 20):
        ltp = pyobject.fetchStockltp("WIPRO", str(x))
        if ltp != 0:
            print(ltp)
            break
