# language: es
Característica: Word Counter
  
  Escenario: Validar el conteo de palabras
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el texto "Hola Jose Andres"
    Entonces el número de palabras debe ser 3

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
    Entonces la palabra más repetida debe ser "hola"
    
  
  Escenario: Validar un texto vacío
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa un texto vacío
    Entonces la aplicacion debe mostrar 0 caracteres

  
  Escenario: Validar conteo de caracteres con palabra
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el texto "Hol@ Jose"
    Entonces la aplicacion debe mostrar 9 caracteres


  Escenario: Validación de conteo con espacios múltiples y saltos de línea
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el siguiente texto
      """
      hola      mundo
      
      selenium
      """
    Entonces el número de palabras debe ser 3
    Y la aplicacion debe mostrar 23 caracteres

  
  
  Escenario: Validar las palabras más repetidas
    Dado que el usuario abre la pagina de WordCounter
    Cuando el usuario ingresa el siguiente texto
      """
      lumu lumu lumu lumu lumu ilumina ilumina ataques y adversarios
      lumu ilumina todos los ataques y adversarios
      """
    Entonces las palabras más repetidas deben ser
      | palabra      | repeticiones |
      | lumu         | 6            |
      | ilumina      | 3            |
      | ataques      | 2            |

   
