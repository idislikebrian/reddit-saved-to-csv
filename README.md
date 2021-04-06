# reddit-saved-to-notion
Exports saved posts and comments on Reddit to a Notion table.

**Columns**: ID, Name, Subreddit, Type, URL
- ID: Starts from 1 and increments for each saved Post or Comment.
- Name: Title of the post.
- Subreddit: Display name of the subreddit.
- Type: Either #Comment or #Post.
- URL: Link of the comment or the post.

## How to Use
* Download or clone the code to your pc.
* Install [Python3](https://www.python.org/downloads/) and then install [praw](https://praw.readthedocs.io/en/latest/getting_started/installation.html) and then install [notion.py](https://github.com/jamalex/notion-py).
* Go to https://www.reddit.com/prefs/apps and create a script.
  * Give any name and description.
  * Redirect uri: http://localhost:8080
  * Create
  * Text below "personal use script" is your client id. We'll need that and the secret.
* Open `reddit_saved_to_notion.py` file with any text editor.
* You'll see below lines at the top:
```python
client = NotionClient(token_v2="") #Obtain the `token_v2` value by inspecting your browser cookies on a logged-in session on Notion.so
page = client.get_block("") #replace the URL with the URL of the page or databse you want to edit

client_id='' # Enter your client ID
client_secret='' # Enter you client secret
username='' # Enter Username
password='' # Enter password
```
* Enter the necessary information into the quotation marks.
* Save the .py file.
* Now you can run the script through command line/ VSCode/ Spyder etc.
* Wait until you get the "**Your saved posts are available in Notion.**" message.
