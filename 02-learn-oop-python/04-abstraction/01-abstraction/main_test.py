import pytest

from main import Human

run_cases = [
    (0, 0, 5, "left", -5, 0),
    (0, 0, 5, "right", 5, 0),
    (0, 0, 5, "up", 0, 5),
]

submit_cases = [
    pytest.param(0, 0, 5, "down", 0, -5, marks=pytest.mark.submit),
    pytest.param(10, 10, 2, "left", 8, 10, marks=pytest.mark.submit),
    pytest.param(10, 10, 2, "right", 12, 10, marks=pytest.mark.submit),
    pytest.param(10, 10, 2, "up", 10, 12, marks=pytest.mark.submit),
    pytest.param(10, 10, 2, "down", 10, 8, marks=pytest.mark.submit),
]


@pytest.mark.parametrize(
    (
        "pos_x",
        "pos_y",
        "speed",
        "move_direction",
        "expected_output_x",
        "expected_output_y",
    ),
    run_cases + submit_cases,
)
def test_human_movement(
    pos_x,
    pos_y,
    speed,
    move_direction,
    expected_output_x,
    expected_output_y,
):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * pos_x: {pos_x}")
    print(f" * pos_y: {pos_y}")
    print(f" * speed: {speed}")
    print(f" * move_direction: {move_direction}")
    expected_output = (expected_output_x, expected_output_y)
    human = Human(pos_x, pos_y, speed)
    if move_direction == "left":
        human.move_left()
    elif move_direction == "right":
        human.move_right()
    elif move_direction == "up":
        human.move_up()
    elif move_direction == "down":
        human.move_down()
    result = human.get_position()
    print(f"Expected x: {expected_output_x}")
    print(f"Actual   x: {result[0]}")
    print(f"Expected y: {expected_output_y}")
    print(f"Actual   y: {result[1]}")
    assert result == expected_output
