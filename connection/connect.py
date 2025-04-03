import pyvisa
import os

def format_text(text):
    """Formats the text by replacing underscores with spaces and 'q' with '?'."""
    text = text.replace("_", " ")
    text = text.replace("Q", "?")

    return text

def send_command(command):
    """Sends a command to the device without expecting data to be returned."""
    rm = pyvisa.ResourceManager()
    command = format_text(command)  # Format command text

    try:
        instr = rm.open_resource(os.environ.get("VISA Address"))
        instr.timeout = 5000  # Set timeout
        instr.write(command)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        instr.close()

def send_query(query):
    """Sends a command to the device and returns the data received in response."""
    rm = pyvisa.ResourceManager()
    query = format_text(query)  # Format query text
    try:
        instr = rm.open_resource(os.environ.get("VISA Address"))
        instr.timeout = 5000  # Set timeout
        return instr.query(query)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        instr.close()


import pyvisa


def gensetup(freq, volt, func):
    # Połączenie z oscyloskopem (zmień adres IP lub port)
    rm = pyvisa.ResourceManager()
    oscilloscope = rm.open_resource(os.environ.get("VISA Address"))   # Adres IP oscyloskopu

    # Wysyłanie komend SCPI do oscyloskopu
    oscilloscope.write(f':WGEN:FUNC {func.upper()}')  # Wybór funkcji (np. SIN, SQU, RAMP, itp.)
    oscilloscope.write(f':WGEN:FREQ {freq}')  # Ustawienie częstotliwości
    oscilloscope.write(f':WGEN:VOLT {volt}')  # Ustawienie amplitudy
    oscilloscope.write(':WGEN:VOLT:OFFS 0')  # Ustawienie offsetu na 0 V (możesz zmienić jeśli potrzeba)

    # Opcjonalnie: Można ustawić inne parametry, takie jak obciążenie, polaryzacja, itd.
    oscilloscope.write(':WGEN:OUTP:LOAD FIFTY')  # Ustawienie obciążenia na 50Ω
    oscilloscope.write(':WGEN:OUTP ON')  # Włączenie wyjścia generatora

    # Zamknięcie połączenia
    oscilloscope.close()


# Przykładowe wywołanie funkcji



