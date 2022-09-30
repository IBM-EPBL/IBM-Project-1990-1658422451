import random
import time
while True:
    temperature = random.randint(-15,100)
    humidity = random.randint(1,100)
    print(f"Checking Temperature: {temperature}"u'\N{DEGREE SIGN}'"C");
    print(f"Checking Humidity: {humidity}%");
    f = (temperature * 1.8 ) +32
    print("Temperature in Fahreheit is:",f)
    if temperature >=37:
        print(f"{temperature}"u'\N{DEGREE SIGN}'"C is a Hot Temperature\n Alarm is activated \n Notification is Notified")
    elif temperature==37:
        print(f"{temperature}"u'\N{DEGREE SIGN}'"C is a Normal Temperature")
    if humidity >= 100:
        print(f"{humidity}% it is a Humid humudity level")
    elif 65<humidity<100 :
        print(f"{humidity}% it is a Prefect humudity level")
    else :
        print(f"{humidity}% it is a Dry humudity level")
    time.sleep(5)