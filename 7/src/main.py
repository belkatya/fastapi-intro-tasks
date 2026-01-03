from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Product(BaseModel):  
    name: str
    price: float = Field(..., gt=0) 
    quantity: int = Field(..., ge=0)  

class Products(Product):
    id: int

class ProductsResponse(BaseModel):
    products: List[Products]

@app.post("/product")
async def add_product(product: Product):
    global product_id_counter, product_list
    product_with_id = Products(
        id=product_id_counter,
        **product.dict()
    )
    product_list.append(product_with_id) 
    product_id_counter += 1 
    return {"message": "Product added successfully", "product": product}  

@app.get("/products", response_model=ProductsResponse)
async def get_products() -> dict:
    return {"products": product_list}
# END
