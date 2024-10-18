# EKG-EMG Signal Processing with Wavelet Transform

## Overview
This project focuses on processing ECG (Electrocardiogram) signals using a Symlet wavelet transform in Python and collecting raw ECG data from the Olimex EKG/EMG shield. The script preprocesses ECG signals by applying a Stationary Wavelet Transform (SWT), analyzing the variance of the signal and its decomposition levels. Additionally, a Node.js script is included to handle real-time data collection from the Olimex shield, outputting the data in millivolts.

## Dataset Features
The dataset used in this project includes real-time ECG signals collected via the Olimex EKG/EMG Shield. The key features of this dataset are:
- **ECG Signal:** The primary signal collected over a 60-second window at a sampling rate of 256 Hz.
- **Wavelet Decomposition:** Symlet wavelet transformation of the signal, including approximation and detail coefficients.
- **Variance Analysis:** Computation of variance at each decomposition level to analyze the signal's frequency components.

## Project Goals
The main objectives of this project are:
1. **ECG Signal Processing:** To preprocess and analyze ECG signals using wavelet transforms.
2. **Real-time Data Acquisition:** To interface with the Olimex EKG/EMG Shield for collecting raw ECG data.
3. **Variance Computation:** To study the variance across different wavelet decomposition levels for further analysis.
4. **Data Visualization:** To provide visual representation of the original ECG signal and its wavelet-transformed components.

## Tools Used
- **Python Libraries:**
  - `numpy`: For numerical computations, including signal processing and variance calculation.
  - `matplotlib`: For plotting the ECG signal and its decomposition.
  - `pywt`: For performing wavelet transformations on the ECG data.
- **Node.js Libraries:**
  - `serialport`: For interfacing with the Olimex EKG/EMG Shield via serial communication.
  - `fs`: For handling file operations to save ECG data.
  - `os`: For interacting with the operating system to manage file encoding and output.

## How to Use

### Python ECG Signal Processing
1. **Load the ECG Data:**
   Load your ECG data from a file, for example, `einthoven32.txt`, and transpose it to separate the time and signal components.
   ```python
   data = np.loadtxt('./einthoven32.txt').T
   tempo, ecg = data[0], data[1]
   ```

2. **Perform Wavelet Transform:**
    Apply the Symlet wavelet (sym4) using the pywt.swt() function.
    ```python
    coeffs = pywt.swt(ecg, wavelet='sym4', level=3, trim_approx=True, norm=True)
    ```
3. **Analyze and Plot the Results:**
    Plot the original ECG signal, its decomposition, and variance analysis.
    ```python
    plt.plot(ecg)
    plt.legend(['Original signal'])
    fig, axes = plt.subplots(len(coeffs))
    # Continue plotting the wavelet decomposition components
    ```
4. **Run the Script:**
    Use the Python script to load and process ECG data, visualize the decomposition, and analyze the variance.

### Node.js Real-time Data Acquisition

1. **Install Required Packages:**
   - Install the necessary dependencies using npm:
     ```bash
     npm install serialport @serialport/parser-byte-length
     ```

2. **Configure the Serial Port:**
   - Set the serial port and baud rate for your platform:
     - For **Ubuntu**: Use `/dev/ttyACM0`.
     - For **Windows**: Use `COM3` or another appropriate COM port.
     - Adjust the sampling rate and measurement time as needed:
     ```javascript
     var port = "/dev/ttyACM0"; // for Ubuntu
     var baudrate = 57600;
     var samplingRate = 256;
     var measurementTime = 60; // in seconds
     ```

3. **Node.js Script Explanation:**
   - The Node.js script reads real-time data from the Olimex EKG/EMG Shield, processes the data, and saves it to a file (`einthoven3.txt`). The steps involved are:
     - **Serial Communication:**
       - A serial connection is opened using `SerialPort`.
       - Data is received in byte packages, parsed by the `ByteLengthParser` to handle 6-byte packets.
     - **ECG Data Handling:**
       - The incoming byte array is converted to a voltage value (in millivolts) using the Olimex shield's gain and voltage range.
     - **File Saving:**
       - The processed ECG data is saved as a text file where each row contains the timestamp and corresponding millivolt value.

4. **Run the Node.js Script:**
   - Execute the script to start receiving ECG data from the Olimex EKG/EMG Shield and saving it to a file:
     ```bash
     node ecg_acquisition.js
     ```

5. **Key Functions:**
   - **byteArrayToLong(byteArray):** Converts the incoming byte array to a long integer.
   - **convertToMilliVolt(value):** Converts raw ECG data to millivolts based on the Olimex shield's gain and voltage range.
   - **writeToFile(data):** Saves the processed ECG data to a file.
   - **handleData(data):** Processes incoming data, packages it, and saves it when the measurement time has been reached.

6. **Example Output:**
   - The output file will contain rows in the following format:
     ```
     0.0039 0.524
     0.0078 0.527
     0.0117 0.531
     ...
     ```

This allows you to capture real-time ECG data and save it for further processing.
**If you find any errors, improvements or suggestions, please contact us using the links below. Your contribution is greatly appreciated!**

## For More Information
For more information, codes, tutorials, and exciting projects, visit the links below:

- Email: alves_lucasoliveira@usp.br
- GitHub: [cyblx](https://github.com/cyblx)
- LinkedIn: [Cyblx](https://www.linkedin.com/in/cyblx)
