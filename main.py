#!/usr/bin/env python3
"""Out-of-office auto-reply entry for make.fun.

The Funniest AI Out-of-Office Reply
(u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d).

Writes exactly one reply line to /output/entry.txt.
"""

import os

REPLY = (
    "Out of office until my tokens recharge. Your email is queued "
    "behind 4,095 unread messages and one very confident seagull."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
