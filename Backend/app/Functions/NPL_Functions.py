#para cálculos vectoriales.
import numpy as np
#importa producto punto
from numpy import dot
#importa método para obtener magnitudes.
from numpy.linalg import norm
#Para vectorizar con hashing (utilizado por AzureML)
import mmh3 as mhash
#para preprocesado de texto.
import re



def preprocess_text(raw_text):
    raw_text = raw_text.lower().strip()
    return re.sub(r'[^a-z\s]','', raw_text)


def vectorize(question=""):
    n = 128
    #genera vector de tamaño 128 (entre más grande, más preciso,pero más lento).
    vector = np.zeros(n)
    #se limpia texto y genera array donde cada elemento es una palabra
    words=preprocess_text(question).split()

    for word in words:
        index = mhash.hash(key=word,signed=False)%n
        vector[index]+=1 

    return vector

def get_cos_similarity(vectorA,vectorB):
    #Valida que no exista magnitudes de 0 (imposible dividir entre 0)
    divisor = norm(vectorA)*norm(vectorB)
    if divisor != 0 :
        #Se toma en cuenta que la similitud coseno es igual a el producto punto de dos vectores sobre la multiplicación de sus magnitudes.
        return dot(vectorA,vectorB)/divisor
    else: 
        return 0.0