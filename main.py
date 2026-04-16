

users: list = [
    {"username": "oliwia", "location": "łódź", "posts": "1", "usermessage": ["kocham legie", "sprzedam opla", "kiwi"]},
    {"username": "paweł", "location": "ostróda", "posts": "2", "usermessage": ["kocham legie1", "sprzedam opla1", ]},
    {"username": "eliza", "location": "radom", "posts": "3", "usermessage": ["kocham legie2", ]},
    {"username": "filip", "location": "dęblin", "posts": "4", "usermessage": ["kocham legie3", "sprzedam opla3", "kiwi3"]},
]

for user in users[1:]:
    print(f"Twój znajomy {user['username']} z miejscowości {user['location']} opublikował {user['posts']} wiadomości. Ostatnia wiadomość: {user['usermessage'][-1]}")

#     Twój znajomy Filip z miejscowości Dęblin opublikował jeden post o treści: zyczenia
