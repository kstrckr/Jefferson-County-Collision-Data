import csv

class AccidentReport:
    '''Represents an individual self report and parses the data'''

    @staticmethod
    def parse_row(row):
        for element in enumerate(row):

            row[element[0]] = element[1].strip()

            if element[1] == '':
                row[element[0]] = None

            if element[1].lower() == 'y':
                row[element[0]] = True

            if element[1].lower() == 'n':
                row[element[0]] = False
                
        return row


    master_file_number = None
    investigating_agency = None
    local_code = None
    collision_status_code = None
    county_name = None
    roadway_number = None
    block_or_house_number = None
    roadway_name = None
    roadway_suffix = None
    roadway_dir_code = None
    latitude = None
    longitude = None
    milepoint_derived = None
    collision_date = None
    collision_time = None
    intersection_roadway_number = None
    intersection_roadway_name = None
    intersection_roadway_sfx = None
    between_st_roadway_num_1 = None
    between_st_roadway_name_1 = None
    between_st_roadway_sfx_1 = None
    between_st_roadway_num_2 = None
    between_st_roadway_name_2 = None
    between_st_roadway_sfx_2 = None
    units_involved = None
    motor_vehicles_involved = None
    killed = None
    injured = None
    weather_code = None
    weather = None
    roadway_condition_code = None
    roadway_condition = None
    hit_and_run_indication = None
    roadway_type_code = None
    roadway_type = None
    directional_analysis_code = None
    directional_analysis = None
    manner_of_collision_code = None
    manner_of_collision = None
    roadway_character_code = None
    roadway_character = None
    light_condition_code = None
    light_condition = None
    ramp_from_roadway_id = None
    ramp_to_roadway_id = None
    secondary_collision_indicator = None

    def return_insert_tuple(self):
        crash_insertable_values = (
            self.master_file_number,
            self.investigating_agency,
            self.local_code,
            self.collision_status_code,
            self.county_name,
            self.roadway_number,
            self.block_or_house_number,
            self.roadway_name,
            self.roadway_suffix,
            self.roadway_dir_code,
            self.latitude,
            self.longitude,
            self.milepoint_derived,
            self.collision_date,
            self.collision_time,
            self.intersection_roadway_number,
            self.intersection_roadway_name, 
            self.intersection_roadway_sfx,
            self.between_st_roadway_num_1,
            self.between_st_roadway_name_1,
            self.between_st_roadway_sfx_1,
            self.between_st_roadway_num_2,
            self.between_st_roadway_name_2,
            self.between_st_roadway_sfx_2,
            self.units_involved,
            self.motor_vehicles_involved,
            self.killed,
            self.injured,
            self.weather_code,
            self.weather,
            self.roadway_condition_code,
            self.roadway_condition,
            self.hit_and_run_indication,
            self.roadway_type_code,
            self.roadway_type,
            self.directional_analysis_code,
            self.directional_analysis,
            self.manner_of_collision_code,
            self.manner_of_collision,
            self.roadway_character_code,
            self.roadway_character,
            self.light_condition_code,
            self.light_condition,
            self.ramp_from_roadway_id,
            self.ramp_to_roadway_id,
            self.secondary_collision_indicator)
    
        return crash_insertable_values

    def __init__(self, input_row):

        parsed_row = self.parse_row(input_row)

        self.master_file_number = int(parsed_row[0])
        self.investigating_agency = parsed_row[1]
        self.local_code = parsed_row[2]
        self.collision_status_code = parsed_row[3]
        self.county_name = int(parsed_row[4])
        self.roadway_number = parsed_row[5]
        self.block_or_house_number = parsed_row[6]
        self.roadway_name = parsed_row[7]
        self.roadway_suffix = parsed_row[8]
        self.roadway_dir_code = parsed_row[9]

        if parsed_row[10]:
            self.latitude = float(parsed_row[10])
        if parsed_row[11]:
            self.longitude = float(parsed_row[11])
        if parsed_row[12]:
            self.milepoint_derived = float(parsed_row[12])

        self.collision_date = parsed_row[13]

        if parsed_row[14]:
                self.collision_time = int(parsed_row[14])

        self.intersection_roadway_number = parsed_row[15]
        self.intersection_roadway_name = parsed_row[16]
        self.intersection_roadway_sfx = parsed_row[17]
        self.between_st_roadway_num_1 = parsed_row[18]
        self.between_st_roadway_name_1 = parsed_row[19]
        self.between_st_roadway_sfx_1 = parsed_row[20]
        self.between_st_roadway_num_2 = parsed_row[21]
        self.between_st_roadway_name_2 = parsed_row[22]
        self.between_st_roadway_sfx_2 = parsed_row[23]

        self.units_involved = int(parsed_row[24])
        self.motor_vehicles_involved = int(parsed_row[25])
        self.killed = int(parsed_row[26])
        self.injured = int(parsed_row[27])

        if parsed_row[28]:
            self.weather_code = int(parsed_row[28])

        self.weather = parsed_row[29]

        if parsed_row[30]:
            try:
                self.roadway_condition_code = int(parsed_row[30])
            except ValueError:
                # 3 rows have a code value of '+ ' and None for condition
                pass
            
        self.roadway_condition = parsed_row[31]
        self.hit_and_run_indication = parsed_row[32]
        
        if parsed_row[33]:
            self.roadway_type_code = int(parsed_row[33])

        self.roadway_type = parsed_row[34]

        if parsed_row[35]:
            self.directional_analysis_code = int(parsed_row[35])
        self.directional_analysis = parsed_row[36]

        if parsed_row[37]:
            self.manner_of_collision_code = int(parsed_row[37])

        self.manner_of_collision = parsed_row[38]

        if parsed_row[39]:
            self.roadway_character_code = int(parsed_row[39])

        self.roadway_character = parsed_row[40]

        if parsed_row[41]:
            self.light_condition_code = int(parsed_row[41])

        self.light_condition = parsed_row[42]
        self.ramp_from_roadway_id = parsed_row[43]
        self.ramp_to_roadway_id = parsed_row[44]
        self.secondary_collision_indicator = parsed_row[45]
 

if __name__ == "__main__":
    crash_list = []
    crash_objects = []

    with open('JEFFERSON COUNTY_CRASH DATA_2010-2017.csv') as crash_csv:
        crash_reader = csv.reader(crash_csv)


        for line in crash_reader:
            crash_list.append(line)

    # for header in enumerate(crash_list[0]):
    #     print(header[0], header[1], crash_list[-1][header[0]])

    for self in crash_list[1:]:
        crash_objects.append(AccidentReport(self))

    def print_single_crash_details(self):
        for k, v in vars(self).items():
            print(k, v)

    print_single_crash_details(crash_objects[30000])
