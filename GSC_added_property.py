import httplib2
import pandas as pd
import time

from apiclient import errors
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from requests.exceptions import HTTPError

clientId = str(input("Please enter the Google API client ID:"))
clientSecret = str(input("Please enter the Google API secret"))
listLocation = str(input("Please enter the exact location of the list containing the websites to be added to your property"))

df = pd.read_excel(listLocation, sheet_name=0) # Specify the sheet
website_list = df['Complete URL'].tolist() # Get the list name
website_list_clean = [website for website in website_list if str(website) != "nan"]

OAUTH_SCOPE = 'https://www.googleapis.com/auth/webmasters'

REDIRECT_URI = 'urn:ietf:wg:oauth:2.0:oob'

flow = OAuth2WebServerFlow(clientId, clientSecret, OAUTH_SCOPE, REDIRECT_URI)
authorize_url = flow.step1_get_authorize_url()
print('Go to the following link in your browser: ' + authorize_url)
code = input('Enter verification code: ').strip()
credentials = flow.step2_exchange(code)

http = httplib2.Http()
http = credentials.authorize(http)

webmasters_service = build('webmasters', 'v3', http=http)

for website in website_list_clean[17:]:
  try:
    webmasters_service.sites().add(siteUrl=website).execute()
  except Exception as err:
    print(f'Other error occurred: {err}')
  else:
    print(website+" has been added to your GSC!")
    time.sleep(5)