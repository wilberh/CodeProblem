
input_data = [
    "1,10000,40",
    "1,10002,45",
    "1,11015,50",
    "2,10005,42",
    "2,11051,45",
    "2,12064,42",
    "2,13161,42"]


def average_temperature(duration, data):
    sensor_id = list(map(lambda s: int(s.split(',')[0]), data))
    timestamp_in_milliseconds = list(map(lambda s: int(s.split(',')[1]), data))
    temp = list(map(lambda s: int(s.split(',')[2]), data))

    #to store temperature-ranges
    timestamp_temp_ranges = []

    #to store temperature-range and temps
    temp_ranges_and_temps = {}

    #to store temperature-range and averages
    temp_ranges_and_averages = {}

    #creating temperature ranges based on "duration"
    for counter in range(len(sensor_id)):
        #starting temperature ranges, stored as a tuple
        if not timestamp_temp_ranges:
            timestamp_temp_ranges.append((timestamp_in_milliseconds[counter]//duration*1000,timestamp_in_milliseconds[counter]//duration*1000+(duration-1)))

        for timestamp_range in timestamp_temp_ranges:
            if between_range(timestamp_in_milliseconds[counter],list(timestamp_range)):
                continue
            else:
                timestamp_temp_ranges.append((timestamp_in_milliseconds[counter]//duration*1000,timestamp_in_milliseconds[counter]//duration*1000+(duration-1)))

    #removing duplicate and sorting "timestamp_temp_ranges"
    timestamp_temp_ranges = sorted(list(set(timestamp_temp_ranges)))

    #grouping temperatures into their "temp_ranges_and_temps"
    for i in range(len(temp)):
        for timestamp_range in timestamp_temp_ranges:
            if between_range(timestamp_in_milliseconds[i],list(timestamp_range)):
                if timestamp_range in temp_ranges_and_temps:
                    temp_ranges_and_temps[timestamp_range].append(temp[i])
                else:
                    temp_ranges_and_temps[timestamp_range] = [temp[i]]
    
    #calculating temperature average for each temperature range
    for key,value in temp_ranges_and_temps.items():
        temp_ranges_and_averages[key] = sum(value) / float(len(value))
    
    #printing output - temperature range, and average
    for key,value in temp_ranges_and_averages.items():
        print('{}-{}: {}'.format(key[0], key[1], str('{:.2f}'.format(value)).rstrip('.0')))



#evaluating if timestamp from sensor data is within a specific timestamp_range
def between_range(timestamp_in_milliseconds,timestamp_range):
    if timestamp_range[0] <= timestamp_in_milliseconds <= timestamp_range[1]:
        return True
    else:
        return False





average_temperature(1000, input_data)








