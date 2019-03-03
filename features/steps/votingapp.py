from behave import *

@given('User accesses to voting web app')
def step_imple(context):
    context.browser.get('http://localhost:8000/polls/')

# ***TOP VIEW***

## **WHEN(Action)**

@when('On the top view: User clicks "{text}" question')
def step_imple(context, text):
    els = context.browser.find_elements_by_xpath("//a[contains(@href, 'polls')]")
    assert len(els) == 1

    # FIXME last element doesn't have text...
    # assert els[0].text == text
    # for i, el in enumerate(els):
    #     print(el.text)

## **THEN(Result)**

@then('On the top view: User should be able to see {num} question, "{text}"')
def step_imple(context, num, text):
    pass


# ***DETAILS VIEW***

## **WHEN(Action)**

@when('On the details view: User clicks "{text}" button')
def step_imple(context, text):
    pass

@when('On the details view: User clicks "{text}" choice')
def step_imple(context, text):
    pass

## **THEN(Result)**

@then('On the details view: User should be able to see "{text}" as title')
def step_imple(context, text):
    pass

@then('On the details view: User should be able to see "{text}" as choice')
def step_imple(context, text):
    pass

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

