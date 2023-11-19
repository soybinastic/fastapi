from fastapi import FastAPI
from routers import users, vehicle


app = FastAPI()

app.include_router(users.router)
app.include_router(vehicle.router)

@app.get("/products/")
def fetch_products():
    return { 'products' : [] }