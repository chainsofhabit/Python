create database maoyan_db default character set 'utf8';
use maoyan_db;

create table maoyan (
    id int auto_increment primary key,
    actor varchar(128),
    movie varchar(512),
    rate varchar(32),
    releasetime varchar(128),
    score varchar(32),
    cover varchar(1024)
);

create index ix_maoyan_actor on manyan(actor);
create unique index ux_maoyan_movie on maoyan(movie);

create table mogu_product (
    id int auto_increment primary key,
    tradeitemid varchar(512),
    tradetype varchar(512),
    img varchar(512),
    clienturl varchar(1024),
    link varchar(1024),
    itemmarks varchar(512),
    acm varchar(512),
    title varchar(512),
    cparam varchar(1024),
    orgprice varchar(512),
    hassimilarity varchar(512),
    sale varchar(512),
    cfav varchar(512),
    price varchar(512),
    similarityurl varchar(1024)
);