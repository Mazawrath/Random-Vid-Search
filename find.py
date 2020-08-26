import json
import urllib.request
import string
import random
import sys

count = 50
apiKey = sys.argv[1]
random = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(3))
# random = 'overwatch'
print(random)

urlData = "https://www.googleapis.com/youtube/v3/search?key={}&maxResults={}&part=snippet&type=video&q={}".format(
    apiKey, count, random)
webURL = urllib.request.urlopen(urlData)
data = webURL.read()
encoding = webURL.info().get_content_charset('utf-8')
results = json.loads(data.decode(encoding))

# print(json.dumps(results))

for data in results['items']:
    videoId = (data['id']['videoId'])
    print("https://www.youtube.com/watch?v=" + videoId)
    # store your ids