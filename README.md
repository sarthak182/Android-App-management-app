# Android-App-management-app

Steps to Run the Application:

1. Install Dependencies:

Install Flask and other required Python packages by running:
pip install flask

2. Set up Android Emulator:

Install ADB (Android Debug Bridge):

Follow the official guide to install ADB. Make sure you also have Android Studio installed.

Create and Start the Emulator:

Open Android Studio and set up an Android Virtual Device (AVD) through the AVD Manager.

Open your terminal and run the following command to start the emulator:
emulator -avd <device_name>
Replace <device_name> with your AVD's name.

3. Verify Device Connection:

Run the following command in the terminal to verify that your emulator is connected
adb devices
Ensure that your device shows up in the list

4. Start Flask App:

Navigate to the folder where main.py is located.

5. Run the Flask app with:

python main.py

6. To Add a device or Install an APK:

Run the Virtual Android Script:

Navigate to where virtual-android.py is located.

Before running the script, change the following variables in the virtual-android.py file:

apk_path: Path to the APK file you want to install.

package_name: The package name of the app you want to install.

Then, run the script:
python virtual-android.py

7. Access the Web App:

Open your browser and go to:
http://127.0.0.1:5000

Finally Your web app should now be live and fully set up!
