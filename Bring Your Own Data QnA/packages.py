from promptflow import tool
import subprocess

@tool
def list_packages(input: str) -> str: 
    # Run the pip list command and save the output to a file
    with open('packages.txt', 'w') as f:
        subprocess.run(['pip', 'list'], stdout=f)