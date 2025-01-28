import subprocess

def send_notification(title, message):
    """Send a notification using notify-send."""
    try:
        # Send the notification
        subprocess.run(['notify-send', title, message], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error sending notification: {e}")

def clean_cache():
    # Your existing cache-cleaning code here
    # For demonstration, let's simulate the cache cleaning process.
    print("Starting cleaning process...")
    # Simulated cache size for demo
    cache_size = "4.0K"
    print(f"Cache directory found: /home/craftworkson/.stremio-server/stremio-cache/")
    print(f"Cache size: {cache_size}")
    
    # Assuming the cache is cleaned successfully:
    print("Cache cleaned successfully.")

    # Now send a notification
    send_notification("Stremio Cache Cleaned", f"Cache size: {cache_size} has been cleaned.")

if __name__ == "__main__":
    clean_cache()
