import socket 
from concurrent.futures import ThreadPoolExecutor

def port_scanner(target, port):
			
			try:
				#Create a socket 
				s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				s.settimeout(1) #Timeout for faster scanning in seconds

				# Try connecting to the port 
				result = s.connect_ex((target, port))
				if result == 0:
					print(f"Port {port} is open.")
				else: 
					print (f"Port {port} is closed. ")


				s.close ()
			except Exception as e: 
				print(f"Error scannig port {port}: {e}")

if __name__ == "__main__":
		target_ip = input("Enter the target IP address: ")
		port_range = range(1, 1025) #From port 1-1024
		
		print(f"Scanning target: {target_ip}")
		with ThreadPoolExecutor(max_workers=100) as executor:
			for port in port_range: 
				executor.submit(port_scanner, target_ip, port)
