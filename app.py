from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11 or cpf == cpf[0] * 11:
        return False
    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        digito = ((soma * 10) % 11) % 10
        if digito != int(cpf[i]):
            return False
    return True

@app.route('/verificar-cpf', methods=['POST'])
def verificar_cpf():
    data = request.get_json()
    cpf = data.get('cpf', '')
    valido = validar_cpf(cpf)
    return jsonify({"valido": valido})

if __name__ == '__main__':
    app.run()
