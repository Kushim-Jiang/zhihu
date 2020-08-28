### 绪论

本专栏主要讨论通用字符集 universal character set 以及历史上的各编码字符集 coded character set 所收录的广义汉字。

通用字符集对汉字的整理首先着眼于多提交源 submitter source 引致的多规约 convention 上。因不同提交源的字形标准不同，对于记录同一语素的汉字，其显现形式 presentation form 因此存在差异。从这一点出发，立刻可以建立抽象构形 abstract shape 与具象构形 actual shape 的二分。即在普泛的层面上首先存在一抽象构形，各提交源上的字形则是该抽象构形在该提交源所属的规约下表现的具象构形。在这个意义上，多栏式 multi-column 的码表 code chart 即在展现同一抽象构形在各提交源下的具体实现。

但在第一份跨国广义汉字字符集的国际标准发布后的约十年内（从 1993 年起至 2003 年），囿于技术限制，对于同一提交源所提交的绝似具象构形，首先考虑从编码字符集兼容性、字书字头区分性等更高层次理由加以强制区分（1993 年至 2000 年），在这些高层次理由被否决后则因认同原则 unification 被撤回（2000 年至 2003 年）。

但 government requirement 仍要求这些 unifiable 具象构形具有字符集层面的区分性，这要求引入一种既保证 unification 的功能，又满足字符集层面区分性的附加结构。这一附加结构即为 2003 年起引入的 ideographic variation database。在这一结构下，一个对应于 CJK unified ideograph 的 codepoint 仅蕴含抽象构形的信息，在给定提交源后依据其规约表现出具象构形，或者在其后接一个 ideographic variation selector 指定该抽象构形所对应的具象构形。由此，一具象构形在通用字符集中的表记或是一 CJK unified ideograph 的 codepoint 与一提交源构成的二元组，或是一 CJK unified ideograph 的 codepoint 与一 ideographic variation selector 的 codepoint 构成的二元组。

此外简要介绍 ideographic description sequence，这是由 ideographic description character 与 CJK unified ideograph 构成的前序表达式。因此本质上任一 ideographic description sequence 蕴含的仅有抽象构形信息，须在一规约下才具有其具象构形。
