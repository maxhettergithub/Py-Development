import json
import pandas as pd
import duckdb as db

# File path to the JSON file
file_path = 'file_path'

# Open and load the JSON file
with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
    data = json.load(file)

# Convert the loaded data to a pandas DataFrame
df = pd.DataFrame(data)

# Convert the 'ts' column to datetime format
df['ts'] = pd.to_datetime(df['ts'])

# Register the DataFrame as a DuckDB table
db.query("create table df as select * from df")

# Run the SQL query on the registered DataFrame
query_results = db.query(
    '''
    with transform as (
        select 
            ms_played / 60000 as minutes_listened,
            master_metadata_album_artist_name as artist_name,
            master_metadata_track_name as track_name,
            *
        from df
        where spotify_episode_uri is null
        and ms_played > 30000
        and ts >= '2024-01-01' 
        and ts <= '2024-11-15'  
    )

    select 
        track_name,
        count(track_name) AS times_listened,
        sum(minutes_listened) AS total_minutes_listened
    from transform 
    group by 1
    order by 2 desc,3 desc
    '''
).df()

# Print the query results
print(query_results)
