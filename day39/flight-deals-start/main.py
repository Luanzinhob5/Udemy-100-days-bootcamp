#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from flight_data import FlightData
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch


data_manager = DataManager()
flight_search = FlightSearch()
sheet_data = data_manager.return_data()["prices"]

cities_list = [data["city"] for data in sheet_data if data["iataCode"] == ""]
sheet_data = flight_search.send_iata_code(cities_list=cities_list,sheet_list=sheet_data)

print(data_manager.upgrade_data(sheet_data))
        
