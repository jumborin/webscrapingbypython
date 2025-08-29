import requests
from bs4 import BeautifulSoup

# 最新のタグ名を取得する関数
def fetch_github_latest_tag(user_name, repository_name):
    
    url = f"https://github.com/{user_name}/{repository_name}/tags"
    resp = requests.get(url)
    resp.raise_for_status()
    
    soup = BeautifulSoup(resp.text, 'html.parser')
    tag_links = soup.find_all('a', {'data-view-component': 'true', 'class': 'Link--primary Link'})
    
    tags = [link.text.strip() for link in tag_links]
    if not tags:
        return None
    return sorted(tags, reverse=True)[0]

# メイン実行部分
if __name__ == "__main__":
    
    user_names = ["sameersbn","sameersbn"]
    repository_names = ["docker-redmine","docker-gitlab"]
    for i, user_name in enumerate(user_names):
      latest = fetch_github_latest_tag(user_name, repository_names[i])
      if latest:
          print(user_name,"latest tag:", latest)
      else:
          print(user_name,f"no {repository_names[i]} tags found")


