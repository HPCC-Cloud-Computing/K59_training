# 1.Virtualization
## Khái niệm
Virtualization là tạo ra một phiên bản ảo của một số phần mềm, linh kiện trong máy tính hay thậm chí là ảo hóa toàn bộ chiếc máy tính.

Các loại ảo hóa:

- Ảo hóa hệ điều hành: Tạo ra nhiều máy ảo trên một máy tính duy nhất, có thể chạy song song cùng lúc 2 hệ điều hành.

- Ảo hóa phần cứng: Có nhiều loại ảo hóa phần cứng:
    - Ảo hóa toàn phần: Toàn bộ phần cứng của máy tính sẽ được ảo hóa hết để hệ điều hành ảo khác có thể chạy trên đó một cách đầy đủ và bình thường.

    - Ảo hóa một phần: Ảo hóa một số phần cứng nhất định của máy tính để tạo ra đủ tài nguyên cần thiết để chạy một phần mềm nào đó.
    
    - Ảo hóa song song: Tạo ra một lớp giao diện phần mềm để các hệ điều hành ảo và hypervisor có thể giao tiếp với nhau, giảm thiểu thời gian mỗi khi thi hành các câu lệnh trên hệ thống.

- Ổ đĩa ảo: Giúp cho máy tính có thể đọc được các file dạng .ISO, .IMG mà không cần phải ghi ra đĩa.

- Desktop ảo: Một máy chủ trung tâm tạo ra nhiều Desktop ảo cho nhiều người dùng. Họ có thể làm việc từ xa, dùng một máy tính khác hoặc các thiết bị di động để truy cập vào Desktop ảo và làm việc. Tất cả dữ liệu sẽ được xử lý và lưu trữ từ xa ngay trên máy chủ trung tâm.

- Ram ảo:
    Trên hệ thống máy chủ, toàn bộ số RAM thực đang có được gộp thành RAM chung cho hệ thống. Các máy tính con trong hệ thống máy chủ có thể truy cập và sử dụng số RAM ảo này mà không bị giới hạn về mặt phần cứng.

    Trên máy tính cá nhân thường dùng một phần ổ cứng chia ra để làm RAM ảo để giảm tải gánh nặng cho RAM thật khi RAM thật không đủ để xử lý các ứng dụng.

- Máy chủ ảo (VPS): Một máy chủ có thể tạo ra nhiều máy chủ ảo để vận hành các website giúp tiết kiệm chi phí thuê, mua server.

## Các công nghệ virtualization
### Hypervisor
Hypervisor có thể là phần cứng, phần mềm hoặc một bản firmware nào đó chịu trách nhiệm tạo và chạy nhiều máy ảo trên 1 hệ thống. Có loại hypervisor chạy trên hệ điều hành, có loại hypervisor chạy bên dưới hệ điều hành và trực tiếp tương tác với tài nguyên phần cứng.

Phân loại hypervisor:

- Type-1, native or bare-metal hypervisors
    Lớp phần mềm hypervisor chạy trực tiếp trên nền tảng phần cứng máy chủ, không thông qua bất kì một hệ điều hành nào khác. Qua đó, các hypervisor này có khả năng điều khiển, kiểm soát phần cứng máy chủ. Đồng thời nó cũng có khả năng quản lý các hệ điều hành chạy trên nó. Các hệ điều hành sẽ nằm trên các hypervisor rồi đến hệ thống phần cứng. Ví dụ một số hệ thống type-1 như Oracle VM, VMware ESX Server, IBM's POWER Hypervisor,...

- Type-2 or hosted hypervisors
    Lớp hypervisor chạy trên nền tảng hệ điều hành, sử dụng các dịch vụ được hệ điều hành cung cấp để phân chia các tài nguyên tới các máy ảo. Ta xem hypervisor này là một lớp phần mềm riêng biệt, do đó các hệ điều hành khách của máy ảo sẽ nằm trên lớp hypervisor rồi đến hệ điều hành của máy chủ và cuối cùng là hệ thống phần cứng. Ví dụ một số hệ thống type-2 như VMware Server, VMware Workstation, Microsoft Virtual Server,...

![](https://upload.wikimedia.org/wikipedia/commons/e/e1/Hyperviseur.png)

### OS-level
OS-level là một phương pháp ảo hóa server, nơi mà nhân (kernel) của hệ điều hành cho phép tạo và chạy được nhiều container cách ly và an toàn dùng chung 1 hệ điều hành. Ngoài các cơ chế cách ly, kernel thường cung cấp các tính năng quản lý tài nguyên để hạn chế tác động của các hoạt động của một container đối với container khác.

# 2. Virtual machine
## Khái niệm
Máy ảo là một chương trình đóng vai trò như một máy tính ảo. Nó chạy trên hệ điều hành hiện tại - hệ điều hành chủ và cung cấp phần cứng ảo tới hệ điều hành khách. Phần cứng ảo bao gồm CPU ảo, RAM ảo, ổ đĩa cứng, giao diện mạng và những thiết bị khác.

Bạn có thể cài đặt nhiều máy ảo lên máy thực và chỉ bị hạn chế dung lượng bộ nhớ lưu trữ hiện có cho chúng. Chúng ta có thể chuyển đổi qua lại giữa các hệ điều hành đang chạy chỉ với vài thao tác mà không cần khởi động lại PC.

## Các công nghệ tạo VM
### VMware
VMware là một chương trình tạo máy ảo trên máy tính, nó giúp cho một máy tính có thể chạy song song nhiều hệ điều hành thay vì một hệ điều hành trên một máy.

Có các loại VMware là: VMware Workstation, VMware server, VMware vSphere,...

### XEN
Xen là một hypervisor, nó cho phép tận dụng ảo hóa trực tiếp từ phần cứng của thiết bị, từ đó cho phép tạo ra các máy ảo với các hệ điều hành khác nhau mà không phụ thuộc vào hệ điều hành của máy chủ vật lý, các máy ảo được tạo ra cũng có các tài nguyên độc lập và có hiệu suất ổn định hơn.

### Hyper-V
Hyper-V là một phần mềm máy ảo được tích hợp sẵn trên hệ điều hành Windows. Lúc đầu Hyper-V là một phần của Windows Server 2008, tuy nhiên sau đó Microsoft đã tích hợp trên Windows 8 và Windows 10. Tính năng Hyper-V cho phép người dùng cài đặt và quản lý những máy ảo mà không cần phải cài thêm phần mềm từ bên thứ 3.

### KVM
KVM là một công nghệ ảo hóa mới cho phép ảo hóa toàn phần trên nền tảng phần cứng. Máy chủ KVM giống như XEN được cung cấp riêng tài nguyên để sử dụng, tránh việc tranh chấp tài nguyên với máy chủ khác trên cùng node. Máy chủ gốc được cài đặt Linux, nhưng KVM hỗ trợ tạo máy chủ ảo có thể chạy cả Linux, Windows.

# 3.Docker
## Định nghĩa
Docker là là một công cụ được thiết kế để tạo, vẩn chuyển và chạy một ứng dụng bất kì vào trong các container.

Các container cho phép developer đóng gói môi trường chạy của ứng dụng. Bằng cách đó, developer có thể yên tâm rằng ứng dụng sẽ chạy trên bất kỳ máy Linux nào.

## Sự khác biệt giữa Docker và VM
Có thể chạy nhiều máy ảo trên một máy thực nhưng mỗi máy ảo phải tạo ra một hệ điều hành riêng, tài nguyên hệ thống riêng để chạy. Docker cho phép nhiều container có thể chạy trên cùng một máy, sử dụng chung một hệ điều hành và dùng chung tài nguyên.

![](https://i.imgur.com/MJHfm1c.jpg)

## Docker container lightweight
Docker container nhẹ bởi vì nó chạy trên máy thật và dùng chung tài nguyên với chính máy thật nên các container sẽ rất nhẹ, việc khởi động, kết nối, tương tác sẽ nhanh gọn.
