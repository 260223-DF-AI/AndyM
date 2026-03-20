Document:

- Partitioning strategy for each fact table
We're going to partition by ranges of dates

- Clustering columns for each table
Cluster on the most common PKS

user
- user_id
- content_id
- leave out device_id since that table will not be joined very often

Subscription
- subscription id
- user id

- Estimated table sizes and growth rates
- Recommended load frequency



Table size + Growth Rate

user - moderate growth rate, large table size, load every entry

content - high growth rate, large table size, load in batches, maybe weekly