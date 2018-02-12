
def furthest_pair_default_order(distance_matrix):

	output={}

	for major, row in enumerate(distance_matrix['rows']):
		for minor, pair in enumerate(row['elements']):
			if pair['status'] == 'OK':
				if output.get('distance'):
					if output['distance'] < pair['distance']['value']:
						output['distance'] = pair['distance']['value']
						output['duration'] = pair['duration']['value']
						output['start'] = distance_matrix['origin_addresses'][major]
						output['end'] = distance_matrix['destination_addresses'][minor]
				else:
					output['distance'] = pair['distance']['value']
					output['duration'] = pair['duration']['value']
					output['start'] = distance_matrix['origin_addresses'][major]
					output['end'] = distance_matrix['destination_addresses'][minor]

					set_waypoints(output, distance_matrix['origin_addresses'][:])

	return output

def set_waypoints(output, addresses):
	output['waypoints'] = addresses
	output['waypoints'].remove(output['start'])
	try:
		output['waypoints'].remove(output['end'])
	except ValueError:
		pass