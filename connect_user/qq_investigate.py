from util import *
import matplotlib.pyplot as plt


def get_email_provider(email):
    i = email.find("@")
    return email[i + 1:]


users = load("users.pickle")
user_clients = load("user_clients.pickle")
client_counter = {}
not_find = set()

qq_user_client_counter = {}
qq_user_counter = 0
mail_provider_counter_app = {}
mail_provider_counter = {}


def add_to_mail_provider_app(provider):
    if provider not in mail_provider_counter_app:
        mail_provider_counter_app[provider] = 1
    else:
        mail_provider_counter_app[provider] += 1


def add_to_mail_provider(provider):
    if provider not in mail_provider_counter:
        mail_provider_counter[provider] = 1
    else:
        mail_provider_counter[provider] += 1


for user in users:
    user_id = user[0]
    email = user[1]
    mail_provider = get_email_provider(email)
    add_to_mail_provider(mail_provider)
    if user_id not in user_clients:
        not_find.add((user_id, email))
    else:
        add_to_mail_provider_app(mail_provider)
        for client_id in user_clients[user_id]:
            if client_id not in client_counter:
                client_counter[client_id] = 1
            else:
                client_counter[client_id] += 1

        if "@qq.com" in email:
            qq_user_counter += 1
            for client_id in user_clients[user_id]:
                if client_id not in qq_user_client_counter:
                    qq_user_client_counter[client_id] = 1
                else:
                    qq_user_client_counter[client_id] += 1

x, y = sort_map(client_counter)
plt.scatter(x, y)
plt.show()

x, y = sort_map(qq_user_client_counter)
plt.scatter(x, y)
plt.show()

print("\n\n\nmail provider:")
x, y = sort_map(mail_provider_counter)
plt.scatter(x, y)
plt.show()


print("\n\n\nmail provider for app:")
x, y = sort_map(mail_provider_counter_app)
plt.scatter(x, y)
plt.show()