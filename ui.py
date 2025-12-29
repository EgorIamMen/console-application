# ===--- ui.py -----------------------------------------------------------=== #
#
# Это модуль для реализации Presentation Layer.
#
# Его задача - просто отрисовать то, что должен видеть пользователь.  Он может
# вызывать действия, описанные в Application Layer и результат выполнения этих
# действий отображать пользователю.  Никакой бизнес-логики в слое представления
# быть не может.  Единственное, что можно делать - проверять валидность данных,
# которые вводит пользователь.  Например, все ли поля заполнены или проверка,
# не ввел ли пользователь мусор.  Если проверка затрагивает бизнес-правила, то
# выполнять ее следует в других слоях.
#
# ===---------------------------------------------------------------------=== #
from typing import List
from global_state import GlobalState
from application import logining
from domain import User, Product
from application import find_user, buy_product
from infrastructure import save_users

def read_msg() -> int | None:
  s = input().strip()
  try:
    return int(s)
  except ValueError:
    return None


def show_msg() -> None:
  state = GlobalState()
  text = state.get("message", "")
  if text:
    print(text)
    state["message"] = ""


def auth_page(users: List[User]) -> str:
  state = GlobalState()
  show_msg()

  print("Меню Авторизации")
  print("1) Войти в аккаунт")
  print("0) Завершить программу")

  choice = read_msg()
  if choice == 0:
    return "exit"
  if choice != 1:
    state["message"] = "Введите 1 или 0"
    return "auth"
  
  login = input("Логин: ").strip()
  password = input("Пароль: ").strip()

  try:
    user = logining(users, login, password)
  except ValueError as e:
    state["message"] = str(e)
    return "auth"
  
  state["current_user"] = user.login
  state["message"] = "Вход прошёл успешно"
  return "profile"


def profile(users: List[User]) -> str:
  state = GlobalState()
  show_msg()

  u = find_user(users, state["current_user"])

  print("Личный кабинет")
  print(f"Логин: {u.login}")
  print(f"Почта: {u.email}")
  print(f"Баланс: {u.balance} рублей")
  print()
  print("1) Перейти в магазин")
  print("2) Выйти из аккаунта")

  choice = read_msg()
  if choice == 1:
    return "shop"
  if choice != 2:
    state["message"] = "Введите 1 или 2"
    return "profile"
  
  state["message"] = "Вы вышли из аккаунта"
  state["current_user"] = None
  return "auth"


def shop(users: List[User], products: List[Product], users_csv_path: str):
  state = GlobalState()
  show_msg()

  print("Магазин")
  print("Выберите товар:")
  for i, p in enumerate(products, 1):
    print(f"{i}) {p.name} {p.price} руб.")
  print("0) Вернуться в личный кабинет из аккаунта")

  choice = read_msg()
  if choice is None:
    state["message"] = "Выберите пункт для покупки"
    return "shop"
  
  if choice == 0:
    return "profile"
  
  if choice < 1 or choice > len(products):
    state["message"] = "Такого товара нет в списке"
    return "shop"
  
  product = products[choice - 1]
  user = find_user(users, state["current_user"])
  try:
    bought = buy_product(users, products, user.login, product.number)
    state["message"] = f"Куплено: {bought.name} за {bought.price} руб."
    save_users(users_csv_path, users)
    return "shop"
  except ValueError as e:
    state["message"] = str(e)
    return "shop"