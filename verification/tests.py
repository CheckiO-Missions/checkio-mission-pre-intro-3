init_code = """
if not "func" in USER_GLOBAL:
    raise NotImplementedError("Define function 'func'")

func = USER_GLOBAL['func']

from inspect import signature

params = signature(func).parameters
if params:
    raise NotImplementedError("'func' must not have arguments")

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
                     test="func()",
                     answer=None),
        ]
    }
