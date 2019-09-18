import json
import urllib.request


class StockData:
    def fetchStockltp(self, stockname, indice):
        ltp = 0
        count = 0
        url = "https://appfeeds.moneycontrol.com/jsonapi/market/marketmap&format=&type=0&ind_id="+indice
        json_url = urllib.request.urlopen(url)
        jsondata = json.loads(json_url.read())
        # jsondata["item"] is in dictionary
        node = jsondata["item"]
        size = int(len(jsondata["item"]))
        for tempNode in range(0, size):
            # node is in List
            for x in node:
                # inner node is again in dictionary
                for key, value in x.items():
                    if str(value).lower().__contains__(stockname.lower()):
                        ltp = x["lastvalue"]
                        count += 1
        if count > 0:
            return ltp
        else:
            return 0
