# GPT2-python-code-generator

## Description

- Toy project for GPT2 finetuning with transformers library
- Finetuned with TOP100 starts python opensource project from github



## Test model
```python3
from transformers import GPT2LMHeadModel, GPT2TokenizerFast
tokenizer = GPT2TokenizerFast.from_pretrained('SIC98/GPT2-python-code-generator')
model = GPT2LMHeadModel.from_pretrained('SIC98/GPT2-python-code-generator')
```

```python3
sequence = """# coding=utf-8
# Copyright 2020 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");"""

inputs = tokenizer.encode(sequence, return_tensors='pt')
outputs = model.generate(inputs, max_length=1024, do_sample=True, temperature=0.5, top_p=1.0)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(text)
```

### Result
```
# coding=utf-8
# Copyright 2020 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import Any, Dict, List, Optional, Tuple

from...file_utils import is_sentencepiece_available
from...utils import logging


logger = logging.get_logger(__name__)

VOCAB_FILES_NAMES = {"vocab_file": "vocab.txt"}

PRETRAINED_VOCAB_FILES_MAP = {
    "vocab_file": {
        "gpt2-base": "https://huggingface.co/gpt2-base/resolve/main/vocab.txt",
        "gpt2-large": "https://huggingface.co/gpt2-large/resolve/main/vocab.txt",
        "gpt2-xlm-base": "https://huggingface.co/gpt2-xlm-base/resolve/main/vocab.txt",
        "gpt2-xlm-large": "https://huggingface.co/gpt2-xlm-large/resolve/main/vocab.txt",
        "gpt2-xlm-head": "https://huggingface.co/gpt2-xlm-head/resolve/main/vocab.txt",
        "gpt2-xlm-head": "https://huggingface.co/gpt2-xlm-head/resolve/main/vocab.txt",
        "gpt2-xlm-decoder": "https://huggingface.co/gpt2-xlm-decoder/resolve/main/vocab.txt",
        "gpt2-xlm-head": "https://huggingface.co/gpt2-xlm-head/resolve/main/vocab.txt",
        "gpt2-xlm-decoder": "https://huggingface.co/gpt2-xlm-decoder/resolve/main/vocab.txt",
        "gpt2-xlm-head": "https://huggingface.co/gpt2-xlm-head/resolve/main/vocab.txt",
        "gpt2-xlm-decoder": "https://huggingface.co/gpt2-xlm-decoder/resolve/main/vocab.txt",
        "gpt2-xlm-head": "https://huggingface.co/gpt2-xlm-head/resolve/main/vocab.txt",
        "gpt2-xlm-decoder": "https://huggingface.co/gpt2-xlm-decoder/resolve/main/vocab.txt",
        "gpt2-xlm-head": "https://huggingface.co/gpt2-xlm-head/resolve/main/vocab.txt",
        "gpt2-xlm-decoder": "https://huggingface.co/gpt2-xlm-decoder/resolve/main/vocab.txt",
        "gpt2-xlm-head": "https://hugging
```

## Model
https://huggingface.co/SIC98/GPT2-python-code-generator
