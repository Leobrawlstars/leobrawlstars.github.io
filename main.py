
from pytube import Playlist
from pytube.exceptions import PytubeError

# Replace with your YouTube playlist URL
playlist_url = "https://www.youtube.com/playlist?list=PLItCJ3M1a3ANIhSGfLduyLh3DaHCMWve6"

# Create a Playlist object
playlist = Playlist(playlist_url)

print("Fetching video links...")
html_links = []

# Format each video link as an <a> tag, skipping problematic videos
i = 0
for video in playlist.videos:
    try:
        html_links.append(f'<a href="{video.watch_url}" target="_blank">{i}</a>')
    except PytubeError as e:
        print(f"Error fetching video details for {video.watch_url}: {e}")
    i =i+1

# Save or print the results
print("HTML links:")
for html_link in html_links:
    print(html_link)

# Optional: Save to an HTML file
with open("video_links.html", "w") as file:
    file.write("<html><body>\n")
    file.write("\n".join(html_links))
    file.write("\n</body></html>")

