class RailFenceCipher:
    def __init__(self):
        pass
    
    def rail_fence_encrypt(self, plain_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        
        for char in plain_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
            
        cipher_text = "".join("".join(rail) for rail in rails)
        return cipher_text
    
    def rail_fence_decrypt(self, encrypted_text, num_rails):
        rails = [[] for _ in range(num_rails)]
        rail_index = 0
        direction = 1
        for char in encrypted_text:
            rails[rail_index].append(char)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        plain_text = ""
        rail_index = 0
        direction = 1
        for _ in encrypted_text:
            plain_text += rails[rail_index].pop(0)
            if rail_index == 0:
                direction = 1
            elif rail_index == num_rails - 1:
                direction = -1
            rail_index += direction
        return plain_text