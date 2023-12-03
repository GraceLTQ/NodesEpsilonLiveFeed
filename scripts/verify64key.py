import base64
import binascii

key = "1ZBGL41X7gK0Wu6YPIjp673qUUpEtGF2nMXZUSrWAfEDdJA0MZ7DNRPafZ2wPbmHqURj5CV7dxkoACDbVmHCQg=="
try:
    decoded_key = base64.b64decode(key)
    print("Key is valid Base64")
except binascii.Error:
    print("Key is not valid Base64")
