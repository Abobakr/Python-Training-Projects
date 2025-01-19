import random
import time
import winsound
from colorama import Fore, Back, Style

# Instead of using if and elif
status = {
    "0": " is open ✅️🚧",
    "1": " is closed ⛔🚧"
}

# CONSTANTS
FREQ = 2500  # Set Frequency To 2500 Hertz
DUR = 1000  # Set Duration To 1000 ms == 1 second

WIND_MAX_DIF = 10
PASS_MAX_DIF = 5

CLOSE_SPEED = 50

# MIN_PASS_TIME = 5  # BRIDGE_DISTANCE / MAX_SPEED = 100/20
MAX_PASS_TIME = 10  # BRIDGE_DISTANCE / MIN_SPEED = 100/10


class Bridge:

    def __init__(self):
        # Inputs
        self.s1_wind_spd = 0
        self.s2_wind_spd = 0
        self.s1_pass_cnt = 0
        self.s2_pass_cnt = 0
        # Outputs
        self.g1_entry = '0'
        self.g1_exit = '0'
        self.g2_entry = '0'
        self.g2_exit = '0'

    def close_entries(self):
        self.g1_entry = '1'
        self.g2_entry = '1'

    def close_exits(self):
        self.g1_exit = '1'
        self.g2_exit = '1'

    def open_entries(self):
        self.g1_entry = '0'
        self.g2_entry = '0'

    def open_exits(self):
        self.g1_exit = '0'
        self.g2_exit = '0'

    def read_wind_sensors(self):
        self.s1_wind_spd = random.randint(5, 50)
        print(f"🌬️💨 Wind speed from sensor 1 = {self.s1_wind_spd}")
        self.s2_wind_spd = self.s1_wind_spd + random.randint(0, 11)  # random.randint(14, 55)
        print(f"🌬️💨  ️Wind speed from sensor 2 = {self.s2_wind_spd}")

    def read_pass_sensors(self):
        self.s1_pass_cnt += round(random.random())
        print(f"🚗🚙 Count of passes from side 1 = {self.s1_pass_cnt}")
        self.s2_pass_cnt += round(random.random())
        print(f"🚗🚙 Count of passes from side 2 = {self.s2_pass_cnt}")

    def describe_status(self):
        print(f"🌉⬅️ Gate-1 entry {status[self.g1_entry]}")
        print(f"⬅️🌉 Gate-1 exit {status[self.g1_exit]}")
        print(f"➡️🌉 Gate-2 entry {status[self.g2_entry]}")
        print(f"🌉➡️ Gate-2 exit {status[self.g2_exit]}")

    @staticmethod
    def send_alert(is_urgent, msj):
        winsound.Beep(FREQ, DUR)
        if is_urgent:
            print(Fore.RED + Back.WHITE + msj)
        else:
            print(Fore.LIGHTYELLOW_EX + Back.WHITE + msj)
        print(Style.RESET_ALL)


def main():
    print("Welcome to our automated suspension bridge 🥳🥳🥳")
    b1 = Bridge()

    b1.describe_status()
    b1.read_wind_sensors()
    b1.read_pass_sensors()

    while abs(b1.s1_wind_spd - b1.s2_wind_spd) <= WIND_MAX_DIF:
        if b1.s1_wind_spd >= CLOSE_SPEED or b1.s2_wind_spd >= CLOSE_SPEED:
            b1.close_entries()
            b1.send_alert(False, "⚠️ALERT !!! 🌀 Possible storm is detected...⛔🚧 Entries are closed...\n"
                                 f"⏱️ Exists will be closed after {MAX_PASS_TIME} sec")
            time.sleep(MAX_PASS_TIME)
            if b1.s1_pass_cnt == b1.s2_pass_cnt:
                b1.close_exits()
            elif abs(b1.s1_pass_cnt - b1.s2_pass_cnt) <= PASS_MAX_DIF:
                b1.send_alert(True, "🚨 ALERT !!! Stopped vehicles on bridge are detected.🚁 Call rescue teams")
            else:
                b1.send_alert(False, "⚠️ ALERT !!! Passing sensor failure is detected.🛠️️ Call maintenance staff")
                b1.close_exits()
        else:
            b1.open_entries()
            b1.open_exits()

        b1.describe_status()
        b1.read_wind_sensors()
        b1.read_pass_sensors()
    # While not then:
    b1.send_alert(True, "🚨🚨🚨 ALERT !!! Wind sensor failure is detected...🛠️ Call maintenance staff"
                        "\n🖥️ System is taking precautions ✋🏻🛑⛔️️")
    b1.close_entries()
    b1.open_exits()
    b1.describe_status()


if __name__ == "__main__":
    main()
