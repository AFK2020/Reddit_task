# Reddit_task

##Directions:
Install virtual environment and activate it.
Install all the dependencies for the project from requirements.txt file


##Input Format 
python3 app.py list_of_subreddits --post_limit i --post_score n list_for_types

list_of_subreddits = This is a required argument. It's a list of comma seperated strings. 
                    It contains names of subreddits

post_limit = Optional argument. Number of posts you want. Default is set to 10
post_score = Optional argument. minimum post score you want. Default is set to 15
list_for_types = what type of filter do you want. Should the program get the hottest, newest or 
                most controversial post

        Accepted argumets for this are: hot , controversial , top, new , best

###Example imput 

python3 app.py python,stars --post_limit 5 --post_score 7 new,hot
