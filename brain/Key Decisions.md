---
date: 2026-04-08
description: "Architectural and workflow decisions worth recalling across sessions — each links to its source work note"
tags:
  - brain
---

# Key Decisions

Architectural or workflow decisions worth recalling. Link to the full [[Decision Record]] when one exists.

---

## Hive 项目决策

### R31 Phase 3: BeeFactory 独立路由组件

**Date**: 2026-04-09
**Decision**: 从 WorkerManager 剥离路由逻辑到独立 BeeFactory 类

**Problem**: `_determine_bee_class` 用 `(dna.mutation_gene or dna.role)` 查找，**完全忽略了 dna.species**。所有 38+ 工蜂全部走 BaseBee。

**Solution**: 路由优先级改为 `role=async → species → mutation_gene → role → BaseBee`
- `dna.species` 优先级最高（之前被忽略）
- 新建 `hive/core/bee_factory.py`

**Evidence**: [[Hive]]

---

### R31 Phase 3: GitHubHarvester 异步化

**Date**: 2026-04-09
**Decision**: 将同步 requests 改造为 httpx.AsyncClient + asyncio.gather 并发

**Problem**: `execute_task` 声明 `async` 但内部用同步 `requests.get()`，多关键词串行搜索

**Solution**: `requests` → `httpx.AsyncClient`，串行 → `asyncio.gather()` 并发

**Evidence**: [[Hive]]

---

### R31 Phase 3: GEP 规模验证

**Date**: 2026-04-09
**Decision**: 通过系统化规模测试验证 GEP 可支撑 production 规模种群

**Finding**: 500 pop ≈ 95ms/gen（快），max_depth 不是瓶颈，population 近线性 O(n)

**Evidence**: [[Hive]]

---

### R31: GEP 基因完整集成

**Date**: 2026-03-31
**Decision**: 将 GEP 基因完整集成到 BeeDNA.calculate_fitness()，dual-mode 设计
- GEP 优先执行
- legacy 回退机制
- Phase 3 完成核心集成

**Context**: 经过 31 轮审查，基因系统在 `calculate_fitness()` 中完整落地

---

### 早期: 采用生物启发式架构

**Decision**: 模仿蜜蜂社会结构设计多智能体系统
- QueenBee 作为协调中枢
- 38+ 专业化 WorkerBee
- 进化引擎驱动自我优化

---

## 量化交易决策

### 多维度验证体系

**Decision**: 交易信号必须多维度验证，单一维度策略无效

**Reasoning**: 市场量化太多，单一指标失效

**Factors**:
1. 大盘位置
2. 冲高回落风险评估
3. 回落支撑位
4. 板块轮动
5. 失败率评估
6. 市场容量 + 主力获利空间

---

### 止盈止损原则

**Decision**: 70%+ 大盘冲高回落诱多 → 高抛低吸策略

**Implications**:
- 买点要考虑大盘环境
- 不可追高
- 严格止损

---

### 15天周期问题

**Decision**: 15天周期太长，他人一出货利润即消失 → 改为更短周期

**Context**: 地量买入 / 三根大阳大阴线后小阴线缩量买入

---

## 技术栈决策

### Hive: TypeScript

**Decision**: 核心代码使用 TypeScript
- 更好的类型安全
- IDE 支持
- 适合复杂多智能体系统

### 量化: Python

**Decision**: 量化系统使用 Python
- 数据科学生态丰富
- 回测框架成熟
- 与 AI/ML 集成方便

---

## Shifts Log

| Date | Shift | Reason |
|------|-------|--------|
| 2026-04-09 | Hive Phase 3 完成：BeeFactory + Async GitHubHarvester + GEP 规模验证 | 技术决策落地 |
| 2026-04-08 | Created in obsidian-mind | 知识库整合 |
