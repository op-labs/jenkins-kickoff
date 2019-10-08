import sys
import requests
import json

# Function to make HTTP requests and return decoded JSON response
def httpReq(method,url,authHeader,showStatus=False):
	res = requests.request(method,url, headers=authHeader)
	if showStatus == True: 
		if res.status_code == 200:
			print('\tItem Running')
		elif res.status_code == 202:
			print('\tItem Queued to Run')
	return json.loads(res.content)

apiKey =  sys.argv[1]
folderId = sys.argv[2]
baseURL = 'https://api.observepoint.com/v2'
authHeader = {'Authorization': 'api_key ' + apiKey}

domainIds = []

# Makes a list of all domains that are in the desired folder
folderData = httpReq('get', baseURL + '/domains', authHeader)
for domain in folderData:
	if domain['folderId'] == folderId:
		domainIds.append(domain['id'])

# Gets a list of all the audits from the above folder/domains
for dom in domainIds:
	auditData = httpReq('get',baseURL + '/domains/' + str(dom) + '/web-audits', authHeader)
	for audit in auditData:
		# Runs the audit if it isn't currently running
		print('Audit ' + str(audit['id']) + ':')
		if (audit['webAuditRunning'] == False):
			auditRunData = httpReq('post',baseURL + '/web-audits/' + str(audit['id']) + '/runs', authHeader,True)
		else:
			print('Item Already Running')

# Gets a list of all the journeys from the above folder/domains
for dom in domainIds:
	journeyData = httpReq('get',baseURL + '/domains/' + str(dom) + '/web-journeys', authHeader)
	for journey in journeyData:
		# Runs the journey if it isn't currently running
		if (journey['webJourneyRunning'] == False):
			print('Running Journey ' + str(journey['id']) + ':')
			journeyRunData = httpReq('post',baseURL + '/web-journeys/' + str(journey['id']) + '/runs', authHeader,True)