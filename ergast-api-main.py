from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/drivers/fernando_alonso")
async def get_alonso_data():
    url = "http://ergast.com/api/f1/drivers/alonso.json"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return {
                "error": f"Failed to retrieve data, status code: {response.status_code}"
            }
