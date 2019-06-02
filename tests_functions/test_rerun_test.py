import pytest
import pytest_rerunfailures
import allure
import os
import random


@pytest.mark.flaky(reruns=5)
def test_file_exists():
    num = random.randint(1, 5)
    assert num == 4
    # assert random.choice([True, False])
    # file_name = "newfile.txt"
    # assert os.path.isfile(file_name)
    # f = open(file_name, "w+")
    # f.close()

