# Sqlite3 code
object: delete rows that have price = 0 in the general.csv; join the updated general.csv with the leak.csv, which is the leaking (true) data from Steam.


### create table general

```
.mode csv
.headers on
create table general(id INTEGER, title STRING, url STRING, price REAL, discount REAL, popularity INTEGER);
.import /Users/xxt/Desktop/general.csv general --skip 1
.mode markdown
select * from general limit 10;
```

### delete rows which price = 0;

```
select count(id)  from general;    (=4600)
delete from general where price = 0;
select count(id)  from general;    (=4489)
```

### create leak table

```
.mode csv
.headers on
create table leak(title STRING, player estimate INTEGER, id INTEGER);
.import /Users/xxt/Desktop/leak.csv leak --skip 1
.mode markdown
select * from leak limit 10;
```

### join two tables on id, export as joint.csv

```
create table joint(id INTEGER, title STRING, estimate_player INTEGER, url STRING, price REAL, discount REAL, popularity INTEGER);

insert into joint select leak.id, leak.title, leak.player, general.url, general.price, general.discount, general.popularity from general join leak where general.id = leak.id;

select count(id) from joint;

.mode csv
.headers on
.output joint.csv
select * from joint order by estimate_player DESC;
.quit
```