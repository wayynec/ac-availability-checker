import slack 
import os
client = slack.WebClient(token=os.environ['slack_token'])