UPDATE dim_content
SET values = new_values ... etc , most_current = False
WHERE content_id = MATCHING_KEY

