# Iron Python Learning Lab

这是一个专门给 Java 工程师学习 Python 的实验室项目。

它和实战组件仓库分开：这里允许大量 demo、断点调试、对比说明和练习；真正稳定下来的工程抽象，再迁移到 `iron-components-python`。

## 学习目标

这个项目不追求做 Python 百科，而是追求四件事：

1. 文档讲清楚：每个阶段解释核心概念、设计动机、和 Java 的差异。
2. 代码能运行：每个阶段都有可执行 demo，不停留在文字层面。
3. 测试能验证：用 pytest 固化关键行为，避免“看起来懂了”。
4. 能迁移到实战：最后阶段衔接 API/SPI/Core/Provider 的技术组件思路。

## 快速开始

推荐用 uv：

```bash
uv sync --group dev
uv run python -m iron_python_learning_lab
uv run python -m iron_python_learning_lab 3
uv run pytest
```

如果你暂时不用 uv，可以先这样跑入口脚本：

```bash
python main.py
python main.py 3
```

如果要直接用 `python -m` 方式运行，需要让 Python 找到 `src` 目录：

```bash
PYTHONPATH=src python -m iron_python_learning_lab
PYTHONPATH=src python -m iron_python_learning_lab 3
```

## 目录结构

```text
iron-python-learning-lab/
├── docs/
│   ├── roadmap.md
│   ├── stage-template.md
│   └── stages/
├── exercises/
├── src/
│   └── iron_python_learning_lab/
└── tests/
```

## 10 个阶段

| 阶段 | 主题 | Java 对比 |
| --- | --- | --- |
| 01 | 基础语法、控制流、异常、模块 | 语法、工具类、checked exception |
| 02 | 对象模型、引用、可变/不可变、拷贝 | 引用变量、String、浅拷贝/深拷贝 |
| 03 | 类型系统、泛型、Protocol、ABC、Annotated、TypeGuard | 接口、抽象类、泛型、注解 |
| 04 | 函数、参数、包、模块、import、uv 项目结构 | 方法、重载、Maven module |
| 05 | OOP、dataclass、value object、依赖注入 | POJO、record、Lombok、Spring DI |
| 06 | 集合、迭代器、生成器、推导式 | Collections、Iterator、Stream |
| 07 | 错误处理、上下文管理器、资源生命周期 | try/catch、try-with-resources |
| 08 | 文件、路径、JSON、序列化、配置 | Path、Jackson、配置类 |
| 09 | 并发、线程、asyncio、TaskGroup | 线程池、CompletableFuture |
| 10 | 小型技术组件实战 | API/SPI/Core/Provider 分层 |

## 学习方法

每个阶段建议按这个顺序走：

1. 读 `docs/stages/stage-xx-*.md`。
2. 跑对应 demo。
3. 在 demo 关键函数上打断点。
4. 看 pytest 如何验证行为。
5. 做 `exercises/stagexx/README.md` 的练习。
