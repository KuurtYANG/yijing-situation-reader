# -*- coding: utf-8 -*-
"""Build and verify the bilingual 64-hexagram table used in SKILL.md.
生成并校验 SKILL.md 中的六十四卦双语总表。

Lines are written bottom-up (初 -> 上), 1 = yang, 0 = yin.
Usage: python3 build_table.py [output.md]
"""

TRI = {  # bottom-up line pattern
    "乾": "111", "兑": "110", "离": "101", "震": "100",
    "巽": "011", "坎": "010", "艮": "001", "坤": "000",
}
ELEM = {"乾": "天", "兑": "泽", "离": "火", "震": "雷", "巽": "风", "坎": "水", "艮": "山", "坤": "地"}

# King Wen order: (name, upper, lower, situation, Zeng's key teaching)
KW = [
    ("乾", "乾", "乾", "实力充足，主动开创、领导局面", "自强不息；按潜见惕跃飞亢分阶段进退，亢龙有悔"),
    ("坤", "坤", "坤", "配合辅助，承接他人主导，需耐心承载", "厚德载物；先迷后得，柔顺而有主见"),
    ("屯", "坎", "震", "万事开头难，草创期在混乱中起步", "始生之难；宜建侯求助，不宜冒进"),
    ("蒙", "艮", "坎", "缺乏经验，需要学习或教导他人", "蒙以养正；求教要诚，教人要因材施教"),
    ("需", "坎", "乾", "条件未成熟，必须等待", "需要等待；有孚光亨，等待中积极准备"),
    ("讼", "乾", "坎", "纠纷争执，利益或是非之争", "作事谋始；讼不可成，宜适可而止、和解"),
    ("师", "坤", "坎", "带团队打硬仗，组织动员，竞争", "师出以正；统帅专权，任人唯贤，小人勿用"),
    ("比", "坎", "坤", "寻求合作结盟，选择亲附对象", "亲比和谐；择善而比，及早亲附，后夫凶"),
    ("小畜", "巽", "乾", "力量尚小，小有积累却被暂时牵制", "以小畜大；密云不雨，蓄德待时"),
    ("履", "乾", "兑", "与强者共事，处境有风险，须讲分寸", "履虎尾不咥人；以柔顺守礼、分寸行事"),
    ("泰", "坤", "乾", "顺利通达，上下沟通良好", "交泰之道；居安思危，修己以安人"),
    ("否", "乾", "坤", "闭塞不通，上下隔绝，不得志", "俭德辟难；守正不苟，否极泰来"),
    ("同人", "乾", "离", "需要团结众人、建立共识", "同人于野；由近及远、大公无私地团结"),
    ("大有", "离", "乾", "资源丰盛，成功拥有之时", "为富要仁；柔中御刚，遏恶扬善"),
    ("谦", "坤", "艮", "有成就、地位上升，最易骄傲之时", "谦谦君子；真谦非假谦虚，劳谦有终"),
    ("豫", "震", "坤", "安乐顺遂，士气振奋", "谦而后豫；安乐不忘忧患，勿耽于逸乐"),
    ("随", "兑", "震", "追随他人或被追随，顺应时势", "随时之义；慎择追随对象，发自内心"),
    ("蛊", "艮", "巽", "积弊腐败，需接手整顿烂摊子", "干父之蛊；败坏不可怕，怕的是无所作为"),
    ("临", "坤", "兑", "居上位亲临管理，事业正上升", "教思无穷；柔顺包容，盛极当惧"),
    ("观", "巽", "坤", "被众人观察，需以身作则或观察形势", "风行草偃；以身作则，观我生观其生"),
    ("噬嗑", "离", "震", "有障碍需清除，需执行规矩、惩处", "明罚敕法；防微杜渐，惩罚适度"),
    ("贲", "艮", "离", "包装修饰，形象与实质的平衡", "文质相称；文饰恰如其分，终归本真"),
    ("剥", "艮", "坤", "衰败侵蚀，小人渐长，根基动摇", "顺而止之；厚植根基，守正以待剥极而复"),
    ("复", "坤", "震", "低谷后复苏，重新开始，改过", "一阳来复；不远而复，及早修复、涵养新机"),
    ("无妄", "乾", "震", "按规律行事，或遭遇意外之灾", "不妄为；依理而行，无心之祸亦须防"),
    ("大畜", "艮", "乾", "大量积累实力人才，蓄势待发", "蓄德日新；审时而动，慎始敬终"),
    ("颐", "艮", "震", "养生养人，言语饮食，自我供养", "自求口实；慎言语、节饮食，养正则吉"),
    ("大过", "兑", "巽", "负担过重，本末失衡，非常时期", "栋桡之象；刚柔相济化险，独立不惧"),
    ("坎", "坎", "坎", "重重险难，反复陷入困境", "行险不失其信；刚中守信，习险而出险"),
    ("离", "离", "离", "需要依附正道、发挥才智光明", "丽乎正；光明须附丽正道，继明照四方"),
    ("咸", "兑", "艮", "感情萌发，相互吸引，心意相通", "无心之感；感应发自真诚，不掺心机"),
    ("恒", "震", "巽", "长期关系或事业，需持之以恒", "立不易方；在变动中坚守根本方向"),
    ("遁", "乾", "艮", "形势不利，需要退让抽身", "以退为进；及早预留退路，全身而退"),
    ("大壮", "震", "乾", "实力强盛，气势正旺", "非礼弗履；刚健合乎正道，不可恃强妄动"),
    ("晋", "离", "坤", "晋升进展，获得赏识", "自昭明德；宽以待人，以柔顺光明上进"),
    ("明夷", "坤", "离", "处境黑暗，才能被压制或遭打压", "用晦而明；内守光明，外表韬光养晦"),
    ("家人", "巽", "离", "家庭或内部团队关系", "言有物而行有恒；忠厚积善，诚信齐家"),
    ("睽", "离", "兑", "意见分歧，互相猜疑，关系乖离", "同而异；放下猜疑，大处求同、小处存异"),
    ("蹇", "坎", "艮", "前路艰难，行动受阻", "反身修德；见险能止，求助大人，往蹇来誉"),
    ("解", "震", "坎", "困难开始化解，紧张缓和", "赦过宥罪；化险为夷，宜早不宜迟"),
    ("损", "艮", "兑", "需要减少、牺牲、节制欲望", "惩忿窒欲；损要有诚，为道日损"),
    ("益", "巽", "震", "获得增益扩张，助人或受助", "损上益下；见善则迁，有过则改"),
    ("夬", "兑", "乾", "需要果断决断，清除积弊或小人", "决而和；公开以德服人，不可尚武逞强"),
    ("姤", "乾", "巽", "不期而遇，新诱惑或风险初萌", "见微知著；相遇不由人，应对由人"),
    ("萃", "兑", "坤", "人群聚集，组织整合", "聚以正；聚而思防，诚信为本"),
    ("升", "坤", "巽", "稳步上升，职位或事业成长", "积小以高大；循序渐进，知升知止"),
    ("困", "兑", "坎", "穷困受限，有理说不清", "困而不失其所；致命遂志，尚口乃穷"),
    ("井", "坎", "巽", "提供服务资源，制度建设，价值被忽视", "井养不穷；不变而通，修井待用"),
    ("革", "兑", "离", "需要变革，改换旧制", "顺天应人；时机成熟、取信于人再变"),
    ("鼎", "离", "巽", "变革后建立新秩序，用人立业", "正位凝命；礼贤下士，才须配位"),
    ("震", "震", "震", "突发冲击，惊恐事件", "恐惧修省；先恐惧后从容"),
    ("艮", "艮", "艮", "需要停下、冷静、止步", "知止不殆；动静有时，思不出其位"),
    ("渐", "巽", "艮", "循序渐进的发展（求职、关系推进）", "居贤德善俗；止而后渐，不可躁进"),
    ("归妹", "震", "兑", "不对等的结合，身不由己的安排", "永终知敝；安分守正，务实戒虚"),
    ("丰", "震", "离", "盛大巅峰，事业最旺之时", "宜日中；盛极生忧，防蒙蔽、贵诚信"),
    ("旅", "离", "艮", "在外漂泊，寄人篱下，身处新环境", "旅贞吉；柔顺谦和守正，切忌骄矜"),
    ("巽", "巽", "巽", "需要渗透、说服、柔性影响", "申命行事；柔顺而有立场，勿过于卑顺"),
    ("兑", "兑", "兑", "和悦沟通、谈判，讨好与被讨好", "刚中柔外；真悦不伪悦，防被谄媚蒙蔽"),
    ("涣", "巽", "坎", "人心涣散，团队分崩，危机后重聚", "以至诚聚涣；舍小我以全大局"),
    ("节", "坎", "兑", "需要节制，立规矩定界限", "制数度议德行；甘节吉，苦节不可贞"),
    ("中孚", "巽", "兑", "需要建立信任，诚信受考验", "中虚外实；合理诚信，而非滥好人"),
    ("小过", "震", "艮", "小事可稍过，宜低调谨慎", "可小事不可大事；宜下不宜上"),
    ("既济", "坎", "离", "事情已成，成功之后", "思患预防；初吉终乱，成功后最易松懈"),
    ("未济", "离", "坎", "尚未完成，临近终点", "永怀希望；小狐濡尾，越近终点越谨慎"),
]

# English: (pinyin name, English title, situation, Zeng's key teaching)
EN = [
    ("Qian", "The Creative", "Strong and ready; taking the initiative and leading", "Strive ceaselessly; advance or hold back by stage, from the hidden dragon to the arrogant dragon who regrets"),
    ("Kun", "The Receptive", "Supporting a lead set by others; patient, steady carrying", "Carry all with generous virtue; lost at first, finding the way later; yielding yet with judgement"),
    ("Zhun", "Difficulty at the Beginning", "Starting something new amid confusion", "All beginnings are hard; find helpers and allies, do not rush ahead"),
    ("Meng", "Youthful Folly", "Inexperienced; needing to learn, or to teach others", "Nurture what is right in the young; learn sincerely, teach according to the person"),
    ("Xu", "Waiting", "Conditions not yet ripe; you must wait", "Wait with sincerity; prepare actively while waiting"),
    ("Song", "Conflict", "A dispute over interests or right and wrong", "Plan well at the start; do not push a dispute to the end, settle it"),
    ("Shi", "The Army", "Leading a team through a hard contest; mobilising people", "Act only for a just cause; one clear commander, appoint the worthy, not petty people"),
    ("Bi", "Holding Together", "Seeking partners or allies; choosing whom to join", "Join the good, and join early; the latecomer meets misfortune"),
    ("Xiaoxu", "Small Taming", "Small strength, modest gains, temporarily held back", "Dense clouds, no rain yet; build virtue and wait for the time"),
    ("Lü", "Treading", "Working alongside the powerful; risk calls for tact", "Tread on the tiger's tail without being bitten: courtesy, gentleness, a sense of measure"),
    ("Tai", "Peace", "Things go smoothly; communication flows up and down", "Heaven and earth in interchange; stay alert in good times, cultivate yourself to settle others"),
    ("Pi", "Standstill", "Blocked; top and bottom cut off; unable to get on", "Keep a low profile to avoid harm; hold to what is right, stagnation turns to peace"),
    ("Tongren", "Fellowship", "Uniting people and building consensus", "Unite from near to far, openly and without partiality"),
    ("Dayou", "Great Possession", "Abundance; the time of success and plenty", "Wealth requires benevolence; curb evil, promote good, firmness guided by gentleness"),
    ("Qian", "Modesty", "Rising in status after success, when pride comes easily", "The truly modest person: real modesty, not false humility; modest hard work ends well"),
    ("Yu", "Enthusiasm", "Ease, success and high spirits", "Contentment follows modesty; never forget worries in times of ease"),
    ("Sui", "Following", "Following others or being followed; going with the times", "Follow what the time requires; choose carefully whom you follow, and follow sincerely"),
    ("Gu", "Repairing Decay", "Inheriting a mess; corruption that needs fixing", "Decay is not the danger; doing nothing about it is"),
    ("Lin", "Approach", "Leading from close at hand while your career is rising", "Teach and care without limit; tolerant rather than forceful; fear the peak"),
    ("Guan", "Contemplation", "Watched by others; lead by example, or survey the situation", "As the wind blows the grass bends; lead by example, look at yourself and at others"),
    ("Shihe", "Biting Through", "An obstacle must be removed; rules must be enforced", "Clear penalties, firm laws; stop small faults early, punish in proportion"),
    ("Bi", "Grace", "Presentation and image versus substance", "Form must suit substance; adornment in due measure, returning to plainness"),
    ("Bo", "Splitting Apart", "Erosion and decline; petty people gaining; foundations shaking", "Yield and stop; strengthen the foundations, hold firm until decline turns"),
    ("Fu", "Return", "Recovery after a low point; a fresh start; correcting mistakes", "One yang returns; correct course early and nurture the new beginning"),
    ("Wuwang", "Innocence", "Acting according to the natural order; or an unexpected setback", "Do nothing reckless; act by principle, and guard even against misfortune you did not cause"),
    ("Daxu", "Great Taming", "Building up strength and talent before acting", "Accumulate and renew your virtue daily; act at the right time, careful from start to finish"),
    ("Yi", "Nourishment", "Nourishing yourself and others; words, food, self-support", "Seek your own sustenance; be careful in speech and moderate in eating"),
    ("Daguo", "Great Exceeding", "Overloaded; top and bottom out of balance; an extraordinary time", "The ridgepole sags; balance firmness with flexibility, stand alone without fear"),
    ("Kan", "The Abysmal (Water)", "Danger upon danger; repeatedly trapped", "Pass through danger without losing good faith; firm at the core, learn the way through"),
    ("Li", "The Clinging (Fire)", "Needing to attach to what is right; showing your brightness", "Brightness must cling to what is right to shine far and long"),
    ("Xian", "Influence", "Mutual attraction; feelings awakening; hearts in tune", "Feeling without contrivance; sincere response, no scheming"),
    ("Heng", "Duration", "A long-term relationship or career; persistence needed", "Stand firm without changing direction; keep the core while things change"),
    ("Dun", "Retreat", "Conditions are against you; time to step back", "Retreat in order to advance; plan your exit early and withdraw intact"),
    ("Dazhuang", "Great Power", "Strong and in full momentum", "Never act against propriety; strength must follow what is right, never rely on force"),
    ("Jin", "Progress", "Promotion, progress, recognition", "Let your own virtue shine; be lenient with others, rise through gentle brightness"),
    ("Mingyi", "Darkening of the Light", "A dark time; your ability is suppressed or attacked", "Hide your light and stay bright within; keep a low profile outwardly"),
    ("Jiaren", "The Family", "Family or close-team relationships", "Words with substance, conduct that lasts; honest, kind and trustworthy at home"),
    ("Kui", "Opposition", "Disagreement, suspicion, drifting apart", "Seek common ground on big things, accept differences on small ones; let go of suspicion"),
    ("Jian", "Obstruction", "The road ahead is hard; your moves are blocked", "Turn inward and cultivate virtue; stop at danger, seek help from the capable"),
    ("Xie", "Deliverance", "Difficulties easing; tension relaxing", "Forgive faults and pardon wrongs; settle things early rather than late"),
    ("Sun", "Decrease", "Needing to cut back, sacrifice, or restrain desires", "Restrain anger and desire; decrease with sincerity"),
    ("Yi", "Increase", "Gaining and expanding; helping or being helped", "Take from above to benefit below; follow the good, correct your faults"),
    ("Guai", "Breakthrough", "A decisive call is needed; clearing out what is rotten", "Decide firmly yet harmoniously; win openly through virtue, not force"),
    ("Gou", "Coming to Meet", "An unexpected encounter; a new temptation or risk emerging", "See the large in the small; you cannot choose what you meet, only how you respond"),
    ("Cui", "Gathering", "People coming together; organising and integrating", "Gather by what is right; prepare for trouble while gathered; good faith is the root"),
    ("Sheng", "Pushing Upward", "Steady rise in position or career", "Accumulate small steps into greatness; rise gradually, know when to stop"),
    ("Kun", "Oppression", "Hard pressed and constrained; your words not believed", "In hardship do not lose your footing; fulfil your aim, do not rely on talk"),
    ("Jing", "The Well", "Providing service or resources; building systems; value overlooked", "The well nourishes without end; change in form, constant in essence; keep it in repair"),
    ("Ge", "Revolution", "Change is needed; replacing the old order", "Follow heaven and respond to people; change when the time is ripe and trust is won"),
    ("Ding", "The Cauldron", "Building a new order after change; appointing people", "Set things in their right places; honour talent, match ability to position"),
    ("Zhen", "Thunder", "A sudden shock or alarming event", "Fear, then reflect and improve; first alarm, then composure"),
    ("Gen", "Keeping Still", "Time to stop, calm down and hold still", "Knowing when to stop avoids danger; move and rest in season, stay within your role"),
    ("Jian", "Gradual Progress", "Step-by-step development (a job search, a relationship)", "Stop first, then advance gradually; never rush"),
    ("Guimei", "The Marrying Maiden", "An unequal match; an arrangement not of your choosing", "Know the flaws that last; keep to your place and stay practical"),
    ("Feng", "Abundance", "At the peak; the most prosperous time", "Like the sun at noon; worry at the peak, guard against being blinded, value good faith"),
    ("Lü", "The Wanderer", "Away from home; dependent on others; a new environment", "Be gentle, modest and upright; above all avoid arrogance"),
    ("Xun", "The Gentle (Wind)", "Needing to penetrate, persuade or influence gently", "Repeat the command and act; gentle yet with a position, never servile"),
    ("Dui", "The Joyous (Lake)", "Pleasant communication, negotiation, flattery given or received", "Firm inside, gentle outside; real joy, not false joy; beware of flattery"),
    ("Huan", "Dispersion", "People drifting apart; a team breaking up; regrouping after a crisis", "Reunite through utmost sincerity; set aside the small self for the whole"),
    ("Jie", "Limitation", "Needing restraint, rules and boundaries", "Set measures and weigh conduct; sweet limits bring luck, bitter limits cannot last"),
    ("Zhongfu", "Inner Truth", "Building trust; integrity being tested", "Empty within, solid without; sensible good faith, not being a pushover"),
    ("Xiaoguo", "Small Exceeding", "Small excess is acceptable; stay low and careful", "Fine for small matters, not for great ones; fly low, not high"),
    ("Jiji", "After Completion", "The thing is done; after success", "Think of trouble and prevent it; good at first, disorder at the end; success breeds slackness"),
    ("Weiji", "Before Completion", "Not yet finished; close to the goal", "Always keep hope; the little fox wets its tail, so the nearer the end, the more care"),
]
assert len(EN) == 64

def full_name(name, up, lo):
    if up == lo:
        return f"{name}为{ELEM[up]}"
    return f"{ELEM[up]}{ELEM[lo]}{name}"

table = []
for i, ((n, up, lo, sit, zeng), (py, title, sit_en, zeng_en)) in enumerate(zip(KW, EN), 1):
    table.append(dict(no=i, name=n, up=up, lo=lo, lines=TRI[lo] + TRI[up], sit=sit, zeng=zeng,
                      full=full_name(n, up, lo), py=py, title=title, sit_en=sit_en, zeng_en=zeng_en))
by_lines = {h["lines"]: h for h in table}
assert len(by_lines) == 64, "duplicate line pattern"

def inv(s): return "".join("1" if c == "0" else "0" for c in s)
for h in table:
    L = h["lines"]
    h["zong"] = by_lines[L[::-1]]["name"]
    h["cuo"] = by_lines[inv(L)]["name"]
    h["hu"] = by_lines[L[1:4] + L[2:5]]["name"]

# Check 1: each King Wen pair is a reversal (综), or an inversion (错) when the hexagram is symmetric
for k in range(0, 64, 2):
    a, b = table[k], table[k + 1]
    rev = a["lines"][::-1]
    expect = rev if rev != a["lines"] else inv(a["lines"])
    assert b["lines"] == expect, (a["name"], b["name"])
# Check 2: spot checks against well-known hexagrams
chk = {"乾": "111111", "坤": "000000", "既济": "101010", "未济": "010101",
       "泰": "111000", "否": "000111", "屯": "100010", "蒙": "010001", "中孚": "110011", "小过": "001100"}
for n, l in chk.items():
    assert by_lines[l]["name"] == n, n
assert table[0]["hu"] == "乾" and table[62]["hu"] == "未济" and table[10]["hu"] == "归妹"
print("all checks passed")

rows = ["| # | 卦 Hexagram | 爻 Lines (初→上) | 综 | 错 | 互 | 常见情境 Typical situation | 曾仕强要旨 Zeng's key teaching |",
        "|---|---|---|---|---|---|---|---|"]
for h in table:
    rows.append(f"| {h['no']} | {h['name']} {h['full']}<br>{h['py']} · {h['title']} | {h['lines']} | {h['zong']} | {h['cuo']} | {h['hu']} "
                f"| {h['sit']}<br>{h['sit_en']} | {h['zeng']}<br>{h['zeng_en']} |")
import sys
out = sys.argv[1] if len(sys.argv) > 1 else "hexagram_table.md"
open(out, "w", encoding="utf-8").write("\n".join(rows) + "\n")
print(len(rows) - 2, "rows written to", out)
