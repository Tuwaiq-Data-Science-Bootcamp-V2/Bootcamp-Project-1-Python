import hashlib

Users = {
    "User1": {
        "Name": "Saeed",
        "Age": 27,
        "ID": 1,
        "Cash": 211.22

    },
    "User2": {
        "Name": "Sara",
        "Age": 24,
        "ID": 2,
        "Cash": 577.56
    },
    "User3": {
        "Name": "Ahmed",
        "Age": 40,
        "ID": 3,
        "Cash": 1897.36
    }
}

filter_users = dict(filter(lambda x: x[1]["Cash"] >= 500, Users.items()))


def hash_user_data(hashed_data: dict):
    for key, value in hashed_data.items():
        hashed_data[key]["Cash"] = hashlib.sha256(str(value["Cash"]).encode()).hexdigest()
    return hashed_data


hashed_user_data = hash_user_data(filter_users)
print(hashed_user_data)
