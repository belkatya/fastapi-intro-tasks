from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class Specifications(BaseModel):
    size: str = Field(..., min_length=1, description="Размер продукта")
    color: str = Field(..., min_length=1, description="Цвет продукта")
    material: str = Field(..., min_length=1, description="Материал продукта")

class Product(BaseModel):
    name: str = Field(..., min_length=1, description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта, должна быть больше 0")
    specifications: Specifications

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

class ProductDetailResponse(BaseModel):
    id: int
    name: str
    price: float
    specifications: Specifications

@app.post("/product")
async def add_product(product: Product):
    global product_id_counter, product_list
    product_with_id = {
        "id": product_id_counter,
        "name": product.name,
        "price": product.price,
        "specifications": product.specifications.dict()
    }
    product_list.append(product_with_id)
    product_id_counter += 1
    return {
        "id": product_with_id["id"],
        "name": product_with_id["name"],
        "price": product_with_id["price"],
        "message": "Product added successfully"
    }

@app.get("/products")
async def get_products():
    products_response = []
    for product in product_list:
        products_response.append({
            "id": product["id"],
            "name": product["name"],
            "price": product["price"]
        })
    
    return products_response

@app.get("/product/{product_id}")
async def get_product(product_id: int):
    for product in product_list:
        if product["id"] == product_id:
            return {
                "id": product["id"],
                "name": product["name"],
                "price": product["price"],
                "specifications": product["specifications"]
            }
    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


# END