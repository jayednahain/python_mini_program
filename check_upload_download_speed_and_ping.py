import speedtest
import os

test = speedtest.Speedtest()

check_option = int(input('''what speed you want to test:
                   press (1) for Donwload speed
                   press (2) upload speed
                   press (3) for check piing
         Enter your choice : '''))
byte = 1000000
bit = 8000000

if check_option == 1:
    download_speed= test.download()
    
    download_speed_mb_byte = download_speed/byte
    download_speed_mb_bite = download_speed/bit

    print("for bytes: ","%.2f",download_speed_mb_byte,"Mbps")
    print("for bites:  %.2f", download_speed_mb_bite,"Mbps")
    

elif check_option ==2:

    upload_speed = test.upload()
    upload_speed_mb_byte = upload_speed/byte
    upload_speed_mb_bite = upload_speed/bit

    print("upload speed for bytes: ",upload_speed_mb_byte,"Mbps")
    print("upload speed for bites: ", upload_speed_mb_bite,"Mbps")

elif check_option ==3:
    ip_check = input("enter a ip addres: ")
    os.system('ping -n 4 {}'.format(ip_check))
else:
    print("you use a worng key word!")
    
                   
