# jenkins-kickoff
Used to kick off audit / journey runs within a given ObservePoint folder from Jenkins.

kickoff.py is written in Python3 and requires the "requests" package in order to make HTTP requests to the ObservePoint API.

The script requires 2 parameters be passed in when executed via shell script, the client's ObservePoint account API key and the ObservePoint folder ID holding the desired audits/journeys to be run. Ex. "python3 kickoff.py {api_key} {folderId}"

The ObservePoint Folder ID is found by  navigating to "https://api.observepoint.com/swagger-ui/index.html#/Folders/getFolders". Then click the "Authorize" button at the top of the page and enter your OP API Key. Under the "/folders" endpoint, select "Try it out" and "Execute. The request's result will contain a list of the account's folders and their respective ID's which you will use to execute this script.
