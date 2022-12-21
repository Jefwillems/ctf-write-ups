from morse_audio_decoder.morse import MorseCode


if __name__ == '__main__':
    morse_code = MorseCode.from_wavfile("morse_chal.wav")
    out = morse_code.decode()
    out = out.lower().replace(' ', '_')
    out = f'picoCTF{{{out}}}'
    print(out)
