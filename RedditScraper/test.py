import requests
import json

package = {
    "User-agent":"your mother"
}
text = requests.get(url="http://api.scraperapi.com/?api_key=96ee07ba33ed9822bfe8479f6ce14acd&url=https://www.reddit.com/r/popular/top/.json&country_code=jp", headers=package).json()
data = json.dumps(text, indent=2)
print(data)

#def weiner(s, t):
   # w = "This guy is weird {s}, {t}".format(s=s, t=t)
    #print(w)

#weiner("cheese", "fart")