import praw
import time
import re
import os

subreddits = ["test", "Shrek", "ShrekIsLove", "smashmouth", "Brogres", "Shrekmemes"]


def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit('bot1')
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit

def run_bot(reddit):
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt", "r") as file:
            posts_replied_to = file.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None, posts_replied_to))

    for subreddit in subreddits:
        subreddit = reddit.subreddit(subreddit)
        for submission in subreddit.hot(limit = 10):
            if re.search("the years start coming", submission.title, re.IGNORECASE):
                #reply to the post even if we have already replied because it's funnier if the years Don't Stop Coming
                submission.reply("and they don't stop coming")
                print('Bot replying to', str(submission.author))
                #remember the post we have replied to
                posts_replied_to.append(submission.id)
            if submission.id not in posts_replied_to:
                if re.search("somebody once told me", submission.title, re.IGNORECASE):
                    #reply to the post
                    submission.reply("the world was gonna roll me")
                    print('Bot replying to', str(submission.author))
                    #remember the post we have replied to
                    posts_replied_to.append(submission.id)
    with open("posts_replied_to.txt", "w") as file:
        for post_id in posts_replied_to:
            file.write(post_id + "\n")

def main():
    reddit = authenticate()
    while True:
        run_bot(reddit)
        time.sleep(15)

if __name__ == '__main__':
    main()
