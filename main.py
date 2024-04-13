from pyOpenBCI import OpenBCICyton
from supabase import create_client

# Hardcoded values for the Supabase URL and API key
url = "https://sfesooveqwsgfzkosmxu.supabase.co"
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InNmZXNvb3ZlcXdzZ2Z6a29zbXh1Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTI5OTg0MzMsImV4cCI6MjAyODU3NDQzM30.VsmHNhrmVG1Iznyva5-KPDykWAo9F58B72y2lZx_blw"
supabase = create_client(url, key)


def print_raw(sample):
    # Constructing data dictionary from the received sample
    data = {
        'pos1': sample.channels_data[0],
        'pos2': sample.channels_data[1],
        'pos3': sample.channels_data[2],
        'pos4': sample.channels_data[3],
        'pos5': sample.channels_data[4],
        'pos6': sample.channels_data[5],
        'pos7': sample.channels_data[6],
    }
    # Printing raw data for debugging
    print("Received sample:", sample.channels_data)

    # Updating data in the Supabase database
    supabase.table('sensor_data').update(data).eq('id', 1).execute()


def print_hi(name):
    # Simple greeting, used for debugging
    print(f'Hi, {name}')


if __name__ == '__main__':
    # Setting up the OpenBCI Cyton board
    board = OpenBCICyton(port='/dev/tty.usbserial-DM01MVJX', daisy=False)
    print_hi('PyCharm')

    # Starting the data stream from the OpenBCI board
    board.start_stream(print_raw)
