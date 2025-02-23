# libos.py
import os
import shutil

def get_file(url):
    os.system(f'curl -O {url}')

def list_files(directory='.'):
    """List all files in the given directory."""
    return os.listdir(directory)

def copy_file(src, dest):
    """Copy a file from src to dest."""
    shutil.copy(src, dest)

def delete_file(filepath):
    """Delete the specified file."""
    if os.path.exists(filepath):
        os.remove(filepath)
    else:
        print(f"The file {filepath} does not exist")


def create_directory(directory):
    """Create a new directory."""
    os.makedirs(directory, exist_ok=True)

def delete_directory(directory):
    """Delete the specified directory."""
    if os.path.exists(directory):
        shutil.rmtree(directory)
    else:
        print(f"The directory {directory} does not exist")



def execute_command(command):
    """Execute the given command."""
    os.system(command)



def create_file(filepath):
    """Create a new file."""
    with open(filepath, 'w') as f:
        f.write('')
        f.close()


def edit_file(filepath, content):
    """Edit the specified file."""
    with open(filepath,
              'w') as f:
        f.write(content)
        f.close()

def read_file(filepath):
    """Read the specified file."""
    with open(filepath, 'r') as f:
        content = f.read()
        f.close()
    return content

