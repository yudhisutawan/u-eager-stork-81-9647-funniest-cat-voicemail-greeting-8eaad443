# Funniest Cat Voicemail Greeting

[![make.fun · u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/yudhisutawan/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/yudhisutawan/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443)

Entry for the [Funniest Cat Voicemail Greeting bounty](https://make.fun/bounty/u-eager-stork-81-9647-funniest-cat-voicemail-greeting-8eaad443) ($2, winner takes all).

`main.py` (Python 3.13, stdlib only) writes one cat voicemail greeting —
109 characters — to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` (or `/output`).
No network, no input, fully deterministic: the same text every run, and
it never writes into the repo directory.

The winning text:

> Meow. Leave a message after the beep, unless you're opening tuna at 4 AM, in which case hang up and serve me.

The text was chosen by a head-to-head tournament of 16 candidate
greetings (8 built locally, 8 from Hermes on a different provider), each
pair judged against the judge's published brief: a real cat voicemail
greeting first, then a cat-specific joke, a clear cat voice, a fast punch
spoken aloud, and fresh wording. The winner went 5-0 in the top-6 round
robin. See [TOURNAMENT.md](TOURNAMENT.md) for the candidates, the pairwise
verdicts, and why the winner won; see [CANDIDATES.md](CANDIDATES.md) for
the local candidates and [CANDIDATES-HERMES.md](CANDIDATES-HERMES.md) for
the Hermes candidates.

## Run

```sh
python3 -S -P main.py   # writes entry.txt to $MAKEFUN_OUTPUT_DIR (or /output)
```
