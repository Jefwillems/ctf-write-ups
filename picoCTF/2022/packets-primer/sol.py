import sys
import codecs
import re

if __name__ == '__main__':
    hexstr = sys.argv[1]
    decode_hex = codecs.getdecoder("hex_codec")
    text = decode_hex(hexstr)[0]
    text = f'{text}'
    text = text.replace(' ', '')
    text = re.findall('picoCTF{.*}', text)
    print(text[0])
