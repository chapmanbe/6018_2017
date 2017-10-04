"""Hello from around the world"""
import random
hellos = {"English":"Hello", "French":"Bonjour", "Farsi":"سلام", "Hindi":"नमस्ते",
          "Mandarin":"你好", "Korean":"여보세요", "Navajo":"Yá'át'ééh",
          "Arabic":"مرحبا", "Finnish":"Hei", "Urdu":"ہیلو"}

def __get_random_hello():
    global hellos
    key = random.choice(list(hellos.keys()))
    return hellos[key]
def hello(name="Brian"):
    global hellos
    return "%s, %s"%(__get_random_hello(),name)

if __name__ == "__main__":
    print("module name is",__name__)
