from flask import Flask
import random
app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>hola esta es una pagina de datos aleatorios</h1> <a href="/random_fact">¡Ver un dato aleatorio!</a>,<a href="/coin.flip"> Ver tiro de moneda </a>'
@app.route("/random_fact")
def facts():
    facts_list=['Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos',
                'Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo',
                'La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos',
                'Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones.']
    return f'<p>{random.choice(facts_list)}</p> <a href="/">¡Volver!</a>'
@app.route('/coin.flip')
def coins():
    resultado = random.choice(["Cara", "Cruz"])
    return f'<p>{resultado}</p>  <a href="/">¡Volver!</a>'
app.run(debug=True)
