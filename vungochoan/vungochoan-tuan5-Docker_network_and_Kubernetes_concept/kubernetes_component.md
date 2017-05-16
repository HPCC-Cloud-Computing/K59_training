# Kubernetes Components
## Master Components
Master components là những thành phần cung cấp control plane của cluster. Ví dụ, master components sẽ có trách nhiệm đưa ra các quyết định chung về cluster (ví dụ: lên kế hoạch), phát hiện và đáp ứng các sự kiện của cluster.

Về lý thuyết, các master component có thể được chạy trên bất kỳ node nào trong cluster. Tuy nhiên, để đơn giản, kịch bản thiết lập thường bắt đầu tất cả các master component trên cùng một máy ảo và không chạy các user container trên máy ảo này.

### Kube-apiserver
kube-apiserver là front-end của Kubernetes control plane. Nó được thiết kế để scale theo chiều ngang. Nghĩa là, nó scales bằng cách triển khai nhiều thể hiện.

### Etcd
Etcd được sử dụng giống như kho lưu trữ của Kubernetes. Tất cả các cụm dữ liệu được lưu trữ ở đây. Luôn có một kế hoạch sao lưu dữ liệu etcd cho cluster Kubernetes của bạn.

### Kube-controller-manager
Kube-controller-manager là một hệ nhị phân chạy bộ điều khiển, là các chủ đề background để xử lý các tác vụ thông thường trong cluster. Về mặt logic, mỗi bộ điều khiển là một quá trình riêng biệt, nhưng để giảm độ phức tạp, tất cả chúng được biên dịch thành một tệp tin nhị phân duy nhất và chạy trong một tiến trình đơn.

Ngoài ra còn các thành phần khác: Cloud-controller-manager, Kube-scheduler, Addons,...

## Node components
Node components chạy trên mỗi node, duy trì các pods đang chạy và cung cấp cho chúng môi trường thời gian chạy Kubernetes.

### Kubelet
Kubelet là tác nhân node chính. Nó giám sát các pod đã được gán cho node của nó (bằng apiserver hoặc thông qua tệp cấu hình cục bộ) và:
- Gắn kết các volume cần thiết của pod
- Tải xuống bí mật của pod
- Chạy các container của pod thông qua Docker (hoặc thực nghiệm, rkt)

### Kube-proxy
Kube-proxy cho phép Kubernetes service trừu tượng hóa bằng cách duy trì các quy tắc mạng trên máy chủ và thực hiện chuyển tiếp kết nối.

### Docker
Docker được sử dụng để chạy các container.

### Supervisord
Supervisord là một quy trình giám sát và điều khiển hệ thống nhẹ có thể được sự dụng để chạy kubelet và docker.

### Fluentd
Fluentd là một daemon giúp cung cấp cluster-level logging.