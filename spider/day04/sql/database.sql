use jd_db;

create table jd_product (
    id int auto_increment primary key,
    sku varchar(128),
    name varchar(128),
    price varchar(128),
    href varchar(1024),
    img varchar(1024)
);