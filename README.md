# Reddit_task

## Directions:
1. Clone the repo ```git clone```
2. Create virtual environment and activate it. 
```
pip install virtualenv
virtualenv env_name
source env_name/bin/activate
```
3. Install all the dependencies for the project from requirements.txt file

```
pip install -r requirements.txt
```


## Input Format:
```
python3 app.py list_of_subreddits --post_limit i --post_score n list_for_types
```
1. **list_of_subreddits** = This is a required argument. It's a list of comma seperated strings. 
                    It contains names of subreddits

2. **post_limit** = Optional argument. Number of posts you want. Default is set to 10

3. **post_score** = Optional argument. minimum post score you want. Default is set to 15

4. **list_for_types** = what type of filter do you want. Should the program get the hottest, newest or 
                most controversial post

        Accepted argumets for this are: hot , controversial , top, new , best

### Example input:
```
python3 app.py python,stars --post_limit 5 --post_score 7 new,hot
```