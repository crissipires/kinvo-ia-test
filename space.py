import spacy 
import json

#carrego o modelo e indentifico qual é a linguagem
nlp = spacy.load("pt_core_news_sm")

#função pra obter a entidade
def getEntity():
    with open('quotes.json','r') as file:
        news = json.loads(file.read())
        output = {}

        for new in news:
            new = new['news']
            doc = nlp(new)
            entidades = []
            for entity in doc.ents:
                entidades.append({
                    "Trexo":entity.text,
                    "Entidade":entity.label_
                    })
            output[new] = entidades
    return output

