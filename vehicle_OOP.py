"""
   Name: Vehicle_OOP.py
   Author: Juan Ardon
   Created: 5/10/2023
   Purpose: Demostrate 4 attributes, 4 methods and user input
"""
# Import vehicle module
import vehicle

# Import Console fro console printing
from rich.console import Console

# Import Panel for title displays
from rich.panel import Panel

# Initialize rich.console
console = Console()

def main():
    # Create a title
    console.print(
        Panel.fit(
        " ------- Joe's Trip -------  ",
        style="bright_green",
        subtitle="Created by Juan Ardon")
    )
    # Get user input 
    # Add color just to the questions
    print()
    name = console.input("[blue] Enter driver name: [/blue]")
    color = console.input("[blue] What color is your car: [/blue]")
    model = console.input("[blue] What model is your car: [/blue]")
    year = console.input("[blue] What year is your car: [/blue]")
    # Let the user know that the speed must be no greater than 200mph.
    console.print("[red]|NOTE: The maximum speed should not be more than 200mph.| [/red]")
    speed = int(console.input("[blue] Maximun Speed: [/blue]"))

    # Create an Objects
    vehicle_speed = vehicle.Vehicle(color, speed, name,  model, year)
    print()
    # Display a message showing the maximun speed of the vehicle
    console.print(f"[bright_white] The {vehicle_speed.get_color()} vehicle maximum speed is {vehicle_speed.get_speed()} mph. [/bright_white]")
    print()

    # Create a still_running
    still_runnig = "z"

    # Create a loop
    while still_runnig == "z":
        # Get user input
        # Add a different color to each section
        user_choice = console.input("[magenta] | (S) tart [/magenta] [cyan] | (A)ccelerate [/cyan] [yellow] | (B)rake [/yellow] [red] | (P)emergency Stop [/red] [bright_black] |  E(x)it: [/bright_black]")
        # Use a decision making for each input instantance according to user_choice 
        if user_choice == "S":
           vehicle_speed.start()
           # Print the user choice with the color according to the section he/she chooses. 
           console.print(f"[magenta] The {vehicle_speed.get_color()} vehicle speed is starting at {vehicle_speed.get_speed()} mph. [/magenta]")
           print()
        # Use a decision making for each input instantance according to user_choice # Use a decision making for each input instantance according to user_choice 
        elif user_choice == "A":
            vehicle_speed.accelerate()
            # Print the user choice with the color according to the section he/she chooses.
            console.print(f"[cyan] The {vehicle_speed.get_color()} vehicle is going at {vehicle_speed.get_speed()} mph. [/cyan]")
            print()
        # Use a decision making for each input instantance according to user_choice 
        elif user_choice == "B":
            vehicle_speed.brake()
            # Print the user choice with the color according to the section he/she chooses.
            console.print(f"[yellow] The {vehicle_speed.get_color()} vehicle decrease velocity and is going at {vehicle_speed.get_speed()} mph. [/yellow]")
            print()
        # Use a decision making for each input instantance according to user_choice 
        elif user_choice =="P":
            vehicle_speed.stop()
            # Print the user choice with the color according to the section he/she chooses.
            console.print(f"[red] The {vehicle_speed.get_color()} vehicle has an emergency stop which the current velocity is {vehicle_speed.get_speed()} mph. [/red]")
            print()
        # Use a decision making to exit the loop
        else:
            still_runnig = "y"
    
# If a standalone program, call the main fuction
# Else, use as a module
if __name__ == "__main__":
    main()