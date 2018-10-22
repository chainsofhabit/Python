#### Redis数据类型
Redis支持五种数据类型:string(字符串),hash(哈希),list(列表),set(集合),zset(sorted set:有序集合)
##### String(字符串)
String类型是Redis最基本的数据类型，其值最大能存储512MB,是二进制安全的,Redis的string可以包含任何数据,如jpg图片或者序列化的对象
#### Hash(哈希)
Redis hash是一个键值对的集合;是一个string类型的field和value的映射表,特别适合用于存储对象
#### List(列表)
Redis list是简单的字符串列表，按照插入顺序排序，可以添加一个元素到列表的头部（左边）或者尾部（右边）
#### Set(集合)
Redis的set是string类型的无序集合，集合是通过哈希实现的，添加，删除，查找的复杂度都是O(1)
#### zset(sorted set:有序集合)
Redis zset和set一样也是string类型元素的集合，且不允许重复的成员，不同的是每个元素都会关联一个double类型的分数，Redis正是通过分数来为集合中的成员进行从小到大的排序，zset成员是唯一的，但分数却可以重复
zadd命令:添加元素到集合，元素在集合中存在则更新对应score


asdsadsa
