import time

from behave import *

@given('User accesses to voting web app')
def step_imple(context):
    context.browser.get('http://localhost:8000/polls/')

# ***TOP VIEW***

## **WHEN(Action)**

@when('On the top view: User clicks "{text}" question')
def step_imple(context, text):
    # TODO Create locator class
    els = context.browser.find_elements_by_xpath("//a[contains(@href, 'polls')]")

    # FIXME last element doesn't have text...
    # for el in els:
    #     if text in el.text:
    #         el.click()
    els[0].click()

## **THEN(Result)**

@then('On the top view: User should be able to see {num} question, "{text}"')
def step_imple(context, num, text):
    # TODO Create locator class
    els = context.browser.find_elements_by_xpath("//a[contains(@href, 'polls')]")
    assert len(els) == 1

    # FIXME last element doesn't have text...
    # assert els[0].text == text
    # for i, el in enumerate(els):
    #     print(el.text)


# ***DETAILS VIEW***

## **WHEN(Action)**

@when('On the details view: User clicks "{text}" button')
def step_imple(context, text):
    el = context.browser.find_element_by_xpath("//input[@value='Vote']")
    el.click()

@when('On the details view: User clicks "{text}" choice')
def step_imple(context, text):
    els = context.browser.find_elements_by_xpath("//label[contains(@for,'choice')]")
    idx = -1
    for i, el in enumerate(els):
        if el.text == text:
            idx = 1+i  # Idx starts with 1
    # print([i for i, el in enumerate(els) if text == el.text])  # TODO Doesn't work somehow
    assert idx != -1
    el = context.browser.find_element_by_id("choice{}".format(idx))
    assert not el.is_selected()
    el.click()
    assert el.is_selected()

## **THEN(Result)**

@then('On the details view: User should be able to see "{text}" as title')
def step_imple(context, text):
    # FIXME Can't catch h1 text
    print(text)
    els = context.browser.find_elements_by_xpath("//h1")
    print(els[0].text)

@then('On the details view: User should be able to see "{text}" as choice')
def step_imple(context, text):
    # TODO Create locator class
    els = context.browser.find_elements_by_xpath("//label[contains(@for,'choice')]")
    assert len([ el.text for el in els if text == el.text ]) == 1

@then('On the details view: User should be able to see "{text}" selected')
def step_imple(context, text):
    pass

# ***RESULT VIEW***

## **WHEN(Action)**

@when('On the result view: User clicks "{text}"')
def step_imple(context, text):
    pass

## **THEN(Result)**

@then('On the result view: User should be able to see "{text}" as title')
def step_imple(context, text):
    pass

@then('On the result view: User should be able to see "{text}" as choise')
def step_imple(context, text):
    pass

@then('On the result view: User should be able to see "{text}" is {num} vote')
def step_imple(context, text, num):
    pass

# ----------------------------------------

@given('')
def step_imple(context):
    pass

@when('')
def step_imple(context):
    pass

@then('')
def step_imple(context):
    pass

