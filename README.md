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

English | [简体中文](https://github.com/opendilab/LLMRiddles/blob/main/README_zh.md) | [日本語](https://github.com/opendilab/LLMRiddles/blob/main/README_ja.md)

## :thinking: What's This
Welcome to LLM Riddles! This is a game of wits and courage with language models. In the game, you need to construct questions that interact with the language model to get answers that meet the requirements. In this process, you can use your brain and use all the methods you can think of to get the model to output the results required by the answer.

## :space_invader: How to Play
We provide an online version for players to directly access and try out. 
- [Hugging Face][ChatGPT + English(w/o key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGPTEN)
- [Hugging Face][ChatGPT + Chinese(w/o key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGPTCN)
- [Hugging Face][ChatGLM + English(w/ key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGLMEN)
- [Hugging Face][ChatGLM + Chinese(w/ key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGLMCN)
- [OpenXLab][ChatGPT + Chinese(w/o key)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGPTCN)
- [OpenXLab][ChatGPT + English(w/o key)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGPTEN)
- [OpenXLab][ChatGLM + Chinese(w/ key)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGLMCN)
- [OpenXLab][ChatGLM + English(w/ key)](https://openxlab.org.cn/apps/detail/OpenDILab/LLMRiddlesChatGLMEN)
- [Private Server][ChatGPT + Chinese(w/ key)](http://llmriddles.opendilab.net/)

We also provide a technical blog about hints and solutions: [link](https://zhuanlan.zhihu.com/p/667801731)

Local deployment can be done in the following ways:
## Installation
### Use ChatGPT / ChatGLM API
```shell
pip3 install -r requirements.txt
```
### Deploy Mistral-7B-Instruct-v0.1 for local inference
```shell
pip3 install -r requirements-dev.txt
```
## Launch
### ChatGPT + Chinese
```shell
QUESTION_LANG=cn QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### ChatGPT + English
```shell
QUESTION_LANG=en QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### ChatGLM + Chinese
```shell
QUESTION_LANG=cn QUESTION_LLM='chatglm' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### ChatGLM + English
```shell
QUESTION_LANG=en QUESTION_LLM='chatglm' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### DeepSeek + Chinese
```shell
Question_Lang=cn QUESTION_LLM='deepseek' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### DeepSeek + English
```shell
Question_Lang=en QUESTION_LLM='deepseek' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### Mistral-7B-Instruct-v0.1 + English
```shell
QUESTION_LANG=en QUESTION_LLM='mistral-7b' python3 -u app.py
```
## :technologist: Why Doing This

Our goal is to use this game to give participants a deeper understanding of the fascinating aspects of prompt engineering and natural language processing. This process will show players how to cleverly construct prompts and how to use them to trigger surprising responses from artificial intelligence systems, while also helping them better understand the incredible power of deep learning and natural language processing technologies. .

## :raising_hand: How to Submit a Custom Level
If you have interesting questions or ideas, players are welcome to submit their own ideas. You can [Initiate a Pull Request](https://github.com/opendilab/LLMRiddles/compare) and submit it to us. We will include it in the level after approval.
The question format should include the following points:
- Pull Request title, example: feature(username): Chapter X-Level Design
- The ID you want to be mentioned
- Modify the corresponding chapter question files
- Modification of \__init__.py

For a complete example, please refer to: [Submit your own level design](https://github.com/opendilab/LLMRiddles/pull/6)

## :writing_hand: Roadmap

- [x] Support custom levels
- [x] Online trial link
- [x] Hugging Face Space link
- [x] Support Mistral-7B（English version）
- [x] Support ChatGLM（Chinese and English version）
- [x] Solution blogs
- [ ] Support Baichuan2-7B（Chinese version）
- [ ] Support LLaMA2-7B（English version）
- [ ] LLM inference speed optimization
- [ ] More question levels

## :speech_balloon: Feedback and Contribution
- [Start an Issue](https://github.com/opendilab/CodeMorpheus/issues/new/choose) on GitHub
- Contact us by email (opendilab@pjlab.org.cn)
- Discuss on OpenDILab's WeChat group (i.e. add us on WeChat: ding314assist)
<img src=https://github.com/opendilab/LLMRiddles/blob/main/llmriddles/assets/wechat.jpeg width=35% />

## :star2: Special Thanks
- Thanks to [Haoqiang Fan](https://www.zhihu.com/people/haoqiang-fan) for his original idea and title, which provided inspiration and motivation for the development and expansion of this project.
- Thanks to [HuggingFace](https://huggingface.co) for supporting and assisting the game.
- Thanks to [ChatGLM](https://chatglm.cn) for supporting and assisting the game, especially sufficient inference token support.
- Thanks to [LLM Riddles contributors](https://github.com/opendilab/LLMRiddles/graphs/contributors) for their implementation and support.

## :label: License
All code within this repository is under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

<p align="right">(<a href="#top">back to top</a>)</p>
