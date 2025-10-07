{{ config(materialized='table') }}
-- Simple mart: daily event counts
select
  date_trunc('day', event_ts) as day,
  event_name,
  count(*) as events
from {{ ref('fct_events') }}
group by 1,2
order by 1,2