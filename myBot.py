import praw
import time




def authenticate():
    print("Authenticating...")
    reddit = praw.Reddit(bot1)
    print("Authenticated as {}".format(reddit.user.me()))
    return reddit

def run_bot(reddit):
    

def main():
    reddit = authenticate()
    while True:
        run_bot(reddit)

if name == '__main__':
    main()
