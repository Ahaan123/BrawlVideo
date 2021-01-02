import praw
from moviepy.editor import *


client_id = '-a3rFPB9I37hbw'
client_secret = 'ghA0sWj50nO50FQe4z5hMvFYwFY'
user_agent = 'BrawlMemer'
username = 'BearNo21'
password = 'Prince#2'

reddit = praw.Reddit(client_id = client_id, client_secret=client_secret, user_agent=user_agent, username=username, password=password)
subred = reddit.subreddit('brawlstars')

def get_memes(li):
    meme_list = []
    for post in subred.search('flair:"Humor"', limit=li):
        #length-4 to length-1
        meme_url = str(post.url)
        extension = meme_url[len(meme_url)-4:len(meme_url)]
        if (extension == '.jpg' or extension == '.png'):
            meme_list.append(meme_url)

    return meme_list

memes = get_memes(50)
clip = ImageSequenceClip(memes, fps=24)
clip.write_videofile('test.mp4')