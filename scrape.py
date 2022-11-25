import requests
from datetime import datetime

def download_file(url, filename):
    r = requests.get(url)
    with open(filename, 'w') as f:
        f.write(r.text)

date = datetime.utcnow().strftime("%Y/%m/%d")
download_file(f"https://ton.twimg.com/birdwatch-public-data/{date}/notes/notes-00000.tsv", "notes-00000.tsv")
download_file(f"https://ton.twimg.com/birdwatch-public-data/{date}/noteRatings/ratings-00000.tsv", "ratings-00000.tsv")
download_file(f"https://ton.twimg.com/birdwatch-public-data/{date}/noteStatusHistory/noteStatusHistory-00000.tsv", "noteStatusHistory-00000.tsv")
download_file(f"https://ton.twimg.com/birdwatch-public-data/{date}/userEnrollment/userEnrollment-00000.tsv", "userEnrollment-00000.tsv")
