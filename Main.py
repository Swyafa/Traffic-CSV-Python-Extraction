

from graphics import *
import csv
import math



data_list = []   #An empty list to load and hold data from csv file 
# TASK (A) USER INPUT DD MM YYYY 8 Marks (Challenge look for months with days less than 31 and try and solve it) Feb, April, June, September, November
def data_info():
    while True: # Ensure question repeated when input incorrect
        try:
            day =int(input("Please enter the day between 1 - 31.\n"))
            if 1 <=day<= 31:
                break
            else:
                print("Value is not between 1 and 31.")
        except ValueError:
            print("Please enter a Day number.")
            
    # MONTH
    while True:
        try:
            month = int(input("Please enter the month between 1 - 12.\n"))
            if 1 <= month <= 12:
                break
            else:
                print("\nMonth value is not between 1 and 12")
        except ValueError:
            print("Please enter a Month number.")

     # YEAR
    while True:
        try:
            year = int(input("Please enter the year between 2000 and 2024.\n"))
            if 2000<=year<=2024:
                break
            else:
                print("Year not in range\n")
        except ValueError:
            print("Please enter a Year Number.")

    return day, month, year # Returning allows me to use it as global variable

def load_csv_data(day, month, year): # returned outputs defined into this function
    csv_filename = f"traffic_data{day:02}{month:02}{year}.csv" # Padds the string var dd,mm and yy, stores the file name 
    try:
        with open(csv_filename, "r") as csv_file: # From CW template 
            csvreader = csv.reader(csv_file) 
            header = next(csvreader) # Header gets skipped 
            for row in csvreader:
                data_list.append(row) # Appending adds to the data_list 
    except FileNotFoundError:
        print("The CSV file entered doesn't exist")
        return None 
# data_list would give me all items in the rows 

def calculations(day,month,year):
    output = "" # To store data for text file
    for i in range(0, 50): # prints separator 
        print("*", end='')
    print() 
    print(f"Date processed for {day}/{month}/{year}")
    # Total Vehicles
    output += f"The total number of vehciels recorded for this date is {len(data_list)}\n"
    
    # Total Number Of Trucks
    truck = 0
    for line in data_list: # This loops all the lines in the reader 
        if line[8] == "Truck": # Reference from Corey Schafer if line has that value 
            truck+=1
    output += f"The total number of trucks recorded for this date is {truck}\n" 
    
    # Total Number Of Electric Vehicles
    electric = 0
    for line in data_list:
        if line[9] == "True":
            electric+=1
    output += f"The total number of electric vehicles recorded is {electric}\n"

    # Total Two-Wheeled Vehciles
    two_wheeled = 0
    for line in data_list:
        if line[8] == "Scooter":
            two_wheeled +=1
        elif line[8] == "Bicycle":
            two_wheeled +=1
        elif line[8] == "Motorcycle":
            two_wheeled +=1
    output += f"The total number of two-wheeled vehicles for this date is {two_wheeled}\n"

    # Bus Passing Through Junction North Elm/Rabbit
    bus_north = 0
    for  line in data_list:
        if line[0] == "Elm Avenue/Rabbit Road":
              if line[4]  == "N":
                  if line[8] == "Buss":
                      bus_north +=1
    output += f"The total number of Busses leaving Elm Avenue/Rabbit Road heading north is {bus_north}\n"

    # Total Vehicles Passing Both Junctions without Turning left or right
    straight= 0
    for line in data_list:
              if line[3] == line[4]:
                  straight +=1
    
    output += f"The total number of vehicles through both junctions not turning left or right is {straight}\n"
        
    # Percentage of trucks
    total_vehicles = int(len(data_list))
    try:
        per_truck = round((truck/total_vehicles)*100,0)
        output += f"The Percentage of total vehicles that are trucks for this date is {per_truck}%\n"
    except ZeroDivisionError:
        output += "There are no Trucks present\n"

    # Average Bikes per hour 
    bike = 0
    for line in data_list:
        if line[8] == "Bicycle":
            bike +=1
        
    hour = 0
    for line in data_list:
        num = int(line[2][0:2])
    for i in range(num):
        if num > num -1:
            hour +=1
    average_bike_per_hour = math.floor(bike/hour) # W3SCHOOLS used because you can't have an extra bike 
    output += f"The average number of Bikes per hour for this date is {average_bike_per_hour} \n"

    # Total number of Vehicles over Speed Limit
    speed_limit = 0
    for line in data_list:
        z = int(line[7])
        if line[6] == "30":
            if z > 30:
                speed_limit +=1
        if line[6] == "20":
            if z > 20:
                speed_limit +=1
    output += f"The total number of vehicles recorded over the speed limit for this date is  {speed_limit}\n"


    # Total number of vehicles through elm/rabbit road
    elm_vehicles = 0
    for line in data_list:
        if line[0] == "Elm Avenue/Rabbit Road":
            elm_vehicles +=1
    output += f"The total number of vehicles that are passing through Elm Avenue/Rabbit Road junction is {elm_vehicles}\n"

    # Total Number of vehicles through only HanleyHighway/Westway
    hanley_vehicles = 0 
    for line in data_list:
        if line[0] == "Hanley Highway/Westway":
            hanley_vehicles +=1
    output += f"The total number of Vehicles that are passing through only Hanley Highway/Westway junction is {hanley_vehicles}\n"
   
    # Percentage of scooters
    scoot = 0
    elm=0
    for line in data_list:
        if line[0] == "Elm Avenue/Rabbit Road":
            elm+=1
            if line[8] == "Scooter":
                scoot +=1
    per_scoot = math.floor((scoot/elm)*100)
    output += f"{per_scoot}% of vehicles recorded through Elm Avenue/Rabbit Rd were scooters \n"
    
        
    #Elm Ave Vehciles per hour histo
    ea_hour_count = {}
    for line in data_list:
        if line[0] == "Elm Avenue/Rabbit Road":
            hour_1 = line[2][:2]
            if hour_1 in ea_hour_count:
                ea_hour_count[hour_1] +=1
            else:
                ea_hour_count[hour_1] = 1

    """print(ea_hour_count)"""
    
    # Highway Hanley Vehicles per hour
    han_hour_count = {} # Empty Dictionary Holds Count/ intialises 
    for line in data_list: # itereates through data_list
        if line[0] == "Hanley Highway/Westway":
            hour = line[2][:2] # Extractd hour from the list
            if hour in han_hour_count:
                han_hour_count[hour] +=1 # Checks hour in dictionary. If not present 1 is assigned to hour. So everytime it goes down the list and finds that same number now, it adds 1 to it
            else:
                han_hour_count[hour] = 1

    # Highest number of vehicles on Hanley Highway
    max_vehicles = max(han_hour_count.values(), default=0) # Max() returns max number for example |5:8|,|2:9|,|4:10|. hour 8 had 5 vehicles therefore 5 will be returned
    """print(han_hour_count)"""
    busiest_hours = []
    for hour, count in han_hour_count.items(): # iterates through pair items in hour_count
        if count == max_vehicles:
            busiest_hours.append(hour)
    start = int(busiest_hours[0])
    end = start + 1 
    
    output += f"The highest number of vehicles in an hour on Hanley Highway/Westway is {max_vehicles}\n"
    output += f"The most vehicles through Hanley Highway/Westway were recorded between {start}:00 and {end}:00\n"

# The hours that it rained 
    rain_hour= {} # EMPTY DICTIONARY
    for line in data_list:
        hour = line[2][:2] # Stores the hours only 
        rain = line[5].lower() # Turns the everything lower case as in csv file its Rain
        if "rain" in rain:
            if hour in rain_hour: #If rain word present and if hour present in empty set we increment by 1  
                rain_hour[hour] +=1
            else:
                rain_hour[hour] =1 # hour dictionary to 1 

    output += f"The number of hours of rain is {len(rain_hour)}\n" # Len(), could've done num_rain_hours = 0  
    

    def window(day,month,year):
        win = GraphWin("Program", 1680, 600)
        # Title
        message = Text(Point(400, 20), f"HISTOGRAM OF VEHICLE FREQUENCY PER HOUR FOR DATE {day}/{month}/{year}")
        message.setFace("helvetica")
        message.setSize(17)
        message.setTextColor("#280137")
        message.draw(win)

    # Key for Elm Avenue/Rabbit Road
        key_text = Text(Point(200, 50), "Elm Avenue/Rabbit Road")
        key_text.setTextColor("#280137")
        key_text.draw(win)
    
        key_rect = Rectangle(Point(100, 30), Point(70, 60))  # Small colored rectangle
        key_rect.setFill("#9e0200")  # Elm Avenue color
        key_rect.setOutline("black")
        key_rect.draw(win)

    # Key for Hanley Highway/Westway
        key_text_2 = Text(Point(200, 90), "Hanley Highway/Westway")
        key_text_2.setTextColor("#280137")
        key_text_2.draw(win)
    
        key_rect_2 = Rectangle(Point(70, 100), Point(100, 70))  # Small colored rectangle
        key_rect_2.setFill("#191970")  # Hanley Highway color
        key_rect_2.setOutline("black")
        key_rect_2.draw(win)

    # Base Line
        bL = Line(Point(90, 500), Point(1520, 500))
        bL.setOutline("#280137")
        bL.setWidth(3)
        bL.draw(win)

    # X-Axis Numbers
        hours = Text(Point(810,520),"00               01                02                03             04               05            06          07              08              09               10           11         12          13         14            15           16           17         18          19        20         21        22       23")
        hours.draw(win)
        
        

    # X-Axis Label
        X_Axis = Text(Point(835, 550), "Hours 00:00 to 24:00")
        X_Axis.setTextColor("#280137")
        X_Axis.draw(win)

    #This retrieves the value to be used in Graph
        ea_count_00 = ea_hour_count.get("00",0) # Graphics.py pdf 
        Text(Point(400,200),ea_count_00) 
        

    # EA RECTANGLES and HAN RECTANGLES 
        ea_rec_00 = Rectangle(Point(97,(300-ea_hour_count.get("00",0))),Point(117,500)) # Alter Y1 value to change height, Remain Y2 as 500 base line
        ea_rec_00.setFill("#9e0200")
        ea_rec_00.draw(win)

        han_rec_00 = Rectangle(Point(117,300-han_hour_count.get("00",0)),Point(137,500))
        han_rec_00.setFill("#191970")
        han_rec_00.draw(win)
        
        ea_rec_01 = Rectangle(Point(157,(300-ea_hour_count.get("01",0))),Point(177,500)) 
        ea_rec_01.setFill("#9e0200")
        ea_rec_01.draw(win)

        han_rec_01 = Rectangle(Point(177,(300-han_hour_count.get("01",0))),Point(197,500))
        han_rec_01.setFill("#191970")
        han_rec_01.draw(win)

        ea_rec_02 = Rectangle(Point(217,(300-ea_hour_count.get("02",0))),Point(237,500)) 
        ea_rec_02.setFill("#9e0200")
        ea_rec_02.draw(win)

        han_rec_02 = Rectangle(Point(237,(300-han_hour_count.get("02",0))),Point(257,500))
        han_rec_02.setFill("#191970")
        han_rec_02.draw(win)


        ea_rec_03 = Rectangle(Point(277,(300-ea_hour_count.get("03",0))),Point(297,500)) 
        ea_rec_03.setFill("#9e0200")
        ea_rec_03.draw(win)

        han_rec_03 = Rectangle(Point(297,(300-han_hour_count.get("03",0))),Point(317,500))
        han_rec_03.setFill("#191970")
        han_rec_03.draw(win)

        ea_rec_04 = Rectangle(Point(337,(300-ea_hour_count.get("04",0))),Point(357,500)) 
        ea_rec_04.setFill("#9e0200")
        ea_rec_04.draw(win)

        han_rec_04 = Rectangle(Point(357,(300-han_hour_count.get("04",0))),Point(377,500))
        han_rec_04.setFill("#191970")
        han_rec_04.draw(win)

        ea_rec_05 = Rectangle(Point(397,(300-ea_hour_count.get("05",0))),Point(417,500)) 
        ea_rec_05.setFill("#9e0200")
        ea_rec_05.draw(win)

        han_rec_05 = Rectangle(Point(417,(300-han_hour_count.get("05",0))),Point(437,500))
        han_rec_05.setFill("#191970")
        han_rec_05.draw(win)

        ea_rec_06  = Rectangle(Point(457,(300-ea_hour_count.get("06",0))),Point(477,500)) 
        ea_rec_06.setFill("#9e0200")
        ea_rec_06.draw(win)

        han_rec_06 = Rectangle(Point(477,(300-han_hour_count.get("06",0))),Point(497,500))
        han_rec_06.setFill("#191970")
        han_rec_06.draw(win)

        ea_rec_07 = Rectangle(Point(517,(300-ea_hour_count.get("07",0))),Point(537,500))
        ea_rec_07.setFill("#9e0200")
        ea_rec_07.draw(win)

        han_rec_07 = Rectangle(Point(537,(300-han_hour_count.get("07",0))),Point(557,500))
        han_rec_07.setFill("#191970")
        han_rec_07.draw(win)

        ea_rec_08 = Rectangle(Point(577,(300-ea_hour_count.get("08",0))),Point(597,500)) 
        ea_rec_08.setFill("#9e0200")
        ea_rec_08.draw(win)

        han_rec_08 = Rectangle(Point(597,(300-han_hour_count.get("08",0))),Point(617,500))
        han_rec_08.setFill("#191970")
        han_rec_08.draw(win)

        ea_rec_09 = Rectangle(Point(637,(300-ea_hour_count.get("09",0))),Point(657,500)) 
        ea_rec_09.setFill("#9e0200")
        ea_rec_09.draw(win)

        han_rec_09 = Rectangle(Point(657,(300-han_hour_count.get("09",0))),Point(677,500))
        han_rec_09.setFill("#191970")
        han_rec_09.draw(win)

        ea_rec_10 = Rectangle(Point(697,(300-ea_hour_count.get("10",0))),Point(717,500)) 
        ea_rec_10.setFill("#9e0200")
        ea_rec_10.draw(win)

        

        han_rec_10 = Rectangle(Point(717,(300-han_hour_count.get("10",0))),Point(737,500))
        han_rec_10.setFill("#191970")
        han_rec_10.draw(win)

    # 10 marker

        ea_rec_11 = Rectangle(Point(757,(300-ea_hour_count.get("11",0))),Point(777,500)) 
        ea_rec_11.setFill("#9e0200")
        ea_rec_11.draw(win)

        han_rec_11 = Rectangle(Point(777,(300-han_hour_count.get("11",0))),Point(797,500))
        han_rec_11.setFill("#191970")
        han_rec_11.draw(win)

        ea_rec_12 = Rectangle(Point(817,(300-ea_hour_count.get("12",0))),Point(837,500)) 
        ea_rec_12.setFill("#9e0200")
        ea_rec_12.draw(win)

        han_rec_12 = Rectangle(Point(837,(300-han_hour_count.get("12",0))),Point(857,500))
        han_rec_12.setFill("#191970")
        han_rec_12.draw(win)

        ea_rec_13 = Rectangle(Point(877,(300-ea_hour_count.get("13",0))),Point(897,500)) 
        ea_rec_13.setFill("#9e0200")
        ea_rec_13.draw(win)

        han_rec_13 = Rectangle(Point(897,(300-han_hour_count.get("13",0))),Point(917,500))
        han_rec_13.setFill("#191970")
        han_rec_13.draw(win)
        
        ea_rec_14 = Rectangle(Point(937,(300-ea_hour_count.get("14",0))),Point(957,500)) 
        ea_rec_14.setFill("#9e0200")
        ea_rec_14.draw(win)

        han_rec_14 = Rectangle(Point(957,(300-han_hour_count.get("14",0))),Point(977,500))
        han_rec_14.setFill("#191970")
        han_rec_14.draw(win)

        ea_rec_15 = Rectangle(Point(997,(300-ea_hour_count.get("15",0))),Point(1017,500)) 
        ea_rec_15.setFill("#9e0200")
        ea_rec_15.draw(win)

        han_rec_15 = Rectangle(Point(1017,(300-han_hour_count.get("15",0))),Point(1037,500))
        han_rec_15.setFill("#191970")
        han_rec_15.draw(win)

        ea_rec_16 = Rectangle(Point(1057,(300-ea_hour_count.get("16",0))),Point(1077,500)) 
        ea_rec_16.setFill("#9e0200")
        ea_rec_16.draw(win)

        han_rec_16 = Rectangle(Point(1077,(300-han_hour_count.get("16",0))),Point(1097,500))
        han_rec_16.setFill("#191970")
        han_rec_16.draw(win)

        ea_rec_17 = Rectangle(Point(1117,(300-ea_hour_count.get("17",0))),Point(1137,500)) 
        ea_rec_17.setFill("#9e0200")
        ea_rec_17.draw(win)

        han_rec_17 = Rectangle(Point(1137,(300-han_hour_count.get("17",0))),Point(1157,500))
        han_rec_17.setFill("#191970")
        han_rec_17.draw(win)

        ea_rec_18 = Rectangle(Point(1177,(300-ea_hour_count.get("18",0))),Point(1197,500)) 
        ea_rec_18.setFill("#9e0200")
        ea_rec_18.draw(win)

        han_rec_18 = Rectangle(Point(1197,(300-han_hour_count.get("18",0))),Point(1217,500))
        han_rec_18.setFill("#191970")
        han_rec_18.draw(win)

        ea_rec_19 = Rectangle(Point(1237,(300-ea_hour_count.get("19",0))),Point(1257,500)) 
        ea_rec_19.setFill("#9e0200")
        ea_rec_19.draw(win)

        han_rec_19 = Rectangle(Point(1257,(300-han_hour_count.get("19",0))),Point(1277,500))
        han_rec_19.setFill("#191970")
        han_rec_19.draw(win)

        ea_rec_20 = Rectangle(Point(1297,(300-ea_hour_count.get("20",0))),Point(1317,500)) 
        ea_rec_20.setFill("#9e0200")
        ea_rec_20.draw(win)

        han_rec_20 = Rectangle(Point(1317,(300-han_hour_count.get("20",0))),Point(1337,500))
        han_rec_20.setFill("#191970")
        han_rec_20.draw(win)

        ea_rec_21 = Rectangle(Point(1357,(300-ea_hour_count.get("21",0))),Point(1377,500)) 
        ea_rec_21.setFill("#9e0200")
        ea_rec_21.draw(win)

        han_rec_21 = Rectangle(Point(1377,(300-han_hour_count.get("21",0))),Point(1397,500))
        han_rec_21.setFill("#191970")
        han_rec_21.draw(win)

        ea_rec_22 = Rectangle(Point(1417,(300-ea_hour_count.get("22",0))),Point(1437,500)) 
        ea_rec_22.setFill("#9e0200")
        ea_rec_22.draw(win)

        han_rec_22 = Rectangle(Point(1437,(300-han_hour_count.get("22",0))),Point(1457,500))
        han_rec_22.setFill("#191970")
        han_rec_22.draw(win)

        ea_rec_23 = Rectangle(Point(1477,(300-ea_hour_count.get("23",0))),Point(1497,500)) 
        ea_rec_23.setFill("#9e0200")
        ea_rec_23.draw(win)

        han_rec_23 = Rectangle(Point(1497,(300-han_hour_count.get("23",0))),Point(1517,500))
        han_rec_23.setFill("#191970")
        han_rec_23.draw(win)
        
    window(day,month,year)
    return output

def main():
    while True:
        day, month, year = data_info()
        load_csv_data(day, month, year)
        if data_list:
            output = calculations(day,month,year)
            print(output)
        else:
            print("No data processed. Please check the file and try again.")


        choice = input("Do you want to process another file? (yes/no): ").strip().lower()
        while choice != "yes":
            print("Exiting the program. bye bye!")
            print("Data has been stored")
            try:
                f = open("data.txt",'w')
                f.write(output)
                break
            except UnboundLocalError:
                break
        if choice == "yes":
            data_list.clear()# Also clears for next file 
            main()
             # Clears data so when new csv file is put doesn't affect https://www.w3schools.com/python/ref_list_clear.asp  
        break
    data_list.clear() 

main()


# https://stackoverflow.com/questions/72792619/how-to-print-a-string-from-another-function
# For this i realised i had to have a variable for each result and concacenate them output



#The code below accesses and prints different elements of data_list

'''print(header) # Prints the header of the csv file
print()
print("data_list[2] is ",data_list[2]) # Prints the 3rd row of the csv file
print("data_list[3] is ",data_list[3]) # Prints the 4th row of the csv file
print("data_list[2][9] is ",data_list[6][2]) # Prints the 3rd cell of the 7th row'''
