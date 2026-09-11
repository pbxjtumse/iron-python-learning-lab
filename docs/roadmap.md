# Python 10 阶段学习路线

这条路线按“先能写，再能理解，再能工程化”的顺序设计。

| 阶段 | 核心问题 | 交付物 |
| --- | --- | --- |
| 01 | Python 程序如何执行，和 Java 基础语法哪里不同 | 基础 demo、异常 demo、模块函数 demo |
| 02 | Python 变量到底是不是对象本身 | 引用、可变对象、浅拷贝 demo |
| 03 | Python 类型提示到底管什么、不管什么 | Protocol、ABC、TypeGuard、Annotated demo |
| 04 | Python 如何组织函数、模块、包 | 函数参数、导入、项目结构 demo |
| 05 | Python OOP 应该怎么写才自然 | dataclass、ABC、Protocol、组合 demo |
| 06 | Python 如何处理集合和数据流 | dict/list/set、生成器、推导式 demo |
| 07 | Python 如何表达资源生命周期 | 异常转换、context manager demo |
| 08 | Python 如何做 I/O 和 JSON | pathlib、json、配置读取 demo |
| 09 | Python 并发和 Java 线程池有什么差异 | asyncio、TaskGroup demo |
| 10 | 如何把语言能力组织成小组件 | API/SPI/Core/Provider 小项目 |

## 每阶段固定结构

- 文档：概念、Java 对比、易错点。
- 代码：可运行 demo。
- 测试：pytest 验证行为。
- 练习：小任务。
- Debug 提示：告诉你看哪些变量。
