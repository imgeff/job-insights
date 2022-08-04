from src.jobs import read
# from jobs import read


def get_unique_job_types(path):
    list_jobs = read(path)
    job_types = set()
    for job in list_jobs:
        job_types.add(job["job_type"])
    return job_types


def filter_by_job_type(jobs, job_type):
    jobs_by_type = []
    for job in jobs:
        type_of_job = job["job_type"]
        if type_of_job == job_type:
            jobs_by_type.append(job)
    return jobs_by_type


def get_unique_industries(path):
    list_jobs = read(path)
    industries = set()
    for job in list_jobs:
        job_industry = job["industry"]
        if len(job_industry) > 0:
            industries.add(job_industry)
    return industries


def filter_by_industry(jobs, industry):
    jobs_by_industry = []
    for job in jobs:
        industry_of_job = job["industry"]
        if industry_of_job == industry:
            jobs_by_industry.append(job)
    return jobs_by_industry


def get_max_salary(path):
    list_jobs = read(path)
    max_salary = 0
    for job in list_jobs:
        job_salary = job["max_salary"]
        if job_salary != "" and job_salary != "invalid":
            salary = int(job["max_salary"])
            if salary > max_salary:
                max_salary = salary
    return max_salary


def get_min_salary(path):
    list_jobs = read(path)
    min_salary = 383416
    for job in list_jobs:
        job_salary = job["min_salary"]
        if job_salary != "" and job_salary != "invalid":
            salary = int(job["min_salary"])
            if salary < min_salary:
                min_salary = salary
    return min_salary


def matches_salary_range(job, salary):
    job_keys = job.keys()
    if "min_salary" not in job_keys or "max_salary" not in job_keys:
        raise ValueError()
    elif not isinstance(job["min_salary"], (int, float)) or (
            not isinstance(job["max_salary"], (int, float))):
        raise ValueError()
    elif job["min_salary"] > job["max_salary"]:
        raise ValueError()
    elif not isinstance(salary, (int, float)):
        raise ValueError()
    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    return []


# if __name__ == "__main__":
#     print(matches_salary_range({"min_salary": 0, "max_salary": 4500}, 3000))
#     jobs = read("src/jobs.csv")
#     print(filter_by_job_type(jobs, "PART_TIME"))
#     print(get_min_salary("tests/mocks/jobs_with_salaries.csv"))
#     print(get_max_salary("src/jobs.csv"))
#     print(get_unique_industries("src/jobs.csv"))
