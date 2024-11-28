from behave import *
from calculator import add, subtract, multiply, divide

@given('the calculator is initialized')
def step_given_calculator_initialized(context):
    context.result = None

@when('I add {a:d} and {b:d}')
def step_when_add(context, a, b):
    context.result = add(float(a), float(b))

@when('I subtract {a:d} from {b:d}')
def step_when_subtract(context, a, b):
    context.result = subtract(float(b), float(a))

@when('I multiply {a:d} and {b:d}')
def step_when_multiply(context, a, b):
    context.result = multiply(float(a), float(b))

@when('I divide {a:d} by {b:d}')
def step_when_divide(context, a, b):
    context.result = divide(float(a), float(b))


@then('the result should be {expected_result}')
def step_then_result_should_be(context, expected_result):
    expected_result = int(expected_result)
    assert context.result == expected_result, \
    f"Expected {expected_result}, but got {context}"