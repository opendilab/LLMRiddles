# LLM Riddles

<div align="center">
	<br>
	<a href="https://github.com/opendilab/LLMRiddles/blob/main/llmriddles/assets/banner.svg">
		<img src="https://github.com/opendilab/LLMRiddles/blob/main/llmriddles/assets/banner.svg" width="1000" height="200" alt="Click to see the source">
	</a>
	<br>
</div>

[English](https://github.com/opendilab/LLMRiddles/blob/main/README.md) | 简体中文

## :thinking: 什么是LLM Riddles
欢迎来到 LLM Riddles！这是一个与语言模型斗智斗勇的游戏。在游戏中，你需要构造与语言模型交互的问题，来得到符合要求的答案。在这个过程中，你可以开动脑筋，用你想到的所有方式，让模型输出答案要求的结果。

## :space_invader: 如何试玩
我们提供了在线版本以供玩家直接访问试玩:
- [ChatGPT + 英文(需配置api key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGPTEN)
- [ChatGPT + 中文(需配置api key)](https://huggingface.co/spaces/OpenDILabCommunity/LLMRiddlesChatGPTCN)
- [Mistral + 英文(已预设api key)](https://5e6f7422e348fc7dec.gradio.live)
- [ChatGPT + 中文(已预设api key)](http://llmriddles.opendilab.net/)

本地部署可以通过以下方式：
### ChatGPT + 中文
```shell
QUESTION_LANG=cn QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### ChatGPT + 英文
```shell
QUESTION_LANG=en QUESTION_LLM='chatgpt' QUESTION_LLM_KEY=<your API key> python3 -u app.py
```
### LLaMA2-7b + 中文
```shell
QUESTION_LANG=cn QUESTION_LLM='llama2-7b' python3 -u app.py
```
### LLaMA2-7b + 英文
```shell
QUESTION_LANG=en QUESTION_LLM='llama2-7b' python3 -u app.py
```
## :technologist: 为什么制作这个游戏

我们的目标是通过这一游戏，让参与者深入领略到提示工程（prompt engineering）和自然语言处理的令人着迷之处。这个过程将向玩家们展示，如何巧妙地构建提示词（prompts），以及如何运用它们来引发人工智能系统的惊人反应，同时也帮助他们更好地理解深度学习和自然语言处理技术的不可思议之处。

## :raising_hand: 如何提交设计好的关卡
如果有好玩的问题或想法，欢迎玩家提交自己的创意，可以
[发起 Pull Request](https://github.com/opendilab/LLMRiddles/compare) 向我们提交， 我们会在审核通过后收录至关卡中。
问题的设计格式应包含以下几点：
- Pull Request标题，示例：feature(username): 章节X-关卡设计
- 希望被提及的ID
- 对应章节问题文件的修改
- __init__.py的修改

完整示例请参考：[提交属于自己的关卡设计](https://github.com/opendilab/LLMRiddles/pull/6)

## :writing_hand: 未来计划

- [x] 支持自定义关卡
- [x] 在线试玩链接
- [x] Hugging Face Space 链接
- [x] 支持Mistral-7B（英文）
- [ ] 支持ChatGLM（中文）
- [ ] 支持Baichuan2-7B（中文）
- [ ] 支持LLaMA2-7B（英文）
- [ ] LLM 推理速度优化

## :speech_balloon: 反馈问题 & 提出建议
- 在 GitHub 上[发起 Issue](https://github.com/opendilab/CodeMorpheus/issues/new/choose)
- 通过邮件与我们联系 (opendilab@pjlab.org.cn)
- 在OpenDILab的群组中加入讨论(通过 WeChat: ding314assist 添加小助手微信)
<img src=https://github.com/opendilab/LLMRiddles/blob/main/llmriddles/assets/wechat.jpeg width=35% />

## :star2: Special Thanks
- 感谢 [Haoqiang Fan](https://www.zhihu.com/people/haoqiang-fan) 的原始创意和题目，为本项目的开发和扩展提供了灵感与动力。
- 感谢 [HuggingFace](https://huggingface.co) 对游戏的支持与协助。
- 感谢 [LLM Riddles contributors](https://github.com/opendilab/LLMRiddles/graphs/contributors) 的实现与支持。

## :label: License
All code within this repository is under [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

<p align="right">(<a href="#top">back to top</a>)</p>
