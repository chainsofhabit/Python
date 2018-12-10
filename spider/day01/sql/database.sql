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
