OpenTargets code test
===


Installation
---

```
pip install git+https://github.com/sashabaranov/ot.git
```


Problem A
---

Main script to use in this package is `tv-calculate-assoc-score`:
```
% tv-calculate-assoc-score --help
Usage: tv-calculate-assoc-score [OPTIONS]

  Calculates max, min, avg and stddev of association_score.overall

Options:
  -d, --disease TEXT  Process disease
  -t, --target TEXT   Process target
  --help              Show this message and exit.
```


Example:
```
tv-calculate-assoc-score -t ENSG00000157764
tv-calculate-assoc-score -d EFO_0002422
```

(looks like API is broken and returs `1` in `association_score.overall`)

Problem B
---

Solution for problem B is located in `scripts/problem-b`.
Usage:
```
% scripts/problem-b --help
Usage: problem-b [OPTIONS] FILENAME OUTPUT_CSV

  Counts academic nausea for given files. Output is stored to sqlite db.

Options:
  --nprocs INTEGER   Number of processes to utilize
  --debug            Print debug output
  --calculate-pairs  Calculate target-target pairs sharing 2+ diseases
  --help             Show this message and exit.
```

The `--calculate-pairs` triggers calculations for second part of a problem.

Example:

```
% time scripts/problem-b --calculate-pairs --debug --nprocs 4 /Users/scrat/Downloads/16.08_evidence_data.json output.csv
(Process-2 - problem-b:18//DEBUG)   Reader started
(PoolWorker-3 - problem-b:30//DEBUG)    Worker started
(PoolWorker-4 - problem-b:30//DEBUG)    Worker started
(PoolWorker-5 - problem-b:30//DEBUG)    Worker started
(PoolWorker-6 - problem-b:30//DEBUG)    Worker started
(Process-2 - problem-b:25//DEBUG)   Reader stopped
(PoolWorker-6 - problem-b:42//DEBUG)    Worker stopped
(PoolWorker-5 - problem-b:42//DEBUG)    Worker stopped
(PoolWorker-3 - problem-b:42//DEBUG)    Worker stopped
(PoolWorker-4 - problem-b:42//DEBUG)    Worker stopped
(MainProcess - problem-b:130//DEBUG)    Result reading finished
(MainProcess - problem-b:132//DEBUG)    Writing results to csv
(MainProcess - problem-b:140//DEBUG)    Calculating pairs
144507250
(MainProcess - problem-b:143//INFO) Done
scripts/problem-b --calculate-pairs --debug --nprocs 4  output.csv  2179.03s user 1141.09s system 230% cpu 23:58.85 total
```