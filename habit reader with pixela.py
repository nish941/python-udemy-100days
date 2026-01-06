from time import strftime
import requests
from datetime import datetime

# look at the notebook for notes of this program 

date = datetime.now().date()
total = date.strftime("%Y%m%d")
print(total)
# date = datetime(year = 2024, month = 6, day = 14)

header = {"X-USER-TOKEN" :"faeh3143gsft"}
params = {"date":total , "quantity":"9.54"}

response = requests.post (url = "https://pixe.la/v1/users/lunarishi1122/graphs/graphcycletrack", json = params, headers = header)
print(response.text)
# but we don't wanna write date times and again

