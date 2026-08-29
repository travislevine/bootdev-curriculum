import pytest

from main import Wizard

run_cases = [
    {
        "wizard_name": "Merlin",
        "wizard_stamina": 10,
        "wizard_intelligence": 10,
        "fireball_damage": 30,
        "potion_mana": 20,
        "expected_health_after": 980,
        "expected_mana_after": 130,
    },
    {
        "wizard_name": "Morgana",
        "wizard_stamina": 20,
        "wizard_intelligence": 5,
        "fireball_damage": 75,
        "potion_mana": 25,
        "expected_health_after": 1945,
        "expected_mana_after": 80,
    },
]

submit_cases = [
    pytest.param(
        {
            "wizard_name": "Madame Mim",
            "wizard_stamina": 100,
            "wizard_intelligence": 500,
            "fireball_damage": 150,
            "potion_mana": 250,
            "expected_health_after": 9950,
            "expected_mana_after": 5750,
        },
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize("case", run_cases + submit_cases)
def test_wizard_damage_and_mana(case):
    print("\n---------------------------------")
    print(
        f"Wizard({case['wizard_name']}, {case['wizard_stamina']}, {case['wizard_intelligence']})"
    )
    wizard = Wizard(
        case["wizard_name"], case["wizard_stamina"], case["wizard_intelligence"]
    )
    print(f"  Starting health: {wizard.health}")
    print(f"  Starting mana:   {wizard.mana}")
    print("")
    print(
        f"  Hit by a {case['fireball_damage']}-damage fireball while at {case['wizard_stamina']} stamina..."
    )
    print(
        f"  Drank a {case['potion_mana']}-mana potion while at {case['wizard_intelligence']} intelligence..."
    )
    wizard.get_fireballed(case["fireball_damage"])
    wizard.drink_mana_potion(case["potion_mana"])
    print("")
    print(f"  Expected health: {case['expected_health_after']}")
    print(f"  Actual health:   {wizard.health}")
    print(f"  Expected mana:   {case['expected_mana_after']}")
    print(f"  Actual mana:     {wizard.mana}")
    assert wizard.health == case["expected_health_after"]
    assert wizard.mana == case["expected_mana_after"]
