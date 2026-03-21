

# 一. 什么是 `unordered_map`？

`unordered_map` 是 C++ STL 中的**哈希表**实现，用于存储**键值对**（key-value pairs）。

**核心特点**：
- 🔍 **快速查找**：平均时间复杂度 O(1)
- 🔄 **无序存储**：不像 `map` 那样按键排序
- 💾 **键值对**：每个元素是一个 (key, value) 对

---

# 二. 为什么需要 `unordered_map`？

## 对比 C++ 中的 Map 容器

| 特性 | `unordered_map` | `map` |
|------|----------------|-------|
| **底层结构** | 哈希表 | 红黑树 |
| **查找速度** | O(1) 平均 | O(log n) |
| **插入速度** | O(1) 平均 | O(log n) |
| **是否有序** | ❌ 无序 | ✅ 按 key 排序 |
| **内存占用** | 较低 | 较高 |

## 什么时候用？

**使用 `unordered_map`**：
- 需要快速查找和插入
- 不关心元素顺序
- 处理算法题（如两数之和）

**使用 `map`**：
- 需要按键排序
- 需要范围查找
- 需要有序遍历

---

# 三. 基本语法

### 1️. 头文件和声明

```cpp
#include <unordered_map>

// 声明一个 unordered_map，key 是 int，value 也是 int
unordered_map<int, int> hashmap;

// 声明一个 unordered_map，key 是 string，value 是 int
unordered_map<string, int> name_to_age;
```

## 2️. 插入元素

```cpp
unordered_map<int, int> hashmap;

// 方法1：使用 [] 运算符
hashmap[1] = 10;
hashmap[2] = 20;

// 方法2：使用 insert 函数
hashmap.insert({3, 30});
hashmap.insert(make_pair(4, 40));
```

## 3️. 访问元素

```cpp
unordered_map<int, int> hashmap = {{1, 10}, {2, 20}, {3, 30}};

// 方法1：使用 [] 运算符（如果 key 不存在，会创建并初始化为 0）
int val1 = hashmap[1];  // val1 = 10

// 方法2：使用 at()（如果 key 不存在，会抛出异常）
int val2 = hashmap.at(2);  // val2 = 20

// 方法3：使用 find()（推荐，更安全）
auto it = hashmap.find(3);
if (it != hashmap.end()) {
    int val3 = it->second;  // val3 = 30
}
```

## 4️. 常用操作

```cpp
unordered_map<int, int> hashmap = {{1, 10}, {2, 20}};

// 检查 key 是否存在
bool exists = hashmap.count(1);  // 1 表示存在，0 表示不存在
bool exists2 = hashmap.find(1) != hashmap.end();  // 更推荐的方式

// 删除元素
hashmap.erase(1);  // 删除 key=1 的元素

// 获取元素个数
int size = hashmap.size();  // 返回 1

// 判断是否为空
bool empty = hashmap.empty();  // 返回 false

// 清空所有元素
hashmap.clear();
```

---

# 四. 注意事项

###  重要提醒

1. **key 不存在时的行为**：
   ```cpp
   unordered_map<int, int> hashmap = {{1, 10}};
   
   // [] 运算符：会创建 key 并初始化为 0
   int a = hashmap[2];     // hashmap[2] = 0, a = 0
   // 副作用：hashmap 现在变成了 {{1, 10}, {2, 0}}
   
   // at() 函数：如果 key 不存在，会抛出异常
   // int b = hashmap.at(3);  // 抛出 out_of_range 异常
   ```

2. **推荐使用 find()**：
   ```cpp
   // 推荐写法（安全）
   auto it = hashmap.find(key);
   if (it != hashmap.end()) {
       // 找到
   }
   
   // 不推荐的写法（可能导致意外插入）
   if (hashmap.count(key) > 0) {
       // 找到
   }
   ```

3. **迭代器遍历顺序**：
   ```cpp
   unordered_map<int, string> hashmap = {{3, "C"}, {1, "A"}, {2, "B"}};
   
   // 遍历顺序是哈希表顺序，不是插入顺序！
   for (auto pair : hashmap) {
       cout << pair.first << ": " << pair.second << endl;
   }
   // 输出可能是：3:C, 1:A, 2:B（顺序不确定）
   ```

4. **自定义类型作为 key**：
   ```cpp
   // 如果使用自定义类型作为 key，需要提供哈希函数
   struct Point {
       int x, y;
       bool operator==(const Point& other) const {
           return x == other.x && y == other.y;
       }
   };
   
   // 自定义哈希函数
   struct PointHash {
       size_t operator()(const Point& p) const {
           return hash<int>()(p.x) ^ (hash<int>()(p.y) << 1);
       }
   };
   
   unordered_map<Point, string, PointHash> pointMap;
   ```

---

# 五. 总结

###  `unordered_map` 核心要点

| 操作 | 方法 | 说明 |
|------|------|------|
| **插入** | `hashmap[key] = value` 或 `insert({key, value})` | 添加键值对 |
| **查找** | `find(key)` 或 `count(key)` | 查找键是否存在 |
| **访问** | `hashmap[key]` 或 `hashmap.at(key)` | 获取值 |
| **删除** | `erase(key)` | 删除键值对 |
| **大小** | `size()` | 返回元素个数 |
| **清空** | `clear()` | 清空所有元素 |

###  使用场景

✅ **算法题**：两数之和、三数之和等  
✅ **计数统计**：统计元素出现次数  
✅ **缓存实现**：快速查找和更新  
✅ **去重**：判断元素是否重复  

### 性能优势

-  **O(1) 平均查找和插入**
-  **内存效率高**
-  **适合大规模数据处理**

---

##  C++ vs Python 对比

```cpp
// C++ unordered_map
unordered_map<int, int> hashmap;
hashmap[1] = 10;
hashmap[2] = 20;

auto it = hashmap.find(1);
if (it != hashmap.end()) {
    cout << it->second << endl;
}
```

```python
# Python dict
hashmap = {}
hashmap[1] = 10
hashmap[2] = 20

if 1 in hashmap:
    print(hashmap[1])
```

**对比**：C++ 的 `unordered_map` 和 Python 的 `dict` 原理类似，都是哈希表实现！

---
