import spacy 
import json

#carrego o modelo e indentifico qual é a linguagem
nlp = spacy.load("pt_core_news_sm")

#função pra obter a entidade

with open('news.json','r') as file:
    news = json.loads(file.read())
    output = {}

    for new in news:
        new = str(new)
        doc = nlp(new)
        entidades = []
        for entity in doc.ents:
            entidades.append({
                "Trexo":entity.text,
                "Entidade":entity.label_
            })
            output[new] = entidades


print(output)