import finnhub

KEY = "*****************"

# Setup client
finnhub_client = finnhub.Client(api_key=KEY)
# Need to use _from instead of from to avoid conflict
print(finnhub_client.company_news('AAPL', _from="2025-05-22", to="2025-05-22"))