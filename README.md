# titan-bot

A bot created with python that responds to twitter users with #TitanUp

This bot was written in November of 2019, and is largely based off of a video from CS Dojo on YouTube detailing how to build a twitter bot. This program uses tweepy to communicate with the Twitter API. 

Keys should be gathered from https://developer.twitter.com, and placed into a keys.py file similar to keys_template, or, one can rename keys to keys_template in the import statement in TitanBot.py. This allows a user to use their own account, and/or protects the keys of the account I used.  The basic idea of this is similar to a .env file.

Every account that tweets and mentions the bot is replied to by mentioning their screen name, followed by "#TitanUp". The bot will then follow the other user. 

This script requires some form of hosting. I used https://www.pythonanywhere.com/ while hosting and testing my bot. 
