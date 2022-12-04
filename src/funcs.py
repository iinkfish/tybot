import json

def incrementInJSON(pathtoFile, serverName, counterType):
    with open(pathtoFile, "r") as f:
        data = json.load(f)
    if serverName not in data['serverData']:
        data['serverData'][serverName] = {
            "counter": {
                'hugCount': 0, 
                'cuteCount': 0
            },
            "watchlist": []
        }
        data['serverData'][serverName]['counter'][counterType] += 1
    else:
        data['serverData'][serverName]['counter'][counterType] += 1
    with open(pathtoFile, "w") as f:
        json.dump(data, f)
    return data['serverData'][serverName]["counter"][counterType]