from src.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    path = "tests/mocks/brazilians_jobs.csv"
    brazilian_jobs_in_english = read_brazilian_file(path)
    keys_in_portuguese = ["titulo", "salario", "tipo"]
    for job in brazilian_jobs_in_english:
        for key in keys_in_portuguese:
            assert key not in job
