import re

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from locators.word_counter_locators import WordCounterLocators
from utils.driver_factory import DriverFactory


class WordCounterPage:
    URL = "https://wordcounter.net/"
    CHARACTER_COUNT = (By.ID, "character_count")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, DriverFactory.DEFAULT_TIMEOUT)

    def open(self):
        self.driver.get(self.URL)
        self._wait_until_loaded()

    def enter_text(self, text):
        editor = self.wait.until(EC.element_to_be_clickable(WordCounterLocators.EDITOR))
        editor.click()
        editor.send_keys(Keys.CONTROL, "a")
        editor.send_keys(Keys.BACKSPACE)
        editor.send_keys(text)
        editor.send_keys(Keys.SHIFT)

    def get_word_count(self):
        counter = self.wait.until(EC.visibility_of_element_located(WordCounterLocators.WORD_COUNT))
        counter_text = counter.text.strip()
        match = re.search(r"\d+", counter_text)

        if not match:
            raise ValueError(f"Word count value was not found in text: '{counter_text}'")

        return int(match.group())

    def wait_for_word_count(self, expected_count):
        try:
            self.wait.until(lambda _: self.get_word_count() == expected_count)
        except TimeoutException as exc:
            actual_count = self.get_word_count()
            raise AssertionError(
                f"Expected {expected_count} words, but found {actual_count}."
            ) from exc

    def get_character_count(self):
        counter = self.wait.until(EC.visibility_of_element_located(self.CHARACTER_COUNT))
        counter_text = counter.text.strip()
        match = re.search(r"\d+", counter_text)

        if not match:
            raise ValueError(f"Character count value was not found in text: '{counter_text}'")

        return int(match.group())
    

    def wait_for_character_count(self, expected_count):
        try:
            self.wait.until(lambda _: self.get_character_count() == expected_count)
        except TimeoutException as exc:
            actual_count = self.get_character_count()
            raise AssertionError(
                f"Expected {expected_count} characters, but found {actual_count}."
            ) from exc

    def get_keyword_density(self):
        items = self.wait.until(
            EC.visibility_of_all_elements_located(WordCounterLocators.KEYWORD_DENSITY_ITEMS)
        )
        density = []

        for item in items:
            word_elements = item.find_elements(*WordCounterLocators.KEYWORD_DENSITY_WORD)

            if not word_elements:
                continue

            word = word_elements[0].text.strip()
            repetitions_text = item.find_element(
                *WordCounterLocators.KEYWORD_DENSITY_REPETITIONS
            ).text.strip()
            match = re.search(r"\d+", repetitions_text)

            if not match:
                raise ValueError(
                    f"Keyword repetitions value was not found in text: '{repetitions_text}'"
                )

            density.append({"palabra": word, "repeticiones": int(match.group())})

        return density

    def wait_for_keyword_density(self, expected_density):
        try:
            self.wait.until(lambda _: self.get_keyword_density()[: len(expected_density)] == expected_density)
        except TimeoutException as exc:
            actual_density = self.get_keyword_density()[: len(expected_density)]
            raise AssertionError(
                f"Expected keyword density {expected_density}, but found {actual_density}."
            ) from exc

    def wait_for_empty_keyword_density(self):
        try:
            self.wait.until(
                lambda _: len(
                    self.driver.find_elements(*WordCounterLocators.KEYWORD_DENSITY_WORDS)
                )
                == 0
            )
        except TimeoutException as exc:
            actual_density = self.get_keyword_density()
            raise AssertionError(
                f"Expected no keyword density results, but found {actual_density}."
            ) from exc
        

    def _wait_until_loaded(self):
        self.wait.until(EC.visibility_of_element_located(WordCounterLocators.EDITOR))
        self.wait.until(EC.visibility_of_element_located(WordCounterLocators.WORD_COUNT))


    def validate_most_repeated_word(self, expected_word):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);"
        )
        time.sleep(0.5)

        elemento_palabra = self.wait.until(EC.visibility_of_element_located(WordCounterLocators.MOST_REPEATED_WORD
            )
        )
        WebDriverWait(self.driver, 5).until(lambda driver: elemento_palabra.text.strip() != ""
        )
        palabra_obtenida = elemento_palabra.text.strip().lower()

        assert palabra_obtenida == expected_word.lower(), (
            f"Se esperaba '{expected_word}' "
            f"pero se obtuvo '{palabra_obtenida}'"
        )
