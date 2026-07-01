from selenium.webdriver.common.by import By


class WordCounterLocators:
    EDITOR = (By.ID, "box")
    WORD_COUNT = (By.ID, "word_count")
    KEYWORD_DENSITY_ITEMS = (By.CSS_SELECTOR, "#kwd-accordion-data .list-group-item")
    KEYWORD_DENSITY_WORDS = (By.CSS_SELECTOR, "#kwd-accordion-data .list-group-item .word")
    KEYWORD_DENSITY_WORD = (By.CSS_SELECTOR, ".word")
    KEYWORD_DENSITY_REPETITIONS = (By.CSS_SELECTOR, ".badge")
    MOST_REPEATED_WORD = (By.XPATH, "//span[@class='word']")
