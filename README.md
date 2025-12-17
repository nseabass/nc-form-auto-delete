# nc-form-auto-delete
A simple script to delete Nextcloud Forms responses older than a certain number of days

Disclosure: This was mostly vibe-coded (AI generated/assisted). I am an end user, not a coder. I did review and debug the code significantly to get it working in the current state, but I am not a knowledgable developer. I'd rather *not* use AI but I don't have the necessary skills to make something like this currently. Implementation of this as a feature of Forms was marked as Maybe Someday, and I unfortunately needed it today (well, this week). 

#Instructions
1. Download the Python3 script and update the following variables:
   * domain: Your fully qualified domain name for nextcloud (ex. nextcloud.example.com)
   * username: The username of the form owner. As far as I can tell, this _must_ be the form owner
   * password: Create an app password for this. Please don't use your regular password
   * form_id: We'll go over this momentarily
   * days: Forms older than this number of days are deleted
2. Identify your form_id
   * I used curl for this task. You will need to manually construct this URL:
   * curl -X GET "https://*(your.domain)*/ocs/v2.php/apps/forms/api/v3/forms" \ -u *(username)*:*(password)* \ -H "OCS-APIRequest: true"
   * Replace your domain, username, and password
   * Skim through the output until you find your form title in the <title> field, then look two lines up for <id>. This ID goes in your form_id variable
3. Test the script on your form by running it manually with Python
4. Automate it
  * I am using Cron because it's nice and easy
