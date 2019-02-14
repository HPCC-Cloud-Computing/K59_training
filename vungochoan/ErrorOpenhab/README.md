Em sử dụng docker để chạy openhab, tag image là 2.1.0-adm64, openhab cài đặt onewire binding. Trên máy cài thêm owserver.

Em tạo các file bao gồm: openhab/conf/scripts/onewiretemp.sh, openhab/conf/items/onewire.items, openhab/conf/things/onewire.things, openhab/conf/sitemap/onewire.sitemap

File onewiretemp.sh là 1 file bash để in dữ liệu.

File onewire.things thực hiện chạy file bash onewiretemp.sh

File onewire.items đọc dữ liệu lấy được

File onewire.sitemap hiển thị dữ liệu trên openhab

Khi chạy openhab vào BasicUI xem dữ liệu thì nó chỉ hiện -*C, không thấy dữ liệu.
Đôi khi openhab không kết nối được đến owserver, mặc dù owserver đang chạy.

Đây là tài liệu em tham khảo:
http://docs.openhab.org/addons/bindings/onewire1/readme.html
http://rdlab.cdmt.vn/r-d-publishing/vietnamese
http://www.itbasic.de/openhab-onewire-sensoren-einbinden/
