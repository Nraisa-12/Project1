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

codex = {
    "codex1": codex1,
    "codex2": codex2
}

@app.route('/')
def get_codex():
    return jsonify(codex)

if __name__ == '__main__':
    app.run(debug=True)



