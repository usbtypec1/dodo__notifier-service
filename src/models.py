import uuid
from datetime import datetime
from typing import TypedDict, TypeAlias

from pydantic import BaseModel


class Event(TypedDict):
    type: str
    unit_id: int
    payload: dict


class CheatedOrder(BaseModel):
    created_at: datetime
    number: str


class CheatedOrders(BaseModel):
    unit_name: str
    phone_number: str
    orders: list[CheatedOrder]


class StopSale(BaseModel):
    unit_name: str
    started_at: datetime


class StopSaleByIngredients(StopSale):
    reason: str
    ingredient_name: str


class StopSaleByChannels(StopSale):
    reason: str
    sales_channel_name: str


class StopSaleByStreets(StopSale):
    street_name: str


class StopSaleBySectors(StopSale):
    sector_name: str


class ReportFromMongoDB(TypedDict):
    chat_id: int
    unit_ids: list[int]


class OrderByUUID(BaseModel):
    unit_name: str
    created_at: datetime
    receipt_printed_at: datetime
    number: str
    type: str
    price: int
    uuid: uuid.UUID


EventPayload: TypeAlias = (
        OrderByUUID
        | StopSaleByStreets
        | StopSaleByChannels
        | StopSaleBySectors
        | StopSaleByIngredients
        | CheatedOrders
)