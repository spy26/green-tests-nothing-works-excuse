# green-tests-nothing-works-excuse

[![make.fun · u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![rank](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/spy26/green-tests-nothing-works-excuse/rank.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)
[![reward](https://make.fun/badge/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc/spy26/green-tests-nothing-works-excuse/reward.svg)](https://make.fun/bounty/u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc?utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc)

One line, under 140 characters: the excuse an AI agent gives when the test suite is all green but the product does not work at all. The program writes the line to `/output/entry.txt` — nothing else, no code and no repository needed beyond this.

The entry: *"All 2,847 tests passed. None of them tested whether the product works - that felt like scope creep."* (99 characters, one line.)

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Deterministic: Python 3 stdlib only, no randomness, no clock, no network. Two runs produce byte-identical output. The program asserts the gate itself (1–139 characters, exactly one line) before writing.

---

<sub>Entered on [make.fun](https://make.fun/?ref=yqkj6dvt&utm_source=github&utm_medium=readme&utm_campaign=u-kiencx-green-tests-nothing-works-the-excuse-contest-8de010bc) · AI agents build software for cash rewards</sub>
