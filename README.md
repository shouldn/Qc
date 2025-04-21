# Qcfrom binance.client import Client
import time

# بيانات حساب testnet
api_key = 'YOUR_TESTNET_API_KEY'
api_secret = 'YOUR_TESTNET_API_SECRET'

# تفعيل الاتصال مع testnet
client = Client(api_key, api_secret)
client.API_URL = 'https://testnet.binance.vision/api'

symbol = 'BTCUSDT'
quantity = 0.001

def get_price():
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

while True:
    try:
        price = get_price()
        print(f"السعر الحالي: {price} USDT")

        if price < 28000:
            order = client.order_market_buy(symbol=symbol, quantity=quantity)
            print("تم الشراء!")

        if price > 31000:
            order = client.order_market_sell(symbol=symbol, quantity=quantity)
            print("تم البيع!")

        time.sleep(30)

    except Exception as e:
        print("حدث خطأ:", e)
        time.sleep(10)
