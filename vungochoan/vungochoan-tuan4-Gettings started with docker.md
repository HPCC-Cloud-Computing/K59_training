# Cài đặt Docker CE engine
[Link cài đặt](https://docs.docker.com/engine/installation/linux/ubuntu/#install-using-the-repository)

# Phân biệt các lệnh
**docker run**  
Tạo mới một container và chạy lệnh.  
Lệnh: `docker run [OPTIONS] IMAGE [COMMAND] [ARG...]`  
Các option ([option](https://docs.docker.com/engine/reference/commandline/run/#options)).

**docker start**  
Chạy một hay nhiều container đang bị dừng.  
Lệnh: `docker start [OPTIONS] CONTAINER [CONTAINER...]`  
Các option ([option](https://docs.docker.com/engine/reference/commandline/start/#options)).

**docker stop**  
Dừng lại một hay nhiều container đang chạy.  
Lệnh: `docker stop [OPTIONS] CONTAINER [CONTAINER...]`  
Các option ([option](https://docs.docker.com/engine/reference/commandline/stop/#options)).

**docker rm**  
Xóa một hay nhiều container.  
Lệnh: `docker rm [OPTIONS] CONTAINER [CONTAINER...]`  
Các option ([option](https://docs.docker.com/engine/reference/commandline/rm/#options)).

# Run mysql
B1:  
`docker run --name demo-sql -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7`  
 Kết quả: 1a51b7f9c5141f7ff0f751a340892a12eb40a6e96f1f7419ab7e4d125c37394e

B2:  
```
docker exec -it demo-sql mysql -uroot -p  
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 3
Server version: 5.7.18 MySQL Community Server (GPL)

Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> CREATE SCHEMA `demo` DEFAULT CHARACTER SET utf8 COLLATE `utf8_unicode_ci`;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| demo               |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.00 sec)

mysql> use demo;
Database changed

mysql> CREATE TABLE `demo`.`user` (
    ->   `user_id` INT NOT NULL AUTO_INCREMENT,
    ->   `user_name` VARCHAR(45) NOT NULL,
    ->   PRIMARY KEY (`user_id`));
Query OK, 0 rows affected (0.01 sec)

mysql> INSERT INTO `demo`.`user` (`user_id`, `user_name`) VALUES ('1', 'user1'); 
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO `demo`.`user` (`user_id`, `user_name`) VALUES ('2', 'user2'); 
Query OK, 1 row affected (0.01 sec)

mysql> exit
Bye
```

B3:
Vào MySQL Workbench chọn database -> Connect to database. Điền địa chỉ IP của container vừa tạo (dùng lệnh `docker inspect container_id` để lấy IP) -> OK.
