from database import Base
from sqlalchemy import Integer,String,Float,ForeignKey, DECIMAL
from sqlalchemy.orm import Mapped,mapped_column , relationship



class seller(Base):
    __tablename__ = "sellers"
 

    id: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length= 100))
    
    products: Mapped[list['product ']] = relationship("product",back_populates='seller',
                                                     cascade="all, delete-orphan")


class product(Base):
    __tablename__ = "products"


    id:Mapped[int]= mapped_column(Integer, primary_key=True, index=True)  
    name : Mapped[str] = mapped_column(String(length = 100))
    description : Mapped[str] = mapped_column(String(length = 500))
    price: Mapped[float] = mapped_column(DECIMAL(10,2))
    seller_id:Mapped[int]= mapped_column(Integer, ForeignKey("sellers.id"))

    sellers: Mapped ['seller'] = relationship("seller",back_populates="products")
    order_id: Mapped[int] = mapped_column(Integer, ForeignKey("orders.id"))
    order: Mapped["order"] = relationship("order", back_populates="products")

class customer (Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(Integer,primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(length= 100))
    orders: Mapped[list['order ']] = relationship('order',back_populates='customer',
                                                 cascade="all, delete-orphan")


class order(Base):
    __tablename__ = "orders"

    id:Mapped[int]= mapped_column(Integer, primary_key=True, index=True)  
    total_price: Mapped[float] = mapped_column(DECIMAL(10,2))
    customer_id:Mapped[int]= mapped_column(Integer, ForeignKey("customers.id"))
    customer: Mapped ['customer'] = relationship("customer",back_populates="orders",
                                                 cascade="all, delete-orphan")
    
    products: Mapped[list["product"]] = relationship("product", back_populates="order")


