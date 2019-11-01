# GSC automatic addition
This python program will add a list of websites to your Google Search Console.
It uses OAuth 2.0 and needs the **owner rights** in order to properly work.
Due to numerous prerequisites, this script is only beneficial for webmasters with a list of >200 websites to add OR agencies having several clients.

## Prerequisites

### Google Search Console owner rights
Be sure to be an owner in Google Search Console!
Otherwise, you will not be able to realise this automatic addition.

### Domains to be added are already verified
The domains to be added have to be verified in your Google Search Console account as precised in the following link:
https://support.google.com/webmasters/answer/9008080#domain_name_verification

### Google Search Console API OAuth privileges
Go to : https://developers.google.com/webmaster-tools/search-console-api-original/v3/quickstart/quickstart-python and follow the instructions under "Step 1: Enable the Search Console API"
**During the instructions, Client ID and Client Secret will be communicated. Make sure to copy them somewhere - you'll need them later!**

### List of all the websites to be added to the Google Search Console
In Excel, create a list of all websites to be added to a Google Search Console.
All the websites have to start by either "http://" or "https://".
The first row has to be named `Complete URL`.

## Installation
1. Open your Terminal and set your directory to Desktop by typing: `cd ~/Desktop/`. Now your terminal is in the Desktop directory.
2. Still in Terminal: copy and execute the following command: `git clone git@github.com:A-Sm1th/GSC_adder.git`. The Python program will be downloaded.
3. In Terminal, execute the following command: `cd GSC_adder`. Now your terminal is in the directory that has been previously downloaded.
4. In Terminal, execute the following command: `pip3 install -r requirements.txt`. This command will automatically install the required packages for this script. If you don't have `pip install`, please follow the instructions under this link: https://www.makeuseof.com/tag/install-pip-for-python/.
5. Then start the script by writing `python3 GSC_added_property.py` and pushing Enter.

## Feedback / Improvement Suggestions
If you have a problem or want to submit a Feedback, please open an issue by clicking on ISSUES (right under the title of this repository)