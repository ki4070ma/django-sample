import os

from selenium import webdriver


def before_scenario(context, scenario):
    print("**Before scenario")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    context.browser = webdriver.Chrome(chrome_options=chrome_options,
    executable_path=os.environ.get('CHROMEDRIVER_PATH'))


def after_scenario(context, scenario):
    print("**After scenario")
    import time
    time.sleep(1)  # Just to check the view on browse by me
    context.browser.quit()
