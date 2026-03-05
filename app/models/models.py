from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, Integer, ForeignKey

class Base(DeclarativeBase):
    # Цей клас буде спільним предком для всіх наших таблиць
    pass

class User(Base):
    __tablename__ = "users" # Назва таблиці в базі

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    username: Mapped[str] = mapped_column(String(50), unique=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)

    # Зв'язок One-to-One з Profile. 
    # uselist=False вказує, що це саме один об'єкт, а не список
    profile: Mapped["Profile"] = relationship(back_populates="user", uselist=False)


class Profile(Base):
    __tablename__ = "profiles"

    id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50))
    last_name: Mapped[str] = mapped_column(String(50))
    
    # Зовнішній ключ (ForeignKey), який посилається на таблицю users
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), unique=True)

    # Зворотний зв'язок до User
    user: Mapped["User"] = relationship(back_populates="profile")


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True)

    # Зв'язок One-to-Many з Product
    products: Mapped[list["Product"]] = relationship(back_populates="category")

class Product(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[int] = mapped_column(Integer)

    # Зовнішній ключ до категорії
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"))

    # Зворотний зв'язок до Category
    category: Mapped["Category"] = relationship(back_populates="products")

    reviews: Mapped[list["Review"]] = relationship(back_populates="product")

class Review(Base):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True)
    text: Mapped[str] = mapped_column(String(500))

    # Зовнішній ключ до продукту
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id"))

    # Зворотний зв'язок до Product
    product: Mapped["Product"] = relationship(back_populates="reviews")