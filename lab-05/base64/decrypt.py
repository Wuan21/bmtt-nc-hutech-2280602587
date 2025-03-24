import base64

def main():
    try:
        with open("data.txt", "r") as file:
            encoded_string = file.read().strip()
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = str(decoded_bytes, "utf-8")
        print(f"Thông tin đã giải mã: {decoded_string}")
    except Exception as e:
        print("Lỗi: ", e)
        
if __name__ == "__main__":
    main()