import requests

API_KEY = 'AIzaSyCrytKleNpXjgzGNUmiEii4G8MViFnWkQA'  # your API key
CSE_ID = '11cc1f1f82aac4178'  # Your CSE ID

def google_search(query, api_key, cse_id, start_index=1, num_results=10):
    url = f"https://www.googleapis.com/customsearch/v1"
    params = {
        'key': api_key,
        'cx': cse_id,
        'q': query,
        'start': start_index,
        'num': num_results
    }
    response = requests.get(url, params=params)
    print(response.json())
    return response.json()

def extract_linkedin_urls(search_results):
    profile_urls = []
    for item in search_results.get('items', []):
        link = item.get('link')
        if 'linkedin.com/in/' in link:
            profile_urls.append(link)
    return profile_urls

query = 'site:linkedin.com/in "Technical Recruiter India"'
all_linkedin_urls = []

# Retrieve up to 1000 results (Google Custom Search API has a hard limit of 100 queries per day)
for i in range(0, 1):  # 100 iterations * 10 results per query = 1000 results
    start_index = i * 10 + 1
    search_results = google_search(query, API_KEY, CSE_ID, start_index)
    linkedin_urls = extract_linkedin_urls(search_results)
    all_linkedin_urls.extend(linkedin_urls)

# Print and open the URLs
for url in all_linkedin_urls:
    print(url)
    
