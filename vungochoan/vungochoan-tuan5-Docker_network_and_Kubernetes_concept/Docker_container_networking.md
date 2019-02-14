# Docker container networking
## Default Networks
Khi cài đặt Docker, nó tự động tạo ra 3 network. Có thể nhìn thấy danh sách các network bằng lệnh:  
```
docker network ls
NETWORK ID          NAME                DRIVER              SCOPE
a89e9db593e9        bridge              bridge              local
cb0cdc4270b2        host                host                local
942d150afa98        none                null                local
```

Ba network này được tích hợp vào trong Docker. Khi chạy một container, bạn có thể sử dụng `--network` để chỉ định network mà container kết nối vào.

`bridge` network đại diện cho `docker0` network có trong tất cả các cài đặt Docker. Trừ khi bạn chọn network khác để kết nối `docker run --network=<NETWORK>`, nếu không Docker daemon sẽ kết nối các container vào network này theo mặc định.

`none` và `host` network không được cấu hình trực tiếp trong Docker. Tuy nhiên, bạn có thể cấu hình default `bridge` network, cũng như user-defined bridge networks.

### The default bridge network
Default `bridge` network có trên tất cả máy chủ Docker. Nếu bạn không ghi rõ một network khác, containers mới sẽ tự động kết nối đến default `bridge` network.

Chạy 2 câu lệnh để bắt đầu 2 container `busybox`, cả 2 sẽ kết nối vào default `bridge` network.

```
$ docker run -itd --name=container1 busybox

3386a527aa08b37ea9232cbcace2d2458d49f44bb05a6b775fba7ddd40d8f92c

$ docker run -itd --name=container2 busybox

94447ca479852d29aeddca75c28f7104df3c3196d7b6d83061879e339946805c
```

Các container kết nối default `bridge` network có thể giao tiếp với nhau bằng địa chỉ IP. Docker không hỗ trợ tìm service tự động trên default `bridge` network. Nếu bạn muốn các container có thể phân giải địa chỉ IP theo tên container, bạn nên sử dụng user-defined networks.

Bạn có thể `attach` vào một `container` đang chạy để xem network trông như thế nào từ bên trong container.

`docker attach container1`

Từ bên trong container, sử dụng lệnh `ping` để kiểm tra kết nối mạng tới địa chỉ IP của container khác.

```
root@0cb243cd1293:/# ping -w3 172.17.0.3

PING 172.17.0.3 (172.17.0.3): 56 data bytes
64 bytes from 172.17.0.3: seq=0 ttl=64 time=0.096 ms
64 bytes from 172.17.0.3: seq=1 ttl=64 time=0.080 ms
64 bytes from 172.17.0.3: seq=2 ttl=64 time=0.074 ms

--- 172.17.0.3 ping statistics ---
3 packets transmitted, 3 packets received, 0% packet loss
round-trip min/avg/max = 0.074/0.083/0.096 ms
```

Default `docker0` bridge network hỗ trợ việc sử dụng ánh xạ cổng và `docker run --link` cho phép các container giao tiếp với nhau trong mạng `docker0`. Cách tiếp cận này không được khuyến khích sử dụng. Nếu có thể, bạn nên sử dụng  user-defined bridge networks.

## User-defined networks
Khuyến khích sử dụng user-defined bridge networks để kiểm soát những container nào có thể giao tiếp với nhau, và cũng để kích hoạt tính năng phân giải DNS tự động tên container ra địa chỉ IP. Docker cung cấp default **network drivers** để tạo các network này.

Bạn có thể tạo nhiều network tùy theo nhu cầu của mình, và một container có thể không có kết nối hoặc kết nối đến nhiều mạng vào bất kỳ thời điểm nào. Ngoài ra, bạn có thể kết nối và ngắt kết nối các container đang chạy từ mạng mà không phải khởi động lại container.

Các phần sau mô tả các driver tích hợp sẵn của Docker một cách chi tiết hơn.

### Bridge networks
`bridge` network là mạng được sử dụng phổ biến nhất trong Docker. Các bridge network cũng tương tự như default `bridge` network, nhưng thêm một số tính năng mới và xóa một số tính năng cũ. Các ví dụ sau tạo ra một vài bridge network và thực hiện một số thử nghiệm trên container.

```
$ docker network create --driver bridge isolated_nw

1196a4c5af43a21ae38ef34515b6af19236a3fc48122cf585e3f3054d509679b

$ docker network inspect isolated_nw

[
    {
        "Name": "isolated_nw",
        "Id": "1196a4c5af43a21ae38ef34515b6af19236a3fc48122cf585e3f3054d509679b",
        "Scope": "local",
        "Driver": "bridge",
        "IPAM": {
            "Driver": "default",
            "Config": [
                {
                    "Subnet": "172.21.0.0/16",
                    "Gateway": "172.21.0.1/16"
                }
            ]
        },
        "Containers": {},
        "Options": {},
        "Labels": {}
    }
]

$ docker network ls

NETWORK ID          NAME                DRIVER
9f904ee27bf5        none                null
cf03ee007fb4        host                host
7fca4eb8c647        bridge              bridge
c5ee82f76de3        isolated_nw         bridge
```

Sau khi tạo mạng, bạn có thể chạy container sử dụng tùy chọn `docker run --network=<NETWORK>`

```
$ docker run --network=isolated_nw -itd --name=container3 busybox

8c1a0a5be480921d669a073393ade66a3fc49933f08bcc5515b37b8144f6d47c

$ docker network inspect isolated_nw
[
    {
        "Name": "isolated_nw",
        "Id": "1196a4c5af43a21ae38ef34515b6af19236a3fc48122cf585e3f3054d509679b",
        "Scope": "local",
        "Driver": "bridge",
        "IPAM": {
            "Driver": "default",
            "Config": [
                {}
            ]
        },
        "Containers": {
            "8c1a0a5be480921d669a073393ade66a3fc49933f08bcc5515b37b8144f6d47c": {
                "EndpointID": "93b2db4a9b9a997beb912d28bcfc117f7b0eb924ff91d48cfa251d473e6a9b08",
                "MacAddress": "02:42:ac:15:00:02",
                "IPv4Address": "172.21.0.2/16",
                "IPv6Address": ""
            }
        },
        "Options": {},
        "Labels": {}
    }
]
```

Các container bạn chạy trên mạng này phải nằm trên cùng một máy chủ Docker. Mỗi container có thể giao tiếp ngay lập tức với các container khác trong mạng.

![](https://docs.docker.com/engine/userguide/networking/images/bridge_network.png)

Trong user-defined bridge network, liên kết không được hỗ trợ. Bạn có thể expose và publish các cổng container trên các container trong mạng này. Điều này rất hữu ích nếu bạn muốn tạo một phần của bridge network có sẵn cho mạng bên ngoài.

![](https://docs.docker.com/engine/userguide/networking/images/network_access.png)

### The `docker_gwbridge` network
`docker_gwbridge` là bridge network cục bộ được tạo tự động bởi Docker trong 2 trường hợp khác nhau:  
- Khi bạn khởi tạo hoặc tham gia một swarm, Docker tạo ra `docker_gwbridge` network và sử dụng nó để liên lạc giữa các node swarm trên các máy khác nhau.  
- Khi không có mạng nào của container kết nối với bên ngoài, Docker kết nối container thêm một mạng nữa là `docker_gwbridge` để container có thể kết nối với mạng bên ngoài hoặc các node swarm khác.

Lệnh sau tạo ra mạng `docker_gwbridge` với một vài tùy chọn.

```
$ docker network create --subnet 172.30.0.0/16
                        --opt com.docker.network.bridge.name=docker_gwbridge
                        --opt com.docker.network.bridge.enable_icc=false
                        docker_gwbridge
```

### Overlay networks in swarm mode
Bạn có thể tạo ra một overlay network trên một node quản lý đang chạy ở chế độ swarm mà không cần lưu trữ key-value bên ngoài. Khi tạo một service sử dụng overlay network, node quản lý sẽ tự động mở rộng overlay network lên các node chạy các tác vụ service.

Chỉ có các service swarm mới có thể kết nối với các overlay network.

### An overlay network without swarm mode
Nếu bạn không sử dụng Docker Engine trong chế độ swarm, `overlay` network sẽ yêu cầu service lưu trữ một key-value hợp lệ. Trước khi tạo mạng này, bạn cần phải cài đặt và cấu hình service lưu trữ key-value đã chọn.

### Custom network plugin
Nếu các mạng trên không giải quyết được yêu cầu của bạn, bạn có thể viết network driver plugin của riêng bạn, sử dụng cơ sở hạ tầng plugin của Docker. Plugin sẽ chạy như một quá trình riêng trên máy chủ mà chạy các Docker daemon.

### Embedded DNS server
Docker daemon chạy một embedded DNS server cung cấp phân giải DNS giữa các container được kết nối trong user-defined network, để các container này có thể phân giải tên container ra địa chỉ IP.

## Exposing and publishing ports
Trong mạng Docker, có 2 cơ chế liên quan đến các cổng mạng: exposing và publishing ports. Nó áp dụng cho default bridge network và user-defined bridge networks.  
- Bạn expose ports bằng cách sử dụng từ khóa `EXPOSE` trong Dockerfile hoặc `--expose` trong `docker run`. Exposing ports là một cách để ghi lại các cổng đã được sử dụng, nhưng không thực sự ánh xạ hoặc mở bất kỳ cổng nào. Exposing ports là tùy chọn.  
- Bạn publish ports bằng cách sử dụng từ khóa `PUBLISH` trong Dockerfile hoặc `--publish` trong `docker run`. Điều này cho Docker biết cổng nào mở trên giao diện mạng của container. Khi một cổng được publish, nó được ánh xạ đến một cổng cao (cao hơn 30000) trên máy chủ, trừ khi bạn chỉ định cổng để ánh xạ đến máy chủ khi chạy. Bạn không thể chỉ định cổng để ánh xạ tới máy chủ trong Dockerfile, vì không có gì đảm bảo cổng đó sẽ có sẵn trên máy chủ nơi bạn chạy image.

Ví dụ sau publishes cổng 80 trong container đến một cổng ngẫu nhiên cao hơn trên máy chủ.

```
$ docker run -it -p 80 nginx

$ docker ps

64879472feea        nginx               "nginx -g 'daemon ..."   43 hours ago        Up About a minute   443/tcp, 0.0.0.0:32768->80/tcp   blissful_mclean
```

Ví dụ tiếp theo chỉ định rằng cổng 80 phải được ánh xạ đến cổng 8080 trên máy chủ. Nó sẽ thất bại nếu cổng 8080 không có sẵn.

```
$ docker run -it -p 80:8080 nginx

$ docker ps

b9788c7adca3        nginx               "nginx -g 'daemon ..."   43 hours ago        Up 3 seconds        80/tcp, 443/tcp, 0.0.0.0:80->8080/tcp   goofy_brahmagupta
```

## Links
Trước khi Docker bao gồm user-defined networks, bạn có thể sử dụng tính năng `--link` để cho phép một container phân giải tên của một container khác ra địa chỉ IP, và cũng cho phép nó truy cập vào các biến môi trường của container được liên kết. Nếu có thể, bạn nên tránh sử dụng `--link`.

Khi bạn tạo một liên kết, nó sẽ hoạt động khác khi bạn sử dụng default `bridge` network hoặc khi bạn sử dụng user-defined bridge networks.