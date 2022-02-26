import json
#coding=utf-8                                                                                                                                                                              
import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import logging
import os
from datetime import datetime
# Import WebClient from Python SDK (github.com/slackapi/python-slack-sdk)
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError


class WebDriver(object):

    def __init__(self):
        self.options = Options()

        self.options.binary_location = '/opt/headless-chromium'
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--start-maximized')
        #self.options.add_argument('--start-fullscreen')
        self.options.add_argument('--single-process')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument("--kiosk")
        self.options.add_argument("window-size=1920,1080")

    def get(self):
        driver = Chrome('/opt/chromedriver', options=self.options)
        return driver


def lambda_handler(event, context):
	instance_ = WebDriver()
	driver = instance_.get()
	options = Options()
	a = os.listdir('/tmp')
	for x in a:
		print(x)
	URL = os.environ.get("URL")
	now = datetime.now()
	dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
	#S = lambda X: driver.execute_script('return document.body.parentNode.scroll'+X)
	#driver.set_window_size(S('Width'),S('Height'))
	#driver.set_window_size(1280, 720)
	# May need manual adjustment        
	driver.get(URL)
	driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div[1]/div/div[1]').screenshot('/tmp/hourly_job_status.png')
	driver.find_element_by_xpath('/html/body/div/div[1]/section[2]/div[1]/div/div[2]').screenshot('/tmp/daily_job_status.png')
	
	
	driver.quit()
	# WebClient instantiates a client that can call API methods
	# When using Bolt, you can use either `app.client` or the `client` passed to listeners.
	client = WebClient(token=os.environ.get("SLACK_BOT_TOKEN"))
	logger = logging.getLogger(__name__)
	# The name of the file you're going to upload
	hourly_file_name = "/tmp/hourly_job_status.png"
	daily_file_name = "/tmp/daily_job_status.png"
	
	# ID of channel that you want to upload file to
	channel_id= os.environ.get("channel_id")
	
	#client.chat_postMessage(channel=channel_id, text="hello")
	try:
		# Call the files.upload method using the WebClient
		# Uploading files requires the `files:write` scope
		hourly_result = client.files_upload(
			channels=channel_id,
			initial_comment="Hourly DAG Status(" + dt_string + ") -> <"+ URL +"|Ops360 link>",
			file=hourly_file_name,
		)
		daily_result = client.files_upload(
			channels=channel_id,
			initial_comment="Daily DAG Status:",
			file=daily_file_name,
		)
		# Log the result
		logger.info(hourly_result)
		logger.info(daily_result)
	
	except SlackApiError as e:
		logger.error("Error uploading file: {}".format(e))
	
		return {
			'statusCode': 200,
			'body': json.dumps('Hello from Lambda!')
		}

