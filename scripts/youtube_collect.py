from googleapiclient.discovery import build
import pandas as pd

API_KEY = "AIzaSyCXaBfKTrGf2vtGsXlMiVYH9ET4eV1riEs"

youtube = build("youtube", "v3", developerKey=API_KEY)

def get_comments(video_id):
    comments = []

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100
    )

    response = request.execute()

    for item in response["items"]:
        text = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        comments.append(text)

    return comments

# EXEMPLO
video_id = "dQw4w9WgXcQ"  # substitua

comments = get_comments(video_id)

df = pd.DataFrame({"text": comments})

df.to_csv("data/raw/youtube_comments.csv", index=False)

print("Coleta concluída!")