import praw
import time
import config
import os

reddit = praw.Reddit(client_id=os.environ.get('client_id'),
                     client_secret=os.environ.get('client_secret'),
                     user_agent= os.environ.get('user_agent'),
                     username=os.environ.get('username'),
                     password=os.environ.get('password'))

reddit.validate_on_submit = True
targetSubreddit = reddit.subreddit("MinecraftEverything")
week = 0


def post_submission(_week):
    _thePost = targetSubreddit.submit(title="[Week " + str(_week) + "] " + config.postTitle,
                                    selftext=config.postDescription)
    config.submissionURL = _thePost.permalink
    _thePost.mod.distinguish(how="yes")
    _thePost.mod.sticky()
    _thePost.flair.select(config.flairID)
    _comment = _thePost.reply(config.topReplyText)
    _stickiedComment = reddit.comment(_comment)
    _stickiedComment.mod.distinguish(sticky=True, how="yes")
    time.sleep(config.delay)
    _thePost.mod.undistinguish()
    _thePost.mod.distinguish(how="yes")


def write_to_wiki():
    page = targetSubreddit.wiki["index"]
    config.wikiContents += "\n\n • [Week " + str(week) + "] " + config.postTitle + " - [Link to the thread](" + config.submissionURL + ")"
    page.edit(config.wikiContents)


# while True:
#     week += 1
#     post_submission(week)
#     write_to_wiki()
print(os.environ.get("username"))