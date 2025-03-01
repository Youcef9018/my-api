{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 from fastapi import FastAPI\
from pydantic import BaseModel\
from typing import List\
\
app = FastAPI()\
\
# Sample in-memory database\
database = []\
\
# Data model\
class DataItem(BaseModel):\
    id: int\
    name: str\
    value: str\
\
# Add data to the database\
@app.post("/add_data/")\
def add_data(item: DataItem):\
    database.append(item)\
    return \{"message": "Data added successfully", "data": item\}\
\
# Retrieve all data\
@app.get("/get_data/", response_model=List[DataItem])\
def get_data():\
    return database\
\
# Retrieve specific data by ID\
@app.get("/get_data/\{item_id\}")\
def get_specific_data(item_id: int):\
    for item in database:\
        if item.id == item_id:\
            return item\
    return \{"error": "Item not found"\}\
\
# Run the API using:\
# uvicorn main:app --reload\
}