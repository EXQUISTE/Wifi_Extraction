import subprocess
import os
import re
from collections import namedtuple
import configparser

def get_windows_saved_ssids():
    """Returns a list of saved SSIDs in a Windows machine using netsh command"""
    # get all saved profiles in the PC
    output = subprocess.check_output("netsh wlan show profiles").decode()
    ssids = []
    profiles = re.findall(r"All User Profile\s(.*)", output)
    for profile in profiles:
        # for each SSID, remove spaces and colon
        ssid = profile.strip().strip(":").strip()
        # add to the list
        ssids.append(ssid)
    return ssids


def get_windows_saved_wifi_passwords(verbose=1):
    """Extracts saved Wi-Fi passwords saved in a Windows machine, this function extracts data using netsh
    command in Windows
    Args:
        verbose (int, optional): whether to print saved profiles real-time. Defaults to 1.
    Returns:
        [list]: list of extracted profiles, a profile has the fields ["ssid", "ciphers", "key"]
    """
    ssids = get_windows_saved_ssids()
    Profile = namedtuple("Profile", ["ssid", "ciphers", "key"])
    profiles = []
    for ssid in ssids:
        try:
            ssid_details = subprocess.check_output(f"""netsh wlan show profile "{ssid}" key=clear""").decode()
            # get the ciphers
            ciphers = re.findall(r"Cipher\s(.*)", ssid_details)
            # clear spaces and colon
            ciphers = "/".join([c.strip().strip(":").strip() for c in ciphers])
            # get the Wi-Fi password
            key = re.findall(r"Key Content\s(.*)", ssid_details)
            # clear spaces and colon
            try:
                key = key[0].strip().strip(":").strip()
            except IndexError:
                key = "None"
            profile = Profile(ssid=ssid, ciphers=ciphers, key=key)
            if verbose >= 1:
                print_windows_profiles(profile)
            profiles.append(profile)
        except subprocess.CalledProcessError:
            print(f"Failed to retrieve details for SSID: {ssid}")
    return profiles

def print_windows_profiles(profile):
    """Prints the given profile (SSID, CIPHERS, KEY)"""
    print(f"{profile.ssid:<24}{profile.ciphers:<14}{profile.key}")

def print_all_windows_profiles(verbose):
    """Prints all extracted SSIDs along with Key on Windows"""
    print("SSID                     CIPHER(S)      KEY")
    print("-"*50)
    get_windows_saved_wifi_passwords(verbose)

# Usage
verbose_mode = True  # Set verbose mode as needed
print_all_windows_profiles(verbose_mode)
