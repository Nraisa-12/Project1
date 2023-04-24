from flask import Flask, jsonify

app = Flask(__name__)

codex1 = {
    "A": "Diabetes mellitus",
    "B": "Hypertension",
    "C": "Coronary artery disease"
}
codex2 = {
    "1": "Infectious and parasitic diseases",
    "2": "Neoplasms",
    "3": "Diseases of the blood and blood-forming organs"
}

@app.route('/api/codex1')
def get_codex1():
    return jsonify(codex1)

@app.route('/api/codex2')
def get_codex2():
    return jsonify(codex2)

if __name__ == '__main__':
    app.run(debug=True)


