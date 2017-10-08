import boto3
import json
import pprint
import sys
import writer

client = boto3.client('lex-runtime', region_name = 'us-east-1', aws_access_key_id='AKIAJ2MGCLIK6IMXHWGA', aws_secret_access_key='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')

activity = None

while activity is None:
	data = raw_input()

	response = client.post_content(
	    botName='Hackerman',
	    botAlias='Prod',
	    userId='requestee',
	    contentType='text/plain; charset=utf-8',
	    accept='text/plain; charset=utf-8',
	    inputStream= data
	)

	activity = response['intentName']

	#pprint.pprint (response)

	if activity is not None:
		print 'executing ' + activity
		writer.ProcessandPrint(activity)