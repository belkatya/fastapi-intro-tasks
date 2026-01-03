from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List


app = FastAPI()

# Временная база данных
product_list = []
product_id_counter = 1

# BEGIN (write your solution here)
class ProductSpecifications(BaseModel):
    size: str = Field(..., min_length=1, description="Размер продукта")
    color: str = Field(..., min_length=1, description="Цвет продукта")
    material: str = Field(..., min_length=1, description="Материал продукта")

class Product(BaseModel):
    name: str = Field(..., min_length=1, description="Название продукта")
    price: float = Field(..., gt=0, description="Цена продукта")
    specifications: ProductSpecifications

class Products(Product):
    id: int

class ProductsResponse(BaseModel):
    products: List[Products]

@app.post("/product")
async def add_product(product: Product):
    global product_id_counter, product_list
    if product.price <= 0:
        raise HTTPException(
            status_code=400,
            detail="Price must be greater than 0"
        )
    
    if not product.specifications:
        raise HTTPException(
            status_code=400,
            detail="Specifications are required"
        )
    product_with_id = Products(
        id=product_id_counter,
        **product.dict()
    )
    product_list.append(product_with_id)
    product_id_counter += 1
    return {"message": "Product added successfully", "product": product_with_id}

@app.get("/products", response_model=ProductsResponse)
async def get_products() -> dict:
    return {"products": product_list}

# END
