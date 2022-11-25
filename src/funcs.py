import json

def incrementInJSON(pathtoFile, serverName, counter):
    with open(pathtoFile, "r") as f:
        data = json.load(f)
    if serverName not in data['serverData']:
        data['serverData'][serverName] = {'hugCount': 0, 'cuteCount': 0}
        data['serverData'][serverName][counter] += 1
    else:
        data['serverData'][serverName][counter] += 1
    with open(pathtoFile, "w") as f:
        json.dump(data, f)
    return data['serverData'][serverName][counter]