# Apache2
1. File cấu hình của service
- apache2.conf
- ports.conf
- Thư mục conf-available, conf-enabled

2. File cấu hình systemd unit của service
- /lib/systemd/system/apache2.service.d/apache2-systemd.conf

3. Lệnh Enable/disable
- Enable: `systemctl start apache2`
- Disable: `systemctl stop apache2`
- Restart: `systemctl restart apache2`

4. Cấu hình tham số môi trường
