from datetime import datetime
from flask import Flask, jsonify, request


app = Flask(__name__)

# Список для хранения объявлений
ads = []
next_id = 1

@app.route('/ads', methods=['POST'])
def create_ad():
    global next_id
    ad = request.json
    if ad['title'] and ad['description'] and ad['owner'] != '':
        ad['id'] = next_id
        ad['created_at'] = datetime.now().strftime("%y-%m-%d")
        ads.append(ad)
        next_id += 1
        return jsonify(ad), 201
    else:
        return jsonify({'error': 'Данные заполнены не полностью, '
                          'проверьте заполненность данных'}), 400

@app.route('/ads', methods=['GET'])
def get_ads():
    return jsonify(ads), 200

@app.route('/ads/<int:ad_id>', methods=['GET'])
def get_ad(ad_id):
    for ad in ads:
        if ad['id'] == ad_id:
            return jsonify(ad), 200
    return jsonify({'error': 'Объявление не найдено'}), 404

@app.route('/ads/<int:ad_id>', methods=['DELETE'])
def delete_ad(ad_id):
    global ads
    ads = [ad for ad in ads if ad['id'] != ad_id]
    return jsonify({'message': 'Объявление удалено'}), 200

@app.route('/ads/<int:ad_id>', methods=['PUT'])
def put_ad(ad_id):
    global ads
    for ad in ads:
        if ad['id'] == ad_id:
            ad_put = request.json
            ads[ad_id - 1].update(ad_put)
            return jsonify({'messege': 'Объявление обновлено с индексом'f' {ad_id}' }), 200
        else:
            return jsonify({'message': 'Объявление не найдено'}), 404


if __name__ == '__main__':
    app.run(debug=True)