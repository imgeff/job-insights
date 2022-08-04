import csv
from functools import lru_cache


@lru_cache
def read(path):
    with open(path, encoding="utf-8") as file:
        dict_jobs = csv.DictReader(file, delimiter=",")
        list_jobs = []
        for job in dict_jobs:
            list_jobs.append(job)
    return list_jobs


# if __name__ == "__main__":
#     print(read("src/jobs.csv")[0])
