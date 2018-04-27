import sqlite3

def db_connection(db_name):
    conn = sqlite3.connect(db_name)
    return conn

def create_crash_table(db_conn):
    table_columns = '''
    master_file_number INTEGER UNIQUE PRIMARY KEY,
    investigating_agency TEXT,
    local_code TEXT,
    collision_status_code TEXT,
    county_name INTEGER,
    roadway_number TEXT,
    block_or_house_number TEXT,
    roadway_name TEXT,
    roadway_suffix TEXT,
    roadway_dir_code TEXT,
    latitude REAL,
    longitude REAL,
    milepoint_derived REAL,
    collision_date TEXT,
    collision_time INTEGER,
    intersection_roadway_number TEXT,
    intersection_roadway_name TEXT, 
    intersection_roadway_sfx TEXT,
    between_st_roadway_num_1 TEXT,
    between_st_roadway_name_1 TEXT,
    between_st_roadway_sfx_1 TEXT,
    between_st_roadway_num_2 TEXT,
    between_st_roadway_name_2 TEXT,
    between_st_roadway_sfx_2 TEXT,
    units_involved INTEGER,
    motor_vehicles_involved INTEGER,
    killed INTEGER,
    injured INTEGER,
    weather_code INTEGER,
    weather TEXT,
    roadway_condition_code INTEGER,
    roadway_condition TEXT,
    hit_and_run_indication BOOLEAN,
    roadway_type_code INTEGER,
    roadway_type TEXT,
    directional_analysis_code INTEGER,
    directional_analysis TEXT,
    manner_of_collision_code INTEGER,
    manner_of_collision TEXT,
    roadway_character_code INTEGER,
    roadway_character TEXT,
    light_condition_code INTEGER,
    light_condition TEXT,
    ramp_from_roadway_id TEXT,
    ramp_to_roadway_id TEXT,
    secondary_collision_indicator BOOLEAN'''

    create_table_string = '''CREATE TABLE crashes'''

    with db_conn:
        db_conn.execute(create_table_string + "(" + table_columns + ");")


if __name__ == "__main__":
    conn = db_connection('crashes.db')

    create_crash_table(conn)