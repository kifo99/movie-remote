import serial
import pyautogui

ser = serial.Serial("COM4", 9600, timeout=1)

ir_actions = {
    "0xE916FF00": "f",
    "0xBC43FF00": "space",       
    "0xEA15FF00": "volumeUp",     
    "0xF807FF00": "volumeDown",  
    "0xBB44FF00": "left",         
    "0xBF40FF00": "right",
}

print("🔁 Listening for IR remote codes...")


while True:
    try:
        line =ser.readline().decode("utf-8").strip()
        if line.startswith("IR Code: 0x"):
            code = line.split("0x")[1]
            full_code = f"0x{code}"
            print(f"Received: {full_code}")
            if full_code in ir_actions:
                action = ir_actions[full_code]
                pyautogui.press(action)
                print(f"✅ Pressed key: {action}")
            else:
                print("❓ Unmapped code")
    except Exception as e:
        print("⚠️ Error:", e)