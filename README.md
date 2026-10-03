# 以象推卦 · Yi Jing (I Ching) Situation Reader

一个 Claude 技能（Skill）：你描述现在发生了什么，它找出最贴切的卦和你所处的阶段（爻位），从四个角度帮你看清局面，再告诉你下一步该怎么做。解读以曾仕强教授《易经的智慧》150 集讲座为主线，中英双语输出。

A Claude Skill: describe what is happening in your life or work, and it finds the best-fitting I Ching hexagram and the stage (line) you are at, shows the situation from four angles, and suggests what to do next. The reading follows Prof. Zeng Shiqiang's 150-episode lecture series *The Wisdom of the Yi Jing (I Ching)* (《易经的智慧》), with answers in both Chinese and English.

> 易经不是算命，而是以象明理、以理指导行动。 / The Yi Jing (I Ching) is not fortune-telling; it is a way to see principles through images and let them guide action.

## 有什么不同 / What makes it different

大多数易经工具先随机起卦，再把结果套到你的问题上。这个技能反过来：**先看你的处境，再找对应的卦**（以象推卦）。这正合曾仕强所说的"善易者不占"——看清处境，自己就知道该怎么做。需要的话也可以用三枚铜钱法起卦。

Most I Ching tools cast a hexagram at random and then fit the answer to your question. This skill works the other way round: **it starts from your situation and finds the hexagram that matches it**. That follows Zeng's point that "those who truly understand the Yi Jing (I Ching) do not divine." Traditional three-coin casting is still available if you ask for it.

每次解读包括 / Each reading covers:

- **本卦 Hexagram**：内卦代表你自己，外卦代表环境 / inner trigram = you, outer trigram = your environment
- **爻位 Line**：你处在事情的哪个阶段 / which stage of the situation you are at
- **四个角度 Four angles**：综卦（对方立场）、错卦（你缺什么）、互卦（内部暗流）、之卦（下一步走向） / the other side's view, what you're missing, the hidden dynamic, and where it heads
- **下一步 Next steps**：该做、不该做、要留意的信号 / do, avoid, and signs to watch for

完整使用说明见 [USAGE.md](USAGE.md)；示例见 [examples/](examples/)。 / See the full user guide in [USAGE.md](USAGE.md), and sample readings in [examples/](examples/).

## 安装 / Install

有三种方式，任选其一。 / There are three ways; pick whichever suits you.

**方式一：不用安装，直接试 / Option 1: Try it without installing**

在任何一个 Claude 对话里粘贴下面这段话，把省略号换成你的处境。Claude 需要能联网读取网页。 / Paste this into any Claude chat, replacing the dots with your situation. Claude needs web access to read the page.

```
请先读取 https://raw.githubusercontent.com/KuurtYANG/yijing-situation-reader/main/yijing-situation-reader/SKILL.md ，然后按照里面的步骤解读我的处境：……

Please read https://raw.githubusercontent.com/KuurtYANG/yijing-situation-reader/main/yijing-situation-reader/SKILL.md and follow its steps to read my situation: …
```

**方式二：Claude 网页版和桌面版 / Option 2: Claude.ai and the Claude desktop app**

1. 下载 zip 文件：[yijing-situation-reader.zip](https://raw.githubusercontent.com/KuurtYANG/yijing-situation-reader/main/dist/yijing-situation-reader.zip)（点击即下载，不用解压）。 / Download the zip: [yijing-situation-reader.zip](https://raw.githubusercontent.com/KuurtYANG/yijing-situation-reader/main/dist/yijing-situation-reader.zip) (the link downloads it directly; don't unzip it).
2. 确认已开启"代码执行"（Settings → Capabilities）。技能需要这个功能才能运行。 / Make sure code execution is turned on (Settings → Capabilities); skills need it to run.
3. 打开 **Customize → Skills**，点 **+**，选 **Create skill**，再选 **Upload a skill**，上传刚才的 zip。 / Open **Customize → Skills**, click **+**, choose **Create skill**, then **Upload a skill**, and upload the zip.
4. 确认技能开关已打开，然后新开一个对话，直接描述你的处境。 / Check the skill is switched on, then start a new chat and describe your situation.

每个人都需要在自己的账号里上传一次。Team 和 Enterprise 方案上传后可以分享给同事。 / Each person uploads it once to their own account. On Team and Enterprise plans you can share it with colleagues after uploading.

**方式三：Claude Code / Option 3: Claude Code**

在 Claude Code 里输入这两条命令： / Run these two commands inside Claude Code:

```
/plugin marketplace add KuurtYANG/yijing-situation-reader
/plugin install yijing-situation-reader@yijing-skills
```

也可以在终端里运行 `claude plugin marketplace add KuurtYANG/yijing-situation-reader` 和 `claude plugin install yijing-situation-reader@yijing-skills`。安装后开一个新会话即可。以后有更新，运行 `/plugin marketplace update yijing-skills`。 / Or run `claude plugin marketplace add KuurtYANG/yijing-situation-reader` and `claude plugin install yijing-situation-reader@yijing-skills` in your terminal. Start a new session afterwards. To get updates later, run `/plugin marketplace update yijing-skills`.

## 使用 / Usage

直接描述你的处境即可，例如： / Just describe your situation, for example:

- 「我刚创业半年，产品有人用但收入不稳，合伙人想放弃，我该怎么办？」
- "My team has been arguing for weeks about the roadmap and two people are thinking of leaving. What hexagram fits, and what should I do?"
- 「帮我起一卦：要不要接受这个海外工作机会？」（起卦模式 / casting mode）

## 准确性 / Accuracy

- 六十四卦的爻码、综卦、错卦、互卦由 [`tools/build_table.py`](tools/build_table.py) 生成并校验：King Wen 卦序中每一对相邻卦都必须互为综卦或错卦，全部通过。 / Line codes and the reverse, inverse and nuclear hexagrams are generated and checked by [`tools/build_table.py`](tools/build_table.py): every adjacent King Wen pair must be a reverse or inverse pair, and all of them pass.
- 修改表格后可重新运行 `python3 tools/build_table.py table.md`，再把输出贴回 SKILL.md。 / After editing the data, rerun `python3 tools/build_table.py table.md` and paste the output back into SKILL.md.

## 说明 / Notes

- 本项目为个人学习整理，非曾仕强教授或其机构的官方作品。表中"曾仕强要旨"是对讲座内容的简要概括，并非原话。 / This is an independent study project, not an official work of Prof. Zeng Shiqiang or his organisation. The "key teaching" entries are brief summaries of his lectures, not direct quotations.
- 《周易》原文属公有领域。 / The *Zhouyi* text is in the public domain.
- 解读仅供思考参考，不构成医疗、法律、财务等专业建议。 / Readings are for reflection only and are not medical, legal or financial advice.

## 许可 / License

[MIT](LICENSE)
