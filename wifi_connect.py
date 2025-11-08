import network
import time


def scan_networks():
    # STA_IF = station interface, connects to a WiFi network
    # AP_IF = access point interface, creates a WiFi network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    print("Scanning for available WiFi networks...")
    networks = wlan.scan()
    print(f"Found {len(networks)} networks:")
    print("-" * 50)

    for i, net in enumerate(networks):
        ssid = net[0].decode("utf-8")
        RSSI = net[3]
        authmode = "🔐" if net[4] > 0 else "😵"
        print(f"{i + 1}. SSID: {ssid}, RSSI: {RSSI}, AuthMode: {authmode}")

    print("-" * 50)
    return networks


def connect_to_wifi(ssid, password, timeout=10):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)

    if wlan.isconnected():
        print(f"Already connected to a WiFi network: {wlan.config('essid')}")
        return True

    print(f"Connecting to WiFi network: {ssid}")
    wlan.connect(ssid, password)

    start_time = time.time()
    while not wlan.isconnected():
        if time.time() - start_time > timeout:
            print("Connection timed out.")
            return False
        time.sleep(1)

    ip_info = wlan.ifconfig()
    print("Connected successfully!")
    print(f"IP Address: {ip_info[0]}")
    print(f"DNS:        {ip_info[3]}")
    return True


if __name__ == "__main__":
    print("WiFi Connector")
    print("*" * 20)
    print("""
          Example usage:
          mpremote connect /dev/cu.usbserial-0001 repl
            >>> import wifi_connect
            >>> wifi_connect.scan_networks()
            >>> wifi_connect.connect_to_wifi('Your_SSID', 'Your_Password')
            """)
    print("*" * 20)
    print(":: scan_networks() - Find available WiFi networks")
    print(":: connect_to_wifi(ssid, password) - Connect to a WiFi network")
