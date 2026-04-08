---
date: 2026-04-09
description: "性能工程能力：设计系统性规模基准测试，发现 O(n) 和亚线性 scaling 特征"
current-level: L3
target-level: L4
tags:
  - perf
  - competency
  - performance
---

# Performance Engineering

## Definition

能够设计并执行系统性的性能基准测试，通过三维参数空间探索发现性能瓶颈和 scaling 规律，为 production 规模决策提供数据支撑。

## Evidence

- **GEP 规模实验（2026-04-09）** — 创建 `test_gep_scale.py`，系统测试 population_size × max_depth × max_genes 三维规模。发现：pop 10→100 (10x) = 11.48x 时间（近线性 O(n)），max_depth 几乎无影响，genes 1→10 (10x) = 4.78x 时间（亚线性）。验证 500 pop ≈ 95ms/gen 可用于 production
  - 证据：[[Hive]]
