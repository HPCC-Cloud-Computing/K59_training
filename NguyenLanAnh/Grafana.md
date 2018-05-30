# Grafana

### 1. Cài đặt, cấu hình Grafana với Docker

- Cài đặt: Grafana dễ dàng được cài đặt bằng Docker với câu lệnh: 

        $ docker run -d -p 3000:3000 grafana/grafana

- Cấu hình: Các thay đổi cấu hình được thiết lập thông qua các biến môi trường ENV. Đồng thời cũng có 2 volumns, sqlite3 database trong /var/lib/grafana, file cấu hình trong /etc/grafana, có thể map những volumns này vời folders tại máy host bằng cách chạy container với câu lệnh:

        $ docker run -d -p 3000:3000 \
            -v /var/lib/grafana:/var/lib/grafana \
            -e "GF_SECURITY_ADMIN_PASSWORD=secret" \
            grafana/grafana

   Theo như câu lệnh trên, biến ENV đã được sử dụng để cấu hình Grafana. Các lựa chọn cấu hình được định nghĩa trong file conf/grafana.ini. Thay đổi cấu hình thông qua biến ENV bằng cách dử dụng theo cú pháp: 
 
           GF_<SectionName>_<KeyName>

   Chi tiết các options của cấu hình có tại: [options](http://docs.grafana.org/installation/configuration/)

- Plugins:

    Grafana là một công cụ với mục đích chính là "visualize" dữ liệu ( phần lớn là dữ liệu time series). Cơ bản Grafana không hỗ trợ lưu trữ dữ liệu như Graphite có thể làm, hay cũng không thể thu thập dữ liệu như Prometheus, nhưng Grafana lại có nhiều plugins để mở rộng thêm tính năng. Gồm những plugins data sources: CloudWatch, Elasticsearch, Graphite, Prometheus, InfuxDB,...; plugins applications: Zabbix, Clock,...; hay những plugins dashboard editing.

    Cài đặt plugin cho Grafana bằng cách sử dụng biến môi trường GF_INSTALL_PLUGINS, như ví dụ dưới đây:

          $ docker run \
                    -d \
                    -p 3000:3000 \
                    --name=grafana \
                    -e "GF_INSTALL_PLUGINS=grafana-clock-panel,grafana-simple-json-datasource" \
                    grafana/grafana

        

### 2. Các quyền người dùng trong Grafana

  - Người sử dụng Grafana có các quyền (Permission) được xác định thông qua 4 yếu tố sau:

                - Vai trò tổ chức (Organization Role): Admin, Editor, Viewer
                - Thông quá các thành viên trong nhóm đã được xác định quyền cụ thể
                - Thông qua các quyền đã được chỉ định trực tiếp đến người dùng ( sử dụng trên folder hoặc dashboard)
                - Sử dụng cờ Grafana Admin ( ví dụ: Super Admin)

  - Một người dùng có thể thuộc về 1 hay nhiều tổ chức (organization), có những vai trò (role) riêng trong mỗi tổ chức, mà trong đó:

              - Admin: 
         Có thể làm mọi thứ như : Thêm, sửa data sources; Thêm, sửa người sử dụng trong tổ chức, nhóm; Cấu hình các plugins hay thiết lập các cài đặt.
              - Editor:
         Có thể khởi tạo, sửa đổi dashboards hoặc các luật cảnh báo (Có thể bị disabled trên những folders hay dashboards đặc biệt; Không thể khởi tạo hay sửa đổi data sources cũng như không thể thêm người dùng.
              - Viewer:
         Có thể xem các dashboards ( Có thể bị disabled trên những folders hay dashboards đặc biệt); Không thể khởi tạo hay sửa đổi dashboards hay data sources. Trong một vài trường hợp, Viewer cũng có thể sửa đổi dashboards những không thể lưu thay đổi.

  - Đối với trường hợp khi sử dụng cờ Grafana Admin, người dùng sẽ trở thành Super Admin, có thể truy cập Server Admin, nơi mà có thể thấy danh sách người dùng, tổ chức được quản trị.
  - Có một trang cấp quyền cho các folders, dashboards, có thể thay đổi các vai trò mặc định cho Editor và Viewer.
  - Sử dụng cơ chế hạn chế truy cập (Restricting Access) bằng cách thay đổi ACL (Access Control List ).


### 3. Các thành phần cơ bản 

  
   Các thành phần có thể kể đến của Grafana như: Data sources, dashboards, panels, alerting. Trong đó: 

- Data sources:

  Đó là những storage backends như: Graphite, InfluxDB, OpenTSDB, Prometheus, Elasticsearch, CloudWatch. Mỗi data source sẽ có những query editor riêng biệt.

- Panel:

  Là phần hiển thì cơ bản trong Grafana. Mỗi Panel cung cấp 1 Query Editor (tùy thuộc vào data sources) cho phép trích xuất thông tin để hiển thị trên panel.
  Các loại panels là:  Graph, Singlestat, Dashlist, Table,and Text, có thể được sắp xếp, kéo thả cho phù hợp trên dashboard. Chi tiết về các loại panels tại [panels](http://docs.grafana.org/features/panels/)

  Dưới đây là hình ảnh về 1  graph panel:

  ![graph](https://i.imgur.com/AMt5Ts3.png)


- Dashboards:

  Một dashboards có thể hiểu đơn giản là tập hợp của tất cả các panels, có thể chia thành 1 hay 2 dòng,... chứa các panels tùy ý. Chi tiết tại [dashboards](http://docs.grafana.org/reference/templating/)











