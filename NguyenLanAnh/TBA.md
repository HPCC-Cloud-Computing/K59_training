# TBA

## 1. 4 mô hình truyền thông trong hệ thống IOT

Truyền thông trong 1 hệ thống IOT chủ yếu liên quan đến việc truyền thông giữa 3 nhóm: Thiết bị, gateways, cloud. Việc truyền thông này chủ yếu liên quan đến trao đổi thông điệp( message). Dựa vào cách thức trao đổi message, có thể chia mô hình truyền thông IOT thành 4 nhóm là:

- Telemetry: Message di chuyển 1 chiều, từ thiết bị đến hệ thống. Mục đích là gửi trạng thái của thiết bị lên hệ thống.
Giao thức triển khai mô hình này phổ biến nhất là: MQTT, MQTT implements luôn cả mô hình publish/subscribe. Với MQTT, các thiết bị được xem như publisher - người xuất bản. Nội dung xuất bản là các dữ liệu mà thiết bị đó thu thập hoặc xử lý được. Đích đến của các dữ liệu đó là các brokers. Để gom nhóm các dữ liệu thành 1 "kênh", MQTT sử dụng khái niệm topic.  Các hệ thống/thiết bị khác muốn lấy thông tin thì sẽ hoạt động như subscriber - người theo dõi. Hành động theo dõi này và các message tương ứng được giới hạn theo từng topic.
Đồng thời, MQTT cũng được hỗ trợ đầy đủ các QoS level.

 Một giao thức đáng chú ý khác cũng implement mô hình này, đó là AMQP. AMQP cung cấp cả 2 phương pháp trao đổi message là request/reply và publish/subscribe.
 So với MQTT, AMQP có một lợi thế lớn. Đó là khả năng thiết đặt một luồng logic điều khiển cho 2 mức khác nhau: mức byte và mức message.

 Nói về nhược điểm, MQTT không hỗ trợ xử lý logic. Vì không hỗ trợ xử lý logic nên một broker có thể bị quá tải (flooded) bởi các messages mà không làm cách nào để dừng nhận các messages này.
- Inquiry: Gửi các requests từ thiết bị lên hệ thống. Các requests này liên quan đến việc thu thập các thông tin mà thiết bị hiện tại không thu thập được. Và hệ thống lại gửi trả lại response.

 Việc implement MQTT theo mô hình Inquiry khó khăn hơn vì ta sẽ phải define các ngữ nghĩa mới ở tầng ứng dụng để đảm bảo việc truyền thông giữa device và hệ thống tuân thủ đúng mô hình Inquiry.

 Khác với MQTT và HTTP, AMQP đáp ứng tốt yêu cầu của việc implement mô hình Inquiry.

 Một điểm mạnh của AMQP khi implements mô hình Inquiry là tính asynchronous của giao thức này. Nhờ đặc tính asynch vốn có, các thông điệp hồi đáp từ phía hệ thống có thể đến thiết bị theo bất kỳ thứ tự nào mà không làm mất đi sự tương quan của message hồi đáp với request yêu cầu nó.

- Command: Hệ thống gửi message tới thiết bị.

 Với giao thức MQTT, nếu muốn implements theo mô hình Command, ta cũng phải đưa ra một số ngữ nghĩa mới ở tầng ứng dụng.

 Bản thân MQTT không hỗ trợ kiểu truyền thông request/reply nên ta cần đưa ra một số ngữ nghĩa mới như: thiết bị subscribe một topic để nhận command, hệ thông sẽ gửi command vào topic đó. Phần payload của command (từ phía hệ thống) sẽ phải chứa request ID. Sau khi thực thi mệnh lệnh, thiết bị publish kết quả kèm theo request ID tương ứng.

 Nếu thiết bị  offline, ta có thể dùng "retain" flag, nhờ đó, mệnh lệnh cuối cùng từ phía hệ thống sẽ được chuyển đến khi device online trở lại.

 ![anh1](https://i.imgur.com/xiFPqvZ.png)

 Một lần nữa, AMQP lại tỏ ra vượt trội hơn khi implements mô hình Command.

 Hệ thống có thể gửi message chứa mệnh lệnh, kèm theo message ID và thuộc tính reply-to. Sau khi thực thi mệnh lệnh, thiết bị  gửi kết quả trong một message khác, kèm theo ID tương ứng với message ID của mệnh lệnh từ phía hệ thống. Message từ phía thiết bị sẽ được gửi đúng về địa chỉ mà hệ thống mong muốn nhờ thuộc tính reply-to. Việc truyền thông này cũng diễn ra không đồng bộ (asynchronous), do đó hệ thống có thể gửi hàng loạt mệnh lệnh mà vẫn nhận được response tương ứng của từng mệnh lệnh đã gửi.

 Nếu thiết bị offline và ta chỉ muốn nó thực thi mệnh lệnh mới nhất từ phía hệ thống? Để giải quyết tình huống này, sử dụng thuộc tính TTL (Time To Live) cho các mệnh lệnh gửi đi từ hệ thống.

 ![anh2](https://i.imgur.com/ErMe2Nt.png)

- Notification:

 Với giao thức MQTT, thiết bị sẽ subscribe một topic. Server publish notification vào topic đó. Mọi thứ diễn ra suôn sẻ vì mô hình Notification này rất gần với cơ chế publish/subscribe của MQTT. Tuy nhiên, nếu không define thêm phần logic xử lý ở tầng ứng dụng, thiết bị có thể bị quá tải do liên tục nhận các notification từ topic đang subscribe.

 Cuối cùng, với AMQP, thiết bị vừa có thể nhận notificaiton vừa có thêm phần logic xử lý giúp thiết bị ngừng nhận notification khi không đủ khả năng xử lý.

## 2. MQTT protocol(Message Queuing Telemetry Transport)

- MQTT là một giao thức publish/subscribe thông điệp, được thiết kế cho công nghệ M2M (Machine to Machine) 1 cách gọn nhẹ.

- Kiến trúc:

 MQTT có mô hình client/server, các cảm biến là clients và kết nối đến một máy chủ, có thể hiểu như một nhà môi giới (broker), thông qua giao thức TCP (Transmission Control Protocol)

 MQTT là giao thức định hướng thông điệp. Mỗi thông điệp là một đoạn rời rạc của tín hiệu và broker không thể nhìn thấy.

 Mỗi thông điệp được publish một địa chỉ, có thể hiểu như một kênh. Client đăng kí vào một vài kênh để nhận/gửi dữ liệu, gọi là subscribe. Client có thể subscribe vào nhiều kênh. Mỗi client sẽ nhận được dữ liệu khi bất kì trạm nào khác gửi dữ liệu vào kênh đã đăng kí. Khi một client gửi một thông điệp đến một kênh vào đó, gọi là publish.

 Ví dụ:

 ![anh3](https://i.imgur.com/8h5boBg.png)

 Bên trên là hình ảnh ví dụ về 3 clients A,B,C kết nối tới broker. 2 kênh B và C cùng đăng kí kênh temperature.

 ![anh4](https://i.imgur.com/ZPgMjsD.png)

 Khi clientA gửi tới broker giá trị mới tới topic temperature, thì lúc này broker sẽ chuyển message tới tất cả clients đã đăng kí kênh temperature.

## 3. MQTT brokers

- MQTT brokers rất đa dạng: mosquitto, HiveMQ, Apache Apollo, Apache ActiveMQ, RabbitMQ, MQTT.js,...

- Thực hành với Apache ActiveMQ:

 Sử dụng JMS(Java Message Service) cho phép gửi, nhận tin nhắn giữa 1 hay nhiều client. Ví dụ A và B gửi thông điệp cho nhau. Với JMS, chúng sẽ không cần kết nối trực tiếp với nhau, mà thông điệp được gửi tới JMS provider và được đặt vào 1 hàng đợi cho đến khi client khác nhận thông điệp.

 ![hinh5](https://i.imgur.com/pJ4A8fD.png)

 message producer là 1 chương trình java gửi JMS message tới hàng đợi trên JMS provider, message consumer là 1 chương trình Java khác cái mà có nhiệm vụ nhận message. 2 chương trình này có thể nằm tại 2 máy riêng biệt nhưng để giao tiếp được chúng phải có được URL của JMS provider. Provider giống như 1 server (như JBoss, Glassfish), ActiveMQ broker sẽ giữ vai trò tương tự thế (1 broker trung gian hay còn gọi là MOM_Message Oriented Middleware).

 [install ActiveMQ](http://activemq.apache.org/getting-started.html)


# end.
