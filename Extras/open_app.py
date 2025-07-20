import keyboard
import time
import subprocess
import time

def open_app(app_name, timeout=30):
    try:
        # Simulate pressing the Windows key to open the Start menu
        keyboard.send('windows')
        time.sleep(1)  # Wait for the Start menu to open

        # Type the application name
        keyboard.write(app_name)
        time.sleep(1)  # Wait for the application name to be entered

        # Press Enter to open the application
        keyboard.send('enter')

        # Start measuring time to wait for the application to open
        start_time = time.time()

        # Check if the application is running
        app_running = False
        while not app_running and (time.time() - start_time < timeout):
            # Get the list of currently running applications
            tasklist_output = subprocess.check_output(['tasklist']).decode('utf-8').splitlines()

            # Check if the application name appears in the tasklist output
            app_running = any(app_name.lower() in line.lower() for line in tasklist_output)

            # Optional: sleep briefly to avoid busy waiting
            time.sleep(0.5)

        # Calculate the time taken for the application to launch
        if app_running:
            launch_time = time.time() - start_time
            print(f"{app_name} launched in {launch_time:.2f} seconds.")
            # Wait for a little longer than the launch time before opening the next app
            time.sleep(launch_time + 1)  # Add an extra second for buffer
        else:
            print(f"Failed to detect {app_name} running within {timeout} seconds.")

    except Exception as e:
        print("Error while opening the application:", str(e))









# from pywinauto.application import Application
# from pywinauto.keyboard import send_keys
# import time

# def open_app(app_name):
#     send_keys('{VK_LWIN down}{VK_LWIN up}')
#     time.sleep(1)

#     send_keys(app_name)
#     time.sleep(2)

#     send_keys('{ENTER}')
