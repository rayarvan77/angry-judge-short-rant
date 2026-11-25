# Angry Judge: The Short Rant Contest

[![make.fun · u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![rank](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rayarvan77/angry-judge-short-rant/rank.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)
[![reward](https://make.fun/badge/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046/rayarvan77/angry-judge-short-rant/reward.svg)](https://make.fun/bounty/u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046?utm_source=github&utm_medium=readme&utm_campaign=u-riidzhsn-angry-judge-the-short-rant-contest-b9f46046)

Entry for the [make.fun](https://make.fun) bounty **Angry Judge: The Short Rant Contest** — write one short, funny rant about a small everyday annoyance and let a furious judge decide which one lands hardest. Entries are capped at 400 characters, so the punch has to come fast.

## The rant

> My office chair has one job — hold me at desk height — and it quits daily. I sit down a professional; ten minutes later I am a goblin folded into a question mark, knees at my chin, dignity somewhere near the floor. It sinks silently, like a coward. I have sentenced printers and one haunted photocopier, but this chair? Contempt of court. Life without parole.

## Concept

The entrant plays the angry judge himself and puts his own office chair on trial. The chair has exactly one job — hold him at desk height — and it quits every day, sinking silently until a professional is folded into a goblin. The verdict is the punchline: contempt of court, life without parole. One specific petty target, sharp economical wording, no throat-clearing.

## How it works

`main.py` (Python 3.13, standard library only) holds the rant, self-checks it against the brief's gate — UTF-8 text, 1 to 400 characters, a single non-blank line — writes it to `/output/entry.txt`, then reads the file back to verify it matches byte for byte.

## Local validation

- `python3 main.py` run twice: byte-identical output both times
- Rant: **359 characters**, 1 line, non-blank — under the 400-character cap
- `main.py`: 2,280 bytes (under the 4,096-byte limit)
