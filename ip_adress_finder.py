import socket
from requests import get


class IPFinder:
    def __init__(self, hostname):
        self.hostname = hostname
        self.ip_locator()

    def ip_locator(self):
        local_ip_locator = socket.gethostbyname(self.hostname)
        public_ip_locator = get('https://api.ipify.org').text

        return f'Hostname: {self.hostname} \nLocal IP: {local_ip_locator} \nPublic IP: {public_ip_locator}'

    def __repr__(self):
        return str(self.ip_locator())


if __name__ == '__main__':
    print(IPFinder(hostname=socket.gethostname()))
