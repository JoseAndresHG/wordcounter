from pages.word_counter_page import WordCounterPage
from utils.driver_factory import DriverFactory


def before_scenario(context, scenario):
    context.driver = DriverFactory.create_driver()
    context.word_counter_page = WordCounterPage(context.driver)


def after_scenario(context, scenario):
    driver = getattr(context, "driver", None)

    if driver:
        driver.quit()
