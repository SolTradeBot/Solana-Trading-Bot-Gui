import os
import time
import requests
import hmac
import hashlib
from typing import Dict, Any
from flask import Flask, render_template_string

class TonSwapClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.tonswap.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from TonSwap: {resp.text}")

class StonfiClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.stonfi.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from Stonfi: {resp.text}")

class DeDustClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.dedust.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from DeDust: {resp.text}")

class MegatonClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.megaton.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from Megaton: {resp.text}")

class TegroClient:
    def __init__(self, api_key: str, secret_key: str):
        self.base_url = "https://api.tegro.com"
        self.api_key = api_key
        self.secret_key = secret_key

    def _sign_request(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        message = "&".join(f"{k}={v}" for k,v in sorted(payload.items()))
        signature = hmac.new(
            self.secret_key.encode('utf-8'),
            message.encode('utf-8'),
            hashlib.sha256
        ).hexdigest()
        headers = {
            "X-API-KEY": self.api_key,
            "X-SIGNATURE": signature
        }
        return headers

    def get_price(self, base: str, quote: str) -> float:
        endpoint = f"{self.base_url}/market/price"
        params = {"base": base, "quote": quote}
        resp = requests.get(endpoint, params=params, timeout=5)
        if resp.status_code == 200:
            data = resp.json()
            return float(data.get("price", 0.0))
        else:
            raise Exception(f"Failed to fetch price from Tegro: {resp.text}")

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Arbitrage Scanner</title>
<style>
body {
  font-family: Arial, sans-serif;
  margin: 20px;
  background: #f5f5f5;
}
h1 {
  color: #333;
}
table {
  border-collapse: collapse;
  width: 100%;
  margin-top: 20px;
  background: #fff;
}
th, td {
  text-align: left;
  padding: 10px;
  border-bottom: 1px solid #ddd;
}
th {
  background: #eee;
}
.highlight {
  color: green;
  font-weight: bold;
}
</style>
</head>
<body>
<h1>Arbitrage Scanner</h1>
<p>Base: {{ base }} | Quote: {{ quote }}</p>
<table>
<thead>
<tr>
<th>Platform</th>
<th>Price</th>
</tr>
</thead>
<tbody>
{% for item in prices %}
<tr>
<td>{{ item[0] }}</td>
<td>{{ item[2] }}</td>
</tr>
{% endfor %}
</tbody>
</table>
{% if opportunity %}
<p class="highlight">Arbitrage opportunity found: Buy from {{ opportunity.cheapest[0] }} at {{ opportunity.cheapest[2] }} and sell on {{ opportunity.priciest[0] }} at {{ opportunity.priciest[2] }}</p>
{% else %}
<p>No profitable opportunity detected.</p>
{% endif %}
</body>
</html>
"""

@app.route("/")
def arbitrage_scanner():
    # API credentials should be secured properly.
    tonswap = TonSwapClient(api_key=os.getenv("TONSWAP_API_KEY", "YOUR_TONSWAP_API_KEY"),
                            secret_key=os.getenv("TONSWAP_SECRET_KEY", "YOUR_TONSWAP_SECRET"))
    stonfi = StonfiClient(api_key=os.getenv("STONFI_API_KEY", "YOUR_STONFI_API_KEY"),
                          secret_key=os.getenv("STONFI_SECRET_KEY", "YOUR_STONFI_SECRET"))
    dedust = DeDustClient(api_key=os.getenv("DEDUST_API_KEY", "YOUR_DEDUST_API_KEY"),
                          secret_key=os.getenv("DEDUST_SECRET_KEY", "YOUR_DEDUST_SECRET"))
    megaton = MegatonClient(api_key=os.getenv("MEGATON_API_KEY", "YOUR_MEGATON_API_KEY"),
                            secret_key=os.getenv("MEGATON_SECRET_KEY", "YOUR_MEGATON_SECRET"))
    tegro = TegroClient(api_key=os.getenv("TEGRO_API_KEY", "YOUR_TEGRO_API_KEY"),
                        secret_key=os.getenv("TEGRO_SECRET_KEY", "YOUR_TEGRO_SECRET"))

    base = "TON"
    quote = "USDT"
    amount = 10.0

    try:
        prices = [
            ("TonSwap", tonswap, tonswap.get_price(base, quote)),
            ("Stonfi", stonfi, stonfi.get_price(base, quote)),
            ("DeDust", dedust, dedust.get_price(base, quote)),
            ("Megaton", megaton, megaton.get_price(base, quote)),
            ("Tegro", tegro, tegro.get_price(base, quote))
        ]

        cheapest = min(prices, key=lambda x: x[2])
        priciest = max(prices, key=lambda x: x[2])

        profit_threshold = 0.05
        if priciest[2] - cheapest[2] > profit_threshold:
            opportunity = {
                "cheapest": cheapest,
                "priciest": priciest
            }
        else:
            opportunity = None

        return render_template_string(HTML_TEMPLATE,
                                      base=base,
                                      quote=quote,
                                      prices=prices,
                                      opportunity=opportunity)
    except Exception as e:
        return f"<h1>Error occurred:</h1><p>{str(e)}</p>", 500

if __name__ == "__main__":
    # Debug mode for testing. Disable in production.
    app.run(host="0.0.0.0", port=8080, debug=True)
