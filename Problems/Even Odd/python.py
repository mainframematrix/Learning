import json
import logging


def is_even_mod(num: int):
    """
    This function uses a mod function to find whether the number is divisible by 2 or not.
    Returns:
        bool: True represents even and False represents odd.
    """
    return abs(num) % 2 == 0


def is_even_bool(num: int):
    """
    This function flips the result and returns the end value.

    Returns:
        bool: True represents even and False represents odd.
    """
    result = True
    for i in range(abs(num)):
        result = not result
    return result


def solution(inputs: list):
    """
    The driver code for the solutions.
    """
    for number in (inputs):
        logging.info("Finding Even or Odd using the mod function.")
        if (is_even_mod(num=number)):
            print(f"{number} is even")
        else:
            print(f"{number} is odd.")

        logging.info("Finding Even or Odd using the boolean method.")
        if (is_even_bool(num=number)):
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")


def load_file(file_path: str):
    """
    Loads the test-case.json file.
    """
    with open(file=file_path, mode='r') as file:
        return json.load(file)


def test_runner(test_cases):
    """
    Runs the tests
    """
    for i, test in enumerate(test_cases):
        logging.info(f"Running test case {i+1}...")
        input_data = test["input"]
        logging.info(f"Input: {input_data}")
        logging.info("-"*40)
        solution(inputs=input_data)
        logging.info("-"*40)


if __name__ == "__main__":
    logging.basicConfig(
        format="[%(levelname)s] - %(message)s",
        level=logging.INFO
    )
    test_cases = load_file("test-cases.json")
    test_runner(test_cases)
