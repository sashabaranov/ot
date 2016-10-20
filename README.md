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

