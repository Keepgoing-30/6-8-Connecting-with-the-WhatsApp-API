import time
import requests
import json
import RPi.GPIO as GPIO 

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_pressed = False 

# --- HÀM GỬI TIN NHẮN (Đã sửa theo Part 6) ---
def send_alert():
    # 1. URL: Theo hướng dẫn Part 3, Step 3
    # Hãy thay đổi "US" nếu bạn ở vùng khác
    url = "https://dev.stedi.me/sendtext?whatsApp=true&region=US" 
    
    # 2. HEADER: Theo hướng dẫn Part 3, Step 12 & Part 6, Step 10-13
    # Key phải là 'suresteps.session.token' chứ không phải 'Authorization'
    headers = {
        "suresteps.session.token": "678d5c1e-f7fa-407f-8a4e-cfb32036bc01", 
        "Content-Type": "application/json"
    }
    
    # 3. PAYLOAD: Theo hướng dẫn Part 3, Step 6 & Part 6, Step 8
    # Cấu trúc đơn giản hơn nhiều so với API gốc
    payload = {
        "phoneNumber": "8089906975", # Ví dụ: "18015551234"
        "message": "Hospital Division" # Hoặc nội dung bạn muốn
    }
    
    # Gửi request
    response = requests.post(url, headers=headers, json=payload)
    
    # Kiểm tra kết quả (Theo Part 6, Step 14)
    if response.status_code == 200:
        print("WhatsApp Alert Sent")
    else:
        print("Failed to send WhatsApp Alert")
        print(response.status_code)
        print(response.text) # In ra lỗi chi tiết nếu có
    
    return response

# --- VÒNG LẶP CHÍNH ---
while True: 
    if GPIO.input(7) == GPIO.HIGH and not button_pressed: 
        print('Someone has pressed the alert button!')
        
        # Gọi hàm gửi tin nhắn
        try:
            send_alert() 
        except Exception as e:
            print(f"Error calling send_alert: {e}")
            
        button_pressed = True
        
    elif GPIO.input(7) == GPIO.LOW and button_pressed:
        button_pressed = False 
        
    time.sleep(0.1)