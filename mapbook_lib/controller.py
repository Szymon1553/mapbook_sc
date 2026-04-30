def read_data(users_data: list) -> None:
    for user in users_data:
        print(
            f"Twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiadomość: {user['usermessage'][-1]}")


def add_user(users_data: list) -> None:
    name = input('Podaj imię: ')
    place = input('Podaj miejscowość: ')
    post_num = int(input('Ile masz postów: '))
    mes_info = input('Przekaż wiadomość: ').split()
    users_data.append({"username": name, "location": place, "posts": post_num, "usermessage": mes_info})


def delete_user(users_data: list) -> None:
    name = input("Podaj imię użytkownika do usunięcia: ")
    for user in users_data:
        if user["username"] == name:
            users_data.remove(user)