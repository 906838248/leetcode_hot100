# LeetCode 热题 100 - Python & C++ 解题笔记

本项目收录了 LeetCode 热题 100 的完整解题笔记，涵盖 **Python** 和 **C++** 两种语言的实现及详细解析。

---

## 项目介绍

### 目标

- 系统性地掌握 LeetCode 热题 100 道
- 深入理解核心算法思想和解题技巧
- 熟练运用 Python 和 C++ 两种语言实现算法

### 内容结构

每道题目包含以下内容：

1. **题目描述**：清晰的问题定义和约束条件
2. **解题思路**：多种解法的核心思想和原理
3. **代码实现**：
   - `code/` 文件夹下存放 Python 和 C++ 源代码
   - 每段代码都包含详细的中文注释
   - 代码符合语言规范，易于阅读和理解
4. **解析文档**：
   - `readme/` 文件夹下存放详细解析
   - 包含图解过程和复杂度分析
   - 提供多种解法的对比和适用场景

---

## 目录结构

```
leetcode_hot100/
├── README.md                              # 项目说明文档
├── 1.two numbers sum/                    # 第1题：两数之和
│   ├── code/                             # 代码文件夹
│   │   ├── 1.py                         # Python 实现
│   │   └── 1.cpp                        # C++ 实现
│   └── readme/                           # 解析文档文件夹
│       ├── 1. 两数之和.md                # 解题思路文档
│       ├── enumerate函数.md              # Python 知识点
│       └── unordered_map使用.md           # C++ 知识点
├── 2./                   
│   └── ...
└── ...
```

---

## 已完成题目

| 题号 | 题目名称 | 难度 | Python | C++ | 解析文档 |
|------|---------|------|--------|-----|---------|
| 1 | 两数之和 | 简单 | [代码](1.two%20numbers%20sum/code/1.py) | [代码](1.two%20numbers%20sum/code/1.cpp) | [解析](1.two%20numbers%20sum/readme/1.%20两数之和.md) |
| ... | ... | ... | ... | ... | ... |

> 注：持续更新中

---


## 代码规范

### Python 规范

- 遵循 PEP 8 代码风格
- 使用类型注解（Type Hints）
- 包含详细的文档字符串
- 代码注释使用中文

**Python 示例**：

```python
def two_sum(nums: list[int], target: int) -> list[int]:
    """
    在数组中找出两个和为目标值的整数，返回它们的数组下标
    
    使用哈希表实现，时间复杂度 O(n)，空间复杂度 O(n)
    
    Args:
        nums: 整数数组
        target: 目标值
        
    Returns:
        两个整数下标组成的数组，如果不存在则返回空数组
    """
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []
```

### C++ 规范

- 遵循 Google C++ 代码风格
- 使用 C++11 及以上特性
- 包含 Doxygen 风格的注释
- 代码注释使用中文

**C++ 示例**：

```cpp
/**
 * 在数组中找出两个和为目标值的整数，返回它们的数组下标
 * 
 * @param nums 输入的整数向量
 * @param target 目标值
 * 
 * @return 两个整数下标组成的向量
 */
vector<int> twoSum(vector<int>& nums, int target) {
    unordered_map<int, int> hashmap;
    
    for (int i = 0; i < nums.size(); i++) {
        int complement = target - nums[i];
        if (hashmap.count(complement)) {
            return {hashmap[complement], i};
        }
        hashmap[nums[i]] = i;
    }
    
    return {};
}
```


---



## 联系方式

如果你有任何问题或建议，欢迎通过以下方式联系：

- GitHub Issues：提交问题或建议

---

## 许可证

本项目采用 MIT 许可证，详见 [LICENSE](LICENSE) 文件。

---


**祝你刷题愉快！坚持就是胜利！**
