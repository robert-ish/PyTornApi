# gets the top 10 best profitable flips.
import PyTornApi as pt
client = pt.TornAPI('LWfGY7dM0GSLYFT2')

item_dataa = client.get_torn(0, pt.TornField.ITEMS)
items = item_dataa.get('items')

flips = []
for item_id, item_data in items:
    name = item_data.get("name")
    buy = item_data.get("buy_price", 0)
    sell = item_data.get("market_value", 0)
    if buy > 0:
        profit = sell-buy
        flips.append({
            "id": item_id,
            "name": name,
            "buy": buy,
            "sell": sell,
            "profit": profit
        })

flips.sort(key=lambda x: x["profit"], reverse=True)
for item in flips[:10]:
    print(f"{item['name']}: Buy ${item['buy']:,} | Sell ${item['sell']:,} | Profit ${item['profit']:,}")
