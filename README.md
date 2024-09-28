
# OTP Bomb

This Python script sends multiple OTP requests to specific phone numbers through two different services: Yogo and IdeaBiz. It's designed for demonstration purposes and should not be used maliciously.

## Features

- Sends OTP requests to a given phone number using Yogo and IdeaBiz services.
- Allows the user to input the number of requests and the delay between each request.
- Displays a dynamic update of the number of requests made during execution.
- At the end of execution, it provides a summary of total requests sent to each service and a combined total.

## How the Code Works

The script takes a mobile number as input along with the number of OTP requests (`count`) and delay time (`delay`) between each request. The script then calls two APIs:

1. **Yogo API**: Sends an OTP request to the Yogo service.
2. **IdeaBiz API**: Sends an OTP request to the IdeaBiz service.

It dynamically updates the number of attacks (requests) for each service and shows the total number of attacks during the process. At the end, the script provides a final summary.

### Key Functions

- **spm()**: Sends an OTP request to Yogo's API and increments the Yogo attack counter.
- **spm1()**: Sends an OTP request to IdeaBiz's API and increments the IdeaBiz attack counter.

The counters for each service are updated and printed in real time as the script runs.

## Requirements

- Python 3.x
- `requests` library (for handling HTTP POST requests)

You can install the required library using:
```bash
pip install requests
```

## How to Clone and Run the Project

### Step 1: Clone the Repository

To get started, clone the repository from GitHub:

```bash
git clone https://github.com/DrkCyph7/otp-bomb.git
```

### Step 2: Navigate to the Project Directory

Once the repository is cloned, navigate into the project directory:

```bash
cd otp-bomb
```

### Step 3: Install Required Libraries

Ensure you have the required `requests` library installed. Run the following command in your terminal:

```bash
pip install -r requirements.txt
```

Alternatively, if `requirements.txt` doesn't exist, you can directly install `requests`:

```bash
pip install requests
```

### Step 4: Run the Script

Run the Python script using the following command:

```bash
python otp_bomb.py
```

### Step 5: Provide Input

Once the script starts, it will ask for the following inputs:
1. **Mobile Number**: Enter the mobile number in the format starting with `0` (e.g., `07xxxxxxxx`).
2. **Count**: The number of OTP requests you want to send.
3. **Delay**: The delay (in seconds) between each request.

The script will then start sending OTP requests and update the status dynamically.

## Example

```bash
>> Enter Mobile number with 0: 07xxxxxxxx
>> Count: 5
>> Delay: 1
Attacks            - 10

Summary:
Yogo Attacks: 5
IdeaBiz Attacks: 5
Total Attacks: 10
```

## Disclaimer

This script is for educational purposes only. Misuse of this script for illegal activities such as harassing individuals with repeated OTP requests is strictly prohibited. The author takes no responsibility for any harm caused by using this script inappropriately.
