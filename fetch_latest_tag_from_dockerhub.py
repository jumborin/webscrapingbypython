import requests

# 最新のタグ名を取得する関数
def fetch_official_image_latest_tag(image_name,tag_index):
    
    url = f"https://hub.docker.com/v2/repositories/library/{image_name}/tags/?page_size=100&name={tag_index}"
    resp = requests.get(url)
    resp.raise_for_status()
    data = resp.json()
    
    tags = [r["name"] for r in data["results"] if r["name"].startswith(tag_index)]
    if not tags:
        return None
    return sorted(tags, reverse=True)[0]

# メイン実行部分
if __name__ == "__main__":
    
    image_names = ["ubuntu","mysql","wordpress"]
    tag_indexs = ["noble-","8.","6.8."]
    for i, image_name in enumerate(image_names):
      latest = fetch_official_image_latest_tag(image_name,tag_indexs[i])
      if latest:
          print(image_name,"latest tag:", latest)
      else:
          print(image_name,"no noble- tags found")


