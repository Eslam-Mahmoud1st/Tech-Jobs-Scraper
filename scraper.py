import requests
import pandas as pd

def fetch_tech_jobs(keyword):
    
    url = f"https://remotive.com/api/remote-jobs?search={keyword}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    print(f"[*] Fetching jobs for '{keyword}'...")
    
    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"[!] Failed to retrieve data. Status code: {response.status_code}")
            return []
            
        data = response.json()
        jobs = data.get("jobs", [])
        
        jobs_list = []

        for job in jobs[:20]: 
            jobs_list.append({
                "Job Title": job.get("title"),
                "Company": job.get("company_name"),
                "Category": job.get("category"),
                "Location": job.get("candidate_required_location", "Remote"),
                "Link": job.get("url")
            })

        return jobs_list

    except Exception as e:
        print(f"[!] An error occurred: {e}")
        return []

def main():
    keyword = input("Enter job title or skill to search (e.g. Python, Data, Web): ").strip()
    if not keyword:
        keyword = "Python"

    jobs = fetch_tech_jobs(keyword)

    if jobs:
        print(f"[+] Found {len(jobs)} jobs!\n")
        df = pd.DataFrame(jobs)
        
        csv_filename = f"{keyword.lower().replace(' ', '_')}_jobs.csv"
        df.to_csv(csv_filename, index=False, encoding="utf-8-sig")
        
        print(f"[✓] Saved results to '{csv_filename}'\n")
        print("First 3 results preview:")
        print(df[["Job Title", "Company", "Location"]].head(3))
    else:
        print("[-] No jobs found for this keyword.")

if __name__ == "__main__":
    main()
