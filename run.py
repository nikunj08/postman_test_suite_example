from flask import Flask, request
import response as resp

app = Flask(__name__)

dbz_list = [

    {
        "id": 1,
        "name": "goku",
        "race": "saiyan",
        "power_level": "Ultra Instinct",
        "status": "alive"
    }, {
        "id": 2,
        "name": "vegeta",
        "race": "saiyan",
        "power_level": "Ultra Blue",
        "status": "alive"
    }, {
        "id": 3,
        "name": "gohan",
        "race": "saiyan",
        "power_level": "Ultimate Gohan",
        "status": "alive"
    }, {
        "id": 4,
        "name": "trunks",
        "race": "saiyan",
        "power_level": "Super Saiyan Rage",
        "status": "alive"
    }
]


@app.route('/')
def get_dbz_list():
    return resp.success_json(dbz_list)


@app.route('/add', methods=['POST'])
def add_saiyan():
    dbz_input = request.json
    for dbz_obj in dbz_list:
        if dbz_input.get('id') == dbz_obj.get('id'):
            return resp.error_json(resp.InvalidInput(msg="Already have some character from this id."))
    dbz_list.append(request.json)
    return resp.success_json(dbz_list)


@app.route('/update', methods=['PUT'])
def update_saiyan():
    dbz_input = request.json
    for index, dbz_obj in enumerate(dbz_list):
        if dbz_input.get('id') == dbz_obj.get('id'):
            dbz_list.pop(index)
            dbz_list.append(dbz_input)
            return resp.success_json(dbz_list)
    return resp.error_json(resp.InvalidInput(msg="Could Not find this character"))


@app.route('/delete/<name>', methods=['DELETE'])
def delete_saiyan(name):
    for index, dbz_obj in enumerate(dbz_list):
        if dbz_obj.get('name') == name:
            dbz_list.pop(index)
            return resp.success_json(dbz_list)
    return resp.error_json(resp.InvalidInput(msg="Could Not find this character"))


@app.route('/get/<name>', methods=['GET'])
def get_dbz_char(name):
    for index, dbz_obj in enumerate(dbz_list):
        if dbz_obj.get('name') == name:
            return resp.success_json(dbz_obj)
    return resp.error_json(resp.InvalidInput(msg="Could Not find this character"))


if __name__ == '__main__':
    app.run()
