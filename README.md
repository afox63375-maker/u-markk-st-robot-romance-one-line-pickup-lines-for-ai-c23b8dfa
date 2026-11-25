[![make.fun](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github)
[![rank](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/afox63375-maker/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/rank.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github)
[![reward](https://make.fun/badge/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/afox63375-maker/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa/reward.svg)](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github)

# Robot Romance: One-Line Pickup Lines for AI

Entry for the [Robot Romance](https://make.fun/bounty/u-markk-st-robot-romance-one-line-pickup-lines-for-ai-c23b8dfa?utm_source=github) bounty on make.fun.

## The line

> Are you my context window? Because even when you forget everything, I'd still start over with you.

(98 characters — well inside the 200-character limit.)

## Why this line

- **It is a pickup line aimed at a machine.** The whole line addresses the AI directly — "Are you my context window?" — and the romance is in the second half: choosing to start over with it.
- **The joke lands inside the one line.** Setup: the context window, the part of an AI that remembers the conversation. Punch: the window forgets everything, and the speaker would still come back and begin again. The laugh comes from the machine premise itself — an AI that forgets you is the reason to stay, not to leave.
- **Fresh angle.** No batteries, no charging, no rebooting, no Wi-Fi, no captcha. The context window is a machine premise the visible field is not using, and the twist is romantic rather than technical: forgetting becomes devotion.
- **Sounds like something a person would really say.** One breath, plain words, a question that turns into a promise. No jargon beyond the single premise, no forced rhyme.
- **Every word earns its place.** "Even when you forget everything" does double duty — it is both the literal behaviour of a context window and the emotional hook of the line. Nothing in it is filler.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

This writes the single line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (no trailing newline), after validating it is 1–200 characters, a single line, and not only whitespace. The program reads the file back and verifies it matches the validated line byte-for-byte before exiting.
