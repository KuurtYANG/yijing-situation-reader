# 使用指南 · User Guide

《以象推卦 · Yijing Situation Reader》使用说明 / How to use the Yijing Situation Reader skill

---

## 1. 它能做什么 / What it does

你描述现在遇到的事，它会做四件事：找出最贴切的卦，判断你处在哪个阶段（爻位），从四个角度帮你看清局面，再给出具体的下一步。解读依据《周易》原文和曾仕强教授《易经的智慧》的讲解，默认中英双语。

You describe what you're dealing with, and it does four things: finds the hexagram that best fits, works out which stage you're at (the line), shows the situation from four angles, and gives concrete next steps. Readings draw on the *Zhouyi* text and Prof. Zeng Shiqiang's lectures, in Chinese and English by default.

它不是算命工具。它帮你换个角度看清处境，决定仍然由你自己做。

It is not fortune-telling. It helps you see your situation from a new angle; the decision is still yours.

---

## 2. 安装 / Install

**Claude.ai 或 Claude 桌面版 / Claude.ai or the Claude desktop app**

1. 下载 `dist/yijing-situation-reader.zip`。 / Download `dist/yijing-situation-reader.zip`.
2. 打开设置 → 功能 → 技能，上传这个 zip，并确认已开启。 / Open Settings → Capabilities → Skills, upload the zip and make sure it is switched on.

**Claude Code**

```bash
git clone https://github.com/KuurtYANG/yijing-situation-reader.git
mkdir -p ~/.claude/skills
cp -r yijing-situation-reader/yijing-situation-reader ~/.claude/skills/
```

安装后开一个新对话即可使用，不需要输入任何命令。 / After installing, start a new chat; no command is needed.

---

## 3. 怎么提问 / How to ask

直接用平常的话描述你的处境。说得越具体，匹配越准。最好包含这五点：

Just describe your situation in everyday words. The more specific you are, the better the match. Try to cover these five points:

| 要点 Point | 例子 Example |
|---|---|
| 发生了什么 What happened | 老板不断加任务，还抱怨没做完 / My boss keeps adding tasks, then complains they aren't done |
| 你的角色 Your role | 我是团队里的执行者，入职两年 / I'm the one doing the work, two years in |
| 你的状态 Your state | 已经超负荷，每天加班 / Already overloaded, working late every day |
| 外部环境 The environment | 老板很强势，不太听解释 / The boss is assertive and doesn't listen to explanations |
| 你想要什么 What you want | 想减轻负担，又不想得罪他 / I want less on my plate without upsetting him |

**好的提问 / A good prompt**

> 我在一家小公司做项目经理一年了。新来的总监推翻了我们原来的方案，团队里两个人想离职。我想留住团队，但总监不听我的。现在是什么卦？我该怎么做？
>
> I've been a project manager at a small company for a year. A new director scrapped our plan, and two people on my team want to quit. I want to keep the team together, but the director won't listen to me. Which hexagram is this, and what should I do?

**太笼统的提问 / Too vague**

> 我最近运气不好。 / My luck has been bad lately.

如果信息不够，它会先追问一个最关键的问题，然后再解读。

If something important is missing, it will ask you one key question first, then give the reading.

---

## 4. 你会得到什么 / What you get

每次解读按同一个结构给出：

Every reading follows the same structure:

| 部分 Section | 意思 What it means |
|---|---|
| 【处境 Situation】 | 复述你的处境，确认理解没错 / Restates your situation so you can check it understood |
| 【本卦 Hexagram】 | 最贴切的一卦及理由：内卦代表你，外卦代表环境 / The best-fitting hexagram and why; the inner trigram is you, the outer is your environment |
| 【卦辞 Judgement】 | 该卦的原文和白话 / The hexagram's text and its plain meaning |
| 【爻位 Line】 | 你处在六个阶段中的哪一个 / Which of the six stages you're at |
| 【四个角度 Four angles】 | 见下表 / See the table below |
| 【曾仕强怎么说 What Zeng says】 | 曾仕强对这一卦或这一爻的核心讲解 / Zeng's key point on this hexagram or line |
| 【下一步 Next steps】 | 该做、不该做、要留意的信号 / Do, avoid, and signs to watch for |

**四个角度 / The four angles**

| 角度 Angle | 用来看 Shows you |
|---|---|
| 综卦 Reverse | 从对方的立场看同一件事 / The same situation from the other side's point of view |
| 错卦 Inverse | 你现在缺什么 / What you're missing |
| 互卦 Nuclear | 事情内部正在酝酿什么 / What's building underneath |
| 之卦 Changed | 这个阶段一变，局面会走向哪里 / Where things head if this stage changes |

**六个爻位 / The six stages**

| 爻 Line | 阶段 Stage |
|---|---|
| 初 1st | 刚开始、基层 / The very start, the ground floor |
| 二 2nd | 骨干、中层 / Core member, middle level |
| 三 3rd | 过渡期、上下不着，最危险 / In transition, caught in between; the riskiest |
| 四 4th | 接近高层、责任加重 / Close to the top, heavier responsibility |
| 五 5th | 主导者、决策者 / In charge, the decision-maker |
| 上 6th | 末期、过头、该收手 / The end, overdone, time to step back |

---

## 5. 解读之后还可以追问 / Follow-up questions

解读之后可以接着问，例如：

After a reading, you can keep going, for example:

- 「我觉得自己其实在第四爻，重新看一下。」 / "I think I'm actually at the fourth line. Can you look again?"
- 「备选卦和本卦有什么区别？」 / "What's the difference between the main hexagram and the alternative?"
- 「详细讲讲这一爻，曾仕强是怎么解释的？」 / "Tell me more about this line. How does Zeng explain it?"
- 「如果我照第二条去做，可能会怎样？」 / "What might happen if I follow step two?"
- 「两周后情况变了：……现在是什么卦？」 / "Two weeks later things have changed: … Which hexagram is it now?"
- 「只用英文回答。」或「只用中文。」 / "English only, please." or "Chinese only."

---

## 6. 起卦模式 / Casting mode

默认它根据你的处境匹配卦，不随机起卦。如果你想用传统方式，可以明确说：

By default it matches a hexagram to your situation rather than casting one at random. If you'd like the traditional method, just say so:

> 帮我起一卦：要不要接受这个海外工作机会？ / Cast a hexagram for me: should I take this overseas job offer?

它会用三枚铜钱法，由程序产生真正的随机结果，再照常解读本卦、变爻和之卦。

It uses the three-coin method, with a genuinely random result produced by code, then reads the primary hexagram, any changing lines and the changed hexagram as usual.

---

## 7. 小贴士 / Tips

- **一次只问一件事。** 几件事混在一起，匹配会变得模糊。 / **One situation at a time.** Mixing several issues blurs the match.
- **说事实，也说感受。** "老板说了什么"比"老板很讨厌"更有用，但你的状态也很重要。 / **Give facts as well as feelings.** "What the boss said" helps more than "the boss is awful", but your own state matters too.
- **情况变了就再问。** 易经讲变化，局面变了，卦也会变。 / **Ask again when things change.** The Yijing is about change; when the situation shifts, so does the hexagram.
- **不认同就说出来。** 如果觉得某一卦不贴切，告诉它原因，它会重新判断。 / **Push back if it doesn't fit.** If a hexagram feels wrong, say why and it will reconsider.
- **重大决定另找专业意见。** 涉及健康、法律、财务的事，解读只能作为参考。 / **Get professional advice for big decisions.** For health, legal or financial matters, treat the reading as one perspective only.

---

## 8. 常见问题 / FAQ

**为什么默认不起卦？ / Why doesn't it cast a hexagram by default?**
曾仕强认为"善易者不占"：看清处境，自己就知道该怎么做。从处境出发找卦，比随机起卦更贴近你的实际情况。
Zeng held that "those who truly understand the Yijing do not divine": once you see your situation clearly, you know what to do. Starting from your situation gives a reading closer to your real circumstances than a random cast.

**需要先学易经吗？ / Do I need to know the Yijing first?**
不需要。每个术语都会用白话解释，直接描述你的处境就行。
No. Every term is explained in plain words; just describe your situation.

**卦的数据准确吗？ / Is the hexagram data accurate?**
六十四卦的爻码和综、错、互关系由 `tools/build_table.py` 生成并程序校验。卦辞、爻辞引自《周易》原文。
The line codes and the reverse, inverse and nuclear relationships for all 64 hexagrams are generated and checked by `tools/build_table.py`. Judgements and line texts are quoted from the *Zhouyi*.

**"曾仕强怎么说"是原话吗？ / Are the "What Zeng says" parts direct quotes?**
大多是对讲座内容的概括，不是逐字原话。本项目也不是曾仕强教授或其机构的官方作品。
Mostly they summarise his lectures rather than quote him word for word. This project is not an official work of Prof. Zeng or his organisation.

---

## 9. 示例 / Examples

- [新工作三个月，想法总被否定 / Three months into a new job, ideas keep getting shut down](examples/example-new-job.md)
- [老板不断加任务又抱怨没做完 / A boss who keeps adding tasks, then complains they aren't done](examples/example-overloaded.md)
