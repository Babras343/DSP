# Token: S_uv7C9UqfyftB3L9gt_COMJ_wI9i0fyN5b9AlGZxTnVWNs-W_mnYg8rN5y5ZuSH2eJWcTLXkZ_Qt6v_VSaRFw==


query = """SELECT *
FROM "census"
WHERE time >= now() - interval '24 hours'
AND ("bees" IS NOT NULL OR "ants" IS NOT NULL)"""

# Execute the query
table = client.query(query=query, database="InfluxDB_RD", language='sql')

# Convert to dataframe
df = table.to_pandas().sort_values(by="time")
print(df)

## And this one tooo...


HAHHas