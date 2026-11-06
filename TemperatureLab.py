import time
import board
import adafruit_dht
from datetime import datetime
from gpiozero import LED
from time import sleep
import gspread


sensor = adafruit_dht.DHT11(board.D16) # Change the pin number to the data pin of  DHT11 
Red = LED(21)
Blue = LED(19)


print("time,celsius,fahrenheit")

def to_fahrenheit(c):
    f = (celsius * 1.8) + 32
    return f 

try:
    gc = gspread.service_account(filename='credentialstemperature.json')
    sh = gc.open('TemperatureLabP')
    worksheet = sh.get_worksheet(0)  # First sheet I think

except Exception as auth_err:
    exit(1)



while True:
    try:
        celsius = sensor.temperature # Get the temperature in Celcius from the sensor
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        print("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))

        Temp = ("{0},{1:0.1f},{2:0.1f}".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
        Time = current_time.strftime("%H:%M:%S")

        #lines = []
        #with open("temperature.csv", "a") as file:
        #         print((Temp), file=file)

       
        row_data = [Time, celsius, fahrenheit]

        #Add the data as a new row
        worksheet.append_row(row_data)
        print('Data sent successfully!')


        if (int(fahrenheit) > 72.0) or (int(fahrenheit) == 72.0):
            Red.on()
            Blue.off()
        else:
            Blue.on()
            Red.off()
        
                 

        
        time.sleep(3.0)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error    
 
#source venv/bin/activate
#python3 /home/funnylizardt/temperature.py





#INSTRUCTIONS IF FORGOTTEN!
#1.Go to the Google Cloud Console, create a new project, and enable the Google Sheets API and Google Drive API.
#2.Create a service account under IAM & Admin, and generate a JSON key file (save it as credentials.json for easier finding on Raspberry Pi).
#3.Create a new Google Sheet on your Google account and share the sheet's edit access with the email address found inside your credentials.json file (client_email).