import subprocess
import time
import requests

def run_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()

print("Checking for connected devices or running emulator...")
devices = run_command("adb devices")
if "device" not in devices:
    print("No devices or emulators found. Please ensure one is connected or running.")
    exit(1)  

apk_path = "<paste the path to the apk here>"
package_name = "<enter your package name here>"

installed_packages = run_command("adb shell pm list packages")
if package_name not in installed_packages:
    print("Installing APK...")
    install_output = run_command(f"adb install {apk_path}")
    print(install_output)
else:
    print("App already installed.")

print("Launching app...")
launch_output = run_command(f"adb shell am start -n {package_name}/.MainActivity")
print(launch_output)

time.sleep(5)  

print("\nFetching system information...")

os_version = run_command("adb shell getprop ro.build.version.release")
device_model = run_command("adb shell getprop ro.product.model")
memory_info = run_command("adb shell cat /proc/meminfo | grep MemTotal")
battery_info = run_command("adb shell dumpsys battery | grep level")
cpu_info = run_command("adb shell cat /proc/cpuinfo")
network_info = run_command("adb shell ifconfig") # (IP Address)

device_data = {
    "device_id": "device123",  
    "device_model": device_model,
    "os_version": os_version,
    "memory": memory_info,
    "battery_info": battery_info,
    "cpu_info": cpu_info,
    "network_info": network_info,
    "linked_app_id": 1 
}

backend_url = "http://localhost:5000/submitdeviceinfo"  
response = requests.post(backend_url, json=device_data)

if response.status_code == 200:
    print(f"Successfully sent data to backend: {device_data}")
else:
    print(f"Failed to send data to backend: {response.status_code}, {response.text}")

print("Closing the app...")
close_output = run_command(f"adb shell am force-stop {package_name}")
print(close_output)