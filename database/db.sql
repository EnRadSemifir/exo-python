use todos;
create table todos (id INT PRIMARY KEY NOT NULL AUTO_INCREMENT, title VARCHAR(100) NOT NULL, description VARCHAR(255), done TINYINT(1));