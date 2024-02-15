import ccxt
import requests


class Client:
    def __init__(self):
        self.exchange_trust_list = self.fetch_exchange_trust_list()
        self.exchanges = self.restructure_ccxt_exchanges()
        self.exchanges = self.sort_exchanges()

    def restructure_ccxt_exchanges(self):
        # Restructure All Available Exchanges From CCXT
        exchanges = []
        for exchange_id in ccxt.exchanges:
            exchange = getattr(ccxt, exchange_id)
            exchange = exchange()

            # Remove Alias Exchanges To Avoid Duplicates
            if exchange.alias:
                continue

            # Append Dict To "exchanges[]"
            obj = {
                "id": exchange_id,
                "name": exchange.name,
                "logo": exchange.urls["logo"],
            }
            exchanges.append(obj)

        # Return "exchanges[]" Or A Default Exchange If Something Went Wrong
        if exchanges:
            return exchanges
        else:
            return [
                {
                    "id": "binance",
                    "name": "Binance",
                    "logo": "https://user-images.githubusercontent.com/1294454/29604020-d5483cdc-87ee-11e7-94c7-d1a8d9169293.jpg",
                }
            ]

    def fetch_exchange_trust_list(self):
        # Fetch Exchanges Based On Trust Score From CoinGecko
        exchange_list = requests.get("https://api.coingecko.com/api/v3/exchanges")
        if exchange_list.status_code == 200:
            data = exchange_list.json()
            exchange_trust_score = []
            for ex in data:
                exchange_trust_score.append(ex["name"])

            return exchange_trust_score
        else:
            return None

    def sort_exchanges(self):
        # Sort The Exchanges Based On The Top 50 Trusted Score From CoinGecko
        def custom_sort(item):
            exchange_name = item["name"]
            try:
                return (
                    self.exchange_trust_list.index(exchange_name)
                    if self.exchange_trust_list is not None
                    else self.exchanges
                )
            except ValueError:
                return len(self.exchanges)

        return sorted(self.exchanges, key=custom_sort)

    def set_client(self, client):
        # On Exchange Change, Adapt The Client
        exchange = getattr(ccxt, client)
        self.current = exchange({"enableRateLimit": True, "timeout": 20000})
        # Fetch "markets", "base_currency" And "base_markets" Based On New Client
        load_markets = self.current.load_markets()
        self.markets = [
            element for element in load_markets.keys() if ":" not in element
        ]

        base_frequency = {}
        for item in self.markets:
            key = item.split("/", 1)[0]
            if key in base_frequency:
                base_frequency[key] += 1
            else:
                base_frequency[key] = 1

        # Create a list of unique elements
        unique_base_items = list(
            dict.fromkeys([element.split("/", 1)[0] for element in self.markets])
        )

        # Sort the unique list based on frequency
        self.base_markets = sorted(
            unique_base_items, key=lambda x: base_frequency[x], reverse=True
        )

        self.timeframes = self.convert_timeframes(self.current.timeframes)

    def convert_timeframes(self, timeframes):
        print(timeframes)
        readable_timeframes = {}

        for key, value in timeframes.items():
            # Extract the numeric part
            numeric_part = "".join(filter(str.isdigit, key))
            # Extract the unit part
            unit = "".join(filter(str.isalpha, key))

            # Check if numeric_part is not empty before converting
            if numeric_part:
                quantity = int(numeric_part)
            else:
                quantity = int(1)

            # Determine the readable format based on the unit
            if unit == "s":
                readable_timeframes[key] = (
                    f"{quantity} Second{'s' if quantity > 1 else ''}"
                )
            elif unit == "m":
                readable_timeframes[key] = (
                    f"{quantity} Minute{'s' if quantity > 1 else ''}"
                )
            elif unit == "h":
                readable_timeframes[key] = (
                    f"{quantity} Hour{'s' if quantity > 1 else ''}"
                )
            elif unit == "d":
                readable_timeframes[key] = (
                    f"{quantity} Day{'s' if quantity > 1 else ''}"
                )
            elif unit == "w":
                readable_timeframes[key] = (
                    f"{quantity} Week{'s' if quantity > 1 else ''}"
                )
            elif unit == "M":
                readable_timeframes[key] = (
                    f"{quantity} Month{'s' if quantity > 1 else ''}"
                )

        return readable_timeframes
