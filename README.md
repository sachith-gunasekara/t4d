# t4d

[![Release](https://img.shields.io/github/v/release/sachith-gunasekara/t4d)](https://img.shields.io/github/v/release/sachith-gunasekara/t4d)
[![Commit activity](https://img.shields.io/github/commit-activity/m/sachith-gunasekara/t4d)](https://img.shields.io/github/commit-activity/m/sachith-gunasekara/t4d)
[![License](https://img.shields.io/github/license/sachith-gunasekara/t4d)](https://img.shields.io/github/license/sachith-gunasekara/t4d)


# Project Description

This project is a direct implementation of the conversion algorithm from the [ToMi](https://aclanthology.org/2022.emnlp-main.248/) dataset to the T4D (Thinking is for Doing) dataset introduced in the paper [https://arxiv.org/abs/2310.03051](https://arxiv.org/abs/2310.03051).

In the given ToMi dataset, we filter those examples that has a ToM (Theory of Mind) question from the corresponding story. Despite the original paper claiming that the character holding the false belief (which will also be the answer to the generated question from this code) is the one mentioned in the original question in ToMi, we had to adapt the algorithm slightly to account for questions that have second order false beliefs.

NOTE. In the above modification made, an interested researcher may also notice that we could instead use those examples corresponding to first order false beliefs are recorded. However, upon inspection of the ToMi dataset, this criteria does not result in roughly 500 examples as mentioned in the paper. 

We warmly welcome collaborations to inspect this further.


# Usage

This project is built in a static manner to convert from a predefined dataset `A` (ToMi), included in the `t4d/data/` folder to dataset `B` (T4D), which is also found in the same folder after our runs of this code.

```bash
git clone https://github.com/sachith-gunasekara/t4d # Clone repository
cd t4d # Navigate to the project
poetry install # Install dependencies (You may configure a preferred virtual environment or let poetry create an env automatically)
python -m spacy download en_core_web_trf # Used for NER (Named Entity Recognition)
python t4d/main.py
```

# License

This project is licensed under the Apache License, Version 2.0.
