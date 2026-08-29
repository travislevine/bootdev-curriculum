Soldier = dict[str, int]


def fight_soldiers(soldier_one: Soldier, soldier_two: Soldier) -> str:
    soldier_one_dps = get_soldier_dps(soldier_one)
    soldier_two_dps = get_soldier_dps(soldier_two)
    if soldier_one_dps > soldier_two_dps:
        return "soldier 1 wins"
    if soldier_two_dps > soldier_one_dps:
        return "soldier 2 wins"
    return "both soldiers die"

def get_soldier_dps(soldier: Soldier):
    return soldier["damage"] * soldier["attacks_per_second"]
    