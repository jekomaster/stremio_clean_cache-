import subprocess

print("Sending notification...")  # Debug message
result = subprocess.run(['notify-send', 'Test Notification', 'This is a test notification'], capture_output=True)

print("Result:", result)  # Print result to see if there was an error
