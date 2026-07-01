# language: es
Característica: Word Counter
  
  Escenario: Validar el conteo de palabras
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el texto "Hola Jose"
    Entonces la aplicacion debe mostrar 2 palabras

  Escenario: Validar el conteo de caracteres
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el texto "Buenos dias"
    Entonces la aplicacion debe mostrar 11 caracteres

  
  Escenario: Validar la palabra más repetida
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el siguiente texto 
      """
      hola hola hola 
      mundo mundo 
      selenium
      """
    Entonces se valida que la palabra más se repite sea "hola"
    
  
  Escenario: Validar un texto vacío
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa un texto vacío
    Entonces la aplicacion debe mostrar 0 caracteres

  
  Escenario: Validar conteo de caracteres con palabra
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el texto "Hol@ Jose"
    Entonces la aplicacion debe mostrar 10 caracteres
   
