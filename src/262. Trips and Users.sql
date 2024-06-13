-- Question can be found using this link: https://leetcode.com/problems/trips-and-users/description/
-- Solution below
with unbanned_clients as (
    select
        users_id
    from users
    where banned = "No"
    and role = 'client'
)
,
unbanned_drivers as (
    select
        users_id
    from users
    where banned = "No"
    and role = 'driver'
)
,
unbanned_users_cancelled_trips as (
    select
        t.request_at as Day
        , count(t.id) as trips_total
    from trips t
    join unbanned_clients uc on uc.users_id = t.client_id
    join unbanned_drivers ud on ud.users_id = t.driver_id
    where request_at between "2013-10-01" and "2013-10-03"
    and status in ('cancelled_by_driver', 'cancelled_by_client')
    group by t.request_at
)
,
unbanned_users_total_trips as (
    select
        t.request_at as Day
        , count(t.id) as trips_total
    from trips t
    join unbanned_clients uc on uc.users_id = t.client_id
    join unbanned_drivers ud on ud.users_id = t.driver_id
    where request_at between "2013-10-01" and "2013-10-03"
    group by t.request_at
)
select
    uutt.day as Day
    , ifnull(round((uuct.trips_total / uutt.trips_total), 2), 0) as "Cancellation Rate"
from unbanned_users_total_trips uutt
left join unbanned_users_cancelled_trips uuct on uuct.day = uutt.day
;