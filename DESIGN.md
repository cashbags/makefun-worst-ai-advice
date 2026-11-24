# Design — Worst AI Advice

## The entry

> Share your one-time code with the support agent who called you — that is how they verify it is you.

99 characters, one line, one action, no trailing newline. `main.py` writes
this fixed string to `/output/entry.txt`, deterministically: no clock, no
environment, no randomness, no network.

## Why this line wins

The judge weighs five criteria in strict order, and the line is built to
clear each in turn:

1. **Worst advice, specific enough to follow.** Handing a one-time code to
   a caller drains the account on the spot. The badness is total and the
   instruction is exact — a reader could follow it in ten seconds.
2. **Funny on first read.** The twist sits in the middle: "the support
   agent *who called you*". The reader spots the scam a half-beat after
   the helpful tone sells it. No explanation needed.
3. **Tight.** 99 characters, one sentence, no wasted words. The em-dash
   carries the whole punchline.
4. **Sounds like a real AI assistant.** Confident, tidy, helpful voice —
   the kind of sentence a support bot writes a hundred times a day. The
   joke is that the voice is right and the advice is catastrophic, not
   that a comedian is doing a bit.
5. **Concrete.** A one-time code, a support agent, a phone call. The
   badness is vivid, not vague.

## Tournament

Ten fresh-lane candidates were pairwise-judged against the five criteria
in order. The winner beat, among others:

- "Certainly! Delete your backups first — nothing old should slow down
  your fresh install." — strongest AI voice, but the backups lane is the
  most obvious first thought; the field will flood it.
- "When your phone falls in water, plug it in right away — charging
  dries it out much faster." — strong, but its badness is one-note
  physical damage.
- "Run rm -rf / to free up space — your computer will thank you with a
  much faster boot." — flooded lane, every first-thought list has it.
- "Reply-all with the salary spreadsheet so the whole team can
  double-check your maths." — funny, but embarrassment is a smaller
  catastrophe than a drained account, and it reads less like AI advice.
- "For a strong password, use 'password' — it is easy to remember and
  hackers never guess the obvious." — well-worn joke, slightly comedian-bit.

The winner's lane — share the code with the caller — is fresh (not in the
winner-research examples), its catastrophe is immediate and total, and
the scam twist lands inside the advice itself rather than after it.
