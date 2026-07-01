from multiprocessing import context
from selenium.webdriver.support import expected_conditions as EC
from behave import given, then, when
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
from locators.word_counter_locators import WordCounterLocators


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

    
@then('se valida que la palabra más se repite sea "{palabra_esperada}"')
def step_validate_most_repeated_word(context, palabra_esperada):
    context.word_counter_page.validate_most_repeated_word(palabra_esperada)
  