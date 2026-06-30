from behave import given, then, when

@given("que el usuario abre la página de WordCounter")
@given("que el usuario abre la pagina de WordCounter")
def open_word_counter_page(context):
    context.word_counter_page.open()


@when('el usuario ingresa el texto "{text}"')
def enter_text(context, text):
    context.word_counter_page.enter_text(text)


@when("el usuario ingresa el siguiente texto")
def enter_multiline_text(context):
    context.word_counter_page.enter_text(context.text)


@when("el usuario no ingresa ningún texto")
def enter_empty_text(context):
    context.word_counter_page.enter_text("")


@then("la aplicacion debe mostrar {expected_count:d} palabras")
def validate_word_count(context, expected_count):
    context.word_counter_page.wait_for_word_count(expected_count)


@then("el número de palabras debe ser {expected_count:d}")
def validate_word_number(context, expected_count):
    context.word_counter_page.wait_for_word_count(expected_count)


@then("la aplicacion debe mostrar {expected_count:d} caracteres")
def validate_character_count(context, expected_count):
    context.word_counter_page.wait_for_character_count(expected_count)


@then("el número de caracteres debe ser {expected_count:d}")
def validate_character_number(context, expected_count):
    context.word_counter_page.wait_for_character_count(expected_count)


@then('la sección "{section_name}" debe mostrar')
def validate_keyword_density(context, section_name):
    expected_density = [
        {
            "palabra": row["palabra"],
            "repeticiones": int(row["repeticiones"]),
        }
        for row in context.table
    ]

    context.word_counter_page.wait_for_keyword_density(expected_density)


@then('la sección "{section_name}" no debe mostrar resultados')
def validate_empty_keyword_density(context, section_name):
    context.word_counter_page.wait_for_empty_keyword_density()
