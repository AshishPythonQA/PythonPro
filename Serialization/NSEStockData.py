from Serialization import JsonSerialization


class JsonParser:
    try:
        ltp = 0
        count = 0
        pyobject = JsonSerialization.StockData()
        for x in range(1, 20):
            ltp = pyobject.fetchStockltp("ADANIPOWER", str(x))
            if ltp != 0:
                print(ltp)
                break
            else:
                raise Exception
    except Exception as e:
        print("Stock Data not found.")
