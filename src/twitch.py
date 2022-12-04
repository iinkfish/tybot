import json 
import requests
from datetime import datetime

with open('./data/botConfig.json') as config_file:
    config = json.load(config_file)

with open('./data/botData.json') as data_file:
    data = json.load(data_file)


def get_app_access_token():
    params = {
        "client_id": config["botMeta"]["TWITCH_CLIENT_ID"],
        "client_secret": config["botMeta"]["TWITCH_CLIENT_SECRET"],
        "grant_type": "client_credentials"
    }

    response = requests.post("https://id.twitch.tv/oauth2/token", params=params)
    access_token = response.json()["access_token"]
    return access_token

# access_token = get_app_access_token()

# print(access_token)

def get_users(login_names): 
    params = {
        "login": login_names
    }

    headers = {
        "Authorization": "Bearer {}".format(config["botMeta"]["TWITCH_CLIENT_TOKEN"]),
        "Client-Id": config["botMeta"]["TWITCH_CLIENT_ID"]
    }

    response = requests.get("https://api.twitch.tv/helix/users", params=params, headers=headers)
    return {entry["login"]: entry["id"] for entry in response.json()["data"]}

def get_streams(users):
    params = {
        "user_id": users.values()
    }

    headers = {
        "Authorization": "Bearer {}".format(config["botMeta"]["TWITCH_CLIENT_TOKEN"]),
        "Client-Id": config["botMeta"]["TWITCH_CLIENT_ID"]
    }

    response = requests.get("https://api.twitch.tv/helix/streams", params=params, headers=headers)
    return {entry["user_login"]: entry for entry in response.json()["data"]}

users = get_users(data["serverData"]["1044668454646587453"]["watchlist"])

# streams = get_streams(users)

# print(streams)

online_users = {}

def get_notifications():
    users = get_users(data["serverData"]["1044668454646587453"]["watchlist"])
    streams = get_streams(users)

    notifications = []
    for user_name in data["serverData"]["1044668454646587453"]["watchlist"]:
        # for full deploy use this but useful for testing
        if user_name not in online_users:
            online_users[user_name] = datetime.utcnow()

        if user_name not in streams:
            online_users[user_name] = None
        else: 
            started_at = datetime.strptime(streams[user_name]["started_at"], "%Y-%m-%dT%H:%M:%SZ")
            if online_users[user_name] is None or started_at > online_users[user_name]:
                notifications.append(streams[user_name])
                online_users[user_name] = started_at

    return notifications


notification = get_notifications()

print(notification)