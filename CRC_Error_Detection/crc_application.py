import tkinter as tk
from tkinter import messagebox
import random


# ============================================================
# CRC CALCULATION
# ============================================================

def calculate_crc(data, generator):
    """
    Calculate CRC remainder using modulo-2 division.
    """

    zeros = len(generator) - 1

    # Append zeros to the original data
    appended_data = data + ("0" * zeros)

    # Convert to list because bits need to be changed during XOR
    remainder = list(appended_data)

    # Perform modulo-2 division
    for i in range(len(data)):
        if remainder[i] == "1":

            for j in range(len(generator)):

                if remainder[i + j] == generator[j]:
                    remainder[i + j] = "0"
                else:
                    remainder[i + j] = "1"

    # Last bits are the CRC remainder
    crc = "".join(remainder[-zeros:])

    return crc


# ============================================================
# CRC CALCULATION WITH STEPS
# ============================================================

def get_crc_steps(data, generator):
    """
    Generate a simple step-by-step explanation of
    the CRC modulo-2 division.
    """

    zeros = len(generator) - 1
    working = list(data + ("0" * zeros))

    steps = []

    steps.append("CRC CALCULATION")
    steps.append("=" * 50)
    steps.append("")
    steps.append("Original Data       : " + data)
    steps.append("Generator Polynomial: " + generator)
    steps.append("Zeros Appended      : " + str(zeros))
    steps.append("Data after padding  : " + "".join(working))
    steps.append("")
    steps.append("Modulo-2 XOR Division")
    steps.append("-" * 50)

    for i in range(len(data)):

        if working[i] == "1":

            before = "".join(working)

            for j in range(len(generator)):

                if working[i + j] == generator[j]:
                    working[i + j] = "0"
                else:
                    working[i + j] = "1"

            after = "".join(working)

            steps.append(
                "Position " + str(i + 1) +
                " : " + before +
                "  XOR  " + generator +
                "  ->  " + after
            )

    crc = "".join(working[-zeros:])

    steps.append("")
    steps.append("-" * 50)
    steps.append("CRC Remainder: " + crc)

    steps.append("")
    steps.append(
        "Transmitted Frame: " + data + crc
    )

    return "\n".join(steps)


# ============================================================
# INPUT VALIDATION
# ============================================================

def validate_inputs():

    data = data_entry.get().strip()
    generator = generator_entry.get().strip()

    if data == "":
        messagebox.showerror(
            "Input Error",
            "Please enter the data bits."
        )
        return None

    if generator == "":
        messagebox.showerror(
            "Input Error",
            "Please enter the generator polynomial."
        )
        return None

    if any(bit not in "01" for bit in data):

        messagebox.showerror(
            "Input Error",
            "Data must contain only 0 and 1."
        )
        return None

    if any(bit not in "01" for bit in generator):

        messagebox.showerror(
            "Input Error",
            "Generator must contain only 0 and 1."
        )
        return None

    if len(generator) < 2:

        messagebox.showerror(
            "Input Error",
            "Generator must contain at least 2 bits."
        )
        return None

    if generator[0] != "1":

        messagebox.showerror(
            "Input Error",
            "Generator polynomial must start with 1."
        )
        return None

    if data == "0" * len(data):

        messagebox.showwarning(
            "Input Warning",
            "The data contains only zeros. "
            "You can still continue, but try a normal binary data value."
        )

    return data, generator


# ============================================================
# GENERATE CRC
# ============================================================

def generate_crc():

    result = validate_inputs()

    if result is None:
        return

    data, generator = result

    crc = calculate_crc(data, generator)

    transmitted = data + crc

    # Display CRC
    crc_result.config(text=crc)

    # Display transmitted frame
    transmitted_result.config(text=transmitted)

    # Store transmitted frame
    global original_transmitted_frame
    original_transmitted_frame = transmitted

    # Clear receiver
    received_entry.delete(0, tk.END)

    error_info_label.config(
        text="Error Position(s): ---"
    )

    result_label.config(
        text="Result: ---"
    )

    status_label.config(
        text="CRC frame generated successfully."
    )

    # Update information
    frame_length_label.config(
        text="Frame Length: " + str(len(transmitted)) + " bits"
    )


# ============================================================
# COPY TRANSMITTED FRAME
# ============================================================

def copy_frame():

    global original_transmitted_frame

    frame = transmitted_result.cget("text")

    if frame == "---":

        messagebox.showerror(
            "Error",
            "Please generate the CRC frame first."
        )
        return

    original_transmitted_frame = frame

    received_entry.delete(0, tk.END)
    received_entry.insert(0, frame)

    error_info_label.config(
        text="Error Position(s): None"
    )

    result_label.config(
        text="Result: Ready for verification"
    )

    status_label.config(
        text="Transmitted frame copied to receiver."
    )


# ============================================================
# INTRODUCE TRANSMISSION ERROR
# ============================================================

def introduce_error():

    global original_transmitted_frame

    frame = transmitted_result.cget("text")

    if frame == "---":

        messagebox.showerror(
            "Error",
            "Please generate the transmitted frame first."
        )
        return

    error_type = error_type_var.get()

    bits = list(frame)
    error_positions = []

    # --------------------------------------------------------
    # NO ERROR
    # --------------------------------------------------------

    if error_type == "No Error":

        corrupted_frame = frame

    # --------------------------------------------------------
    # SINGLE BIT ERROR
    # --------------------------------------------------------

    elif error_type == "Single Bit Error":

        position = random.randint(
            0,
            len(bits) - 1
        )

        if bits[position] == "0":
            bits[position] = "1"
        else:
            bits[position] = "0"

        error_positions.append(position + 1)

        corrupted_frame = "".join(bits)

    # --------------------------------------------------------
    # MULTIPLE BIT ERROR
    # --------------------------------------------------------

    elif error_type == "Multiple Bit Error":

        number_of_errors = min(3, len(bits))

        positions = random.sample(
            range(len(bits)),
            number_of_errors
        )

        for position in positions:

            if bits[position] == "0":
                bits[position] = "1"
            else:
                bits[position] = "0"

            error_positions.append(position + 1)

        error_positions.sort()

        corrupted_frame = "".join(bits)

    # --------------------------------------------------------
    # RANDOM ERROR
    # --------------------------------------------------------

    else:

        maximum_errors = min(5, len(bits))

        number_of_errors = random.randint(
            1,
            maximum_errors
        )

        positions = random.sample(
            range(len(bits)),
            number_of_errors
        )

        for position in positions:

            if bits[position] == "0":
                bits[position] = "1"
            else:
                bits[position] = "0"

            error_positions.append(position + 1)

        error_positions.sort()

        corrupted_frame = "".join(bits)

    # Put corrupted frame into receiver
    received_entry.delete(0, tk.END)
    received_entry.insert(0, corrupted_frame)

    # Display error positions
    if error_positions:

        error_info_label.config(
            text="Error Position(s): " +
            ", ".join(
                map(str, error_positions)
            )
        )

    else:

        error_info_label.config(
            text="Error Position(s): None"
        )

    # Display status
    if error_positions:

        status_label.config(
            text="Transmission error simulated successfully."
        )

    else:

        status_label.config(
            text="No transmission error introduced."
        )

    # Reset result until verification
    result_label.config(
        text="Result: Ready for CRC verification"
    )


# ============================================================
# VERIFY CRC
# ============================================================

def verify_crc():

    received_frame = received_entry.get().strip()
    generator = generator_entry.get().strip()

    if received_frame == "":

        messagebox.showerror(
            "Verification Error",
            "Please enter or copy a received frame."
        )
        return

    if generator == "":

        messagebox.showerror(
            "Verification Error",
            "Please enter the generator polynomial."
        )
        return

    if any(bit not in "01" for bit in received_frame):

        messagebox.showerror(
            "Verification Error",
            "Received frame must contain only 0 and 1."
        )
        return

    if any(bit not in "01" for bit in generator):

        messagebox.showerror(
            "Verification Error",
            "Generator must contain only 0 and 1."
        )
        return

    if len(generator) < 2:

        messagebox.showerror(
            "Verification Error",
            "Generator must contain at least 2 bits."
        )
        return

    if len(received_frame) < len(generator):

        messagebox.showerror(
            "Verification Error",
            "Received frame is shorter than the generator."
        )
        return

    zeros = len(generator) - 1

    temp = list(received_frame)

    # Modulo-2 division
    for i in range(
        len(received_frame) - zeros
    ):

        if temp[i] == "1":

            for j in range(len(generator)):

                if temp[i + j] == generator[j]:

                    temp[i + j] = "0"

                else:

                    temp[i + j] = "1"

    remainder = "".join(
        temp[-zeros:]
    )

    # --------------------------------------------------------
    # NO ERROR
    # --------------------------------------------------------

    if remainder == "0" * zeros:

        result_label.config(
            text="RESULT: ✓ NO ERROR DETECTED"
        )

        status_label.config(
            text="CRC verification successful."
        )

        messagebox.showinfo(
            "CRC Verification",
            "✓ No error detected in the received frame."
        )

    # --------------------------------------------------------
    # ERROR
    # --------------------------------------------------------

    else:

        result_label.config(
            text="RESULT: ✗ ERROR DETECTED"
        )

        status_label.config(
            text="CRC detected an error in the received frame."
        )

        messagebox.showwarning(
            "CRC Verification",
            "✗ Error detected in the received frame.\n\n"
            "Remainder: " + remainder
        )


# ============================================================
# SHOW CRC CALCULATION STEPS
# ============================================================

def show_crc_steps():

    result = validate_inputs()

    if result is None:
        return

    data, generator = result

    steps = get_crc_steps(
        data,
        generator
    )

    # Create new window
    steps_window = tk.Toplevel(window)

    steps_window.title(
        "CRC Calculation Steps"
    )

    steps_window.geometry(
        "850x600"
    )

    heading = tk.Label(
        steps_window,
        text="CRC Calculation - Step by Step",
        font=("Arial", 18, "bold")
    )

    heading.pack(pady=10)

    text_area = tk.Text(
        steps_window,
        width=100,
        height=30,
        font=("Consolas", 10)
    )

    text_area.pack(
        padx=15,
        pady=10,
        fill="both",
        expand=True
    )

    text_area.insert(
        tk.END,
        steps
    )

    text_area.config(
        state="disabled"
    )


# ============================================================
# HOW CRC WORKS
# ============================================================

def show_how_crc_works():

    help_window = tk.Toplevel(window)

    help_window.title(
        "How CRC Works"
    )

    help_window.geometry(
        "650x550"
    )

    heading = tk.Label(
        help_window,
        text="How Cyclic Redundancy Check Works",
        font=("Arial", 18, "bold")
    )

    heading.pack(pady=15)

    explanation = (
        "1. The sender enters binary data.\n\n"

        "2. A generator polynomial is selected.\n\n"

        "3. Zeros are appended to the original data.\n\n"

        "4. The sender performs modulo-2 division "
        "using XOR operations.\n\n"

        "5. The remainder obtained is called the CRC.\n\n"

        "6. The CRC is attached to the original data "
        "to form the transmitted frame.\n\n"

        "7. At the receiver, the complete frame is "
        "divided again by the same generator.\n\n"

        "8. If the remainder is all zeros, "
        "no error is detected.\n\n"

        "9. If the remainder is not zero, "
        "an error is detected.\n\n"

        "This application also allows transmission "
        "errors to be simulated by changing one or "
        "more bits in the transmitted frame."
    )

    text = tk.Label(
        help_window,
        text=explanation,
        font=("Arial", 11),
        justify="left",
        anchor="w"
    )

    text.pack(
        padx=30,
        pady=10,
        fill="both",
        expand=True
    )


# ============================================================
# CLEAR EVERYTHING
# ============================================================

def clear_all():

    global original_transmitted_frame

    original_transmitted_frame = ""

    data_entry.delete(
        0,
        tk.END
    )

    generator_entry.delete(
        0,
        tk.END
    )

    received_entry.delete(
        0,
        tk.END
    )

    crc_result.config(
        text="---"
    )

    transmitted_result.config(
        text="---"
    )

    error_info_label.config(
        text="Error Position(s): ---"
    )

    result_label.config(
        text="Result: ---"
    )

    status_label.config(
        text="Ready."
    )

    frame_length_label.config(
        text="Frame Length: ---"
    )

    error_type_var.set(
        "Single Bit Error"
    )


# ============================================================
# MAIN WINDOW
# ============================================================

window = tk.Tk()

window.title(
    "CRC Error Detection System"
)

window.geometry(
    "750x900"
)

window.resizable(
    False,
    False
)


# Store transmitted frame
original_transmitted_frame = ""


# ============================================================
# TITLE
# ============================================================

title = tk.Label(
    window,
    text="CRC Error Detection System",
    font=("Arial", 22, "bold")
)

title.pack(
    pady=15
)


subtitle = tk.Label(
    window,
    text="Cyclic Redundancy Check - Error Detection",
    font=("Arial", 11)
)

subtitle.pack(
    pady=(0, 10)
)


# ============================================================
# SENDER SECTION
# ============================================================

sender_label = tk.Label(
    window,
    text="SENDER",
    font=("Arial", 16, "bold")
)

sender_label.pack(
    pady=5
)


# Data

data_label = tk.Label(
    window,
    text="Enter Data Bits:",
    font=("Arial", 12)
)

data_label.pack()


data_entry = tk.Entry(
    window,
    width=55,
    font=("Arial", 12)
)

data_entry.pack(
    pady=4
)


# Generator

generator_label = tk.Label(
    window,
    text="Enter Generator Polynomial:",
    font=("Arial", 12)
)

generator_label.pack(
    pady=(8, 0)
)


generator_entry = tk.Entry(
    window,
    width=55,
    font=("Arial", 12)
)

generator_entry.pack(
    pady=4
)


# CRC result

crc_label = tk.Label(
    window,
    text="CRC Remainder:",
    font=("Arial", 12)
)

crc_label.pack(
    pady=(8, 0)
)


crc_result = tk.Label(
    window,
    text="---",
    font=("Arial", 14, "bold")
)

crc_result.pack(
    pady=3
)


# Transmitted frame

transmitted_label = tk.Label(
    window,
    text="Transmitted Frame:",
    font=("Arial", 12)
)

transmitted_label.pack(
    pady=(5, 0)
)


transmitted_result = tk.Label(
    window,
    text="---",
    font=("Arial", 14, "bold"),
    wraplength=650
)

transmitted_result.pack(
    pady=3
)


frame_length_label = tk.Label(
    window,
    text="Frame Length: ---",
    font=("Arial", 10)
)

frame_length_label.pack(
    pady=2
)


# ============================================================
# SENDER BUTTONS
# ============================================================

button_frame = tk.Frame(
    window
)

button_frame.pack(
    pady=8
)


generate_button = tk.Button(
    button_frame,
    text="Generate CRC",
    font=("Arial", 11, "bold"),
    width=16,
    command=generate_crc
)

generate_button.grid(
    row=0,
    column=0,
    padx=5
)


steps_button = tk.Button(
    button_frame,
    text="CRC Steps",
    font=("Arial", 11),
    width=16,
    command=show_crc_steps
)

steps_button.grid(
    row=0,
    column=1,
    padx=5
)


help_button = tk.Button(
    button_frame,
    text="How CRC Works",
    font=("Arial", 11),
    width=16,
    command=show_how_crc_works
)

help_button.grid(
    row=0,
    column=2,
    padx=5
)


clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 11),
    width=16,
    command=clear_all
)

clear_button.grid(
    row=0,
    column=3,
    padx=5
)


# ============================================================
# RECEIVER SECTION
# ============================================================

receiver_label = tk.Label(
    window,
    text="RECEIVER",
    font=("Arial", 16, "bold")
)

receiver_label.pack(
    pady=(10, 5)
)


received_label = tk.Label(
    window,
    text="Received Frame:",
    font=("Arial", 12)
)

received_label.pack()


received_entry = tk.Entry(
    window,
    width=55,
    font=("Arial", 12)
)

received_entry.pack(
    pady=4
)


# ============================================================
# ERROR TYPE
# ============================================================

error_type_label = tk.Label(
    window,
    text="Select Error Type:",
    font=("Arial", 11)
)

error_type_label.pack(
    pady=(5, 2)
)


error_type_var = tk.StringVar()

error_type_var.set(
    "Single Bit Error"
)


error_type_menu = tk.OptionMenu(
    window,
    error_type_var,
    "No Error",
    "Single Bit Error",
    "Multiple Bit Error",
    "Random Error"
)

error_type_menu.config(
    width=20
)

error_type_menu.pack(
    pady=3
)


# ============================================================
# RECEIVER BUTTONS
# ============================================================

receiver_button_frame = tk.Frame(
    window
)

receiver_button_frame.pack(
    pady=5
)


copy_button = tk.Button(
    receiver_button_frame,
    text="Copy Transmitted Frame",
    font=("Arial", 10),
    width=22,
    command=copy_frame
)

copy_button.grid(
    row=0,
    column=0,
    padx=5
)


error_button = tk.Button(
    receiver_button_frame,
    text="Introduce Error",
    font=("Arial", 10, "bold"),
    width=18,
    command=introduce_error
)

error_button.grid(
    row=0,
    column=1,
    padx=5
)


# Error positions

error_info_label = tk.Label(
    window,
    text="Error Position(s): ---",
    font=("Arial", 11, "bold")
)

error_info_label.pack(
    pady=4
)


# Verify

verify_button = tk.Button(
    window,
    text="Verify CRC",
    font=("Arial", 11, "bold"),
    width=18,
    command=verify_crc
)

verify_button.pack(
    pady=5
)


# ============================================================
# RESULT
# ============================================================

result_label = tk.Label(
    window,
    text="Result: ---",
    font=("Arial", 14, "bold")
)

result_label.pack(
    pady=5
)


status_label = tk.Label(
    window,
    text="Ready.",
    font=("Arial", 10)
)

status_label.pack(
    pady=3
)


# ============================================================
# START APPLICATION
# ============================================================

window.mainloop()