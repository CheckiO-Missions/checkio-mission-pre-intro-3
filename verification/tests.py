init_code = """
if not "function" in USER_GLOBAL:
    raise NotImplementedError("Define function 'function'")

function = USER_GLOBAL['function']

from inspect import signature

params = signature(function).parameters
if params:
    raise NotImplementedError("'function' must not have arguments")

"""

run_test = """
RET['code_result'] = {}
"""

def prepare_test(test="", answer=None, middle_code="", show_code=None):
    if show_code is None:
        show_code = middle_code + "\n" + test
    if not test:
        return_code = "\nRET['code_result'] = ''"
        answer = ''
    else:
        return_code = run_test.format(test)
    return {"test_code": {"python-3": init_code + middle_code + return_code},
            "show": {"python-3": show_code},
            "answer": answer}

TESTS = {
    "First": [
        prepare_test(middle_code='''''',
                     test="function()",
                     answer=None),
        ]
    }