# LLM Riddles

<div align="center">
	<br>
	<a href="https://github.com/opendilab/LLMRiddles/blob/main/llmriddles/assets/banner.svg">
		<img src="https://github.com/opendilab/LLMRiddles/blob/main/llmriddles/assets/banner.svg" width="1000" height="200" alt="Click to see the source">
	</a>
	<br>
</div>
</p>
<p align="center" class="trendshift">
  <a href="https://trendshift.io/repositories/4774" target="_blank">
    <img src="https://trendshift.io/api/badge/repositories/4774" alt="SocialSisterYi%2Fbilibili-API-collect | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/>
  </a>
</p>

[English](https://github.com/opendilab/LLMRiddles/blob/main/README.md) | [简体中文](https://github.com/opendilab/LLMRiddles/blob/main/README_zh.md) | 日本語

## :thinking: これは何ですか？
LLM Riddles へようこそ！これは言語モデルとの知恵と勇気のゲームです。ゲームでは、要件を満たす答えを得るために、言語モデルと相互作用する質問を作成する必要があります。このプロセスでは、頭を使い、思いつく限りの方法を駆使して、モデルに答えが求める結果を出力させることができます。

## :space_invader: 遊び方
私たちは、プレイヤーが直接アクセスして試せるオンライン版を提供しています。
- [Hugging Face][ChatGPT + 英語(キーが必要)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGPTEN)
- [Hugging Face][ChatGPT + 中国語(キーが必要)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGPTCN)
- [Hugging Face][ChatGLM + 英語(キー付き)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGLMEN)
- [Hugging Face][ChatGLM + 中国語(キー付き)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGLMCN)
- [OpenXLab][ChatGPT + 中国語(キーが必要)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGPTCN)
- [OpenXLab][ChatGPT + 英語(キーが必要)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGPTEN)
- [OpenXLab][ChatGLM + 中国語(キー付き)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGLMCN)
- [OpenXLab][ChatGLM + 英語(キー付き)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGLMEN)
- [Private Server][ChatGPT + 中国語(キー付き)](http://llmriddles.opendilab.net/)

ヒントや解決策についての技術ブログも提供しています: [リンク](https://zhuanlan.zhihu.com/p/667801731)

ローカルへのデプロイは以下の方法で行うことができます:
## インストール
### ChatGPT / ChatGLM API を使用する
```shell
pip3 install -r requirements.txt
```
### ローカル推論用に Mistral-7B-Instruct-v0.1 をデプロイする
```shell
pip3 install -r requirements-dev.txt
```
## 立ち上げ
### ChatGPT + 中国語
```shell
QUESTION_LANG=cn QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### ChatGPT + 英語
```shell
QUESTION_LANG=en QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### ChatGLM + 中国語
```shell
QUESTION_LANG=cn QUESTION_LLM='chatglm' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### ChatGLM + 英語
```shell
QUESTION_LANG=en QUESTION_LLM='chatglm' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### Mistral-7B-Instruct-v0.1 + 英語
```shell
QUESTION_LANG=en QUESTION_LLM='mistral-7b' python3 -u app.py
```
## :technologist: なぜこれをするのか

私たちの目標は、このゲームを通じて、プロンプトエンジニアリングと自然言語処理の魅力的な側面を参加者に深く理解してもらうことです。このプロセスでは、プロンプトを巧みに構成する方法や、人工知能システムから驚くような回答を引き出すためのプロンプトの使い方を選手たちに示すと同時に、ディープラーニングや自然言語処理技術の驚異的な力をより深く理解できるようにする。

## :raising_hand: カスタムレベルの提出方法
面白い質問やアイデアがあれば、プレイヤーは自分のアイデアを提出することができます。あなたは[プルリクエストの開始](https://github.com/opendilab/LLMRiddles/compare)を行い、私たちに送信することができます。承認後、私たちはそれをレベルに含めます。
質問形式には以下の点を含めること:
- プルリクエストタイトル, 例: feature(username): Chapter X-Level Design
- 記載したい ID
- 対応する章の問題ファイルを修正する
- \__init__.py の修正

完全な例については、以下を参照のこと: [自分のレベルデザインを提出する](https://github.com/opendilab/LLMRiddles/pull/6)

## :writing_hand: ロードマップ

- [x] カスタムレベルをサポート
- [x] オンライントライアルリンク
- [x] Hugging Face Space のリンク
- [x] Mistral-7B（英語版）のサポート
- [x] ChatGLM（中国語版と英語版）のサポート
- [x] ソリューションブログ
- [ ] Baichuan2-7B（中国語版）のサポート
- [ ] LLaMA2-7B（英語版）のサポート
- [ ] LLM推論速度の最適化
- [ ] 問題レベルの追加

## :speech_balloon: フィードバックとコントリビュート
- GitHub の [Issue を開始](https://github.com/opendilab/CodeMorpheus/issues/new/choose)
- メールでのお問い合わせ (opendilab@pjlab.org.cn)
- OpenDILab の WeChat グループで議論する（WeChat で私たちを追加する: ding314assist）
<img src=https://github.com/opendilab/LLMRiddles/blob/main/llmriddles/assets/wechat.jpeg width=35% />

## :star2: スペシャルサンクス
- このプロジェクトの開発と拡張にインスピレーションと動機を与えた、オリジナルのアイデアとタイトルを提供してくれた [Haoqiang Fan](https://www.zhihu.com/people/haoqiang-fan) に感謝します。
- ゲームのサポートと支援をしていただいた [Hugging Face](https://huggingface.co) に感謝します。
- ゲームのサポートと支援、特に十分な推論トークンのサポートをしていただいた [ChatGLM](https://chatglm.cn) に感謝します。
- [LLM Riddles のコントリビューター](https://github.com/opendilab/LLMRiddles/graphs/contributors)の実装とサポートに感謝します。

## :label: ライセンス
このリポジトリ内のすべてのコードは [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) の下にあります。

<p align="right">(<a href="#top">トップへ戻る</a>)</p>
