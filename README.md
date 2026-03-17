# Motif-search

Script to search motifs in fasta files.

### Options:

| Short | Option | Type | Default | Description |
|--------|-------|------|---------|-------------|
  |`-h`| `--help  `          |||show this help message and exit|
  |`-i`| `--inp INP  `       |path|Required|Input fasta file|
  |`-m`| `--motif MOTIF`   |string|Required|Motif to be searched|
  |`-p`| `--relax_perc` |float|100|Relaxed percentage similarity|
  |`-o`| `--out `         |string|motif_result.txt|Output file|

## motif-search v2

Refactoring code for better readability, adding fixes and features.

### Fixes:

1. Changing genome variable to list instead of string. 
2. Option to define output file.
3. Changing code structure for better readability.

### Features:

1. Added argparse instead of input.
2. Motif search on complementary strand.
3. Search motif on multiple chromosomes.

### Future:

1. Option to include gaps.
2. Option to include bedfile with selected regions for motif search
3. Multiple motif searches


## motif-search v1

A simple motif search code that I wrote during my introduction to computational biology during my master's



