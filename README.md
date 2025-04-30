# Mid-Interview

Objetivos:  
* Registrar FAQs  
* Buscar FAQ más parecida utilizando cálculo de similitud coseno.
  
Para ejecución:
1. Clonar repositorio.
2. ejecutar docker compose up --build.
3. acceder a http://localhost:3000/ desde un web browser.
   
### Hashing Trick / Feature Hashing    
1. Se concatenan pregunta + respuesta.
2. Se normalizan textos (se descartan carácteres no alfabéticos)
3. Se tokeniza el texto y se hashea la tabla de tokens.
4. los índices de la tabla hash corresponden a las posiciones en un vector de 128 elementos.

La similitud coseno se calculó dividiendo el producto punto de los vectores a comparar entre el producto de las magnitudes de los vectores.  

Las características a favor de este programa como prototipo:
* Las preguntas y respuestas se concatenan incorporando información de la respuesta (siendo que ambas están estrechamente relacionadas).
* HashTrick es eficiente (complejidad O(n))
* Similitud Coseno es un cálculo liviano.
* HashTrick resuelve el problema de dimensionalidad.
* Se puede ajustar la longitud del vector. Esta afecta la relación Costo/Presición
* Procesamiento general liviano.


  Tiempo invertido bruto: 32 horas.
