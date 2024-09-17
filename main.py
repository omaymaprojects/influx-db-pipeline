import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = "3aWcKsLwUf6d610lKqGD26NzYc0ZB9AQMssSMqZzuKC-zRkgQ4uHfYqtTAFWP_QyfwFIMsJvoD_KUUgNH3TJ8A=="  # Replace with your actual token
org = "my-org"
url = "http://localhost:8087"

write_client = influxdb_client.InfluxDBClient(url=url, token=token, org=org)
bucket = "my-bucket"

write_api = write_client.write_api(write_options=SYNCHRONOUS)
   
for value in range(5):
  point = (
    Point("measurement1")
    .tag("tagname1", "tagvalue1")
    .field("field1", value)
  )
  write_api.write(bucket=bucket, org=org, record=point)
  time.sleep(1) # separate points by 1 second
