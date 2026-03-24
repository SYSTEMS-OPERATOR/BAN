"""Run BAN hub scans from the examples directory.

Dev Agent Breadcrumbs
---------------------
1. Import the orchestrating ``main`` coroutine from ``src.hub``.
2. Execute the async runtime with ``asyncio.run``.
"""

import asyncio

from src.hub import main


if __name__ == "__main__":
    asyncio.run(main())
