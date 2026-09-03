import pytest

from main import Human

run_cases = [
    ((0, 0, 5, 3), ["sprint_right"], (10, 0, None)),
    (
        (0, 0, 20, 3),
        [
            "sprint_left",
            "sprint_left",
            "sprint_left",
        ],
        (-120, 0, None),
    ),
    (
        (1, 1, 3, 1),
        ["sprint_down", "sprint_right"],
        (1, -5, "not enough stamina to sprint"),
    ),
]

submit_cases = [
    pytest.param(
        (1, 1, 5, 2),
        ["sprint_left", "sprint_up", "sprint_down"],
        (-9, 11, "not enough stamina to sprint"),
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    ("human_args", "methods", "expected_output"), run_cases + submit_cases
)
def test_sprint(human_args, methods, expected_output):
    print("\n---------------------------------")
    print("Starting values:")
    human = Human(*human_args)
    print(f" * x: {human_args[0]}")
    print(f" * y: {human_args[1]}")
    print(f" * speed: {human_args[2]}")
    print(f" * stamina: {human_args[3]}")
    for method in methods:
        print(f" - calling {method}...")
    try:
        for method in methods:
            getattr(human, method)()
        actual_x, actual_y = human.get_position()
        actual_err = None
    except Exception as error:
        actual_x, actual_y = human.get_position()
        actual_err = str(error)
    expected_x, expected_y, expected_error = expected_output
    print(f"Expected x: {expected_x}")
    print(f"Actual   x: {actual_x}")
    print(f"Expected y: {expected_y}")
    print(f"Actual   y: {actual_y}")
    print(f"Expected error: {expected_error}")
    print(f"Actual   error: {actual_err}")
    assert (actual_x, actual_y, actual_err) == expected_output
