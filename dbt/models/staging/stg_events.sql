{{ config(materialized='view') }}
select
  cast(event_id as text) as event_id,
  cast(user_id as text) as user_id,
  cast(session_id as text) as session_id,
  cast(event_name as text) as event_name,
  cast(event_ts as timestamp) as event_ts,
  cast(consent as boolean) as consent
from read_csv_auto('../data/events.csv')