import pytest

from main import Wizard

run_cases = [
    {
        "wizard1_name": "Merlin",
        "wizard1_stamina": 10,
        "wizard1_intelligence": 10,
        "wizard2_name": "Morgana",
        "wizard2_stamina": 8,
        "wizard2_intelligence": 8,
        "fireball_cost": 50,
        "fireball_damage": 30,
        "expect_success": True,
        "expected_wizard1_mana_after": 50,
        "expected_wizard2_alive": True,
    },
    {
        "wizard1_name": "Gandalf",
        "wizard1_stamina": 15,
        "wizard1_intelligence": 12,
        "wizard2_name": "Saruman",
        "wizard2_stamina": 10,
        "wizard2_intelligence": 9,
        "fireball_cost": 80,
        "fireball_damage": 50,
        "expect_success": True,
        "expected_wizard1_mana_after": 40,
        "expected_wizard2_alive": True,
    },
]

submit_cases = [
    pytest.param(
        {
            "wizard1_name": "Harry",
            "wizard1_stamina": 5,
            "wizard1_intelligence": 1,
            "wizard2_name": "Voldemort",
            "wizard2_stamina": 2,
            "wizard2_intelligence": 15,
            "fireball_cost": 200,
            "fireball_damage": 400,
            "expect_success": False,
            "expected_wizard1_mana_after": 10,
            "expected_wizard2_alive": True,
        },
        marks=pytest.mark.submit,
    ),
    pytest.param(
        {
            "wizard1_name": "Ron",
            "wizard1_stamina": 5,
            "wizard1_intelligence": 7,
            "wizard2_name": "Hermione",
            "wizard2_stamina": 2,
            "wizard2_intelligence": 15,
            "fireball_cost": 70,
            "fireball_damage": 400,
            "expect_success": True,
            "expected_wizard1_mana_after": 0,
            "expected_wizard2_alive": False,
        },
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize("case", run_cases + submit_cases)
def test_cast_fireball(case):
    print("\n---------------------------------")
    print(
        f"{case['wizard1_name']} (Stamina: {case['wizard1_stamina']}, Intelligence: {case['wizard1_intelligence']})"
    )
    wizard1 = Wizard(
        case["wizard1_name"], case["wizard1_stamina"], case["wizard1_intelligence"]
    )
    print(f"  Starting health: {wizard1.health}")
    print(f"  Starting mana:   {wizard1.mana}")

    wizard2 = Wizard(
        case["wizard2_name"], case["wizard2_stamina"], case["wizard2_intelligence"]
    )
    print(
        f"{case['wizard2_name']} (Stamina: {case['wizard2_stamina']}, Intelligence: {case['wizard2_intelligence']})"
    )
    print(f"  Starting health: {wizard2.health}")
    print(f"  Starting mana:   {wizard2.mana}")
    print("")

    try:
        wizard1.cast_fireball(wizard2, case["fireball_cost"], case["fireball_damage"])
        success = True
        print(f"{case['wizard1_name']} cast fireball at {case['wizard2_name']}...")
        print(f"  Fireball cost:   {case['fireball_cost']}")
        print(f"  Fireball damage: {case['fireball_damage']}")
        print("")
    except Exception as error:
        success = False
        print(f"Exception: {error}")

    wizard1_mana_after = wizard1.mana
    wizard2_alive_after = wizard2.is_alive()

    print(f"Expected cast success: {case['expect_success']}")
    print(f"Actual cast success:   {success}")
    print(
        f"Expected {case['wizard1_name']} mana after: {case['expected_wizard1_mana_after']}"
    )
    print(f"Actual {case['wizard1_name']} mana after:   {wizard1_mana_after}")
    print(
        f"Expected {case['wizard2_name']} alive after: {case['expected_wizard2_alive']}"
    )
    print(f"Actual {case['wizard2_name']} alive after:   {wizard2_alive_after}")
    assert success == case["expect_success"]
    assert wizard1_mana_after == case["expected_wizard1_mana_after"]
    assert wizard2_alive_after == case["expected_wizard2_alive"]
