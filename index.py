from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/data', methods=['GET'])
def get_data():
    # Aqui você pode definir seu JSON de exemplo ou buscar os dados de outra fonte
    data = {
        "nome": "Exemplo",
        "idade": 30,
        "cidade": "São Paulo"
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)