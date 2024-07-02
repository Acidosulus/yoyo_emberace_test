rem http://192.168.0.112:3000/airports?airport_code=eq.NYA
rem curl "http://192.168.0.112:3000/rpc/get_airport_info?airport_code_param=NYA"
curl -X POST -H "Content-Type: application/json" -d '{"airport_code_param":"NYA"}' "http://192.168.0.112:3000/rpc/get_airport_info"
