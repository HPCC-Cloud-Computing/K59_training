# I. Tổng quan
## 1. Kubernetes là gì
Kubernetes là một nền tảng mã nguồn mở để tự động triển khai, mở rộng và vận hành các container ứng dụng trên các nhóm máy chủ, cung cấp cơ sở hạ tầng tập trung vào container.

### Tại sao lại dùng containers
![](https://kubernetes.io/images/docs/why_containers.svg)

Cách cũ để triển khai ứng dụng là cài đặt ứng dụng trên một máy chủ sử dụng trình quản lý gói hệ điều hành. Điều này gây khó khăn cho việc thực thi, cấu hình, thư viện, và vòng đời giữa các ứng dụng với nhau và với hệ điều hành của máy chủ.

Cách mới là triển khai các container dựa trên OS-level hơn là hardware virtualization. Các container bị cô lập với nhau và từ máy chủ: chúng có hệ thống tệp tin của riêng mình, chúng không thể nhìn thấy tài nguyên của nhau và việc sử dụng tài nguyên tính toán có thể bị giới hạn. Chúng dễ xây dựng hơn các máy ảo, và vì chúng được tách riêng với cơ sở hạ tầng cơ bản, và từ hệ thống tệp tin máy chủ, chúng có thể đi qua clouds và phân bố của hệ điều hành.

## 2. Làm việc với các đối tượng Kubernetes
### 2.1. Tìm hiểu các đối tượng Kubernetes
Kubernetes Objects là các thực thể trong hệ thống Kubernetes. Kubernetes sử dụng các thực thể này để biểu thị trạng thái các cluster của bạn. Nó mô tả:
- Ứng dụng container nào đang chạy (và trên các node nào)
- Các tài nguyên sẵn có cho các ứng dụng đó
- Những chính sách xung quanh việc cách ứng dụng đó hoạt động, chẳng hạn như khởi động lại chính sách, nâng cấp và khả năng chịu lỗi.

Để làm việc với các Kubernetes Objects, như thêm, sửa hoặc xóa chúng - bạn cần phải sử dụng API Kubernetes.

#### 2.1.1 Object Spec và Status
Mỗi Kubernetes object bao gồm 2 trường đối tượng lồng nhau quản lý cấu hình của đối tượng: object spec và object status. Spec, cái bạn phải cung cấp, mô tả trạng thái mong muốn của bạn cho đối tượng-các đặc tính mà bạn muốn các đối tượng có. Status mô tả các trạng thái thực tế của các đối tượng, và được cung cấp và cập nhật bởi hệ thống Kubernetes.

#### 2.1.2 Mô tả một Kubernetes object
Khi tạo một đối tượng trong Kubernetes, bạn phải cung cấp cho object spec trạng thái mong muốn của nó và một số thông tin cơ bản. Khi bạn sử dụng API Kubernetes để tạo đối tượng (trực tiếp hoặc thông qua `kubectl`), yêu cầu API đó phải bao gồm thông tin là JSON. Thông thường, bạn cung cấp thông tin đến `kubectl` trong tệp **.yaml**

#### 2.1.3 Phần bắt buộc
Trong tệp tin **.yaml** của Kubernetes object bạn muốn tạo, bạn cần đặt gía trị cho các trường sau:
- `apiVersion` - Phiên bản API Kubernetes nào bạn đang sử dụng để tạo ra đối tượng này
- `kind` - Bạn muốn tạo loại đối tượng nào
- `metadata` - dữ liệu giúp xác định đối tượng là duy nhất, bao gồm name string, UID và tùy chọn namespace.
Bạn cũng cần cung cấp trường object spec. Định dạng đúng của object spec là khác nhau cho mọi Kubernetes object, và chứa các trường lồng nhau riêng của đối tượng đó.

# II. Container
## 1. Images
Bạn tạo image Docker của bạn và push nó vào một đăng ký trước khi đề cập đến nó trong Kubernetes pod.

Tính chất **image** của một container hỗ trợ cú pháp giống như lệnh **docker** 

### Updating Images
Kubernetes sẽ không pull một image nếu nó đã tồn tại. Nếu bạn không chỉ định tag của image, nó sẽ được gỉa sử là **`:latest`**. Lưu ý rằng bạn nên tránh sử dụng **`:latest`** tag.

## 2. Biến môi trường container
### 2.1. Môi trường container
Môi trường container Kubernetes cung cấp một số tài nguyên quan trọng cho container:
- Một hệ thống tệp tin, là sự kết hợp của một image và một hoặc nhiều volumes.
- Thông tin về chính container
- Thông tin về các đối tượng khác trong cluster.

#### 2.1.1. Thông tin container
Tên máy chủ của một container là tên của Pod trong đó container đang chạy. Nó có sẵn thông qua lệnh **hostname** hay gọi hàm `gethostname` trong libc.

Tên Pod và không gian tên có sẵn dưới dạng các biến môi trường thông qua **downward API**.

#### 2.1.2. Thông tin cluster
Một danh sách tất cả các dịch vụ đang chạy khi một container được tạo ra có sẵn cho container đó như các biến môi trường. Những biến môi trường phù hợp với cú pháp của liên kết Docker.

## 3. Container Lifecycle Hooks
Tương tự như nhiều framework ngôn ngữ lập trình có component lifecycle hooks, Kubernetes cung cấp Containers với các lifecycle hooks. Hooks cho phép Container nhận biết được các sự kiện trong vòng đời quản lý của chúng và chạy code được thực hiện trong trình xử lý khi hook lifecycle tương ứng được thực thi.

### Container hooks
Có 2 hooks được tiếp xúc với Containers:

**PostStart**

Hook này thực hiện ngay sau khi một container được tạo ra. Tuy nhiên không có gì đảm bảo rằng hook này sẽ thực thi trước container ENTRYPOINT. Không có tham số nào được truyền cho trình xử lý.

**PreStop**

Hook này được gọi ngay trước khi container được kết thúc. Đó là chặn, có nghĩa là nó đồng bộ, do đó nó phải hoàn thành trước khi lời gọi xóa các container có thể được gửi. Không có tham số nào được truyền cho trình xử lý.

# III. Workloads
## 1. Pods
### 1.1 Tổng quan về Pod
Pod là khối xây dựng cơ bản của Kubernetes - đơn vị nhỏ nhất và đơn giản nhất trong mô hình đối tượng Kubernetes mà bạn tạo ra hoặc triển khai. Một Pod đại diện cho một tiến trình đang chạy trên cluster của bạn.

Pods được sử dụng theo một số cách trong Kubernetes cluster như sau:
- Pods chạy một container: Mô hình "one-container-per-Pod" là trường hợp phổ biến nhất. Trong đó Pods như một cái vỏ bao xung quanh container, và Kubernetes quản lý Pods chứ không trực tiếp quản lý container.
- Pods chạy nhiều container cùng làm việc với nhau: Một Pod có thể gói gọn một ứng dụng bao gồm nhiều container được kết nối chặt chẽ và cần chia sẻ tài nguyên. Pod bao gồm các container và các tài nguyên lưu trữ như một thực thể quản lý đơn.

Các container trong một Pod chia sẻ một địa chỉ IP và một không gian cổng, có thể tìm thấy nhau thông qua **`localhost`**. Khi các container giao tiếp với các thực thể bên ngoài, chúng phải sử dụng tài nguyên mạng chia sẻ.

### 1.2 Pod Lifecycle
Một trường trạng thái của Pod là một đối tượng PodStatus, có một trường `phase`

Các giá trị có thể có cho `phase`
- Pending: Pod đã được chấp nhận bởi hệ thống Kubernetes nhưng một hoặc nhiều image container không được tạo ra. Điều này bao gồm thời gian trước khi được lập lịch cũng như thời gian tải các image, sẽ mất một khoảng thời gian.
- Running: Pod đã được ràng buộc với một node, và tất cả các container đã được tạo. Ít nhất một container vẫn đang chạy, hoặc đang trong quá trình khởi động hoặc khời động lại.
- Succeeded: Tất cả các container trong Pods đã kết thúc thành công, và sẽ không được khởi dộng lại.
- Failed: Tất cả các Container trong Pod đã bị kết thúc, và ít nhất một Container đã bị hủy. Tức là, Container hoặc đã thoát với trạng thái khác 0 hoặc đã bị hệ thống kết thúc.
- Unknown: Đối với một số lý do, trạng thái của Pod không thể đạt được, thông thường do một lỗi trong giao tiếp với các máy chủ của Pod.

### 1.3 Init Containers
Một Pod có thể có nhiều Container chạy các ứng dụng bên trong nó, nhưng nó cũng có thể có một hoặc nhiều Init Container, được chạy trước khi Containers ứng dụng được chạy.

Init container giống với container thông thường, ngoại trừ:
- Chúng luôn chạy đến khi hoàn thành
- Mỗi cái phải hoàn thành thành công trước khi cái tiếp theo được bắt đầu

Nếu một Init Container chạy thất bại, Kubernetes khởi động lại Pod một lần nữa cho đến khi Init Container thành công.

## 2. Controller
### 2.1. Replica Sets
ReplicaSet là thế hệ kế tiếp của Replication Controller. Sự khác biệt duy nhất giữa ReplicaSet và Replication Controller là sự lựa chọn hỗ trợ. 

### 2.2. Replication Controller
Một Replication Controller đảm bảo rằng một pod hay bộ đồng nhất của pod luôn sẵn sàng và sẵn có. Nếu có quá nhiều pod, nó sẽ xóa đi một ít, nếu có quá ít, nó sẽ khởi động nhiều hơn. Không giống như các pod được tạo thủ công, các pod được duy trì bởi một ReplicationController sẽ tự động được thay thế nêú chúng bị lỗi, bị xóa hoặc bị kết thúc.

### 2.3. Deployment
Deployment cung cấp thông tin cập nhật cho Pods và ReplicaSets. Bạn chỉ cần mô tả trạng thái mong muốn trong một đối tượng Deployment, và bộ điều khiển Deployment sẽ thay đổi trạng thái thực tế sang trạng thái mong muốn với tỷ lệ được kiểm soát cho bạn.

Ngoài ra còn nhiều thành phần khác nữa của Controller như: StatefulSets, PetSets, Daemon Sets,...

# IV. Storage
## 1. Volumes
Các tệp trên ổ đĩa trong một container là tạm thời, trong đó nói về một số vấn đề đối với các ứng dụng không tầm thường khi chạy trong các container. Thứ nhất, khi một containerontainer bị treo, kubelet sẽ khởi động lại nó, nhưng các tệp tin sẽ bị mất, container sẽ bắt đầu lại với trạng thái trống. Thứ hai, khi chạy các container với nhau trong một pod thường cần phải chia sẻ các tệp tin giữa các container. Volume Kubernetes sẽ giải quyết cả hai vấn đề này.

Kubernetes hỗ trợ một số loại Volumes:
- emptyDir: được tạo ra lần đầu tiên khi một Pod được gán cho một node, và tồn tại miễn là Pod đang chạy trên node đó. Khi một Pod được gỡ bỏ từ một node vì bất kỳ lý do gì, dữ liệu trong nó sẽ bị xóa mãi mãi.
- hostPath: gắn kết một tập tin hoặc thư mục từ hệ thống tập tin của các node máy chủ vào pod của bạn.
- gcePersistentDisk: gắn kết một Google Compute Engine (GCE) Persistent Disk vào trong port của bạn. Khi một Pod được gỡ bỏ, nội dung của một PD volume được bảo toàn và volume chỉ là chưa gỡ bỏ.
- awsElasticBlockStore: gắn kết một Amazon Web Services (AWS) EBS Volume vào trong port của bạn. Khi một Pod được gỡ bỏ, nội dung của một EBS volume được bảo toàn và volume chỉ là chưa gỡ bỏ.
- nfs: cho phép chia sẻ NFS (Network File System) hiện có để gắn vào pod của bạn. Khi một Pod được gỡ bỏ, nội dung của một NFS volume được bảo toàn và volume chỉ là chưa gỡ bỏ.
- iscsi: cho phép một volume iSCSI (SCSI trên IP) hiện có để gắn vào pod của bạn. Khi một Pod được gỡ bỏ, nội dung của một iscsi volume được bảo toàn và volume chỉ là chưa gỡ bỏ. 
- flocker: là trình quản lý volume dữ liệu container mã nguồn mở. Nó cho phép một tập dữ liệu Flocker được gắn kết vào một pod. 
- glusterfs: cho phép glusterfs volume (một hệ thống tập tin mã nguồn mở nối mạng) được gắn vào pod của bạn. Khi một Pod được gỡ bỏ, nội dung của một glusterfs volume được bảo toàn và volume chỉ là chưa gỡ bỏ.
- rbd: cho phép Rados Block Device volume được gắn vào pod của bạn. Khi một Pod được gỡ bỏ, nội dung của một rbd volume được bảo toàn và volume chỉ là chưa gỡ bỏ.

Ngoài ra còn có các loại volume khác:
- cephfs
- gitRepo
- secret
- persistentVolumeClaim
- downwardAPI
- azureFileVolume
- azureDisk
- vsphereVolume
- Quobyte
- PortworxVolume
- ScaleIO