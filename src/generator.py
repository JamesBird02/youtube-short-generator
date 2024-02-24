from dotenv import load_dotenv
import random
import os
from moviepy.editor import *
import moviepy.video.fx.crop as crop_vid
from openai import OpenAI
import elevenlabs
from reddit_scraper import get_user_input

load_dotenv()

labs_key = os.environ["eleven_labs_key"]
elevenlabs.set_api_key(labs_key)

client = OpenAI(api_key=os.environ["OPEN_AI_KEY"])
title, post_content = get_user_input(os.environ["subreddit"])



# Ask for video info
print(f"Selected title for the video: {title}")
option = input('Generate content about this? (y/n) >  ')

if option == 'yes':
    # Generate content using OpenAI API
    theme = post_content
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
                    {"role": "system", "content": "You are a knowledgeable assistant asked to provide a brief and engaging summary on a specified topic."},
                    {"role": "user", "content": f"Provide a brief, engaging summary on the topic - \"{theme}\", that highlights the main issues, advancements, or concerns associated with it. The content should immediately capture the viewer's interest, pose a critical question or highlight a significant challenge, and be suitable for a brief video format aimed at sparking discussion or raising awareness. Please keep it direct and compelling, without needing an introduction or specifying a title."}
                ]
        # temperature=0.7,
        # max_tokens=200,
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0
    )
    print(response.choices[0].message.content)
    yes_no = input('\nIs this fine? (y/n) >  ')
    if yes_no == 'y':
        content = response.choices[0].message.content
    else:
        content = post_content

# Create the directory
if os.path.exists('generated') == False:
    os.mkdir('generated')

# Generate speech for the video
speech = elevenlabs.generate(text=content,
                             voice= 'Sam')
elevenlabs.save(speech, "generated/speech.mp3")

gp = random.choice(["1", "2"])
start_point = random.randint(1, 500)
audio_clip = AudioFileClip("generated/speech.mp3")

if (audio_clip.duration + 1.3 > 58):
    print('\nSpeech too long!\n' + str(audio_clip.duration) + ' seconds\n' + str(audio_clip.duration + 1.3) + ' total')
    exit()

print('\n')

# Trim a random part of minecraft gameplay and slap audio on it
video_clip = VideoFileClip("gameplay/gameplay_" + gp + ".mp4").subclip(start_point, start_point + audio_clip.duration + 1.3)
final_clip = video_clip.set_audio(audio_clip)

# Resize the video to 9:16 ratio
w, h = final_clip.size
target_ratio = 1080 / 1920
current_ratio = w / h

if current_ratio > target_ratio:
    # The video is wider than the desired aspect ratio, crop the width
    new_width = int(h * target_ratio)
    x_center = w / 2
    y_center = h / 2
    final_clip = crop_vid.crop(final_clip, width=new_width, height=h, x_center=x_center, y_center=y_center)
else:
    # The video is taller than the desired aspect ratio, crop the height
    new_height = int(w / target_ratio)
    x_center = w / 2
    y_center = h / 2
    final_clip = crop_vid.crop(final_clip, width=w, height=new_height, x_center=x_center, y_center=y_center)

# Write the final video
final_clip.write_videofile("generated/" + title + ".mp4", codec='libx264', audio_codec='aac', temp_audiofile='temp-audio.m4a', remove_temp=True)