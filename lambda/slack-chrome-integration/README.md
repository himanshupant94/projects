# Introduction


## Pre-requisite:
- Need to have python3.7 to use chrome-headless and selenium (stable version)
- Need to have **SLACK_BOT_TOKEN** and **Channel_id** to push text/image in slack channel


### Required Modules apart from zip file.
- Install pip module:

	`pip install slack_sdk --target layer/python/lib/python3.7/site-packages`
### Steps to setup AWS Lambda process
- Download chrome-headless.zip, It has slack, chrome driver and selenium modules.
- Place zip file in S3 Bucket and create a layer with python3.7
- Use python code to take screenshot of URL and save into /tmp/ directory 
- Set 2 environment variables(SLACK_BOT_TOKEN,Channel_id) in AWS lambda 

### Steps to setup Slack App (Need SLACK_BOT_TOKEN)
- Go to socket mode and turn **on** 
- Got to **OAuth and Permissions** and select below configuration to get necessary permissions to post image in channel.


![image](https://user-images.githubusercontent.com/10596429/154865755-e62de7cb-a1c7-40e2-8b4b-95ff1897d64b.png)

