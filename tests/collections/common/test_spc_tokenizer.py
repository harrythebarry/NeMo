# Copyright (c) 2020, NVIDIA CORPORATION.  All rights reserved.
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

import pytest

from nemo.collections.common.tokenizers.sentencepiece_tokenizer import SentencePieceTokenizer
from nemo.collections.common.tokenizers.tokenizer_utils import MODEL_SPECIAL_TOKENS


class TestSentencePieceTokenizer:
    model_name = "/m_common.model"

    @pytest.mark.unit
    def test_add_special_tokens(self, test_data_dir):
        tokenizer = SentencePieceTokenizer(test_data_dir + self.model_name)
        special_tokens = MODEL_SPECIAL_TOKENS['bert']
        tokenizer.add_special_tokens(special_tokens)
        assert tokenizer.vocab_size == tokenizer.original_vocab_size + len(set(special_tokens.values()))

    @pytest.mark.unit
    def test_text_to_tokens(self, test_data_dir):
        tokenizer = SentencePieceTokenizer(test_data_dir + self.model_name)
        special_tokens = MODEL_SPECIAL_TOKENS['bert']
        tokenizer.add_special_tokens(special_tokens)

        text = "[CLS] a b c [MASK] e f [SEP] g h i [SEP]"
        tokens = tokenizer.text_to_tokens(text)

        assert len(tokens) == len(text.split())
        assert tokens.count("[CLS]") == 1
        assert tokens.count("[MASK]") == 1
        assert tokens.count("[SEP]") == 2

    @pytest.mark.unit
    def test_tokens_to_text(self, test_data_dir):
        tokenizer = SentencePieceTokenizer(test_data_dir + self.model_name)

        text = "[CLS] a b c [MASK] e f [SEP] g h i [SEP]"
        tokens = tokenizer.text_to_tokens(text)
        result = tokenizer.tokens_to_text(tokens)

        assert text == result

    @pytest.mark.unit
    def test_text_to_ids(self, test_data_dir):
        tokenizer = SentencePieceTokenizer(test_data_dir + self.model_name)
        special_tokens = MODEL_SPECIAL_TOKENS['bert']
        tokenizer.add_special_tokens(special_tokens)

        text = "[CLS] a b c [MASK] e f [SEP] g h i [SEP]"
        ids = tokenizer.text_to_ids(text)

        assert len(ids) == len(text.split())
        assert ids.count(tokenizer.token_to_id("[CLS]")) == 1
        assert ids.count(tokenizer.token_to_id("[MASK]")) == 1
        assert ids.count(tokenizer.token_to_id("[SEP]")) == 2

    @pytest.mark.unit
    def test_ids_to_text(self, test_data_dir):
        tokenizer = SentencePieceTokenizer(test_data_dir + self.model_name)
        special_tokens = MODEL_SPECIAL_TOKENS['bert']
        tokenizer.add_special_tokens(special_tokens)

        text = "[CLS] a b c [MASK] e f [SEP] g h i [SEP]"
        ids = tokenizer.text_to_ids(text)
        result = tokenizer.ids_to_text(ids)

        assert text == result

    @pytest.mark.unit
    def test_tokens_to_ids(self, test_data_dir):
        tokenizer = SentencePieceTokenizer(test_data_dir + self.model_name)
        special_tokens = MODEL_SPECIAL_TOKENS['bert']
        tokenizer.add_special_tokens(special_tokens)

        text = "[CLS] a b c [MASK] e f [SEP] g h i [SEP]"
        tokens = tokenizer.text_to_tokens(text)
        ids = tokenizer.tokens_to_ids(tokens)

        assert len(ids) == len(tokens)
        assert ids.count(tokenizer.token_to_id("[CLS]")) == 1
        assert ids.count(tokenizer.token_to_id("[MASK]")) == 1
        assert ids.count(tokenizer.token_to_id("[SEP]")) == 2

    @pytest.mark.unit
    def test_ids_to_tokens(self, test_data_dir):
        tokenizer = SentencePieceTokenizer(test_data_dir + self.model_name)
        special_tokens = MODEL_SPECIAL_TOKENS['bert']
        tokenizer.add_special_tokens(special_tokens)

        text = "[CLS] a b c [MASK] e f [SEP] g h i [SEP]"
        tokens = tokenizer.text_to_tokens(text)
        ids = tokenizer.tokens_to_ids(tokens)
        result = tokenizer.ids_to_tokens(ids)

        assert len(result) == len(tokens)

        for i in range(len(result)):
            assert result[i] == tokens[i]
