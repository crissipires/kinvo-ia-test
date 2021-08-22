from flask import Flask,requests
from werkzeug.wrappers import response
import spacy 

app = Flask("Minerando")

@app.route("/")
def scrape():
    params = {
        'news':'news',
        'start_requests':True
    }
    response = requests.get('http://localhost:9080/crawl.json',params)


@app.route('/extrair')
def extrairEntidades():
    nlp = spacy.load("pt_encore_web_sm")


    arq = open('quotes.json', encoding='utf8')
    doc = nlp(arq.read())

    print([(entity, entity.label) for entity in doc.ents])

