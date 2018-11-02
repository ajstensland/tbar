#!/usr/bin/env python3
from datetime import datetime   # To fetch date and time info
from time import sleep          # To sleep between data fetches
import sys
from configparser import ConfigParser
from subprocess import call


COLORS = {  "end"   : "\33[0m",
            "black" : "\33[30m",
            "red"   : "\33[31m",
            "green" : "\33[32m",
            "yellow": "\33[33m",
            "blue"  : "\33[34m",
            "violet": "\33[35m",
            "beige" : "\33[36m",
            "white" : "\33[37m",
            "grey"  : "\33[90m",

            "blackbg" : "\33[40m",
            "redbg"   : "\33[41m",
            "greenbg" : "\33[42m",
            "yellowbg": "\33[43m",
            "bluebg"  : "\33[44m",
            "violetbg": "\33[45m",
            "beigebg" : "\33[46m",
            "whitebg" : "\33[47m",
            "greybg"  : "\33[100m",

            "brightred"   : "\33[91m",
            "brightgreen" : "\33[92m",
            "brightyellow": "\33[93m",
            "brightblue"  : "\33[94m",
            "brightviolet": "\33[95m",
            "brightbeige" : "\33[96m",
            "brightwhite" : "\33[97m",

            "brightredbg"   : "\33[101m",
            "brightgreenbg" : "\33[102m",
            "brightyellowbg": "\33[103m",
            "brightbluebg"  : "\33[104m",
            "brightvioletbg": "\33[105m",
            "brightbeigebg" : "\33[106m",
            "brightwhitebg" : "\33[107m",
            
            "none"      : ""}


class TBar:
    def __init__(self):
        # Load config file
        self.config = ConfigParser()
        self.config.read("tbar.conf")


    def run(self):
        # Until the user uses a keyboard interrupt...
        while True:
            # Display the bar
            self.display()

            # Sleep for specified amount of time
            sleep(int(self.config["OTHER"]["sleeptime"]))

    def display(self):
        print(COLORS[self.config["COLORS"]["default"]] + COLORS[self.config["COLORS"]["defaultbg"]]+ self.config["LAYOUT"]["line1"].replace("'", "").replace("<b>", COLORS["end"]  + self.battery_widget() + COLORS[self.config["COLORS"]["default"]] + COLORS[self.config["COLORS"]["defaultbg"]]).replace("<t>", COLORS["end"] + self.time_widget() + COLORS[self.config["COLORS"]["default"]] + COLORS[self.config["COLORS"]["defaultbg"]]) + COLORS["end"])
        

    def time_widget(self):
        # Create base string to add to
        widget = ""

        # Add raw label to widget with color
        widget += COLORS[self.config["COLORS"]["timelabel"]] + COLORS[self.config["COLORS"]["timelabelbg"]] + self.config["TIME"]["label"].replace("'", "") + COLORS["end"]

        # Add the time color
        widget += COLORS[self.config["COLORS"]["timecontent"]] + COLORS[self.config["COLORS"]["timecontentbg"]]

        # Fetch time data
        current_time = datetime.now()

        # Get hour data
        hour = current_time.hour

        # If the user opted for 12 hour time...
        if not self.config["TIME"].getboolean("24hr"):
            if hour == 0:
                hour = 12
            elif hour > 12:
                hour -= 12

        # Cast hour to string
        hour = str(hour)

        # If the user opted for leading zeroes...
        if self.config["TIME"].getboolean("lead0"):
            if (len(hour) == 1):
                hour = "0" + hour

        # Add the hour to the widget
        widget += hour
        
        # Get minute data
        minute = current_time.minute
        
        # Colon
        widget += ":"

        # Add it to the widget with formatting
        widget += str(minute) if minute > 10 else "0" + str(minute)

        # If the user opted for AM/PM...
        if self.config["TIME"].getboolean("ampm") and not self.config["TIME"].getboolean("24hr"):
            
            # If the user opted for gaps...
            if self.config["TIME"].getboolean("gap"):
                widget += " "
            
            # If the time is in AM...
            if current_time.hour < 12:
                
                if self.config["TIME"].getboolean("periods") and self.config["TIME"].getboolean("caps"):
                    widget += "A.M."
                
                elif self.config["TIME"].getboolean("periods") and not self.config["TIME"].getboolean("caps"):
                    widget += "a.m."

                elif not self.config["TIME"].getboolean("periods") and self.config["TIME"].getboolean("caps"):
                    widget += "AM"

                else:
                    widget += "am"

            else:
                
                if self.config["TIME"].getboolean("periods") and self.config["TIME"].getboolean("caps"):
                    widget += "P.M."
 
                elif self.config["TIME"].getboolean("periods") and not self.config["TIME"].getboolean("caps"):
                    widget += "p.m."

                elif not self.config["TIME"].getboolean("periods") and self.config["TIME"].getboolean("caps"):
                    widget += "PM"

                else:
                    widget += "pm"
       
        # End time color
        widget += COLORS["end"]

        # Return the widget
        return widget

    def battery_widget(self):
        # Create base widget string
        widget = ""

        # Add in the label with color
        widget += COLORS[self.config["COLORS"]["battlabel"]] + COLORS[self.config["COLORS"]["battlabelbg"]] + self.config["BATTERY"]["label"].replace("'", "") + COLORS["end"]

        # Add battery color
        widget += COLORS[self.config["COLORS"]["battcontent"]] + COLORS[self.config["COLORS"]["battcontentbg"]]

        # Get battery data
        with open("/sys/class/power_supply/BAT0/charge_now", "r") as current_file:
            current_batt = int(current_file.readline())

        with open("/sys/class/power_supply/BAT0/charge_full", "r") as full_file:
            full_batt = int(full_file.readline())

        # Calculate battery percentage
        batt_percent = int(current_batt / full_batt * 100)

        # Add to widget
        widget += str(batt_percent) + "%"

        # End color on widget
        widget += COLORS["end"]

        # Return the widget
        return widget
        

if __name__ == "__main__":
    TBar().run()

