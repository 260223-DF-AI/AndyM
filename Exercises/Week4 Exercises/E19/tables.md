FACTS:
grain: one row for each user viewing a piece of content
user_fact each view is a transaction
    user_id -> FK dim_user 0
    content_id -> FK dim_user 0
    time_watched -> int additive 1
    completion_percent -> decimal additive 1
    is_premeium -> boolean 0


grain: one row for each subscription instance of a user
subscription_fact
user_id -> FK dim_user 0
plan_id -> FK dim_subscriptions 2
created-> date 0



DIMENSIONS
users
id->PK int 0
gender -> string 2
age -> int 1
ssn -> string 2
region -> string 2

content
id -> pk int 0
genre : string 2
name : string 0
desc : string 2
release_date : date 0

devices
id : PK int 0
brand : string 1
model : string 1
expensive : bool 0


subscription_type
type : string PK 0
price : decimal 2
duration : decimal 1
Access : string 2

Time 
subscription_id int FK 0
date_subscribed : date 2
date unsubscribed : date 2