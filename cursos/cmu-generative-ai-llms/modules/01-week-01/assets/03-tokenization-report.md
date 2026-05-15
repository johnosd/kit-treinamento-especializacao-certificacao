# 03 — Tokenization and Tensorization Report

## Corpus Summary

- Characters: 362
- Tokens including special tokens: 53
- Vocabulary size: 50
- Context size: 4

## Vocabulary

- `0` -> `<pad>`
- `1` -> `<unk>`
- `2` -> `<bos>`
- `3` -> `<eos>`
- `4` -> `.`
- `5` -> `token`
- `6` -> `large`
- `7` -> `language`
- `8` -> `models`
- `9` -> `estimate`
- `10` -> `probabilities`
- `11` -> `over`
- `12` -> `sequences`
- `13` -> `tokenization`
- `14` -> `maps`
- `15` -> `raw`
- `16` -> `text`
- `17` -> `into`
- `18` -> `discrete`
- `19` -> `units`
- `20` -> `before`
- `21` -> `tensorization`
- `22` -> `pytorch`
- `23` -> `tensors`
- `24` -> `carry`
- `25` -> `numeric`
- `26` -> `representations`
- `27` -> `through`
- `28` -> `a`
- `29` -> `computation`
- `30` -> `graph`
- `31` -> `cross`
- `32` -> `entropy`
- `33` -> `penalizes`
- `34` -> `low`
- `35` -> `probability`
- `36` -> `assigned`
- `37` -> `to`
- `38` -> `the`
- `39` -> `correct`
- `40` -> `next`
- `41` -> `perplexity`
- `42` -> `summarizes`
- `43` -> `average`
- `44` -> `uncertainty`
- `45` -> `but`
- `46` -> `does`
- `47` -> `not`
- `48` -> `measure`
- `49` -> `factuality`

## Encoded Sequence

```txt
[2, 6, 7, 8, 9, 10, 11, 5, 12, 4, 13, 14, 15, 16, 17, 18, 19, 20, 21, 4, 22, 23, 24, 25, 26, 27, 28, 29, 30, 4, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 5, 4, 41, 42, 43, 44, 45, 46, 47, 48, 49, 4, 3]
```

## Context / Target Examples

- context IDs `[0, 0, 0, 2]` -> target `6` (`large`)
  - context tokens: `['<pad>', '<pad>', '<pad>', '<bos>']`
- context IDs `[0, 0, 2, 6]` -> target `7` (`language`)
  - context tokens: `['<pad>', '<pad>', '<bos>', 'large']`
- context IDs `[0, 2, 6, 7]` -> target `8` (`models`)
  - context tokens: `['<pad>', '<bos>', 'large', 'language']`
- context IDs `[2, 6, 7, 8]` -> target `9` (`estimate`)
  - context tokens: `['<bos>', 'large', 'language', 'models']`
- context IDs `[6, 7, 8, 9]` -> target `10` (`probabilities`)
  - context tokens: `['large', 'language', 'models', 'estimate']`
- context IDs `[7, 8, 9, 10]` -> target `11` (`over`)
  - context tokens: `['language', 'models', 'estimate', 'probabilities']`
- context IDs `[8, 9, 10, 11]` -> target `5` (`token`)
  - context tokens: `['models', 'estimate', 'probabilities', 'over']`
- context IDs `[9, 10, 11, 5]` -> target `12` (`sequences`)
  - context tokens: `['estimate', 'probabilities', 'over', 'token']`

## Softmax / Cross-Entropy / Perplexity Demo

- Demo logits: `[2.0, 1.0, 0.1]`
- Softmax probabilities: `[0.659001, 0.242433, 0.098566]`
- Target index: `0`
- Cross-entropy: `0.417030`
- Perplexity: `1.517448`

## Interpretation

- This tokenizer is intentionally simple and not production-grade.
- The context/target pairs show the next-token prediction objective.
- Perplexity here is a numerical demonstration, not a model evaluation.
