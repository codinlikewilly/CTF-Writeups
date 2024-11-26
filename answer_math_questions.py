import socket
import re

# Server configuration
SERVER_IP = "172.24.0.4"
SERVER_PORT = 8008

def answer_math_questions():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((SERVER_IP, SERVER_PORT))
        
        # Send HTTP/0.9 GET request
        request = f"GET / HTTP/0.9\r\nHost: {SERVER_IP}\r\n\r\n"
        s.sendall(request.encode())
        
        print("Connected to the server.")
        
        while True:
            line = s.recv(1024).decode('utf-8').strip()
            if not line:
                print('no')
                break
            print(f"Server: {line}")
            match = re.search(r'(\d+)([+\-*/])(\d+)=', line)
            
            if match:
                num1 = int(match.group(1))
                operator = match.group(2)
                num2 = int(match.group(3))
                if operator == '+':
                    answer = num1 + num2
                elif operator == '-':
                    answer = num1 - num2
                elif operator == '*':
                    answer = num1 * num2
                elif operator == '/':
                    answer = round(num1 / num2, 2)
                else:
                    continue
                print(f"Answer: {answer}")
                s.sendall(f"{answer}\n".encode())
                print("Answer sent")

def main():
    answer_math_questions()

if __name__ == "__main__":
    main()
