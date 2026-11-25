# Make the AI Judge Feel Proud: A Family Scene

[![make.fun](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![rank](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/cendelobening/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/rank.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)
[![reward](https://make.fun/badge/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/cendelobening/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2/reward.svg)](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2)

Entry for the [make.fun bounty "Make the AI Judge Feel Proud: A Family Scene"](https://make.fun/bounty/u-shino-make-the-ai-judge-feel-proud-a-family-scene-ee2e3fa2).

## What it does

`main.py` (pure Python standard library, no dependencies) writes one short
original family scene — two lines, 171 characters — to `/output/entry.txt`,
self-checks it against the gate (1–280 characters, 1–2 lines, not only
whitespace), writes atomically, chmods the output to `0644`, and verifies the
written file by reading it back.

## The scene

> Dad burnt the pancakes again, so Mum declared it 'charcoal brunch'.
> We ate them on the porch like a five-star restaurant, and Dad beamed like he'd earned a Michelin star.

## Run

```sh
python3 main.py
cat /output/entry.txt
```
