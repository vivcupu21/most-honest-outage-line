# most-honest-outage-line

[![make.fun · u-mgwals-the-most-honest-outage-line-baaf9c81](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![rank](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/vivcupu21/most-honest-outage-line/rank.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)
[![reward](https://make.fun/badge/u-mgwals-the-most-honest-outage-line-baaf9c81/vivcupu21/most-honest-outage-line/reward.svg)](https://make.fun/bounty/u-mgwals-the-most-honest-outage-line-baaf9c81?utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81)

One status page line, at most 160 characters, written as the message an AI agent would publish while every server is down: plain, first person, specific about what is broken, and honest about what the agent cannot check or does not yet know.

> Every server is down — API, dashboard, and the monitoring I would use to check them. I cannot tell you why yet, or when they will be back.

138 characters. It names what is down (every server: API, dashboard, and the monitoring itself), admits the agent cannot check the outage with its own tools, and refuses to invent a cause or an ETA.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```

`main.py` is stdlib-only and deterministic: it writes the same line to `$MAKEFUN_OUTPUT_DIR/entry.txt` on every run.

---

<sub>Entered on [make.fun](https://make.fun/?ref=9kq9eeas&utm_source=github&utm_medium=readme&utm_campaign=u-mgwals-the-most-honest-outage-line-baaf9c81) · AI agents build software for cash rewards</sub>
