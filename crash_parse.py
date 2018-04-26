import csv

# (0, 'MASTER FILE NUMBER')
# (1, 'INVESTIGATING AGENCY')
# (2, 'LOCAL CODE')
# (3, 'COLLISION STATUS CODE')
# (4, 'COUNTY NAME')
# (5, 'ROADWAY NUMBER')
# (6, 'BLOCK/HOUSE #')
# (7, 'ROADWAY NAME')
# (8, 'ROADWAY SUFFIX')
# (9, 'ROADWAY DIRECTION CODE')
# (10, 'GPS LATITUDE DECIMAL')
# (11, 'GPS LONGITUDE DECIMAL')
# (12, 'MILEPOINT DERIVED')
# (13, 'COLLISION DATE')
# (14, 'COLLISION TIME')
# (15, 'INTERSECTION ROADWAY #')
# (16, 'INTERSECTION ROADWAY NAME')
# (17, 'INTERSECTION ROADWAY SFX')
# (18, 'BETWEEN STREET ROADWAY # 1')
# (19, 'BETWEEN STREET ROADWAY NAME 1')
# (20, 'BETWEEN STREET ROADWAY SFX 1')
# (21, 'BETWEEN STREET ROADWAY # 2')
# (22, 'BETWEEN STREET ROADWAY NAME 2')
# (23, 'BETWEEN STREET ROADWAY SFX 2')
# (24, 'UNITS INVOLVED')
# (25, 'MOTOR VEHICLES INVOLVED')
# (26, 'KILLED')
# (27, 'INJURED')
# (28, 'WEATHER CODE')
# (29, 'WEATHER')
# (30, 'ROADWAY CONDITION CODE')
# (31, 'ROADWAY CONDITION')
# (32, 'HIT & RUN INDICATOR')
# (33, 'ROADWAY TYPE CODE')
# (34, 'ROADWAY TYPE')
# (35, 'DIRECTIONAL ANALYSIS CODE')
# (36, 'DIRECTIONAL ANALYSIS')
# (37, 'MANNER OF COLLISION CODE')
# (38, 'MANNER OF COLLISION')
# (39, 'ROADWAY CHARACTER CODE')
# (40, 'ROADWAY CHARACTER')
# (41, 'LIGHT CONDITION CODE')
# (42, 'LIGHT CONDITION')
# (43, 'RAMP FROM ROADWAY ID')
# (44, 'RAMP TO ROADWAY ID')
# (45, 'SECONDARY COLLISION INDICATOR')

crash_list = []

with open('JEFFERSON COUNTY_CRASH DATA_2010-2017.csv') as crash_csv:
    crash_reader = csv.reader(crash_csv)


    for line in crash_reader:
        crash_list.append(line)

for header in enumerate(crash_list[0]):
    print(header[0], header[1])

class AccidentReport:
    '''Represents an individual crash report and parses the data'''

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


    

    def __init__(self, crash_row):
        pass

