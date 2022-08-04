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
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


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
#     jobs = read("src/jobs.csv")
#     print(filter_by_job_type(jobs, "PART_TIME"))
#     print(get_min_salary("tests/mocks/jobs_with_salaries.csv"))
#     print(get_max_salary("src/jobs.csv"))
#     print(get_unique_industries("src/jobs.csv"))
