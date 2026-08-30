import pytest

from main import BankAccount

run_cases = [
    ("1234567890", 100.0, 50.0, 75.0, 75.0, None, None),
    ("0987654321", 500.0, 100.0, 200.0, 400.0, None, None),
    (
        "0987654321",
        200.0,
        0.0,
        10.0,
        190.0,
        "cannot deposit zero or negative funds",
        None,
    ),
]

submit_cases = [
    pytest.param(
        "1234567890",
        100.0,
        50.0,
        200.0,
        150.0,
        None,
        "insufficient funds",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "0987654321",
        500.0,
        500.0,
        500.0,
        500.0,
        None,
        None,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "1234567890",
        300.0,
        -10.0,
        20.0,
        280.0,
        "cannot deposit zero or negative funds",
        None,
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "1234567890",
        -20.0,
        10.0,
        10.0,
        -10.0,
        None,
        "insufficient funds",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "0987654321",
        100.0,
        10.0,
        -10.0,
        110.0,
        None,
        "cannot withdraw zero or negative funds",
        marks=pytest.mark.submit,
    ),
    pytest.param(
        "1234567890",
        900.0,
        100.0,
        0.0,
        1000.0,
        None,
        "cannot withdraw zero or negative funds",
        marks=pytest.mark.submit,
    ),
]


@pytest.mark.parametrize(
    (
        "account_number",
        "initial_balance",
        "deposit_amount",
        "withdraw_amount",
        "expected_balance",
        "deposit_err",
        "withdraw_err",
    ),
    run_cases + submit_cases,
)
def test_bank_account(
    account_number,
    initial_balance,
    deposit_amount,
    withdraw_amount,
    expected_balance,
    deposit_err,
    withdraw_err,
):
    print("\n---------------------------------")
    print("Inputs:")
    print(f" * account_number: {account_number}")
    print(f" * initial_balance: {initial_balance:.2f}")
    print(f" * deposit_amount: {deposit_amount:.2f}")
    print(f" * withdraw_amount: {withdraw_amount:.2f}")
    account = BankAccount(account_number, initial_balance)

    try:
        account.deposit(deposit_amount)
        if deposit_err:
            print(f'Expected error "{deposit_err}"')
            print("Actual output: No error was raised")
        assert deposit_err is None
    except ValueError as error:
        print(f'Expected error: "{deposit_err}"')
        print(f'Actual error:   "{error}"')
        assert str(error) == deposit_err

    try:
        account.withdraw(withdraw_amount)
        if withdraw_err:
            print(f'Expected error: "{withdraw_err}"')
            print("Actual output:  No error was raised")
        assert withdraw_err is None
    except ValueError as error:
        print(f'Expected error: "{withdraw_err}"')
        print(f'Actual error:   "{error}"')
        assert str(error) == withdraw_err

    print(f"Expected balance: ${expected_balance:.2f}")
    print(f"Actual balance:   ${account.get_balance():.2f}")
    assert account.get_balance() == expected_balance
