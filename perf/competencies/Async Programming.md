---
date: 2026-04-09
description: "异步编程能力：将同步阻塞的 requests 改造为 httpx.AsyncClient + asyncio.gather 并发"
current-level: L3
target-level: L4
tags:
  - perf
  - competency
  - async
---

# Async Programming

## Definition

掌握 asyncio 异步编程范式，能够将同步阻塞代码改造为真正的异步并发，充分利用 I/O bound 任务的等待时间。

## Evidence

- **GitHubHarvester 异步化（2026-04-09）** — 将同步 `requests.get()` + `time.sleep()` 改造为 `httpx.AsyncClient` + `asyncio.gather()`，多个关键词从串行搜索变为并发搜索，显著降低总延迟
  - 证据：[[Hive]]
