{{ config(materialized='table') }}
select *
from {{ ref('stg_events') }}
where consent = true