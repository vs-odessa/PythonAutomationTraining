import pytest
import pytest_rerunfailures
import allure
import os
import random
import pytest

@pytest.mark.unit
@pytest.mark.flaky(reruns=5)
@allure.tag('unit')
@allure.title('Generate random number - Check Rerun')
def test_random_num():
    num = random.randint(1, 6)
    assert num > 4
    # assert random.choice([True, False])
    # file_name = "newfile.txt"
    # assert os.path.isfile(file_name)
    # f = open(file_name, "w+")
    # f.close()

