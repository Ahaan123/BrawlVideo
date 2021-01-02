import praw
from moviepy.editor import *
from PIL import Image
import requests
import os
from pytesseract import image_to_string

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

memes = get_memes(5)
for idx, meme in enumerate(memes):
    img_data = requests.get(meme).content
    with open(str(idx)+'.png', 'wb') as handler:
        handler.write(img_data)
    
    background = Image.new('RGB', (1920, 1080), color='white')
    img2 = Image.open(str(idx)+'.png')
    img_w, img_h = img2.size
    bg_w, bg_h = background.size
    offset = ((bg_w - img_w) // 2, (bg_h - img_h) // 2)
    background.paste(img2, offset)
    background.save('video_data/'+str(idx)+'.png')
    os.remove(str(idx)+'.png')

files = os.listdir('video_data')
cleaned_files = ['video_data/'+path for path in files]
image_text  = []
for fpath in cleaned_files:
    i = Image.open(fpath)
    st = image_to_string(i)
    image_text.append(st)

print(image_text)
clip = ImageSequenceClip(cleaned_files, fps=1)
clip.write_videofile('test.mp4')