import googlemaps
import pandas as pd
import tsman, time, json

API_KEY = 'AIzaSyD0H_G1JKCgklUtvDFVcdoMtto3ooyalZ8'
MODE = 'driving'
gmaps = googlemaps.Client(key=API_KEY)
address_column = "Addresses"

def get_directions(origin, destination, waypoints):

	return gmaps.directions(origin = origin, destination = destination,
		waypoints = waypoints, mode = MODE)


def get_distances(origins, destinations):

	results = gmaps.distance_matrix(origins = origins,
		destinations = destinations,
		mode = MODE)

	return results

def read_file(input_filename):
	data = pd.read_csv(input_filename, encoding='utf8')
	return data[address_column].tolist()

def main():
	addresses = read_file("input.csv")
	print(addresses)

	distance_matrix = get_distances(addresses, addresses)
	print(distance_matrix)


	furthest_points = tsman.furthest_pair_default_order(distance_matrix)
	print(furthest_points)

	directions = get_directions(origin = furthest_points['start'], destination = furthest_points['end'],
		waypoints = furthest_points['waypoints'])
	print(len(directions[0]['legs']))
	return

if __name__ == '__main__':
	main()




