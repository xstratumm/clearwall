from config import token
from requests import get
from time import sleep

def clear(token):
    ids = [0]

    while ids:
        ids.clear()
        posts = get_posts(token)

        for id in posts["response"]["items"]:
            ids.append(id["id"])

        for id in ids:
            get("https://api.vk.com/method/wall.delete",
                params = {"post_id": id, "access_token": token, "v": 5.103})

            sleep(0.5)


def get_posts(token):
    posts = get("https://api.vk.com/method/wall.get",
                params = {"count": 100, "access_token": token, "v": 5.103}).json()

    return posts


if __name__ == "__main__":
    clear(token)
