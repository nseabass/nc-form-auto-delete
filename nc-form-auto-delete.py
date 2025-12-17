#Import libraries etc
import requests
from datetime import datetime, timedelta
import json

# Define base URL, credentials, and other data
domain = "example.com" #FQDN such as nextcloud.example.com
username = "user" #This needs to be the owner of the form as far as I can tell
password = "password" #Create an app password for this task
form_id = "4" #Obtained by running the submission URL with headers but leaving out the form ID
days = 6 #Submissions older than this value (in days) will be deleted

#Do some setup
base_url = f"https://{domain}/ocs/v2.php/apps/forms/api/v3"
headers = {
        "OCS-APIRequest": "true",
        "Accept": "application/json"
        }
url = f"{base_url}/forms/{form_id}/submissions?format=json"

#Get submissions
def get_submissions(form_id):
    response = requests.get(url, auth=(username, password), headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to retrieve submissions")
        return None

#Delete submission(s)
def delete_submission(form_id, submission_id):
        data = {"submissionId": submission_id}
        response = requests.delete(url, auth=(username, password), headers=headers, json=data)
        if response.status_code == 200:
                print(f"Submission {submission_id} deleted successfully.")
        else:
                print(f"Failed to delete submission {submission_id}. Status code: {response.status_code}")

#Obtain submissions, calculate date, delete expired submissions
def main():
    submissions = get_submissions(form_id)

    if submissions and 'ocs' in submissions:
        elements = submissions['ocs']['data']['submissions']

        current_time = datetime.now()
        expired_time = current_time - timedelta(days=days) #Feels silly, but the second days is from up above

        for submission in elements:
            last_updated = datetime.fromtimestamp(submission['timestamp'])

            if last_updated < expired_time:
                print(f"Deleting old submission: {submission['id']}")
                delete_submission(form_id, submission['id'])
                
if __name__ == "__main__":
        main()

