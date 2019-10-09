# jenkins-kickoff
Used to kick off audit / journey runs within ObservePoint from Jenkins.

kickoff.py is written in Python3 and requires the "requests" module in order to make HTTP requests to the ObservePoint API.

The script requires 2 parameters be passed in when executed via shell script, the client's ObservePoint account API key, and the ObservePoint folder ID holding the desired audits/journeys to be run. Ex. "python3 kickoff.py {api_key} {folderId}"
