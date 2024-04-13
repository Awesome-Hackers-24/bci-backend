import os
from supabase import create_client, Client

def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')


url: str = os.environ.get("https://sfesooveqwsgfzkosmxu.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNmZXNvb3ZlcXdzZ2Z6a29zbXh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI5OTg0MzMsImV4cCI6MjAyODU3NDQzM30.VsmHNhrmVG1Iznyva5-KPDykWAo9F58B72y2lZx_blw")
supabase: Client = create_client(url, key)
