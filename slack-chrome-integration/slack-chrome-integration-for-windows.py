
#coding=utf-8                                                                                                                                                                              
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import os
import boto3

# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

URL = os.environ.get("URL")
driver.get(URL)

S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
#driver.set_window_size(S('Width'),S('Height'))
driver.set_window_size(1920, 1080)
# May need manual adjustment                                                                                                                
driver.find_element_by_tag_name('body').screenshot('web_screenshot.png')

driver.quit()
# WebClient instantiates a client that can call API methods
# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
client = client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
logger = logging.getLogger(__name__)
# The name of the file you're going to upload
file_name = r"C:\Users\hpant\Documents\projects\projects\jira-integration\web_screenshot.png"
# ID of channel that you want to upload file to
channel_id= os.environ.get("channel_id")
#client.chat_postMessage(channel=channel_id, text="hello")
try:
    # Call the files.upload method using the WebClient
    # Uploading files requires the `files:write` scope
    result = client.files_upload(
        channels=channel_id,
        initial_comment="Job Status: <"+ URL +"+|Ops360 link>",
        file=file_name,
    )
    # Log the result
    logger.info(result) 

except SlackApiError as e:
    logger.error("Error uploading file: {}".format(e))
