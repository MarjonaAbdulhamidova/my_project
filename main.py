from models import *
from database import Base,engine,SessionLocal ,sessionmaker


Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind = engine)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

try:
    # 1. Seller qo'shish
    s_name = input("Sotuvchi ismini kiriting: ")
    new_seller = seller(name=s_name)
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    print(f"Sotuvchi qo'shildi! ID: {new_seller.id}")

    
    p_name = input("Mahsulot nomini kiriting: ")
    p_desc = input("Tavsifini kiriting: ")
    p_price = float(input("Narxini kiriting: "))
    new_product = product(name=p_name, description=p_desc, price=p_price)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    print(f"Mahsulot qo'shildi! ID: {new_product.id}")

    
    c_name = input("Mijoz ismini kiriting: ")
    new_customer = customer(name=c_name)
    db.add(new_customer)
    db.commit()
    db.refresh(new_customer)
    print(f"Mijoz qo'shildi! ID: {new_customer.id}")

except Exception as e:
    db.rollback()
    print(f"Xatolik yuz berdi: {e}")
finally:
    db.close()