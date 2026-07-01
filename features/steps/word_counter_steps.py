from multiprocessing import context

from behave import given, then, when


@given("que el usuario abre la pagina de WordCounter")
def open_word_counter_page(context):
    context.word_counter_page.open()


@when('el usuario ingresa el texto "{text}"')
def enter_text(context, text):
    context.word_counter_page.enter_text(text)


@when("el usuario ingresa el siguiente texto")
def enter_multiline_text(context):
    context.word_counter_page.enter_text(context.text)


@when("el usuario ingresa un texto vacío")
def step_impl(context):
    context.word_counter_page.enter_text("")


@then("el número de palabras debe ser {expected_count:d}")
def validate_word_number(context, expected_count):
    context.word_counter_page.wait_for_word_count(expected_count)


@then("la aplicacion debe mostrar {expected_count:d} caracteres")
def validate_character_count(context, expected_count):
    context.word_counter_page.wait_for_character_count(expected_count)


@then("el número de caracteres debe ser {expected_count:d}")
def validate_character_number(context, expected_count):
    context.word_counter_page.wait_for_character_count(expected_count)


@then('la palabra más repetida debe ser "{expected_word}"')
def validate_most_repeated_word(context, expected_word):
    context.word_counter_page.validate_most_repeated_word(expected_word)     
  

@then("las palabras más repetidas deben ser")
def validate_words_by_frequency(context):
    expected = [
        (row["palabra"], int(row["repeticiones"]))
        for row in context.table
    ]
    context.word_counter_page.validate_words_by_frequency(expected)