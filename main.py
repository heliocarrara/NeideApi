import pandas as pd
from flask import Flask, jsonify

app = Flask(__name__)

# Construir funcionalidades


@app.route('/')
def homepage():
  return 'A Api está no ar!'


@app.route('/pegarvendas')
def pegarvendas():
  tabela = pd.read_csv('12-18 - Criando API no Python.csv')
  total_vendas = tabela['Vendas'].sum()

  resposta = {'Total vendas:': total_vendas}

  return jsonify(resposta)


# Rodar
#if __name__ == '__main__':
    #app.run(host='0.0.0.0', port=8080, debug=False, use_reloader=False)

