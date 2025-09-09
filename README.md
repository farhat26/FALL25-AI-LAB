import csv
import os

# Create a sample CSV file if it does not exist
if not os.path.exists("rooms_temps.csv"):
    with open("rooms_temps.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Room", "Temperature"])
        writer.writerow(["Living Room", 32])
        writer.writerow(["Bedroom", 34])
        writer.writerow(["Kitchen", 36])

class SimpleReflexAgent:
    def __init__(self, temp):
        self.fixed_temp = temp

    def sensor(self, temp):
        self.current_temp = temp

    def performance(self):
        if self.current_temp > self.fixed_temp:
            return "AC was ON"
        else:
            return "AC was OFF"

    def actuator(self):
        action = self.performance()
        print(f"{self.current_temp} => Action: {action}")

    def check_match(self):
        return self.current_temp == self.fixed_temp


agent = SimpleReflexAgent(34)

with open("rooms_temps.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  

    for row in reader:
        room = row[0]
        temp = int(row[1])
        agent.sensor(temp)
        if agent.check_match(): 
            print(f"{room} : {temp} => Temperature MATCHED with agent")
