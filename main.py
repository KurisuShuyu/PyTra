from fastapi import FastAPI
import os
from binance.client import Client
from dotenv import load_dotenv

# Cargar las variables del archivo .env
load_dotenv()

app = FastAPI()

# Obtener las claves de entorno
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")

# Inicializar el cliente de Binance
# Nota: Si estás usando la Testnet (de prueba), debes habilitar testnet=True
client = Client(api_key, api_secret, testnet=True)

@app.get("/")
def leer_inicio():
    return {"mensaje": "¡Mi bot de Binance con FastAPI está funcionando!"}

@app.get("/precio/{simbolo}")
def obtener_precio(simbolo: str):
    try:
        # Consulta el precio a Binance (ejemplo: BTCUSDT)
        ticker = client.get_symbol_ticker(symbol=simbolo.upper())
        return ticker
    except Exception as e:
        return {"error": str(e)}

print(obtener_precio)