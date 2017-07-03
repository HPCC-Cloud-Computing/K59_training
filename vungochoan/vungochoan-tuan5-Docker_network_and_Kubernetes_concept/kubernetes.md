# I. Tổng quan
## 1. Kubernetes là gì
Kubernetes là một nền tảng mã nguồn mở giúp tự động triển khai, mở rộng và vận hành các app Container trên các nhóm máy chủ, cung cấp cơ sở hạ tầng tập trung vào container.

### Tại sao lại dùng containers
![](https://kubernetes.io/images/docs/why_containers.svg)

Cách cũ để triển khai ứng dụng là cài đặt ứng dụng trên một máy chủ sử dụng trình quản lý gói hệ điều hành. Điều này gây khó khăn cho việc thực thi, cấu hình, thư viện, và vòng đời giữa các ứng dụng với nhau và với hệ điều hành của máy chủ.

Cách mới là triển khai các container dựa trên OS-level hơn là hardware virtualization. Các container bị cô lập với nhau và từ máy chủ: chúng có hệ thống tệp tin của riêng mình, chúng không thể nhìn thấy tài nguyên của nhau và việc sử dụng tài nguyên tính toán có thể bị giới hạn. Chúng dễ xây dựng hơn các máy ảo, và vì chúng được tách riêng với cơ sở hạ tầng cơ bản, và từ hệ thống tệp tin máy chủ, chúng có thể đi qua clouds và phân bố của hệ điều hành.

## 2. Làm việc với các đối tượng Kubernetes
### 2.1. Tìm hiểu các đối tượng Kubernetes
Kubernetes Objects là các thực thể trong hệ thống Kubernetes. Kubernetes sử dụng các thực thể này để biểu thị trạng thái các cluster. Nó mô tả:
- Ứng dụng container nào đang chạy (và trên các node nào)
- Các tài nguyên sẵn có cho các ứng dụng đó
- Những chính sách xung quanh việc cách ứng dụng đó hoạt động, chẳng hạn như khởi động lại chính sách, nâng cấp và khả năng chịu lỗi.

Để làm việc với các Kubernetes Objects, như thêm, sửa hoặc xóa chúng - bạn cần phải sử dụng API Kubernetes.

#### 2.1.1 Object Spec và Status
Mỗi Kubernetes object bao gồm 2 trường đối tượng lồng nhau quản lý cấu hình của đối tượng: object spec và object status. Spec mô tả trạng thái mong muốn của bạn cho đối tượng - các đặc tính mà bạn muốn các đối tượng có. Status mô tả các trạng thái thực tế của các đối tượng, và được cung cấp, cập nhật bởi hệ thống Kubernetes.

#### 2.1.2 Mô tả một Kubernetes object
Khi tạo một đối tượng trong Kubernetes, bạn phải cung cấp cho object spec mô tả trạng thái mong muốn và một số thông tin cơ bản. Khi bạn sử dụng API Kubernetes để tạo đối tượng (trực tiếp hoặc thông qua `kubectl`), yêu cầu API đó phải bao gồm thông tin là JSON. Thông thường, bạn cung cấp thông tin đến `kubectl` trong tệp **.yaml**

Ví dụ:
```
apiVersion: apps/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```

#### 2.1.3 Phần bắt buộc
Trong tệp tin **.yaml** của Kubernetes object bạn muốn tạo, bạn cần đặt gía trị cho các trường sau:
- `apiVersion` - Phiên bản API Kubernetes nào bạn đang sử dụng để tạo ra đối tượng này
- `kind` - Bạn muốn tạo loại đối tượng nào
- `metadata` - dữ liệu giúp xác định đối tượng là duy nhất, bao gồm name string, UID và tùy chọn namespace.

Bạn cũng cần cung cấp trường object spec. Định dạng đúng của object spec của các Kubernetes object là khác nhau, và chứa các trường lồng nhau của riêng đối tượng đó.

### 2.2 Name
Tất cả các đối tượng trong Kubernetes REST API được xác định rõ ràng bởi một tên và một UID. Đối với các thuộc tính non-unique user-provided, Kubernetes cung cấp label và chú thích.

#### Name
Tên thường được cung cấp bởi khách hàng. Chỉ có một đối tượng của một loại nhất định có thể có một tên được đặt tại một thời điểm. Nhưng nếu bạn xóa một đối tượng, bạn có thể tạo ra một đối tượng mới có cùng tên. Tên được sử dụng trong một tài nguyên URL.

#### UIDs
UID được tạo ra bởi Kubernetes. Mỗi đối tượng được tạo ra trong toàn bộ vòng đời của một Kubernetes cluster có một UID riêng biệt.

### 2.3 Namespace
Kubernetes hỗ trợ nhiều virtual clusters bởi cùng một physical cluster. Các virtual clusters này được gọi là namespace. Namespace giúp cô lập các project, team hay các khách hàng trên cùng 1 cluster với nhau.


#### Khi nào sử dụng nhiều namespace
Namespace được sử dụng trong môi trường với nhiều người dùng trải rộng trên nhiều nhóm hoặc nhiều project. Đối với các nhóm có một vài đến vài chục người dùng, bạn không cần phải tạo hoặc suy nghĩ về namespace nào cả. Sử dụng namespace khi bạn cần các tính năng mà chúng cung cấp.

Namespace cung cấp phạm vi cho tên. Tên của tài nguyên cần phải là duy nhất trong một namespace.

Namespace là một cách phân chia các tài nguyên của cluster giữa nhiều lần sử dụng (thông qua resource quota).

#### Làm việc với namespace
##### Xem namespace
```
$ kubectl get namespaces
NAME          STATUS    AGE
default       Active    1d
kube-system   Active    1d
```

Kubernetes bắt đầu với hai không gian tên ban đầu:
- **default** Namespace mặc định cho các đối tượng không có namespace.
- **kube-system** Namespace cho các đối tượng được tạo bởi hệ thống Kubernetes

##### Cài đặt namespace cho một request
```
$ kubectl --namespace=<insert-namespace-name-here> run nginx --image=nginx
$ kubectl --namespace=<insert-namespace-name-here> get pods
```

### 2.4 Label
Label là cặp key/value gắn liền với các đối tượng, chẳng hạn như pod. Label được sử dụng để xác định thuộc tính của các đối tượng có ý nghĩa và có liên quan đến người dùng. Label có thể được sử dụng để tổ chức và chọn các tập hợp con của đối tượng. Label có thể gắn liền với đối tượng trong thời gian tạo và có thể thêm hoặc sửa đổi bất kỳ lúc nào. Mỗi đối tượng có thể có một bộ label key/value được xác định. Mỗi key phải là duy nhất cho một đối tượng.

### 2.5 Annotations
Bạn có thể chọn label hoặc annotation để đính kèm metadata vào đối tượng Kubernetes. Label có thể được sử dụng để chọn các đối tượng và tìm các collection của đối tượng đáp ứng được một số điều kiện nhất định. Ngược lại các annotation không được sử dụng để xác định và chọn đối tượng. Metadata trong annotation có thể nhỏ hoặc lớn, có cấu trúc hoặc không có cấu trúc và có thể bao gồm các ký tự mà label không cho phép.

# II. Kubernetes Architecture
## 1.Nodes
### Định nghĩa
Một node là một worker machine trong Kubernetes. Một node có thể là một máy ảo hoặc máy vật lý, tùy thuộc vào cluster. Mỗi node có các dịch vụ cần thiết để chạy các pod và được quản lý bởi master conponent. Các dịch vụ trên một node bao gồm Docker, kubelet và kube-proxy.

### Trạng thái node
Trạng thái node chứa các thông tin sau:
- Addresses
- Phase
- Condition
- Capacity
- Info

#### Addresses
Việc sử dụng các trường này tùy thuộc vào nhà cung cấp cloud của bạn hoặc bare metal configuration.
- HostName: Tên máy chủ lưu trữ được report bởi nhân của node. Có thể được ghi đè bằng tham số **`--hostname-override`**.
- ExternalIP: Thông thường địa chỉ IP của node có thể được định tuyến bên ngoài (có sẵn từ bên ngoài cluster).
- InternalIP: Thông thường địa chỉ IP của node chỉ có thể định tuyến trong cluster.

#### Phase
Node phase không còn được sử dụng.

#### Condition
Trường Condition mô tả trạng thái của tất cả các node đang chạy
| Node Condition | Description |
| ------ | ------ |
| OutOfDisk | **True** nếu không có đủ không gian trống trên node để thêm các pod mới, ngược lại là **False**|
| Ready | **True** nếu node đó khỏe mạnh và sẵn sàng chấp nhận pod, **False** nếu node không khỏe mạnh và không chấp nhận pod, **Unknown** nếu node controller không nghe thấy từ node trong 40 giây cuối|
| MemoryPressure | **True** nếu node không có sức ép memory, ngược lại là **False**|
| DiskPressure | **True** nếu không có sức ép disk, ngược lại là **False** |

#### Capacity
Mô tả các tài nguyên sẵn có trên node: CPU, bộ nhớ và số lượng tối đa các pod có thể được lên kế hoạch trên node.

#### Info
Thông tin chung về node, chẳng hạn như phiên bản kernel, phiên bản Kubernetes (phiên bản kubelet và kube-proxy), phiên bản Docker (nếu được sử dụng), tên hệ điều hành. Info được thu thập bởi Kubelet từ node.

### Management
Không giống như pod và các service, một node vốn không phải được tạo ra bởi Kubernetes: nó được tạo ra từ bên ngoài bởi các nhà cung cấp cloud, hoặc tồn tại trong pool của máy vật lý hay máy ảo. Khi Kubernetes tạo ra một node, nó chỉ là tạo ra một đối tượng đại diện cho node. Sau khi tạo, Kubernetes sẽ kiểm tra xem node có hợp lệ hay không. Nếu hợp lệ, nó có đủ điều kiện để chạy một pod. Nếu không hợp lệ, nó sẽ bị bỏ qua trong các hoạt động của cluster. Lưu ý rằng, Kubernetes sẽ gĩư lại các node không hợp lệ, trừ khi nó bị xóa bởi client, và nó sẽ tiếp tục kiểm tra xem node có hợp lệ hay không.

Hiện tại, có ba thành phần tương tác với giao diện Kubernetes node: node controller, kubelet và kubectl.


#### Node Controller
Node Controller là một Kubernetes master component quản lý các khía cạnh khác nhau của các node.

Node Controller có nhiều vai trò trong vòng đời của một Node. Đầu tiên là gán một khối CIDR cho node khi nó được tạo (nếu CIDR được bật).

Thứ hai là duy trì danh sách bên trong node controller của node cập nhật với danh sách các máy có sẵn của nhà cung cấp cloud.

Thứ ba là theo dõi tình trạng của các node. Node controller có trách nhiệm cập nhật trạng thái NodeReady của NodeStatus thành ConditionUnknown nếu không thể truy cập được node.

#### Tự tạo node
Khi **`--register-node`** là true, kubelet sẽ cố gắng đăng ký chính nó với API server. Để tự đăng ký, kubelet được bắt đầu với các option:
- **`--api-servers`** Vị trí của apiserver.
- **`--kubeconfig`** Đường dẫn tới các chứng chỉ để xác thực chính nó với apiserver.
- **`--cloud-provider`** Cách nói chuyện với nhà cung cấp cloud để đọc metadata về chính nó.
- **`--register-node`** Tự động tạo với  API server
- **`--register-with-taints`** Tạo các node với danh sách các taints nhất định
- **`--node-ip`** Địa chỉ IP của node.
- **`--node-labels`** Label để thêm khi tạo node trong cluster.
- **`--node-status-update-frequency`** Xác định tần suất kubelet posts node status đến master.

#### Node capacity
Dung lượng của node (số lượng CPU và dung lượng bộ nhớ) là một phần của đối tượng node. Thông thường, các node tự tạo và báo cáo dung lượng của chúng khi tạo đối tượng node. Nếu quản lý node thủ công thì bạn cần thiết lập dung lượng node khi thêm node.

## 2. Master-Node communication
### Tổng quan
Tài liệu này liệt kê các đường dẫn truyền thông giữa các master (apiserver) và Kubernetes cluster. Mục đích là để cho phép người dùng tùy chỉnh cài đặt để làm cứng cấu hình mạng sao cho cluster có thể chạy trên một mạng không đáng tin cậy (hoặc trên các IP công cộng trên một nhà cung cấp cloud).

### Cluster -> Master
Tất cả các đường dẫn truyền thông từ cluster đến master sẽ kết thúc tại apiserver (không có master component nào được thiết kế để expose các dịch vụ từ xa). Các apiserver được cấu hình để lắng nghe các kết nối từ xa trên một cổng HTTPS an toàn (443) với một hoặc nhiều form client xác thực được kích hoạt.

Node cần được cung cấp với chứng chỉ root công khai cho cluster sao cho chúng có thể kết nối an toàn với apiserver cùng với chứng chỉ client hợp lệ.

Pod muốn kết nối với apiserver có thể thực hiện bằng cách tận dụng tài khoản dịch vụ để Kubernetes tự động chèn vào chứng chỉ root công cộng và một token hợp lệ vào pod khi nó được khởi tạo. Các dịch vụ `kubernetes` (trong tất cả các namespace) được cấu hình với một địa chỉ IP ảo và được chuyển hướng (thông qua Kube-proxy) cho HTTPS endpoints trên apiserver.

Các master component kết nối với cluster apiserver qua cổng không an toàn (không được mã hóa hoặc chứng thực). Cổng này thường chỉ được hiển thị trên giao diện localhost của máy chủ, do đó các master component, tất cả chạy trên cùng một máy, có thể giao tiếp với cluster apiserver. Theo thời gian, các master component sẽ được di chuyển để sử dụng cổng an toàn với xác thực và ủy quyền.

### Master -> Cluster
Có hai đường liên lạc chính từ master (apiserver) đến cluster. Đầu tiên là từ apiserver đến quá trình kubelet chạy trên mỗi node trong cluster. Thứ hai là từ apiserver đến node, pod hoặc service bất kỳ thông qua chức năng proxy của apiserver.

#### Apiserver -> kubelet
Các kết nối từ apiserver đến kubelet được sử dụng để tìm kiếm các bản ghi cho các pod, gắn kết (thông qua kubectl) với các pod đang chạy, và sử dụng chức năng kubelet port-forwarding. Các kết nối này kết thúc tại điểm cuối HTTPS của kubelet.

Theo mặc định, máy apiserver không xác minh chứng chỉ phục vụ của kubelet, làm cho kết nối này bị tấn công man-in-the-middle, và không an toàn khi chạy qua các mạng không tin cậy và/hoặc mạng public.

Để xác minh kết nối này, sử dụng **`--kubelet-certificate-authority`** để cung cấp cho apiserver một gói chứng chỉ root để sử dụng để xác minh chứng chỉ phục vụ của kubelet.

Nếu không thể, sử dụng đường hầm SSH giữa apiserver và kubelet để tránh kết nối qua mạng không tin cậy hoặc mạng public.

Cuối cùng,Kubelet xác thực và/hoặc ủy quyền được kích hoạt để đảm bảo API kubelet.

#### Apiserver -> node, pod và service
Các kết nối từ apiserver đến node, pod hoặc service mặc định là kết nối HTTP thông thường, do đó không được chứng thực hay mã hóa.

#### Đường hầm SSH
Google Container Engine sử dụng đường hầm SSH để bảo vệ đường dẫn truyền thông của Master -> Cluster. Trong này, apiserver sẽ khởi tạo một đường hầm SSH tới mỗi node trong cluster (kết nối đến máy chủ ssh nghe trên cổng 22) và truyền tất cả các lưu lượng cho một kubelet, node, pod, hoặc service qua đường hầm.

# III. Containers
## 1. Images
Bạn tạo image Docker và push nó vào một registry trước khi đề cập đến nó trong Kubernetes pod.

Tính chất **image** của một container hỗ trợ cú pháp giống như lệnh **docker**.

### Updating Images
Kubernetes sẽ không pull một image nếu nó đã tồn tại. Nếu bạn không chỉ định tag của image, nó sẽ được gỉa sử là **`:latest`**. Lưu ý rằng bạn nên tránh sử dụng **`:latest`** tag.

## 2. Container Environment Variables
### Container environment
Môi trường container Kubernetes cung cấp một số tài nguyên quan trọng cho container:
- Một hệ thống tệp tin, là sự kết hợp của một image và một hoặc nhiều volumes.
- Thông tin về chính container
- Thông tin về các đối tượng khác trong cluster.

#### Thông tin container
Tên hostname của một container là tên của Pod, trong đó container đang chạy. Nó có sẵn thông qua lệnh **hostname** hay gọi hàm `gethostname` trong libc.

Tên Pod và không gian tên có sẵn dưới dạng các biến môi trường thông qua **downward API**.

#### Thông tin cluster
Một danh sách chứa tất cả các service đang chạy khi một container được tạo ra là có sẵn cho container đó như các biến môi trường. Những biến môi trường phù hợp với cú pháp của liên kết Docker.

## 3. Container Lifecycle Hooks
Tương tự như nhiều framework ngôn ngữ lập trình có component lifecycle hooks, Kubernetes cung cấp Containers với các lifecycle hooks. Hooks cho phép Container nhận biết được các sự kiện trong vòng đời quản lý của chúng và code được thực hiện trong một handler khi hook lifecycle tương ứng được thực thi.

### Container hooks
Có 2 hooks được tiếp xúc với Containers:

**PostStart**

Hook này thực hiện ngay sau khi một container được tạo ra. Tuy nhiên không có gì đảm bảo rằng hook này sẽ thực thi trước container ENTRYPOINT. Không có tham số nào được truyền cho handler.

**PreStop**

Hook này được gọi ngay trước khi container được kết thúc. Đó là chặn, có nghĩa là nó đồng bộ, do đó nó phải hoàn thành trước khi lời gọi xóa các container được gửi. Không có tham số nào được truyền cho handler.

#### Hook xử lý triển khai
Container có thể truy cập vào hook bằng cách thực hiện và tạo một handler cho hook đó. Có 2 loại hook xử lý có thể được thực hiện cho container:
- Exec - Thực hiện một lệnh cụ thể, chẳng hạn như **`pre-stop.sh`** bên trong cgroups và namespace của container. Tài nguyên được tiêu thụ bởi lệnh này được tính vào container.
- HTTP - Thực hiện một HTTP request đối với một endpoint xác định trên container.

#### Hook xử lý thực hiện
Khi một hook quản lý vòng đời của container được gọi, hệ thống quản lý Kubernetes sẽ thực hiện xử lý trong container được tạo ra bởi hook đó.

Hook xử lý các lời gọi được đồng bộ trong bối cảnh của Pod chứa container. Điều này có nghĩa là đối với hook **`PostStart`**, container ENTRYPOINT và hook fire không đồng bộ. Tuy nhiên nếu hook mất quá nhiều thời gian để chạy hoặc treo, container sẽ không đạt được trạng thái **`running`**.

Tương tự đối với hook **`PreStop`**. Nếu hook treo trong quá trình thực hiện, Pod sẽ ở trạng thái **`running`** và không bị **`failed`**. Nếu một hook **`PostStart`** hoặc **`PreStop`** bị lỗi, container sẽ bị chết.

# IV. Workloads
## 1. Pods
### 1.1 Tổng quan về Pod
Pod là khối xây dựng cơ bản của Kubernetes - đơn vị nhỏ nhất và đơn giản nhất trong mô hình đối tượng Kubernetes mà bạn tạo ra hoặc triển khai. Một Pod đại diện cho một tiến trình đang chạy trên cluster của bạn.

Một Pod bao gồm một app container (hoặc nhiều container), các tài nguyên lưu trữ, một mạng IP duy nhất và các option để tùy chỉnh các container. Một Pod đại diện cho một đơn vị triển khai: một ví dụ của một ứng dụng trong Kubernetes, có thể có một container đơn hoặc một số lượng nhỏ các container được kết nối chặt chẽ và chia sẻ tài nguyên.

Pods được sử dụng theo một số cách trong Kubernetes cluster như sau:
- Pods chạy một container: Mô hình "one-container-per-Pod" là trường hợp phổ biến nhất. Trong đó Pods như một cái vỏ bao xung quanh container, và Kubernetes quản lý Pods chứ không trực tiếp quản lý container.
- Pods chạy nhiều container cùng làm việc với nhau: Một Pod có thể gói gọn một ứng dụng bao gồm nhiều container được kết nối chặt chẽ và cần chia sẻ tài nguyên. Pod bao gồm các container và các tài nguyên lưu trữ như một thực thể và quản lý nó.

Mỗi Pod chạy một thể hiện duy nhất của một ứng dụng nhất định. Nếu bạn muốn scale ứng dụng theo chiều ngang (ví dụ chạy nhiều thể hiện), bạn nên sử dụng nhiều Pods, một Pod cho một thể hiện. Trong Kubernetes, điều này thường được gọi là sao chép . Các bản sao lặp lại thường được tạo và quản lý bởi một nhóm trừu tượng gọi là Controller.

#### Làm thế nào Pods quản lý nhiều Containers
Pods được thiết kế để hỗ trợ nhiều quá trình hợp tác (như container) tạo thành một đơn vị kết hợp của service. Các container trong một Pod được tự động định vị và lập lịch trên cùng một máy ảo hoặc vật lý trong cluster. Các container có thể chia sẻ tài nguyên, phụ thuộc, giao tiếp và phối hợp với nhau.

Lưu ý rằng nhóm nhiều co-located và co-managed trong một pod đơn là một trường hợp sử dụng tương đối khó. Bạn chỉ nên sử dụng nó trong các trường hợp cụ thể mà trong đó các container được liên kết chặt chẽ. Ví dụ: bạn có thể có một container hoạt động giống như một web server cho các file trong một volume chia sẻ, và một container "sidecar" riêng biệt cập nhật các file đó từ một nguồn từ xa, như trong sơ đồ sau:

![](https://kubernetes.io/images/docs/pod.svg)

Pods cung cấp hai loại tài nguyên chia sẻ: networking và storage

##### Networking
Mỗi Pod được gán một địa chỉ IP duy nhất. Các container trong một Pod chia sẻ network namespace bao gồm địa chỉ IP và cổng mạng, có thể giao tiếp với nhau thông qua **`localhost`**. Khi các container giao tiếp với các thực thể bên ngoài, chúng phải sử dụng tài nguyên mạng chia sẻ (như các cổng).

##### Storage
Một Pod có thể chỉ định một tập hợp các volume lưu trữ chia sẻ. Tất cả các container trong Pod có thể truy cập đến các volume chia sẻ, cho phép các container chia sẻ dữ liệu. Volumes cũng cho phép dữ liệu tồn tại khi một container khởi động lại.

#### Làm việc với Pod
Không nên nhầm lẫn giữa việc khởi động lại container trong Pod với việc khởi động lại Pod. Bản thân Pod không chạy, nhưng nó là môi trường để các container hoạt động và tồn tại đến khi nó bị xóa.

Pod không có khả năng tự phục hồi. Nếu một Pod được lập lịch đến một Node không thành công, hoặc nếu bản thân quá trình lập lịch không thành công, Pod sẽ bị xóa. Tương tự, Pod sẽ không tồn tại nếu nó gặp trục trặc do thiếu tài nguyên hoặc bảo trì Node.

##### Pod and Controller
Một Controller có thể tạo và quản lý nhiều Pod, xử lý nhân rộng, triển khai và cung cấp khả năng self-healing ở phạm vi cluster. Ví dụ: nếu một Node bị lỗi, Controller có thể tự động thay thế Pod bằng cách lập lịch một sự thay thế giống nhau trên một Node khác.

Một vài ví dụ của Controller chứa một hoặc nhiều Pod bao gồm:
- Deployment
- StatefulSet
- DaemonSet

### 1.2 Pod Lifecycle
#### Pod phase
Pod phase là một bản tóm tắt đơn giản, cấp cao về nơi Pod ở trong vòng đời của nó. Các giá trị có thể có cho **`phase`**:
- Pending: Pod đã được chấp nhận bởi hệ thống Kubernetes nhưng một hoặc nhiều image container không được tạo ra. Điều này bao gồm thời gian trước khi được lập lịch cũng như thời gian tải các image, sẽ mất một khoảng thời gian.
- Running: Pod đã được ràng buộc với một node, và tất cả các container đã được tạo. Ít nhất một container vẫn đang chạy, hoặc đang trong quá trình khởi động hoặc khởi động lại.
- Succeeded: Tất cả các container trong Pods đã kết thúc thành công, và sẽ không được khởi động lại.
- Failed: Tất cả các Container trong Pod đã bị kết thúc, và ít nhất một Container đã bị hủy. Tức là, Container hoặc đã thoát với trạng thái khác 0 hoặc đã bị hệ thống kết thúc.
- Unknown: Đối với một số lý do, trạng thái của Pod không thể đạt được, thông thường do một lỗi trong giao tiếp với các máy chủ của Pod.

#### Pod condition
Mỗi Pod có một PodStatus, trong đó có một mảng PodCondition. Mỗi phần tử của mảng PodCondition có một trường **`type`** và một trường **`status`**. Trường **`type`** là một chuỗi, với gía trị có thể: PodScheduled, Ready, Initialized và Unschedulable. Trường **`status`** là một chuỗi, với gía trị có thể: True, False và Unknown.

#### Container probes
Một Probe là một chuẩn đoán được thực hiện định kỳ bởi kubelet trên một container. Để thực hiện một chuẩn đoán, kubelet gọi một Handler được thực hiện bởi Container. Có 3 loại handler:
- ExecAction: Thực hiện một lệnh được chỉ định bên trong Container. Chuẩn đoán là thành công nếu lệnh xuất hiện với mã trạng thái là 0.
- TCPSocketAction: Thực hiện kiểm tra TCP với địa chỉ IP của Container trên một cổng được chỉ định. Chuẩn đoán là thành công nếu cổng mở.
- HTTPGetAction: Thực hiện một HTTP Get request với địa chỉ IP của Container trên một cổng và đường dẫn được chỉ định. Chuẩn đoán là thành công nếu response có mã trạng thái >= 200 và < 400.

Mỗi một probe có một trong ba kết quả:
- Success: Container vượt qua việc chuẩn đoán.
- Failure: Container thất bại trong việc chuẩn đoán.
- Unknown: Chuẩn đoán không thành công, do đó không có hành động nào được thực hiện.

Kubelet có thể tùy ý thực hiện và phản ứng với 2 loại probe khi chạy container:
- **`livenessProbe`**: Cho biết container đang chạy hay không. Nếu liveness probe không thành công, kubelet sẽ kill Container, và Container phải tuân theo chính sách khởi động lại của nó. Nếu một Container không cung cấp một liveness probe, trạng thái mặc định là **`Success`**.
- **`readinessProbe`**: Cho biết Container đã sẵn sàng để yêu cầu dịch vụ hay không. Nếu readiness probe không thành công, endpoint controller sẽ xóa địa chỉ IP của Pod khỏi các endpoint của tất cả các service ứng với Pod.

### 1.3 Init Containers
#### Tìm hiểu Init Container
Một Pod có thể có nhiều Container chạy các ứng dụng bên trong nó, nhưng nó cũng có thể có một hoặc nhiều Init Container, được chạy trước khi app Containers được chạy.

Init container giống với container thông thường, ngoại trừ:
- Chúng luôn chạy đến khi kết thúc
- Mỗi cái phải kết thúc thành công trước khi cái tiếp theo được bắt đầu

Nếu một Init Container chạy thất bại, Kubernetes khởi động lại Pod cho đến khi Init Container thành công. Tuy nhiên, nếu trường **`restartPolicy`** của Pod có gía trị Never thì không phải khởi động lại.

Để chỉ định là một Init Container, hãy thêm trường **`initContainers`** trên PodSpec dưới dạng mảng JSON của các đối tượng thuộc loại v1.Container bên cạnh mảng app container. Trạng thái của các Init Container được trả về trong trường **`status.initContainerStatuses`** như một mảng các trạng thái container (tương tự như trường **`status.containerStatues`**).

##### Khác biệt với các container thông thường
Init Containers hỗ trợ tất cả các lĩnh vực và tính năng của app container, bao gồm giới hạn tài nguyên, volumes và cài đặt bảo mật. Tuy nhiên các yêu cầu và giới hạn về tài nguyên của một Init Container được xử lý hơi khác. Ngoài ra Init Container không hỗ trợ readiness probes bởi vì chúng phải chạy đến khi kết thúc trước khi Pod có thể sẵn sàng.

Nếu có nhiều Init Container được chỉ định cho một Pod, những container này sẽ  được chạy tuần tự. Cái trước phải chạy thành công trước khi cái sau chạy. Khi tất cả các Init Container kết thúc, Kubernetes sẽ khởi tạo Pod và chạy app Container như bình thường.

#### Init Container có thể được sử dụng để làm gì
Vì các Init Container chứa các image riêng biệt từ các app container, chúng có một số start-up related code:
- Chúng có thể chứa và chạy các tiện ích không mong muốn bao gồm app container image với lý do bảo mật.
- Chúng có thể chứa các tiện ích hoặc custom code để thiết lập những cái không có trong app image. Ví dụ không cần phải làm một image **`FROM`** image khác chỉ để sử dụng tool như **`sed`**, **`awk`**, **`python`**, **`dig`** trong quá trình cài đặt.
- The application image builder và deployer roles có thể hoạt động độc lập mà không cần phải cùng nhau xây dựng một app image.
- Chúng sử dụng Linux namespaces để có các cách khác nhau có thể xem hệ thống tệp tin từ các app Container. Do đó, chúng có thể được cấp quyền truy cập đến Secret mà các app Container không thể truy cập.
- Chúng chạy đến khi hoàn thành trước khi bất kỳ app Containers nào bắt đầu, trong khi đó app Containers chạy song song, do đó Init Container cung cấp một cách đơn giản để chặn hoặc trì hoãn việc khởi động app Containers cho đến khi một số điều kiện tiên quyết được đáp ứng.

##### Init Container in use
Ta sẽ tạo ra 1 pod đơn giản trong đó có 2 Init Container. Đầu tiên là **`myservice`**, tiếp theo là **`mydb`**. Khi cả 2 container này hoàn thành, Pod sẽ bắt đầu.

Với phiên bản Kubernetes v1.6:
```
apiVersion: v1
kind: Pod
metadata:
  name: myapp-pod
  labels:
    app: myapp
spec:
  containers:
  - name: myapp-container
    image: busybox
    command: ['sh', '-c', 'echo The app is running! && sleep 3600']
  initContainers:
  - name: init-myservice
    image: busybox
    command: ['sh', '-c', 'until nslookup myservice; do echo waiting for myservice; sleep 2; done;']
  - name: init-mydb
    image: busybox
    command: ['sh', '-c', 'until nslookup mydb; do echo waiting for mydb; sleep 2; done;']
```

#### Detailed behavior
Trong quá trình khởi động của một Pod, Init Containers được khởi động theo thứ tự, sau khi network và volume được khởi tạo. Một Pod không thể **`Ready`** nếu tất cả các Init container chưa thành công.

Nếu Pod khởi động lại, tất cả Init Containers sẽ thực hiện lại.

Các thay đổi đối với Init Container spec được giới hạn trong trường container image. Thay đổi trường container image bằng với việc khởi động lại Pod.

Tên của mỗi app và Init Container trong một Pod phải là duy nhất.

##### Lý do Pod khởi động lại
Một Pod có thể khởi động lại, gây ra việc thực hiện lại các Init Containers, vì những lý do sau:
- Một người dùng cập nhật PodSpec làm cho Init Container image thay đổi. Thay đổi app Container image chỉ khởi động lại app Container.
- Pod infrastructure container được khởi động lại. Điều này ít khi xảy ra và phải được thực hiện bởi một người có quyền truy cập root vào các Node.
- Tất cả các container trong Pod bị ngắt, trong khi **`restartPolicy`** được thiết lập là Always, bắt buộc phải khởi động lại và bản ghi hoàn thành của Init Container đã bị mất do thu gom rác. 

## 2. Controller
### 2.1. Replica Sets
ReplicaSet là thế hệ kế tiếp của Replication Controller. Sự khác biệt duy nhất giữa ReplicaSet và Replication Controller là selector support. ReplicaSet hỗ trợ các yêu cầu new set-based selector. Trong khi Replication Controller chỉ hỗ trợ các yêu cầu equality-based selector.

### 2.2. Replication Controller
Một Replication Controller đảm bảo rằng một pod hay homogeneous set (bộ đồng nhất) của pod luôn sẵn sàng và sẵn có. Nếu có quá nhiều pod, nó sẽ xóa bớt đi, nếu có quá ít, nó sẽ khởi động nhiều hơn. Không giống như các pod được tạo thủ công, các pod được duy trì bởi một ReplicationController sẽ tự động được thay thế nếu chúng bị lỗi, bị xóa hoặc bị kết thúc.

Một trường hợp đơn giản là tạo một đối tượng ReplicationController để chạy một thể hiện của một Pod. Một trường hợp sử dụng phức tạp hơn là chạy một số bản sao giống nhau của một replicated service, ví dụ như các web server.

#### Ví dụ một ReplicationController
Đây là một ví dụ cấu hình ReplicationController. Nó chạy 3 bản sao của nginx web server.
```
apiVersion: v1
kind: ReplicationController
metadata:
  name: nginx
spec:
  replicas: 3
  selector:
    app: nginx
  template:
    metadata:
      name: nginx
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx
        ports:
        - containerPort: 80
```

#### Viết một ReplicationController Spec
##### Pod Template
**`.spec.template`** là trường bắt buộc duy nhất của **`.spec`**.

**`.spec.template`** là một pod template. Nó giống như schema của Pod, ngoại trừ nó được lồng và không có **`apiVersion`** hoặc **`kind`**.

Ngoài các trường bắt buộc của Pod, pod template trong một ReplicationController phải chỉ rõ label thích hợp (nghĩa là không chồng chéo với các controller khác) và chính sách khởi động lại thích hợp.

**`.spec.template.spec.restartPolicy`** chỉ được phép là **`Always`**. là default nếu nó không được chỉ định.

##### Labels trên ReplicationController
Các ReplicationController có thể tự nó có label (**`.metadata.labels`**). Thông thường bạn sẽ thiết lập nó là **`.spec.template.metadata.labels`**; nếu **`metadata.labels`** không được chỉ định thì nó sẽ mặc định là **`.spec.template.metadata.labels`**. Tuy nhiên chúng được cho phép khác nhau, và **`metadata.labels`** không ảnh hưởng đến hành vi của ReplicationController.

##### Pod Selector
Trường **`.spec.selector`** là một label selector. Một replication controller quản lý tất cả các pod với các label khớp với selector. Nó không phân biệt việc các pod được tạo ra hay bị xóa do nó làm hay do người khác hoặc quá trình làm. Điều này cho phép ReplicationController được thay thế mà không ảnh hưởng đến các pod đang chạy.

Nếu được chỉ định, **`.spec.template.metadata.labels`** phải bằng **`.spec.selector`**, hoặc nó sẽ bị API từ chối. Nếu **`.spec.selector`** không xác định, nó sẽ được mặc định là **`.spec.template.metadata.labels`**.

##### Multiple Replicas
Bạn có thể chỉ định số lượng các Pod chạy đồng thời bằng cách thiết lập **`.spec.replicas`**. Nếu không chỉ định, **`.spec.replicas`** mặc định là 1.

#### Làm việc với ReplicationControllers
##### Xóa một ReplicationController và các Pod của nó
Để xóa một ReplicationController và tất cả các Pod của nó, sử dụng **`kubectl delete`**. Kubectl sẽ scale ReplicationController về 0 và chờ cho nó xóa từng Pod trước khi xóa ReplicationController. Nếu lệnh này bị ngắt, nó có thể được khởi động lại.

##### Chỉ xóa một ReplicationController
Bạn có thể xóa một ReplicationController mà không ảnh hưởng đến các Pod của nó. Sử dụng **`kubectl delete`** với option **`cascade=false`**.

Khi sử dụng REST API hoặc go client library, chỉ cần xóa đối tượng ReplicationController.

Một khi bản gốc bị xóa, bạn có thể tạo một ReplicationController mới để thay thế. Miễn **`.spec.selector`** của bản cũ và bản mới là như nhau, sau đó bản mới sẽ chấp nhận các Pod cũ. Tuy nhiên nó sẽ không thực hiện bất kỳ điều gì để làm cho các Pod hiện có phù hợp với một pod template khác.

##### Cô lập các Pod từ một ReplicationController
Pods có thể được xóa bỏ từ một ReplicationController's target set bằng cách thay đổi label của chúng. Kỹ thuật có thể sử dụng để loại bỏ các Pod từ service để debugging, phục hồi dữ liệu,... Các Pod được gỡ bỏ theo cách này sẽ được thay thế tự động (gỉa sử số lượng các replicas không thay đổi).

### 2.3. Deployment
Deployment cung cấp thông tin cập nhật cho Pods và ReplicaSets. Bạn chỉ cần mô tả trạng thái mong muốn trong một đối tượng Deployment, và Deployment controller sẽ thay đổi trạng thái thực tế sang trạng thái mong muốn với tỷ lệ được kiểm soát.

Bạn có thể định nghĩa các Deployment để tạo mới ReplicaSets, hoặc gỡ bỏ Deployments hiện tại và sử dụng tất cả các tài nguyên của nó cho Deployments mới.

#### Tạo Deployment
Ví dụ:
```
apiVersion: apps/v1beta1 # for versions before 1.6.0 use extensions/v1beta1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.7.9
        ports:
        - containerPort: 80
```

Chạy ví dụ bằng lệnh:
```
$ kubectl create -f docs/user-guide/nginx-deployment.yaml --record
deployment "nginx-deployment" created
```

### 2.4 StatefulSets
StatefulSets là một Controller cung cấp định dạng duy nhất cho Pods của nó. Nó cung cấp bảo đảm về thứ tự deployment và scaling.

#### Sử dụng StatefulSets
StatefulSets đáp ứng yêu cầu của application:
- Stable, xác định mạng duy nhất
- Stable, lưu trữ liên tục
- Ordered, graceful deployment và scale
- Ordered, graceful deletion và termination.

Stabe đồng nghĩa với sự kiên trì trong việc lập lịch Pod (lại).

#### Các thành phần
Ví dụ dưới đây thể hiện các thành phần của StatefulSet
- Một Headless Service tên là nginx, được sử dụng để kiểm soát miền mạng.
- StatefulSet tên là web, Spec chỉ ra rằng có 3 replicas của các container nginx.
- VolumeClaimTemplates cung cấp stable storage bằng cách sử dụng PersistentVolumes được cung cấp bởi một PersistentVolume Provisioner.

```
apiVersion: v1
kind: Service
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx
---
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 3
  template:
    metadata:
      labels:
        app: nginx
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: nginx
        image: gcr.io/google_containers/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
      annotations:
        volume.beta.kubernetes.io/storage-class: anything
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

### 2.5 DaemonSet
DaemonSet đảm bảo tất cả (hoặc một số) node chạy một bản sao của một pod. Khi một node được thêm vào cluster, các pod sẽ được thêm vào. Xóa một DaemonSet sẽ xóa các Pod do nó tạo ra.

Một số sử dụng điển hình của DaemonSet:
- Chạy một daemon lưu trữ cluster, chẳng hạn như **`glusterd`**, **`ceph`** trên mỗi node.
- Chạy một logs collection daemon trên mỗi node, chẳng hạn như **`fluentd`** hoặc **`logstash`**
- Chạy một node monitoring daemon trên mỗi node

### 2.6 PetSet
Mục tiêu của PetSet là tách riêng sự phụ thuộc bằng cách gán các đặc điểm nhận dạng cho các thể hiện riêng biệt của một ứng dụng không bị gắn kết với cơ sở hạ tầng vật chất bên dưới.

**Mối quan hệ giữa Pets và Pods**: PetSet yêu cầu có {0...N-1} Pets. Mỗi Pet có một tên xác định - PetSetName-Ordinal và một định danh duy nhất. Mỗi Pet có nhiều nhất một Pod, và mỗi PetSet có tối đa một Pet với một định danh nhất định.

#### Ví dụ về PetSet
```
# A headless service to create DNS records
apiVersion: v1
kind: Service
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  # *.nginx.default.svc.cluster.local
  clusterIP: None
  selector:
    app: nginx
---
apiVersion: apps/v1alpha1
kind: PetSet
metadata:
  name: web
spec:
  serviceName: "nginx"
  replicas: 2
  template:
    metadata:
      labels:
        app: nginx
      annotations:
        pod.alpha.kubernetes.io/initialized: "true"
    spec:
      terminationGracePeriodSeconds: 0
      containers:
      - name: nginx
        image: gcr.io/google_containers/nginx-slim:0.8
        ports:
        - containerPort: 80
          name: web
        volumeMounts:
        - name: www
          mountPath: /usr/share/nginx/html
  volumeClaimTemplates:
  - metadata:
      name: www
      annotations:
        volume.alpha.kubernetes.io/storage-class: anything
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

# V. Configuration
## 1. Configuration Best Practices
### General Config Tips
- Khi xác định cấu hình, chỉ định phiên bản API ổn định mới nhất.
- File cấu hình nên được lưu trữ trong version controll trước khi được push vào cluster. Điều này cho phép nhanh chóng roll-back lại cấu hình nếu cần. Nó cũng hỗ trợ việc tái tạo và khôi phục lại cluster nếu cần thiết.
- Viết các file cấu hình bằng YAML chứ không phải JSON. Mặc dù các định dạng này có thể thay thế cho nhau, nhưng YAML có xu hướng thân thiện hơn.
- Nhóm các đối tượng liên quan vào một file. Một file thường dễ quản lý hơn nhiều file.
- Không chỉ định các gía trị mặc định không cần thiết, để đơn giản hóa, giảm bớt cấu hình và giảm lỗi. Ví dụ: bỏ qua selector và label trong **`ReplicationController`** nếu bạn muốn chúng giống như label **`podTemplate`**, vì các trường đó được nhập từ label **`podTemplate`** theo mặc định.
- Đặt một mô tả đối tượng trong một annotation để cho phép theo dõi tốt hơn.

### Services
- Tốt nhất là tạo ra một service trước các replication controller tương ứng. Điều này cho phép scheduler phân bố các pod bao gồm service.

Bạn cũng có thể sử dụng quá trình này để đảm bảo rằng ít nhất một replica hoạt động trước khi tạo ra nhiều hơn:
  1. Tạo một replication controller mà không cần xác định replicas (điều này sẽ thiết lập replicas = 1)
  2. Tạo một service
  3. Sau đó scale up replication controller

-  Không sử dụng **`hostPort`** trừ khi cần thiết (ví dụ: cho một node daemon). Nó chỉ định số cổng để expose trên máy chủ.

Nếu bạn cần expose mọt cổng của Pod hãy xem xét sử dụng NodePort trước khi sử dụng hostPort.

- Tránh sử dụng **`hostNetwork`**, vì những lý do tương tự như **`hostPort`**
- Sử dụng các headless service để tìm service dễ dàng khi bạn không cần kube-proxy cân bằng tải.

### Sử dụng labels
- Labels xác định thuộc tính ngữ nghĩa của ứng dụng hoặc deployment. Ví dụ thay vì gán label vào một tập các pod để mô tả một số service (ví dụ: **service: myservice**), hoặc mô tả cho replication controller quản lý các pod (ví dụ **controller: mycontroller**), hãy đính kèm các label xác định thuộc tính ngữ nghĩa. Điều này sẽ cho phép bạn chọn các nhóm đối tượng thích hợp.
- Bạn có thể dùng label để debugging. Vì các Kubernetes replication controller và các service khớp với các pod sử dụng label, điều này cho phép bạn xóa một pod khỏi controller. Nếu bạn xóa các label hiện có của một pod, controller của nó sẽ tạo ra pod mới.

## 2. Quản lý tính toán tài nguyên cho containers
Khi bạn xác định một pod, bạn có thể chỉ định bao nhiêu CPU và bộ nhớ (RAM) cho container. Khi container yêu cầu tài nguyên, scheduler có thể đưa ra các quyết định tốt hơn về các Node nào để đặt Pod.

### Yêu cầu tài nguyên và giới hạn của Pod và Container
Mỗi Container của Pod có thể chỉ định một hoặc nhiều thứ sau đây:
- **`spec.containers[].resources.limits.cpu`**
- **`spec.containers[].resources.limits.memory`**
- **`spec.containers[].resources.requests.cpu`**
- **`spec.containers[].resources.requests.memory`**

### Ý nghĩa của memory
Giới hạn và yêu cầu của **`memory`** được tính bằng byte. Dưới đây là một ví dụ. Pod có hai Containers. Mỗi Container yêu cầu 0,25 CPU và 64MiB (2^26 byte) memory. Mỗi Container có giới hạn là 0,5 CPU và 128MiB. Bạn có thể nói Pod yêu cầu 0,5 CPU và 128 MiB memory, và giới hạn là 1 CPU và 256 MiB memory.
```
apiVersion: v1
kind: Pod
metadata:
  name: frontend
spec:
  containers:
  - name: db
    image: mysql
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
  - name: wp
    image: wordpress
    resources:
      requests:
        memory: "64Mi"
        cpu: "250m"
      limits:
        memory: "128Mi"
        cpu: "500m"
```
### Làm thế nào Pod yêu cầu tài nguyên được lập lịch
Khi bạn tạo một Pod, Kubernetes scheduler chọn một node cho Pod để chạy trên đó. Mỗi node có công suất tối đa cho mỗi loại tài nguyên: số lượng CPU và memory nó có thể cung cấp cho Pods. Scheduler đảm bảo rằng, đối với từng loại tài nguyên, tổng các request tài nguyên của các Container nhỏ hơn khả năng của node. Lưu ý rằng mặc dù thực tế bộ nhớ hoặc tài nguyên CPU sử dụng trên các node rất thấp, scheduler vẫn từ chối đặt Pod lên node nếu kiểm tra dung lượng lỗi. Điều này bảo vệ chống lại sự thiếu hụt tài nguyên trên node khi việc sử dụng tài nguyên đó tăng lên.

## 3. Secret
Secret là một đối tượng có chứa một lượng nhỏ dữ liệu nhạy cảm như mật khẩu, mã thông báo hoặc khóa. Thông tin này có thể được đặt trong một đặc tả Pod hoặc một image. Đặt nó vào một đối tượng secret sẽ cho phép kiểm soát việc sử dụng chúng.

Người dùng và hệ thống đều có thể tạo secret.

Để sử dụng secret, mỗi pod cần tham chiếu đến secret. Một secret có thể được sử dụng với một Pod theo hai cách: như các file trên một volume gắn trên một hoặc nhiều container của nó, hoặc được sử dụng bởi kubelet khi pull image cho các pod.

### Sử dụng secret
#### Sử dụng secret như các file từ một Pod
Để dùng Secret trong volume trong Pod:
1. Tạo một secret hoặc sử dụng cái đang có. Nhiều pod có thể tham chiếu đến cùng một secret.
2. Sửa đổi định nghĩa Pod để thêm volume dưới dạng **`spec.volumes[]`**. Đặt tên cho volume và có trường **`spec.volumes[].secret.secretName`** bằng với tên của đối tượng secret.
3. Thêm **`spec.containers[].volumeMounts[]`** vào mỗi container cần bí mật. Chỉ định **`spec.containers.volumeMounts[].readOnly = true`** và **`spec.containers[].volumeMounts[].mountPath`** là tên thư mục bạn muốn secret xuất hiện.
4. Sửa đổi image và/hoặc dòng lệnh để chương trình tìm kiếm các file trong thư mục đó. Mỗi key trong secret **`data`** ánh xạ sẽ trở thành tên file dưới **`mountPath`**.

Ví dụ:
```
{
 "apiVersion": "v1",
 "kind": "Pod",
  "metadata": {
    "name": "mypod",
    "namespace": "myns"
  },
  "spec": {
    "containers": [{
      "name": "mypod",
      "image": "redis",
      "volumeMounts": [{
        "name": "foo",
        "mountPath": "/etc/foo",
        "readOnly": true
      }]
    }],
    "volumes": [{
      "name": "foo",
      "secret": {
        "secretName": "mysecret"
      }
    }]
  }
]
```

Mỗi secret bạn muốn sử dụng phải được tham chiếu đến **`spec.volumes`**.

Nếu có nhiều container trong pod, thì mỗi container cần có khối **`volumeMounts`** riêng của nó, nhưng chỉ một **`spec.volumes`** được cần trên secret.

Bạn có thể đóng gói nhiều file vào một secret, hoặc sử dụng nhiều secret, tùy từng trường hợp.

##### Chiếu key của secret tới các đường dẫn cụ thể
Chúng ta cũng có thể kiểm soát các đường dẫn trong volume mà các key secret được dự báo. Bạn có thể sử dụng trường **`spec.volumes[].secret.items`** để thay đổi đường dẫn của mỗi key:
```
{
 "apiVersion": "v1",
 "kind": "Pod",
  "metadata": {
    "name": "mypod",
    "namespace": "myns"
  },
  "spec": {
    "containers": [{
      "name": "mypod",
      "image": "redis",
      "volumeMounts": [{
        "name": "foo",
        "mountPath": "/etc/foo",
        "readOnly": true
      }]
    }],
    "volumes": [{
      "name": "foo",
      "secret": {
        "secretName": "mysecret",
        "items": [{
          "key": "username",
          "path": "my-group/my-username"
        }]
      }
    }]
  }
}
```

**`username`** secret được lưu trữ dưới file **`/etc/foo/my-group/my-username`** thay vì **`/etc/foo/username`**

#### Sử dụng secret giống như biến môi trường
Để sử dụng secret trong một biến môi trường trong một Pod:
1. Tạo một secret hoặc sử dụng cái đang có. Nhiều Pod có thể tham chiếu đến cùng một secret.
2. Sửa đổi định nghĩa Pod trong mỗi container mà bạn muốn dùng gía trị của key secret để thêm một biến môi trường. Biến môi trường dùng key secret nên nhập tên secret và key trong **`env[x].valueFrom.secretKeyRef`**.
3. Sửa đổi image và/hoặc dòng lệnh để chương trình tìm kiếm các gía trị trong các biến môi trường được chỉ định.

Ví dụ:
```
apiVersion: v1
kind: Pod
metadata:
  name: secret-env-pod
spec:
  containers:
    - name: mycontainer
      image: redis
      env:
        - name: SECRET_USERNAME
          valueFrom:
            secretKeyRef:
              name: mysecret
              key: username
        - name: SECRET_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysecret
              key: password
  restartPolicy: Never

```

# VI. Storage
## 1. Volumes
Các tệp trên ổ đĩa trong một container là tạm thời, trong đó nói về một số vấn đề đối với các ứng dụng non-trivial khi chạy trong các container. Thứ nhất, khi một container bị treo, kubelet sẽ khởi động lại nó, nhưng các tệp tin sẽ bị mất, container sẽ bắt đầu lại với trạng thái trống. Thứ hai, khi chạy các container với nhau trong một pod thường cần phải chia sẻ các tệp tin giữa các container. Volume Kubernetes sẽ giải quyết cả hai vấn đề này.

Kubernetes hỗ trợ một số loại Volumes:
- emptyDir: được tạo ra lần đầu tiên khi một Pod được gán cho một node, và tồn tại miễn là Pod đang chạy trên node đó. Khi một Pod được gỡ bỏ từ một node vì bất kỳ lý do gì, dữ liệu trong nó sẽ bị xóa mãi mãi.

Ví dụ:
```
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: gcr.io/google_containers/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /cache
      name: cache-volume
  volumes:
  - name: cache-volume
    emptyDir: {}
```

- hostPath: gắn kết một tập tin hoặc thư mục từ hệ thống tập tin của các node máy chủ vào pod của bạn.

Ví dụ:
```
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: gcr.io/google_containers/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /test-pd
      name: test-volume
  volumes:
  - name: test-volume
    hostPath:
      # directory location on host
      path: /data
```

- gcePersistentDisk: gắn kết một Google Compute Engine (GCE) Persistent Disk vào trong port của bạn. Khi một Pod được gỡ bỏ, nội dung của một PD volume được bảo toàn và volume chỉ là chưa gỡ bỏ.

Ví dụ:
```
apiVersion: v1
kind: Pod
metadata:
  name: test-pd
spec:
  containers:
  - image: gcr.io/google_containers/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /test-pd
      name: test-volume
  volumes:
  - name: test-volume
    # This GCE PD must already exist.
    gcePersistentDisk:
      pdName: my-data-disk
      fsType: ext4
```

- awsElasticBlockStore: gắn kết một Amazon Web Services (AWS) EBS Volume vào trong port của bạn. Khi một Pod được gỡ bỏ, nội dung của một EBS volume được bảo toàn và volume chỉ là chưa gỡ bỏ.

Ví dụ:
```
apiVersion: v1
kind: Pod
metadata:
  name: test-ebs
spec:
  containers:
  - image: gcr.io/google_containers/test-webserver
    name: test-container
    volumeMounts:
    - mountPath: /test-ebs
      name: test-volume
  volumes:
  - name: test-volume
    # This AWS EBS volume must already exist.
    awsElasticBlockStore:
      volumeID: <volume-id>
      fsType: ẽt4
```

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

## 2. Persistent Volumes
Quản lý storage là một vấn đề riêng biệt từ việc quản lý tính toán. Hệ thống con **`PersistentVolume`** cung cấp một API cho người dùng và quản trị viên tóm tắt các chi tiết về cách thức lưu trữ được cung cấp từ cách thức tiêu thụ. Để làm được điều này, có 2 tài nguyên API mới: **`PersistentVolume`** và **`PersistentVolumeClaim`**.

Một **PersistentVolume** (PV) là một phần của bộ nhớ trong cluster đã được cung cấp bởi một administrator. Nó là một tài nguyên trong cluster. PVs là plugin giống Volumes, nhưng có một vòng đời độc lập với bất kỳ pod nào sử dụng PV. Đối tượng API này nắm bắt các chi tiết về việc thực hiện lưu trữ, đó là NFS, iSCSI hoặc hệ thống lưu trữ cụ thể của nhà cung cấp cloud.

Một **`persistentVolumeClaim`** (PVC) là yêu cầu lưu trữ bởi người dùng. Nó cũng tương tự như một pod. Pod tiêu thụ tài nguyên node và PVC tiêu thụ tài nguyên PV. Pod có thể yêu cầu các cấp độ tài nguyên cụ thể (CPU và memory). Claims có thể yêu cầu kích thước cụ thể và chế độ truy nhập (ví dụ, có thể được gắn kết một lần read/write hoặc nhiều lần read-only).

Một **`StorageClass`** cung cấp một cách để administrator mô tả các lớp lưu trữ. Các lớp khác nhau có thể ánh xạ tới các cấp độ, hoặc các chính sách sao lưu, hoặc các chính sách tùy ý do các administrator cluster quyết định.

### PersistentVolume
Mỗi PV chứa một spec và status, đó là đặc tả và trạng thái của volume
```
apiVersion: v1
  kind: PersistentVolume
  metadata:
    name: pv0003
  spec:
    capacity:
      storage: 5Gi
    accessModes:
      - ReadWriteOnce
    persistentVolumeReclaimPolicy: Recycle
    storageClassName: slow
    nfs:
      path: /tmp
      server: 172.17.0.2
```

#### Access Modes
Các chế độ truy cập là:
- ReadWriteOnce - volume có thể được gắn kết như read-write bởi một node duy nhất.
- ReadOnlyMany - volume có thể được gắn kết read-only bởi nhiều node.
- ReadWriteMany - volume có thể được gắn kết như read-write bởi nhiều node.

### PersistentVolumeClaims
Mỗi PVC chứa một spec và status, đó là đặc tả và trạng thái của claim
```
kind: PersistentVolumeClaim
apiVersion: v1
metadata:
  name: myclaim
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 8Gi
  storageClassName: slow
  selector:
    matchLabels:
      release: "stable"
    matchExpressions:
      - {key: environment, operator: In, values: [dev]}

```

#### Access Modes
Giống PV

#### Resources
Claims, giống như Pod, có thể yêu cầu số lượng cụ thể của một tài nguyên. Trong trường hợp này, requests được lưu trữ.

#### Selector
Claims có thể chỉ định một label selector để lọc bộ của volumes. Chỉ các volume có label khớp với selector có thể bị ràng buộc bởi claims. Selector có thể gồm 2 trường:
- MatchLabels - volume phải có một label với gía trị này.
- MatchExpressions - một danh sách các yêu cầu được thực hiện bằng cách xác định key, danh sách các value và toán tử liên quan đến key và value. Các toán tử hợp lệ bao gồm In, NotIn, Exists và DoesNotExist.

Tất cả các yêu cầu từ cả hai **`matchLabels`** và **`matchExpressions`** được ANDed với nhau - tất cả đều phải thỏa mãn để phù hợp.

# VII. Cluster Administration
## 1. Cluster Networking
Kubernetes gỉa định rằng các Pod có thể giao tiếp với nhau. Ta cung cấp cho tất cả các Pod địa chỉ IP của riêng mình, do đó bạn không cần phải tạo các liên kết giữa các Pod và bạn không cần phải ánh xạ các cổng container đến các cổng host.

### Mô hình Kubernetes
Kubernetes áp đặt các yêu cầu cơ bản sau cho bất kỳ việc thực hiện mạng nào (trừ các chính sách phân đoạn mạng cố định):
- Tất cả các container có thể giao tiếp với nhau mà không có NAT.
- Tất cả các node có thể giao tiếp với các container (và ngược lại) mà không có NAT.
- Địa chỉ IP mà một container nhìn thấy chính là địa chỉ IP tương tự mà người khác xem.

Điều này có nghĩa là trong thực tế bạn không thể chỉ dùng hai máy tính chạy Docker và yêu cầu Kubernetes hoạt động. Bạn phải đảm bảo các yêu cầu cơ bản được đáp ứng.

Trong thực tế, Kubernetes áp dụng các địa chỉ ở phạm vi Pod - các container bên trong Pod chia sẻ network namespaces - bao gồm cả địa chỉ IP. Điều này có nghĩa là các container bên trong một Pod có thể đi tới tất cả các cổng của nhau trên **`localhost`**.

Có một số cách để network model được thực hiện. Ví dụ: Cilium, Flannel, GCE, OpenVSwitch, Weave Net,...

## 2. Logging and Monitoring Cluster Activity
Application và systems logs có thể giúp bạn hiểu những gì đang xảy ra bên trong cluster của bạn. Các bản ghi đặc biệt hữu ích cho việc gỡ rối các vấn đề và giám sát hoạt động của cluster. Hầu hết các ứng dụng có một loạt các cơ chế logging.

Tuy nhiên, các chức năng được cung cấp bởi một container engine hoặc thời gian chạy không đủ cho giải pháp logging hoàn chỉnh. Ví dụ: nếu một container bị treo, một Pod bị thu hồi hoặc một node chết, bạn thường muốn truy cập application's logs. Các log cần có một bộ lưu trữ riêng biệt và vòng đời độc lập với các node, pod hoặc container. Khái niện này được gọi là cluster-level-logging. Kubernetes không cung cấp giải pháp lưu trữ logs nhưng bạn có thể tích hợp vào Kubernetes.

### Basic logging in Kubernetes
Ví dụ:
```
apiVersion: v1
kind: Pod
metadata:
  name: counter
spec:
  containers:
  - name: count
    image: busybox
    args: [/bin/sh, -c,
            'i=0; while true; do echo "$i: $(date)"; i=$((i+1)); sleep 1; done']
```

Để chạy pod sử dụng lệnh:
```
$ kubectl create -f https://k8s.io/docs/tasks/debug-application-cluster/counter-pod.yaml
pod "counter" created
```

Để lấy các log, sử dụng lệnh:
```
$ kubectl logs counter
0: Mon Jan  1 00:00:00 UTC 2001
1: Mon Jan  1 00:00:01 UTC 2001
2: Mon Jan  1 00:00:02 UTC 2001
...
```

Bạn có thể sử dụng **`kubectl logs`** để lấy các log từ một sự kiện trước của một container bằng flag **`--previous`**, trong trường hợp container bị treo.

### Logging at the node level
![](https://kubernetes.io/images/docs/user-guide/logging/logging-node-level.png)

Tất cả mọi thứ một containerized application viết đến **`stdout`** và **`stderr`** được xử lý và chuyển hướng ở đâu đó bằng container engine. Ví dụ, Docker container engine chuyển hướng hai luồng này sang logging driver, được cấu hình trong Kubernetes để ghi vào một file định dạng json.

Theo mặc định, nếu một container khởi động lại, kubelet gĩư container bị hủy bỏ với các log của nó. Nếu một Pod bị đuổi khỏi node, tất cả các container tương ứng cũng sẽ bị đuổi ra, cùng với các log của chúng.

Khi bạn chạy **`kubectl logs`** như trong ví dụ trên, kubelet trên node xử lý yêu cầu và đọc trực tiếp từ file log, trả lại nội dung trong response. Lưu ý: hiện tại nếu một số hệ thống bên ngoài đã thực hiện quay, chỉ có nội dung file log mới nhất sẽ có sẵn thông qua **`kubectl logs`**. Ví dụ nếu có file 10MB, **`logrotate`** thực hiện quay và có 2 file, một file có kích thước 10MB và một file rỗng. **`kubectl logs`** sẽ trả về response trống.

#### System component logs
Có hai loại thành phần hệ thống: những loại chạy trong container và những loại không chạy trong container. Ví dụ:
- Kubernetes scheduler và kube-proxy chạy trong container.
- The kubelet và container runtime, ví dụ như Docker, không chạy trong container.

Trên máy có systemd, the kubelet và container runtime sẽ ghi vào journald. Nếu không có systemd, chúng sẽ ghi vào các file **`.log`** trong **`/var/log`**. Các thành phần hệ thống bên trong container luôn ghi vào **`/var/log`**. Chúng sử dụng library glog.

Tương tự như container logs, system component logs trong **`/var/log`** phải được quay.

### Kiến trúc Cluster-level logging
Mặc dù Kubernetes không cung cấp giải pháp riêng cho cluster-level logging, nhưng có một số cách tiếp cận phổ biến mà ta có thể xem xét:
- Sử dụng một tác tử node-level logging chạy trên mỗi node.
- Include một sidecar container dành riêng cho logging trong một application pod.
- Push logging trực tiếp vào một backend từ bên trong application.

#### sử dụng một node logging agent
![](https://kubernetes.io/images/docs/user-guide/logging/logging-with-node-agent.png)

The logging agent là một công cụ dành riêng để expose logs hoặc push logs vào backend. Thông thường, the logging agent là một container có quyền truy cập vào thư mục có logs file từ tất cả các application container trên node đó.

Sử dụng node-level logging agent là một các tiếp cận phổ biến và khuyến khích sử dụng cho Kubernetes cluster vì nó chỉ tạo ra một agent cho một node, và nó không yêu cầu bất kỳ thay đổi nào đối với các application chạy trên node. Tuy nhiên node-level logging chỉ hoạt động cho applications' standard output và standard error.


