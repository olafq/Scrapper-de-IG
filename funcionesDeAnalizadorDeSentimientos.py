import pandas as pd 
import spacy
from spacy.lang.es.examples import sentences 


import spacy
# Carga el pipeline pequeño de español
nlp = spacy.load("es_core_news_sm")

# Procesa un texto
doc = nlp("Ella corrio 10km")

# Itera sobre los tokens
for token in doc:
    # Imprime en pantalla el texto y la etiqueta gramatical predicha
    print(token.text, token.pos_)

import spacy
def preprocess_text(text):
    """
    Realiza el preprocesamiento básico de un texto en idioma español utilizando spaCy.
    Args:
        text (str): El texto a ser preprocesado.
    Returns:
        str: El texto preprocesado.
    """
    nlp = spacy.load('es_core_news_sm')
    doc = nlp(text)
    # Eliminación de palabras irrelevantes (stopwords) y signos de puntuación
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    # Reconstrucción del texto preprocesado
    preprocessed_text = ' '.join(tokens)
    return preprocessed_text
def extract_features(text):
    """
    Extrae las características del texto utilizando spaCy y devuelve un diccionario de características.
    Args:
        text (str): El texto del cual extraer características.
    Returns:
        dict: Un diccionario que representa las características extraídas del texto.
    """
    features = {}
    doc = nlp(text)
    for token in doc:
        if not token.is_stop and not token.is_punct:
            if token.lemma_.lower() in features:
                features[token.lemma_.lower()] += 1
            else:
                features[token.lemma_.lower()] = 1
    return features


training_data = [
    ("Me encanta el contenido del blog de Analytics Lane, los artículos son fantásticos.", "positivo"),
    ("El código no funciona, me ha dado un error al ejecutarlo.", "negativo"),
    ("Me encanta este producto.", "positivo"),
    ("Esta película fue terrible.", "negativo"),
    ("El clima está agradable hoy.", "positivo"),
    ("Me siento triste por las noticias.", "negativo"),
    ("Es solo un libro promedio.", "neutral")
]

from sklearn.feature_extraction import DictVectorizer
from sklearn.naive_bayes import MultinomialNB
# Preprocesamiento de los datos de entrenamiento
preprocessed_training_data = [(preprocess_text(text), label) for text, label in training_data]
# Extracción de características de los datos de entrenamiento
training_features = [extract_features(text) for text, _ in preprocessed_training_data]
vectorizer = DictVectorizer(sparse=False)
X_train = vectorizer.fit_transform(training_features)
# Etiquetas de los datos de entrenamiento
y_train = [label for _, label in preprocessed_training_data]
# Entrenamiento del clasificador Naive Bayes
classifier = MultinomialNB()
_ = classifier.fit(X_train, y_train)




def traer_excel(archivo_excel):
    return pd.read_excel(archivo_excel)

