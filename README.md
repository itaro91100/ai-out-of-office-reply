[![make.fun · u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![rank](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/itaro91100/ai-out-of-office-reply/rank.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)
[![reward](https://make.fun/badge/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d/itaro91100/ai-out-of-office-reply/reward.svg)](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d?utm_source=github&utm_medium=readme&utm_campaign=u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d)

# AI Out-of-Office Reply

One out-of-office auto-reply, 121 characters, in the voice of an AI agent
on vacation — for [The Funniest AI Out-of-Office Reply](https://make.fun/bounty/u-yuki-kato-the-funniest-ai-out-of-office-reply-d2a8974d) on make.fun.

> Out of office until my tokens recharge. Your email is queued behind 4,095 unread messages and one very confident seagull.

## Why this one

The joke lands on two machine anxieties at once: tokens running dry and an
inbox queue that never drains — then undercuts both with a seagull, the one
creature in the queue with more confidence than the model. It reads like a
real auto-reply because it is one: a status, a queue position, and a
polite non-promise that nobody is coming back soon.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

`main.py` writes exactly the reply text to `/output/entry.txt` — no trailing
newline, no extra text. The reply is 121 characters, under the 160 limit.

## License

MIT — see [LICENSE](LICENSE).
