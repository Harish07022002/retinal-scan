import cv2
import numpy as np
known_retina_data = "sample_retina_data"

def capture_retina_image():
    
    captured_retina_data = "captured_retina_data"
    return captured_retina_data

def match_retina_data(captured_retina_data, known_retina_data):
    
    return captured_retina_data == known_retina_data

def unlock_door():
    print("Door unlocked!")

def main():
  
    captured_retina_data = capture_retina_image()
   
    match_result = match_retina_data(captured_retina_data, known_retina_data)

    if match_result:
        unlock_door()
    else:
        print("Retina scan failed. Access denied.")

if __name__ == "__main__":
    main()
