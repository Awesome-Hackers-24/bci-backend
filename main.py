import os
from pyOpenBCI import OpenBCICyton
from supabase import create_client, Client

def print_raw(sample):
    data = {
        'pos1': sample.channels_data[0],
        'pos2': sample.channels_data[1],
        'pos3': sample.channels_data[2],
        'pos4': sample.channels_data[3],
        'pos5': sample.channels_data[4],
        'pos6': sample.channels_data[5],
        'pos7': sample.channels_data[6],
    }
    supabase.table('sensor_data').update(data).eq('id', 1).execute()

board = OpenBCICyton(port='COM3', daisy=False)

def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('PyCharm')
    board.start_stream(print_raw)


url: str = os.environ.get("https://sfesooveqwsgfzkosmxu.supabase.co")
key: str = os.environ.get("eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNmZXNvb3ZlcXdzZ2Z6a29zbXh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI5OTg0MzMsImV4cCI6MjAyODU3NDQzM30.VsmHNhrmVG1Iznyva5-KPDykWAo9F58B72y2lZx_blw")
supabase: Client = create_client(url, key)
