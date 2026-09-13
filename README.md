# Tech Jobs & Internships Scraper

A lightweight Python CLI tool that fetches real-time tech job listings and internships from public APIs based on user-defined search keywords (e.g., Python, Data, Web).

## Features
- Dynamic search queries via CLI input.
- Clean data extraction including Job Title, Company, Location, Category, and Direct Application Link.
- Exports results automatically into a structured `.csv` file.

## Prerequisites
Install the required dependencies:
```bash
pip install -r requirements.txt

How to Run
 * Run the script:
python scraper.py

 * Enter your target skill or position when prompted:
Enter job title or skill to search (e.g. Python, Data, Web): Python

 * The results will be displayed in the terminal and saved as a local CSV file (e.g., python_jobs.csv).