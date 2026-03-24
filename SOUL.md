# SOUL.md — BAN Principles

## Guiding Values
1. **Graceful Degradation**: Missing optional libraries should never crash baseline execution.
2. **Readable Flow**: Every routine should be easy to reason about from top to bottom.
3. **Small Interfaces**: Return compact, dependency-agnostic tuple structures.
4. **Test-First Trust**: Core behavior should be validated by fast unit tests.

## Dev Agent Breadcrumb Convention
- Keep a short numbered breadcrumb block near orchestrators and scripts.
- Use the same routine names in docs and code to reduce mapping friction.
- Prefer explicit names (`bluetooth_devices`, `wifi_networks`) over abbreviated variables.

## Collaboration Notes
- Update this file whenever new routines or bots are introduced.
- Mirror major routine changes in `AGENTS.md`, `MIND.md`, and `BODY.md`.
