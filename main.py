from global_state import GlobalState
from infrastructure import load_users, load_products
from ui import auth_page, profile, shop
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
USERS_CSV = str(BASE_DIR / "data" / "users.csv")
PRODUCTS_CSV = str(BASE_DIR / "data" / "products.csv")

def main() -> None:
    state = GlobalState()
    state["message"] = ""
    state["current_user"] = None

    users = load_users(USERS_CSV)
    products = load_products(PRODUCTS_CSV)

    page = "auth"

    while True:
        if page == "auth":
            page = auth_page(users)
        elif page == "profile":
            page = profile(users)
        elif page == "shop":
            page = shop(users, products, USERS_CSV)
        elif page == "exit":
            break
        else:
            state["message"] = "Неизвестная страница"
            page = "auth"


if __name__ == "__main__":
    main()
