# Stage 05 - OOP、dataclass、value object、依赖注入

## 目标

本阶段围绕：OOP、dataclass、value object、依赖注入。

学习方式不是死记语法，而是把 Python 行为和你熟悉的 Java 心智模型放在一起比较。

## Java 对比

| Python 关注点 | Java 类比 |
| --- | --- |
| OOP、dataclass、value object、依赖注入 | POJO、record、Lombok、Spring DI |

## 本阶段必须搞懂

1. Python 在这个主题下的默认写法是什么。
2. 哪些 Java 习惯可以迁移，哪些不能迁移。
3. 这个知识点未来如何服务技术组件或 AI 工程代码。

## 易错点

- 不要为了像 Java 一样而把所有函数都塞进 class。
- 看到 Python 写法简单，不代表没有边界。
- 看到类型提示，不代表运行时自动强校验。

## 代码位置

以 `registry.py` 中的 stage 注册为准。

## Debug 建议

1. 运行 `uv run python -m iron_python_learning_lab 5`。
2. 在对应 stage 文件的 `demo()` 函数打断点。
3. 观察返回的 dict，每个字段都代表一个核心现象。
4. 再看 `tests/` 中对应断言如何验证这个行为。

## 小练习

见：

```text
exercises/stage05/README.md
```
