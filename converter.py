from pytube import YouTube

# Function to download YouTube video
def download_youtube_video(url, save_path="."): 
    try:
        # Create YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path=save_path)

        print(f"Video '{yt.title}' has been downloaded successfully to '{save_path}'!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
if __name__ == "__main__":
    # URL of the YouTube video
    video_url = input("Enter the YouTube video URL: ")
    
    # Path where the video will be saved
    save_path = input("Enter the path to save the video (leave blank for current directory): ").strip()

    if not save_path:
        save_path = "."

    # Download the video
    download_youtube_video(video_url, save_path)
