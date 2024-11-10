import pyvisa

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
        instr = rm.open_resource('TCPIP0::192.168.0.100::hislip0::INSTR')
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
        instr = rm.open_resource('TCPIP0::192.168.0.100::hislip0::INSTR')
        instr.timeout = 5000  # Set timeout
        return instr.query(query)
    except Exception as e:
        print("An error occurred:", e)
    finally:
        instr.close()

