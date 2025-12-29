# ===--- infrastructure.py -----------------------------------------------=== #
#
# Это модуль для реализации Infrastructure Layer.
#
# Его задача состоит в том, чтобы выполнить определенные действия, связанные с
# внешним миром.  Например, отправить данные в базу, закодировать пароль по
# определенному принципу, получить какую-то картинку из интернета и т. д.
# Этот слой - исполнитель, он делает то, что ему говорит Application Layer и
# отдает ему результат.
#
# ===---------------------------------------------------------------------=== #
from domain import User, Product
from typing import List
import csv 

def load_users(csv_path: str) -> List[User]:
  with open(csv_path, "r", encoding="utf-8", newline="") as f:
    users = []
    arr = csv.reader(f, delimiter=",")
    next(arr, None)
    for s in arr:
      login, password, email, balance = s
      users.append(User(login, password, email, int(balance)))
  return users


def load_products(csv_path: str) -> List[Product]:
  with open(csv_path, "r", encoding="utf-8", newline="") as f:
    products = []
    data = csv.reader(f, delimiter=",")
    next(data, None)
    for row in data:
      number, name, price = row
      products.append(Product(int(number), name, int(price)))
  return products


def save_users(csv_path: str, users: List[User]) -> None:
  with open(csv_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=",")
    writer.writerow(["login", "password", "email", "balance"])
    for elem in users:
      writer.writerow([elem.login, elem.password, elem.email, elem.balance])

