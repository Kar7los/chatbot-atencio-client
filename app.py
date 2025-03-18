from flask import Flask, request, jsonify
import random

app = Flask(__name__)

# Escenaris d'atenció al client
scenarios = {
    "producte_defectuós": "He rebut la meva comanda, però el producte està defectuós. Què puc fer?",
    "dubte_producte": "Estic interessat a comprar aquest producte, però tinc alguns dubtes sobre les seves característiques.",
    "suport_tècnic": "El meu dispositiu no funciona correctament. Em podrien ajudar?",
    "devolució": "Vull fer una devolució. Quin és el procediment?",
    "factura": "Necessito una factura amb les meves dades. Com puc sol·licitar-la?"
}

# Funció per avaluar respostes segons la rúbrica
def avaluar_resposta(resposta):
    criteris = {
        "cortesia": 1 if "gràcies" in resposta.lower() or "si us plau" in resposta.lower() else 0,
        "claredat": 1 if len(resposta) > 10 else 0,
        "resolució": 1 if "pot" in resposta.lower() or "solució" in resposta.lower() else 0,
        "formalitat": 1 if "estimat" in resposta.lower() or "atentament" in resposta.lower() else 0,
        "ortografia": 1  # Aquí podríem integrar un corrector ortogràfic més avançat
    }
    puntuacio_total = sum(criteris.values())
    return {"puntuacio": puntuacio_total, "detalls": criteris}

@app.route("/obtenir_escenari", methods=["GET"])
def obtenir_escenari():
    """Retorna un escenari aleatori per a l'alumne."""
    escenari = random.choice(list(scenarios.values()))
    return jsonify({"escenari": escenari})

@app.route("/avaluar_resposta", methods=["POST"])
def avaluar():
    """Rep una resposta de l'alumne i l'avalua segons la rúbrica."""
    data = request.json
    resposta = data.get("resposta", "")
    avaluacio = avaluar_resposta(resposta)
    return jsonify(avaluacio)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
