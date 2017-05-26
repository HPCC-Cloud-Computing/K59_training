# Kubernetes Components
## Master Components
Master components là những thành phần cung cấp control plane của cluster. Ví dụ, master components sẽ có trách nhiệm đưa ra các quyết định chung về cluster (ví dụ: lên kế hoạch), phát hiện và đáp ứng các sự kiện của cluster.

Về lý thuyết, các master component có thể được chạy trên bất kỳ node nào trong cluster. Tuy nhiên, để đơn giản, kịch bản thiết lập thường bắt đầu tất cả các master component trên cùng một máy ảo và không chạy các user container trên máy ảo này.

### Kube-apiserver
kube-apiserver là front-end của Kubernetes control plane. Nó được thiết kế để scale theo chiều ngang, bằng cách triển khai nhiều thể hiện.

### Etcd
Etcd được sử dụng giống như kho lưu trữ của Kubernetes. Tất cả các cụm dữ liệu được lưu trữ ở đây. Luôn có một kế hoạch sao lưu dữ liệu etcd cho cluster Kubernetes của bạn.

### Kube-controller-manager
Kube-controller-manager là một hệ nhị phân chạy bộ điều khiển, là các chủ đề background để xử lý các tác vụ thông thường trong cluster. Về mặt logic, mỗi bộ điều khiển là một quá trình riêng biệt, nhưng để giảm độ phức tạp, tất cả chúng được biên dịch thành một tệp tin nhị phân duy nhất và chạy trong một tiến trình đơn.

Bộ điều khiển bao gồm:
- Node Controller: Chịu trách nhiệm thông báo và trả lời khi các node đi xuống.
- Replication Controller: Chịu trách nhiệm duy trì chính xác số lượng các pod cho mỗi đối tượng replication controller trong hệ thống.
- Endpoints Controller: Nạp các đối tượng Endpoints (có nghĩa là kết hợp Services & Pods).
- Service Account & Token Controllers: Tạo tài khoản mặc định và API truy cập các token với không gian tên mới.

### Cloud-controller-manager
Cloud-controller-manager quản lý các bộ điều khiển tương tác với các nhà cung cấp cloud cơ bản. Cloud-controller-manager chỉ chạy vòng điều khiển cloud-provider-specific. Bạn có thể vô hiệu hóa các vòng điều khiển bằng cách thiết lập `--cloud-provider` để `external` khi bắt đầu chạy kube-controller-manager.

### kube-scheduler
kube-scheduler hiển thị các pod được tạo mới mà không có các node được gán, và chọn một node để chúng chạy trên.

### Addons
Addons là các pod và các service thưc hiện các tính năng của cluster. Các pod có thể được quản lý bởi Deployments, ReplicationControllers,... Các đối tượng addons được tạo ra trong không gian tên **kube-system**.

Addon manager tạo và duy trì các tài nguyên addon.

### DNS
Tất cả các Kubernetes cluster nên có cluster DNS. Cluster DNS là một máy chủ DNS, ngoài các máy chủ DNS khác trong môi trường của bạn, phục vụ các bản ghi DNS cho các Kubernetes service.

Các container được bắt đầu bởi Kubernetes tự động bao hàm máy chủ này trong các DNS tìm kiếm của chúng.

### User Interface
Kube-ui cung cấp một cái nhìn tổng quan read-only về trạng thái cluster.

### Container Resource Monitoring
Container Resource Monitoring ghi các số liệu time-series chung về các container trong cơ sở dữ liệu trung tâm và cung cấp UI để người dùng duyệt dữ liệu đó. 

### Cluster-level Logging
Một cơ chế Cluster-level logging có trách nhiệm lưu các log vào một trung tâm lưu trữ log với giao diện search/browsing.

## Node components
Node components chạy trên mỗi node, duy trì các pods đang chạy và cung cấp cho chúng môi trường thời gian chạy Kubernetes.

### Kubelet
Kubelet là tác nhân node chính. Nó giám sát các pod đã được gán cho node của nó (bằng apiserver hoặc thông qua tệp cấu hình cục bộ) và:
- Gắn kết các volume cần thiết của pod.
- Tải xuống bí mật của pod.
- Chạy các container của pod thông qua Docker (hoặc thực nghiệm, rkt).
- Định kỳ thực hiện bất kỳ yêu cầu thăm dò liveness container.
- Báo cáo lại trạng thái của pod back cho phần còn lại của hệ thống, bằng cách tạo ra một mirror pod nếu cần.
- Báo cáo trạng thái của node back cho phần còn lại của hệ thống.

### Kube-proxy
Kube-proxy cho phép Kubernetes service trừu tượng hóa bằng cách duy trì các quy tắc mạng trên máy chủ và thực hiện chuyển tiếp kết nối.

### Docker
Docker được sử dụng để chạy các container.

### Supervisord
Supervisord là một quy trình giám sát và điều khiển hệ thống nhẹ có thể được sự dụng để chạy kubelet và docker.

### Fluentd
Fluentd là một daemon giúp cung cấp cluster-level logging.