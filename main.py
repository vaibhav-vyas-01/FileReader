import os

if __name__ == '__main__':
    print("welcome to filereader 1.1 created by vaibhav")
    while True:
        filename = input("Enter full file path OR text: ")
        if filename == "quit":
            break

        if os.path.exists(filename):
            with open(filename, "r", encoding="utf-8") as f:
                x = f.read().replace("\n", " ")
            print(x)
            os.system(
                   f'powershell -Command "Add-Type -AssemblyName System.Speech; '
                   f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{x}\')"'
            )
        elif filename:
            z = filename
            os.system(
                f'powershell -Command "Add-Type -AssemblyName System.Speech; '
                f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{z}\')"'
            )

        else:
            print("File not found!")