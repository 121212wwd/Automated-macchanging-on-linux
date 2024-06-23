import subprocess
import time

# DO NOT CHANGE OPTIONS
options = print('''
                                  d8P                                                             
                               d888888P                                                           
     d888b8b      ?88   d8P      ?88'       d8888b       88bd8b,d88b      d888b8b       d8888b    
    d8P' ?88      d88   88       88P       d8P' ?88      88P'`?8P'?8b    d8P' ?88      d8P' `P    
    88b  ,88b     ?8(  d88       88b       88b  d88     d88  d88  88P    88b  ,88b     88b        
    `?88P'`88b    `?88P'?8b      `?8b      `?8888P'    d88' d88'  88b    `?88P'`88b    `?888P'

OPTIONS:
	1: AUTO mac changing
		Description:
		Every time ping fails on google.com (not for commercial use)
		mac changing happens with a program called macchanger
		if the ping passes, mac changing doesn't happen everyone
		is happy.
		if ping fails, macchanging will happen
		if ping passes macchanging will be on hold
	2: EXIT

''')

def menu():
    print(options)
    try:
        user_input_options = input(int('what would you like?'))
        return user_input_options
    except Warning:
        print('Incorrect choice, try again.')
# NEED TO CHANGE THIS

def automated_ping_requests():
    print('Automated connection requests')
    print('')
    print('-----------------------------------------')
    print('')
    result = subprocess.run(['ping', 'google.com', '-c', '5'], capture_output=True, text=True)
    if result.returncode == 0:
        return 0
    else:
        return 1

def ping_google():
    print('Please Wait\nPinging in progress >> ')
    print('-----------------------------------------')
    result = subprocess.run(['ping', 'google.com', '-c', '5'], capture_output=True, text=True)
    return result
    
def ping_google_retry():
    print('Retrying')
    time.sleep(1)
    subprocess.run(['clear'])
    ping_google()

def macchanger_operation(): 
        # Process after the ping to then change mac adress if filtered connections
        print('Sucsessfull!\nStarting MacChanger')
        print('-----------------------------------------')
        subprocess.run(['sudo', 'ifconfig', 'wlan0', 'down'])
        subprocess.run(['sudo', 'macchanger', '--random', 'wlan0'])
        time.sleep(1)
        print('------------------------------------------')
        time.sleep(1)
        subprocess.run(['sudo', 'ifconfig', 'wlan0', 'up'])
        result = subprocess.run(['macchanger', '--show', 'wlan0'], capture_output=True, text=True, check=True)
        return result

def main():
    result = ping_google()
    while True:
        # Ping results
        if result.returncode == 0:
            # Start macchanger
            result_mac = macchanger_operation()
            if result_mac.returncode == 0:
                print('Automated checking process started')
                times_checked = 1
                while True:
                    print(f'Times checked = {times_checked}')
                    time.sleep(2)
                    subprocess.run(['clear'])
                    auto_result = automated_ping_requests()
                    if auto_result == 0:
                        times_checked = times_checked + 1
                    elif auto_result == 1:
                        macchanger_operation()
                    else:
                        break
            else:
                print('')
        else:
            ping_google_retry()

if __name__ == '__main__':
    main()

