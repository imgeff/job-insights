from src.counter import count_ocurrences


def test_counter():
    resultCounter = count_ocurrences('src/jobs.csv', 'Work')
    assert resultCounter == 14174
