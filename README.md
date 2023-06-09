# Wifi_Extraction
Extract Saved WiFi Passwords From Your Windows Computer

This script allows you to extract saved Wi-Fi passwords on a Windows machine using the netsh command. 
It retrieves a list of saved SSIDs and their corresponding Wi-Fi profiles,
including the SSID, ciphers, and Wi-Fi password.

The script consists of the following functions:

get_windows_saved_ssids(): Retrieves a list of saved SSIDs by executing the netsh wlan show profiles command and parsing the output.

get_windows_saved_wifi_passwords(verbose): Extracts saved Wi-Fi passwords for each SSID. It iterates through the list of SSIDs,
retrieves the Wi-Fi profile details using the netsh wlan show profile command,
and extracts the ciphers and Wi-Fi password from the output. It returns a list of namedtuples containing the profile details.

print_windows_profiles(profile): Prints the given profile (SSID, ciphers, and Wi-Fi password) in a formatted manner.

print_all_windows_profiles(verbose): Prints all extracted SSIDs along with their corresponding ciphers and Wi-Fi passwords. 
It calls the get_windows_saved_wifi_passwords() function and prints the profiles in a table format.

To use the script, set the verbose_mode variable to True if you want to print the profiles as they are extracted or set it to False 
if you only want the final table output.

Feel free to adjust the code and adapt it to your specific needs.

*btw it does include exception handling...*

Bye
