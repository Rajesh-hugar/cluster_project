import requests # request img from web
import shutil # save img locally


url = "https://coffee.alexflipnote.dev/random.json"

image_dict = {}
for i in range(10):
    response = requests.get(url)
    image_dict[i] = response.json()['file']
    print(response.json())

for i in range(10):
    file_name = str(i)+'.jpg'
    res = requests.get(image_dict[i], stream = True)
    with open(file_name,'wb') as f:
        shutil.copyfileobj(res.raw, f)
    print('Image sucessfully Downloaded: ',file_name)
