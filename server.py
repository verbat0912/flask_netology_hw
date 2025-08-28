from flask import Flask, jsonify, request

app = Flask(__name__)

# Список для хранения объявлений
ads = []
next_id = 1

@app.route('/ads', methods=['POST'])
def create_ad():
    global next_id
    ad = request.json
    ad['id'] = next_id
    ads.append(ad)
    next_id += 1
    return jsonify(ad), 201

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

if __name__ == '__main__':
    app.run(debug=True)