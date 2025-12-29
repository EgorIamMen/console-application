# ===--- domain.py -------------------------------------------------------=== #
#
# Это модуль для реализации Domain Layer.
#
# Смысл его в том, чтобы описать модели, с которыми будет работать приложение.
# Например, пользователь, продукт, квартира, машина и т. д.  Эти модели
# содержат в себе свойства (баланс, цена, цвет и т. д.) и бизнес-правила,
# на которых держится приложение.  Например, в модели пользователя можно
# проверить, достаточно ли у него денег для покупки товара,а в модели
# товара - есть ли он на складе.
#
# ===---------------------------------------------------------------------=== #

class LittleMoney(Exception):
  pass

class NotFoundError(Exception):
  pass

class InvalidValueError(Exception):
  pass

class Product:
  def __init__(self, number: int, name: str, price: int) -> None:
    self.number = number
    self.name = name
    self.price = price


class User:
  def __init__(self, login: str, password: str, email: str, balance: int):
    self.login = login
    self.password = password
    self.email = email
    self.balance = balance


  def decrease_money(self, amount: int) -> None:
    if (self.balance < amount):
      raise LittleMoney("Недостаточно денег")
    
    self.balance -= amount