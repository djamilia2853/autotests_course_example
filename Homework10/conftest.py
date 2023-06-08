import pytest
import datetime


@pytest.fixture(scope='class')
def start_end_time():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    print(f"\nВремя начала: {start_time}")
    print(f"Время окончания: {end_time}")


@pytest.fixture()
def execution_time():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    execution_time = end_time - start_time
    print(f"Время теста: {execution_time.total_seconds()} секунд")