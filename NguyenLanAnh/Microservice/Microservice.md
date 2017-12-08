## Microservice giữa hai tầng fog và cloud
### 1. Mô hình
Microservice trong hệ thống có nhiệm vụ như một bộ lọc(filter), lọc dữ liệu từ tầng fog gửi lên và chuyển lên tầng cloud.
Mô hình như dưới đây:

![mohinh](http://imageshack.com/a/img924/1986/h1yTcH.png)

Dữ liệu sẽ được chuyển  dưới dạng message queue, qua 1 mqtt broker( như trong mô hình sử dụng Rabbitmq). Dữ liệu được lọc tại Filter, qua mqtt broker tiếp đó, và được gửi tới Cloud.

### 2. Thực hiện
Bước 1: Tạo 2 container Rabbitmq trên Docker

Bước 2: Tạo Filter, Filter vừa có khả năng nhận message từ Rabbitmq1, xử lí dữ liệu, vừa gửi dữ liệu tới Rabbitmq2. Tức nó sẽ vừa là consumer, vừa là producer. Nó phải biết cả hai địa chỉ của 2 broker để thực hiện nhiệm vụ.
Sử dụng thư viện Pika của Python.

Bước 3: Build image filterdata,   
Tạo một file config.cfg để chứa địa chỉ các broker, file config này mount với image filterdata, để cập nhật những thay đổi. Build image filterdata sử dụng chương trình lọc tạo ở bước 2, và file config.cfg.

### End.
