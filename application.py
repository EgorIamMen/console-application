# ===--- application.py --------------------------------------------------=== #
#
# Это модуль для реализации Application Layer.
#
# Суть его состоит в том, чтобы описать логические действия, которые возможны
# в приложении.  В этой работе он может импортировать модули инфраструктуры,
# но смысл этого модуля - именно описать, что можно делать в приложении.
# Например, зарегистрироваться, сделать заказ, обновить данные профиля.  Для
# этого модуль может вызвать инфраструктурные методы, в которых содержится
# непосредственно реализация функционала.  Таким образом, будет получаться
# логическая цепочка, не привязанная к реализации.
#
# ===---------------------------------------------------------------------=== #
from typing import List
from domain import User, Product, NotFoundError, InvalidValueError

def find_user(users: List[User], username: str) -> User:
  for u in users:
    if u.login == username:
      return u
  raise NotFoundError("Пользователь не найден")


def find_product(products: List[Product], number: int) -> Product:
  for item in products:
    if item.number == number:
      return item
  raise NotFoundError("Товар не найден")


def logining(users: List[User], username: str, password: str) -> User:
  user = find_user(users, username)
  if user.password == password:
    return user
  
  raise InvalidValueError("Неверный логин или пароль")


def buy_product(users: List[User], products: List[Product], username: str, number: int) -> Product:
  user = find_user(users, username)
  product = find_product(products, number)
  user.decrease_money(product.price)
  return product




