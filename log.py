import time

months = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

def log(log_contents):
    log_file = open("logfile.txt", "a+")

    localtime = time.localtime(time.time())
    
    full_log_message = f"{months[localtime.tm_mon]} {localtime.tm_mday} {localtime.tm_year}: {localtime.tm_hour}:{prepend_zero(localtime.tm_min)} {log_contents}"
    log_file.write(full_log_message + "\n")

    log_file.close()
    print(f"Wrote '{full_log_message}' to logfile.txt")

def prepend_zero(seconds):
    if seconds < 10: return '0' + str(seconds)
    else: return str(seconds)