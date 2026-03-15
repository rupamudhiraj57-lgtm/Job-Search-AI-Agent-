import requests

API_KEY = "c24d55e707msh9f215066792fd41p1d4a34jsn31e8181897be"

url = "https://jsearch.p.rapidapi.com/search"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

def search_jobs(keyword, location):

    querystring = {
        "query": f"{keyword} in {location}",
        "page": "1",
        "num_pages": "1"
    }

    response = requests.get(url, headers=headers, params=querystring)

    data = response.json()

    jobs = []

    for job in data.get("data", [])[:10]:

        job_info = {
            "title": job.get("job_title"),
            "company": job.get("employer_name"),
            "location": job.get("job_city"),
            "salary": job.get("job_salary")
        }

        jobs.append(job_info)

    return jobs