from gtts import gTTS
from moviepy.editor import *
import os
import uuid

def generate_video_from_script(script):
    # Tạo tên file ngẫu nhiên
    unique_id = str(uuid.uuid4())
    audio_path = f"{unique_id}.mp3"
    video_path = f"{unique_id}.mp4"

    # Chuyển văn bản thành giọng nói
    tts = gTTS(script, lang="vi")
    tts.save(audio_path)

    # Tạo nền video (đen) + chèn âm thanh
    audioclip = AudioFileClip(audio_path)
    duration = audioclip.duration

    videoclip = ColorClip(size=(1280, 720), color=(0, 0, 0), duration=duration)
    videoclip = videoclip.set_audio(audioclip)
    videoclip.write_videofile(video_path, fps=24)

    # Xoá file audio tạm
    os.remove(audio_path)

    return video_path
