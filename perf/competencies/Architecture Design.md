---
date: 2026-04-09
description: "系统架构设计能力：从 WorkerManager 剥离 BeeFactory，单一职责、依赖倒置"
current-level: L3
target-level: L4
tags:
  - perf
  - competency
  - architecture
---

# Architecture Design

## Definition

能够设计清晰的系统架构，将混合职责的组件拆分为单一职责的独立模块，通过接口解耦实现可测试、可组合的系统。

## Evidence

- **Hive BeeFactory 路由重构（2026-04-09）** — 从 `WorkerManager` 剥离路由逻辑到独立 `BeeFactory` 类，解决 38+ 工蜂全部走 BaseBee 的架构问题。路由优先级：`role=async → species → mutation_gene → role → BaseBee`
  - 证据：[[Hive]]
