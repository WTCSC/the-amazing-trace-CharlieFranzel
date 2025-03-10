import subprocess

def traceroute(destination):
    # Run the traceroute command using subprocess
    command = ['traceroute', destination]
    
    try:
        # Execute the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred: {e}")

# Example usage
destination = 'google.com'
traceroute(destination)
