# Hướng dẫn cài đặt

Tài liệu sơ lược của hệ thống: `https://docs.google.com/document/d/1xddKaOtnopvNmW4zvqcGcjFwh5k_taKj8zh20NsxhrU/edit`

## Cài đặt ban đầu

- Chạy influxdb làm cơ sở dữ liệu của Collector
	`docker run -p 8086:8086 --name influxdb-collector influxdb:1.5`
- Chạy mySQL làm cơ sở dữ liệu cho Registry
	`docker run --name mysql-registry -p 3306:3306 -e MYSQL_ROOT_PASSWORD=root -idt mysql:5.7`
- Chạy Rabbitmq để làm Broker tầng Cloud
	`docker run -d --hostname my-rabbit --name broker-cloud -p 15672:15672 -p 5672:5672 rabbitmq:3-management`
- Chạy Mosquitto để làm Broker tầng Fog
	`docker run -d --name broker-fog -p 1883:1883 haiquan5396/mqtt`

## Chạy các thành phần khác ở chế độ 'Develop'

Khi muốn chỉnh sửa code hay chạy trực tiếp thì ta sửa MODE_CODE thành 'Develop'. Nó sẽ gán các biến môi trường bằng `localhost`

Chạy hệ thống lần lượt theo thứ tự: Forwarder_Cloud_to_Fog, Forwarder_Fog_to_Cloud, Registry, DBwriter, Filter, Collector, DBreader, API, IoT Platform, Driver

## Chạy hệ thống bằng Docker

Export các biến môi trường: 
	export BROKER_CLOUD= địa chỉ rabbitmq
	export BROKER_FOG= địa chỉ mosquitto
	export HOST_MYSQL= địa chỉ mysql
	export HOST_INFLUXDB= địa chỉ influxdbM
	export MODE= có thể là PULL hoặc PUSH, 

Sử dụng các file để chạy hệ thống: 

- `script/start_system_cloud.sh`: để chạy hệ thống tầng Cloud
- `script/start_system_fog.sh`: để chạy hệ thống tầng fog

Sử dụng các file sau để tắt hệ thống: 
- `script/stop_system_cloud.sh`: để tắt hệ thống tầng Cloud
- `script/stop_system_fog.sh`: Để tắt hệ thống tầng Fog

