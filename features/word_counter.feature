# language: es
Característica: Word Counter

  Escenario: Validar el conteo de palabras
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el texto "Jose"
    Entonces la aplicacion debe mostrar 1 palabras


  Escenario: Validar el conteo de caracteres
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el texto "Hola"
    Entonces la aplicacion debe mostrar 4 caracteres


  Escenario: Validar las tres palabras más repetidas
    Dado que el usuario abre la página de WordCounter
    Cuando el usuario ingresa el siguiente texto
      """
      rojo rojo rojo
      azul azul
      verde
      """
    Entonces la sección "Densidad de palabras clave" debe mostrar
      | palabra | repeticiones |
      | rojo    | 3            |
      | azul    | 2            |
      | verde   | 1            |


  Escenario: Validar un texto vacío
    Dado que el usuario abre la página de WordCounter
    Cuando el usuario no ingresa ningún texto
    Entonces el número de palabras debe ser 0
    Y el número de caracteres debe ser 0
    Y la sección "Densidad de palabras clave" no debe mostrar resultados
