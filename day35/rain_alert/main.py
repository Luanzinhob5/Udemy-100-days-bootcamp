import requests
api_key = "1096b0f9049e23ef32d88dc8ee2489a2"
lat = "-20.316839"
lon = "-40.309921"

requisicao = requests.get(f"")
requisicao.raise_for_status()
