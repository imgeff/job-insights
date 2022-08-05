from src.sorting import sort_by


def test_sort_by_criteria():
    list_jobs = [
        {
            "job_title": "Marketing",
            "company": "Relief",
            "state": "NY",
            "city": "New York",
            "min_salary": "",
            "max_salary": "",
            "job_desc": "Marketing operations of the company.",
            "industry": "Finance",
            "rating": "4.0",
            "date_posted": "2020-05-08",
            "valid_until": "2020-06-07",
            "job_type": "FULL_TIME",
            "id": "0",
        },
        {
            "job_title": "Senior Scientist Pharmacometrics.",
            "company": "Genentech",
            "state": "CA",
            "city": "South San Francisco",
            "min_salary": 166713,
            "max_salary": 200487,
            "job_desc": 'The PositionThe Position.',
            "industry": "Biotech & Pharmaceuticals",
            "rating": "3.9",
            "date_posted": "2020-04-29",
            "valid_until": "2020-06-05",
            "job_type": "FULL_TIME",
            "id": "1719",
        },
        {
            "job_title": "Data Engineer",
            "company": "Sharpedge Solutions Inc",
            "state": "CA",
            "city": "Menlo Park",
            "min_salary": 103202,
            "max_salary": 137168,
            "job_desc": "Â\n\nJD:\n\n10+ years of experience.",
            "industry": "Media",
            "rating": "4.7",
            "date_posted": "2020-04-24",
            "valid_until": "2020-06-05",
            "job_type": "FULL_TIME",
            "id": "1720",
        },
    ]
    jobs_before_sort = list_jobs.copy()
    sort_by(list_jobs, "min_salary")
    assert list_jobs[0] == jobs_before_sort[2]
    assert list_jobs[-1] == jobs_before_sort[0]
    sort_by(list_jobs, "max_salary")
    assert list_jobs[0] == jobs_before_sort[1]
    assert list_jobs[-1] == jobs_before_sort[0]
    # sort_by_date_posted = sort_by(list_jobs, "date_posted")
    # assert sort_by_date_posted[0] == list_jobs[0]
