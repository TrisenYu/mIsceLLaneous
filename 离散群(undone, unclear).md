先前写过一次方程根和群的关系，但是理解不够深，而且部分解释可能有误，于是就删掉了。这次再来试着写一点自己的理解。

最开始研究方程 $a_{n - 1}x^{n - 1} + \cdots + a_{1} x + a_{0} = 0, a_{n - 1} \neq 0$ 的根，方程的系数均在有理数构成的集合内。

后来抽象到研究 $f(x) = a_{n - 1}x^{n - 1} + \cdots + a_{1} x + a_{0}, a_{n - 1} \neq 0$ 的零点。

而对于此类方程的零点，这里不加证明的引用代数基本定理，也即求出所有满足 $\forall \alpha_{i} \in \{\alpha_{1}, \ldots, \alpha_{n-1}\}, f(\alpha_{i}) = 0$ 的解构成的集合，并找到一种可以用简单加减乘除和开任意次方根号来表示的通用形式。

早前在研究过程中，先假定已经知道了根，提前列出连乘式，根据逻辑展开化简后得到根与系数的关系，并试图由此反解方程的根式求根公式，即 
$$a_{n - 1} \cdot \displaystyle\prod_{i = 1}^{n - 1}(x - \alpha_i) = 0 \Rightarrow \displaystyle\prod_{i = 1}^{n - 1}(x - \alpha_i) = x^{n-1} - \Big(\sum_{i = 1}^{n - 1}\alpha_{i}\Big) x^{n-2} +  \cdots + (-1)^{n-1}\displaystyle\prod_{i = 1}^{n - 1}\alpha_{i} = 0$$

> 注意到方程的首项系数从 $\alpha_{n - 1}$ 变为了 $1$。
>> 不失一般性，将最开始的方程转移到这种首项系数为 $1$（简称首一）的多项式方程上。即直接认为 $x^{n - 1} + a_{n - 2}x^{n - 2} +\cdots + a_{1} x + a_{0} = 0$ 即为原始方程。

进而得到 $n-1$ 个对称多项式，分别确定的系数。

$$\begin{cases}
   \delta_{1} = \sum\limits \alpha_{i} = -a_{n-2} \\
   \delta_{2} =\sum\limits \alpha_{i}\alpha_{j} = a_{n-3} \\
   \delta_{3} =\sum\limits \alpha_{i}\alpha_{j}\alpha_{k} =-a_{n-4} \\
   \quad \quad \quad \quad  \vdots \\
   \delta_{n-1} =\alpha_{1}\alpha_{2}\alpha_{3}\cdots \alpha_{n-1} = (-1)^{n-1}a_{0}
\end{cases}$$

不难看到无论如何交换根，因加法与乘法的交换律的存在，上式始终不变。

还注意到根可能并不会在原有的有理数集合中，否则第一次数学危机不会出现。

且因集合本身并未加入额外的运算，故现从最基础的单个运算与集合开始研究原本的代数系统。

------------------------

为了描述『划分某个大类为多个小类』的数学表示，考察大类 $S$ 内的元素 $x$ 及其所代表的等价类 $[x]$。 存在关系 $\sim$ 满足：

- $x\in S, x\sim x$。自反射性（所谓自反性、Reflectivity）。
- $x, y\in [x], x\sim y \iff y \sim x$。对称性。
- $x, y, z\in [x], x\sim y, x\sim z \Rightarrow  y \sim z$。传递性。

因此，关系 $\sim$ 形成对大类 $S$ 的一种划分方式。可将整个大类模掉关系 $\sim$ 后得到剩余的小类。

于是可在有限的步骤内借由这种对等价类的划分来细分大类。

因方程的对称性，考虑对所有根构成集合的置换操作。

而群是从研究排列而抽象出的代数结构。研究群可直接从两方面入手：群自身的结构以及群对另外某个结构的作用。

称 $N_s = \begin{pmatrix} 1 &2 &3 &\cdots &n\end{pmatrix}$ 表示自然序列。

简记 $(i, j)$ 为对 $i$ 和 $j$ 的对换。记 $(i, j, k)$ 为以 $i$ 为操作对象，依次交换掉 $j$ 和 $k$ 的三次轮换，即 $3-$ 轮换。其它次数的轮换同理。

**定理一** 任何一个 $k-$ 轮换，都能被分解为若干对换的复合。


表示上有 $\begin{bmatrix}
  1 &2 &3 &\cdots &i &\cdots &j &\cdots &k &\cdots &n \\
  \downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow\\
  1 &2 &3 &\cdots &j &\cdots &i &\cdots &k &\cdots &n \\
  \downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow&\downarrow\\
  1 &2 &3 &\cdots &j &\cdots &k &\cdots &i &\cdots &n \\
\end{bmatrix}$。


轮换可被分解为多个对换的复合。但在此之前，定义这种一个或者多个轮换与对换构成的置换操作是一种对原始自然序列的映射 $\sigma$。

不难看出这样的 $\sigma$ 共有 $n!$ 个，且任意多个映射在先后顺序上的复合能够被这 $n!$ 个中的一个完全确定。

同时，能注意到这种 $\sigma$ 之间的复合一定满足结合律但并不总是满足交换律，除了一种保持原有序列不动的映射能使之满足交换律。且对 $n!$ 中任意元素而言，总是存在另一个属于此 $n!$ 个元素构成集合中的元素，在复合后变回保持原有序列不动的映射。

> 此处可用魔方的转动形象理解。


由上述启发，定义

- 群是一种由封闭在集合 $\{x_{1}, x_{2}, \ldots, x_{n}\}$ 内的有限或无限个元素以及某个唯一的特定运算 $\circ$ 构成的代数结构 $G \stackrel{\operatorname{def}}{=}\langle\{x_{1}, x_{2}, \ldots, x_{n}\}, \circ\rangle$。并定义群中元素个数为 $|G|$。

- 置换操作形成群。且这种群可以**作用于**集合 / 自然排列。

> 为方便起见，本文不讨论李群，而只讨论有限元素的群。

在操作 $\circ$ 无歧义的情况下，本文直接以群代指集合，并略去运算符。

群需满足以下四个公理：

- 封闭性：$\forall a, b \in G, ab \in G$。动机：保持集合性质。
- 结合性：$\forall a, b, c \in G, (ab)c = a(bc)$。动机：保持运算的性质，也就是使得某些映射 / 运算顺序一定时，先做前面和先做后面的效果一致。
- 存在单位元：$\forall a \in G, \exists e \in G, \operatorname{s.t.}ae = ea = a$。动机：在对某一元素施加运算后保持元素不变。
- 存在逆元。$\forall a \in G, \exists b \in G, \operatorname{s.t.}ab = ba = e$。

> 至此，如仅仅研究整数集 $\mathbb{Z}$ 和  $+$ 构成的代数系统，不难发现 $\langle\mathbb{Z}, +\rangle$ 形成上述定义的群。

受连续加法 $\overbrace{a+a+a+\cdots+a}^{n} = n\cdot a$ 自然引出乘法，连续乘法 $\overbrace{a\cdot a\cdot a\cdot \cdots\cdot a}^{n} = a^n$ 引出次幂的启发，直接定义群上对同一个元素的多次运算为幂运算。即

$$\forall a \in G, k \in \mathbb{N}^{+}, a^{k} = \overbrace{a\circ a\circ a\circ \cdots \circ a}^{k}$$

- 因群封闭，故 $\forall k \in \mathbb{N}^{+}, a \in G, a^{k} \in G$。
- 因群具有结合律，有推论 $\begin{cases}
    a^{m + n} = \overbrace{a\circ a\circ a\circ \cdots \circ a}^{m}\circ\overbrace{a\circ a\circ a\circ \cdots \circ a}^{n} = a^{m} \circ a^{n} = a^{n} \circ a^{m} = a^{n+m} \\
    a^{mn} = \underbrace{\overbrace{(a\circ a\circ a\circ \cdots \circ a)}^{m}\circ\cdots\circ(a\circ a\circ a\circ \cdots \circ a)}_{n} = (a^{m})^{n}
\end{cases}$。
- 因群存在单位元，有推论 $\forall k \in \mathbb{N}^{+}, e^k = e$。
- 因群中存在逆元，有推论 $a^{-k} = \overbrace{a^{-1}\circ a^{-1}\circ a^{-1}\circ \cdots \circ a^{-1}}^{k}$。

在此，群的四个公理衍生出了非常有趣的性质。

- 注意到幂运算中，群封闭推导出的结论并不代表群中任意元素的任意次幂能完全复原整个群。如所有群都具有的最平凡的子群 $\lang \Set{e}, \circ \rang$。
  - 也就是说，群中包含有一个潜在的、并可能覆盖不了自身的封闭循环结构，且应能类比集合的直积，**群也应该能被剖分成多个子群的直积**。

- 又注意到幂运算中，幂次的加法和乘法可交换。不妨将其推广：在群上的运算 $\circ$ 能使得交换变元位置后结果依然保持不变时，称群为阿贝尔群，意即可交换的群。

- 考虑单位元外其它所有元素中，首次能形成单位元的幂运算次数 $\forall a \in G, k \in \mathbb{N}^{+}, a^{k} = e, \operatorname{ord}(a) = \min k$，并将 $\operatorname{ord}(a)$ 定义为群元素 $a$ 的阶。

由上述推论，自然考虑以下几个定义：
- 在幂运算次数到达阶数时，生成了群内其余元素的元素称为群 $G$ 的生成元 $g$。将其形成的集合记为 $\{g\}$。
  - 那么，进而有不那么明显的三个推论 $\begin{cases}
    \forall a \in G, a^{k} = e \Rightarrow \operatorname{ord}(a) \mid k \\ \\
    \exists a^{k} \in \{g\} \Rightarrow a, a^{-1} \in \lang a^{k} \rang \Rightarrow \exists s \in \mathbb{N}^{+}, a^{sk} = a \iff a^{sk - 1} = e \Rightarrow \operatorname{ord}(a) \mid sk - 1 \Rightarrow \gcd(k, \operatorname{ord}(a)) = 1 \\ \\
    |\{g\}| = \varphi \Big(\operatorname{ord}(a)\Big), \varphi(x) = \sum\limits^{x}_{i=1}[\gcd(i, x) = 1]
\end{cases}$
  - 因群中的某个元素 $a$ 的幂运算生成子群的过程类似迭代循环，称此类方式生成的子群为循环子群，记为 $\lang a\rang$。
- 在对群上的集合做某种合理的剖分后，如原有集合的子集与 $\circ$ 依然保持群的四个公理，则称子集与运算构成群 $G$ 的子群 $H$。
- 满足交换时，任取群中的两个元素 $a,b$，从而有 $\boxed{a\circ b = b \circ a}\Rightarrow a\circ b\circ a^{-1}\circ b^{-1} = e$。故有推论非交换群不总是满足 $a\circ b\circ a^{-1}\circ b^{-1} = e$。那么可记 $a\circ b\circ a^{-1}\circ b^{-1}$ 为群元素 $a$ 和 $b$ 的换位子 $[a,b]$。

> 在此之后用于理解正规子群的另一个方式是从交换群出发。因多一个性质，群上的代数便会更加简单。这个群便会比一般的群性质更好。于是就可以研究如何讲一个群转化为阿贝尔群。

沿用集合的研究手段，定义群的子群 $H$ 与群 $G$ 具有关系 $H \subset G$，也即 $H \leq G$。当子群是真子群时，则 $H < G$。

因子群具有群本身的性质，则继续按照公理研究：
- 封闭性：$\forall a, b \in H, ab \in H, ab \in G$。
- 结合性：$\forall a, b, c \in H, (ab)c = a(bc)$。
- 单位元：$\forall a \in H, ae = ea = a$。且子群中的单位元一定是原有群的单位元。
- 逆元：$\forall a \in H, \exists a^{-1} \in H, aa^{-1} = a^{-1}a = e$。

那么，可以借由封闭性与逆元存在直接得到子群的判定定理：$\forall a,b\in H, ab^{-1} \in H$。此处略去证明。

假定群 $G$ 能由 $H$ 划分，为了从整体到局部地看出划分的构成并依然保持群的性质，首先从集合的等价关系考虑。

在整个集合中，任取两个等价类 $[x], [y]$ 无非只有两种情况：$[x]\cap [y] = \varnothing, [x] = [y]$。但能用一个等价类划分出整个集合时，其余生成的等价类与此等价类**一定存在**结构上的相似性。

为描述这种相似性，借用映射的观点来研究。

> 更一般的理解可借助范畴论来描述。

取集合 $X, Y$。
- 定义单射表示为集合 $X$ 中的每个元素都能通过映射 $f$ **唯一映射**到集合 $Y$ 中的相应元素。即 $f(x_{1}) = f(x_{2}) \Rightarrow x_{1} = x_{2}$。数量上， $|Y|$ 可能多于 $|X|$，即 $X$ 可能覆盖不满 $Y$。

- 定义满射表示为集合 $X$ 中的元素能通过映射 $f$ **覆盖满**集合 $Y$ 中的所有元素。其中，可能会将不同的 $x$ 映射到相同的 $y$。即 $\forall y \in Y, \exists x \in X, f(x) = y$。

- 定义双射是同时满足单射和满射的映射。
- 定义两个映射 $f,g$ 的复合表示为 $f\circ g$。因映射性质，映射不一定总是满足交换律，但一定满足结合律。
  - 定义恒等映射 $\operatorname{id}_{X}: X\mapsto X$ 为保持自身不动的映射。
  - 恒等映射具有关系：$\forall f, f\circ \operatorname{id}_X = f = \operatorname{id}_{Y}\circ f$。
- 若两映射 $f: X\to Y; g: Y\to X$ 存在关系 $f\circ g = \operatorname{id}_{X}, g\circ f = \operatorname{id}_{Y}$。则称两映射可逆。

**_注意到_**，$f$ 是 $X\to Y$ 的单射，当且仅当其是某个映射的右逆。即 $g:Y\to X, g\circ f = \operatorname{id}_{Y}$；$f$ 是 $X\to Y$ 的满射，当且仅当其是某个映射的左逆。即 $h:Y\to X, f\circ h = \operatorname{id}_{X}$。

回过头来，视 $H$ 为一种等价类，而以其划分整个集合形成的所有新等价类记为 $[y]_{i}$。
<!-- 整体来看，$\exist h:G \longrightarrow H, x \mapsto [x]$，使得 $h$ 满射。又
-->
显然 **存在双射** 使得 $\exist f_{i}: H \to [y]_{i}, \exist g_{i}: [y]_{i} \to H$。此时 $f_{i} = g_{i}^{-1}$。

因此在某种意义上，只要定义了合适的运算，$[y]_{i}$ 也能像 $\lang H, \circ\rang$ 一样是 $G$ 的子群。

为了更精确地描述两个群是构造相同的，以及群是类似于自身的子群的这种表述，不妨先假定存在运算 $\oplus$ 使得 $\lang [y]_{i}, \oplus \rang$ 和 $\lang H, \circ \rang$ 在性质上完全等价。

考察 $\gamma:\lang H, \circ \rang\longrightarrow\lang [y]_{i}, \oplus \rang$ 和 $\phi:\lang G, \circ \rang\longrightarrow\lang [y]_{i}, \oplus \rang$。

因两群在性质上完全一致，任取 $a, b \in H$，显然存在关系 $\gamma(a)\oplus \gamma(b) = \gamma(a\circ b)$，同时**反过来**，对 $a, b \in [y]_{i}$ 也是成立的。由此，我们得到了描述两个群构造相同的最基本方式。即存在双射使得两个群之间形成一一对应的映射。

考察上述两个构造相同的群的两个可能并不相同的单位元 $e_{H}, e_{[y]_{i}}$。显然依然存在关系 $\gamma(e_{H})\gamma(e_{H}) = \gamma(e_{H}) \Rightarrow \gamma(e_{H})=\gamma(e_{H})\gamma(e_{H}) [\gamma(e_{H})]^{-1} = e_{[y]_{i}}$。

而对于群 $G$ 到 $\lang[y]_i, \oplus\rang$ 的映射 $\phi$，这种方式反过来并不能成立因为可能存在多个 $g_{1}, g_{2}\in G, \operatorname{s.t.} \phi(g_{1}) = \phi(g_{2})$。

因为上面的推论，不难看出 $\phi$ 满射且宏观上可以说群 $G$ 与 $\lang[y]_i, \oplus\rang$ 是类似的。

称由 $\phi$ 建立起从 $G$ 到 $\lang[y]_i, \oplus\rang$ 的群同态。因满射，称此同态为满同态。相应地，满足单射称为单同态。如果全满足说明两个群均能通过映射来一一相互对应，故此同态称为同构，说明样例即 $\gamma:\lang H, \circ \rang\longrightarrow\lang [y]_{i}, \oplus \rang$ 和 $\gamma^{-1}:\lang [y]_{i}, \oplus \rang \longrightarrow\lang H, \circ \rang$。

由于满同态的性质， $G$ 中会有多个元素对应 $\lang[y]_i, \oplus\rang$ 中的单位元，考虑满射与 $G$ 中多个元素形成的等价类，称其为 $\ker \phi = \set{a\in G|\phi(a) = e_{[y]_{i}}}$。相应地，称映射群后产生的对象为群的像集 $\operatorname{img} \phi = \set{\phi(g) | g \in G}$。

至此，可以看到 $\ker \phi$ 中元素的个数描述了剖分的个数。如深究其性质，有：

- $\forall a, b \in \ker \phi, \phi(a)\oplus\phi(b) = \phi(\boxed{a\circ b}) = e_{[y]_{i}}\oplus e_{[y]_{i}} = e_{[y]_{i}}$，即 $\ker\phi$ 内的元素封闭。
- 结合性显然。
- 单位元 $e_{G}$ 必定存在于 $\ker \phi$。故显然。
- 对于逆元，取 $a \in \ker\phi \Rightarrow \phi(e_G) = \phi(a \circ a^{-1}) = \phi(a)\oplus\phi(a^{-1}) = e_{[y]_{i}}\oplus\phi(a^{-1}) = e_{[y]_{i}} \Rightarrow \phi(a^{-1}) = e_{[y]_{i}}$。说明 $\ker\phi$ 中的所有元素都有逆元。

因此，$\lang\ker\phi, \circ\rang$ 也是 $G$ 的子群。

至此，已经能隐约猜出可通过一定手段，借助 $\ker\phi$ 和假定的 $H$ 逐步抽象恢复整个群 $G$。考虑使用 $\ker\phi$ 内的所有元素与 $H$ 中的所有元素相互施行 $\circ$，**且不区分运算的方向**。即 $\forall e\in \ker\phi, h\in H, eh = he = h$。从抽象的角度来说，实际上是作用到了整个 $H$。即 $e \in \ker\phi, eH = He = H$，故只要对其余 $e\in \ker\phi, e\neq e_G$ 做同样的操作，即可恢复由 $H$ 划分后其余 $\ker\phi$ 所在的等价类，进而复原整个群 $G$。

此外，对于 $H$ 内的任意的元素 $h$ 而言，因为 $H$ 封闭，$hH = Hh = H$ 显然也是成立的；受上述操作启发，即使与 $H$ 运算的元素从 $\ker\phi$ 变为与 $\ker\phi$ 所在等价类中的任意元素运算，依然可以认为封闭在 $\ker\phi H$ 或者说 $H\ker\phi$ 内。

那么，这样我们就找出了

- 商群 $G/H$。
  - 显然封闭在群 $G$ 内。
  - 显然满足结合律。
  - 单位元：$H$。
  - 显然存在逆元。
- 子群 $H$ 需要有的性质 $\forall g \in G, \forall h \in H, hg = gh$ 也即 $\forall g\in G, gH = Hg$，分别表示左右方向上的陪集(coset)。

以下仅提供便于理解的示意图。
```
      *------- H --*       *------------ e2H = He2 -------*
      |            |       |                              |
      |            v       v                              |
      |    +-------+-------+-------+ <...........         |                  
      |    |e######|e1     |e2     |            .         | 
      |    |#######|       |       |            .         |
      |    |#######|       |       |            .         |
      *--> +-------+-------+-------+ <----------.---------*
           |e3     |e4     |e5     |            .
           |       |       |       |            .
           |       |       |       |            .
           +-------+-------+-------+            G
           |e6     |e7     |e8     |            .
           |       |       |       |            .
           |       |       |       |            .
           +-------+-------+-------+            .
           ▲                                    .
           |                                    .
           ......................................

<ker, o> := <{e, e1, e2, e3, e4, e5, e6, e7, e8}, o>
```

将满足 $\forall g \in G, gH = Hg$ 这种**交换性质**的子群称为正规子群，并记其与群 $G$ 的关系为 $H \lhd G$ 或者 $G \rhd H$。

进而可以定义商群。

> $G\rhd H$，则 $G/H$ 构成商群。且该商群可由同态 $\pi:G\longrightarrow G/H$ 表示。此时有 $\pi(x) = xH = Hx, \forall x \in G$。此时同态核 $\ker\pi = H$。商群中的元素，如按示意图，可理解为中的 $e, e_1, e_2, \ldots, e_8$ 所在的分块。

此时还得到推论：$G\rhd H \Rightarrow |G| = |H||G/H|$。
> 更一般的拉格朗日定理就只需要考虑陪集后得到的集合个数，此时有 $H\subset G, |G| = [G:H]|H|$。此处 $[G:H]$ 即为不同左陪集的个数。此时并不保证 $G/H$ 依然具有群结构。

受到正规子群定义的启发，考虑将等式 $gh = hg$ 变形为 $g = hgh^{-1}$ 推广考察 $\forall a, b, g\in G, a = gbg^{-1}$。

- 实质上可以认为群内元素 $a,b$ 因 $g$ 的运算作用而共轭到一块，且显然这种共轭在一起的关系可形成等价类：自身关系一致（自反性）、共轭关系可传递（传递性）、共轭关系是对称的（对称性）。此外，还有左平移映射 $\forall a,g \in G, a\to ga$ 也将群中的元素映射到群中的另一个元素。亦可视为一种等价关系的划分。
- 这实际上形成了 $f:G\to G, \forall a, b, g\in G, b\to gbg^{-1} = a$，一种既单又满的同态。因自身双射到自身，故称为群的自同构映射。
  - 显然，群的所有自同构映射于复合运算可形成一个映射后保持封闭的群。称此群为群的自同构群 $\operatorname{Aut}(G)$。
  - 不难发现，某种意义上自同构群其实就是置换群。因为在操作上，置换将位置映射到位置，且映射是双射，所以置换是一种到自身的同构，即自同构映射。
    - 而这种群上的映射作用显然也能做一点推广。之后再做进一步的叙述。


言归正传。受到商群的启发，可从两个群构造出一个新群。在构造上，将子群间的直积称为内直积，两个可能没什么关系的群之间的直积称为外直积。同时，循环群的直积常被称为直和。

> 目前笔者找到的对于群论的资料貌似都在混用直和与直积。这好么？这可能不太好。不分清楚到学环论的时候不要乱叫。

具体而言，取群 $S$ 和 $T$，并定义群直积为 $S \times T$ ，对直积所得元素定义的运算：$\forall (s_i, t_i) \in S \times T, (s_i, t_i)(s_j, t_j) = (s_is_j, t_it_j)$。其中的 $s_is_j$ 代表两元素通过 $S$ 的运算得到的结果。$t_it_j$ 同理。

容易看出群直积后的结果也构成群。
- 单位元 $(e_S, e_T)$。
- 结合律显然、逆元显然存在、元素显然封闭。

对于循环群而言，因整个群可由除单位元外的其它元素多次运算（首次生成到所有元素的次数即自身的阶数）后生成，不妨使用记号 $\mathbb{C}_{m}$ 代表该循环群，其中 $m$ 表示循环群元素的个数（或者说除单位元外，其它生成元的阶数）。考虑两循环群 $\mathbb{C}_n, \mathbb{C}_m$ 直积后形成的新群 $\mathbb{C}_n \times \mathbb{C}_m$。

$$\left.\begin{matrix}
\begin{cases}
  \forall a \in \mathbb{C}_n, b \in \mathbb{C}_m, (a,b)^x = (a^x, b^x)\\
  (e_{\mathbb{C}_n}, e_{\mathbb{C}_m})
\end{cases}  \Rightarrow \operatorname{ord}\Big((a,b)\Big) = \operatorname{lcm}(n, m)\\ \\
\gcd(n,m) = 1
\end{matrix}\right\} \Rightarrow \mathbb{C}_n \times \mathbb{C}_m \cong \mathbb{C}_{n\times m}$$

也有记法将上式记为 $\mathbb{C}_n \oplus \mathbb{C}_m \cong \mathbb{C}_m \oplus \mathbb{C}_n \cong \mathbb{C}_{n\times m}$。

从而能看到一个事实：**某些群是可以被分解的**。

> 有的时候并不能直接分解群，因为两个群并不总是可交换的。即不能总是保证两个群满足 $H\cap K = 0, \boxed{G\rhd H, G\rhd K}, H\times K = K\times H = G$。有时只能满足一个群是正规的。
> 而当两个群直接存在群同态 $\phi: H\to \operatorname{Aut}(K)$ 以及 $K$ 满足 $G \rhd K$ 时，此时可由半直积来生成新的群，即 $\forall k_1,k_2 \in K, h_1, h_2 \in H, (k_1, h_1)(k_2, h_2) = (k_1\phi_{h_1}(k_2), h_1h_2)\in K \rtimes H$。

结合上述思考角度，回过头来考虑先前所有可行的置换对序列的**作用**。记所有置换操作与复合运算构成的群为 $\lang S_n, \circ\rang, |S_n| = n!$。

由于这种置换群中的元素可直接按特定顺序交换序列中的元素，非常自然；不妨将其推广到任意可以对集合施加变换操作的群。为了能够让集合构成的特定序列使用上这种交换，需要建立起任意群**嵌入**到 $S_n$ 的群同态。

记为 $\phi: G \to S_n, \forall a, b \in G, \phi(ab) = \phi(a)\circ\phi(b)$。那么群对于集合的作用就相当于替换，即 $\forall a \in G, x \in X, x \to \phi(a)(x):=\phi_a(x)$。

> 表示习惯上省去这种群同态，直接以 $a\cdot x$ 或 $ax$ 描述对应到置换群上的交换操作。并将映射上的表示换为 $\alpha: G \cdot X \to X; \forall g_1, g_2 \in G, \alpha(g_1, \alpha(g_2, x)) = \alpha(g_1g_2, x), \alpha(e_G, x) = x$ 以区分直积。
> 同时，将构建起来的这种满同态，稍加证明即可得到群 $G$ 同构于集合置换群上的一个子群。因范围不限，推广得到**每个群同构于其可施加操作集合上的置换群子群**。此即 cayley 定理，本文暂时略去对其的证明。
> 当作用对象是自身，群作用实际上变成了群运算。这也是为什么群作用会省掉群到集合置换群的同态。

在此约定记号 $\operatorname{Orb}(x) = \set{gx|\forall g\in G} \subseteq X$ 代表 $x$ 的轨道（即整个群作用于 $x$ 后，作用结果依然封闭于集合内的一个集合），$\operatorname{Stab}(x)=\set{g|\forall g\in G, gx = x}$ 代表 $x$ 的稳定化子，整个群作用于 $X$ 之后的不动点集为 $\operatorname{Fix}_G = \set{x|\forall g\in G, x\in X, gx = x}$。$\operatorname{Fix}_{g} = \set{x\in X| gx=x}$ 称为群元素 $g$ 关于 $X$ 的不动点集。

> 上述概念如不注意区分，很容易混淆。在此特地提醒。

显然 $\operatorname{Stab}(x)$ 中的元素充当了对 $x$ 而言的作用单位元，保持作用后 $x$ 的不变。不难发现稳定化子关于复合运算也构成群。即

- 运算封闭。$\forall g, h \in \operatorname{Stab}(x), (g\circ h)x \in X$。
- 满足结合律。$\forall f, g, h\in \operatorname{Stab}(x), f[(g\circ h)x] = (f\circ g\circ h)x \in X$。
- 具有单位元。$\forall x \in X, (e)x = x$。
- 显然存在逆元。

注意到稳定化子不一定是群的正规子群，只对 $x$ 的作用保持 $x$ 不动。于是考虑整个群对 $x$ 的稳定化子的商映射，此时有 $f: G\to G/\operatorname{Stab}(x), \forall a\in G, a\to a\operatorname{Stab}(x)\leadsto\forall g\in \operatorname{Stab}(x), ag\in a\operatorname{Stab}(x) \Rightarrow (ag)x = a(gx) = ax \in \operatorname{Orb}(x)$。因双射显然、定义良好且不保证 $G\rhd\operatorname{Stab}(x)$，

故而存在 $|G:\operatorname{Stab}(x)| = |\operatorname{Orb}(x)|$。从而得到轨道稳定子定理：

$$\begin{aligned}
  |G| = |\operatorname{Stab}(x)||\operatorname{Orb}(x)|
\end{aligned}$$

根据等价类性质，等价类要么完全重合，要么两两不交。考虑两两不交的轨道并集为 $\Omega = X = \bigcup\limits\operatorname{Orb}(x_i), \forall x_i, x_j\in X, x_i \neq x_j\Rightarrow \operatorname{Orb}(x_i)\cap\operatorname{Orb}(x_j) = \varnothing$。
稍加变形得到 BurnSide 定理：考虑集合内所有元素的稳定化子和群内每个元素的不动点集，显然有

$$\begin{aligned}
  &\sum\limits_{g\in G}|\operatorname{Fix}_g|=\sum\limits_{x\in X}|\operatorname{Stab}(x)| \\
 =&\sum\limits_{i=1}^{N}\sum\limits_{o\in \operatorname{Orb}(x_i)}|\operatorname{Stab}(o)| &&X = \Omega = \bigcup\limits^{N}_{i=1}\operatorname{Orb}(x_i) \\
=&\sum\limits_{i=1}^{N}|\operatorname{Orb}(x_i)||\operatorname{Stab}(x_i)| \\
=&N|G|\\
\therefore \ &N = \dfrac{1}{|G|}\sum\limits_{g\in G}|\operatorname{Fix}_g|
\end{aligned}$$


言归正传，结合先前正规子群与可交换性质定义得到的 **共轭类** 对群内其它元素所作的作用形成交换，即具有**正规性**；现在来考虑一种群到自身的映射 $\alpha: G\cdot G \to G, g\to aga^{-1},\forall a, g\in G$。因等价于构建群的自同构映射 $f_a:G\to G, f_a\in \operatorname{Aut}(G) = S_{|G|}$ 此处可认为作用相当于直接施加群上的运算，即 $f_a(g) = aga^{-1}$。

定义共轭类形成的轨道为 $\operatorname{Conj}(x) = [x] = \set{gxg^{-1}|\forall g\in G}$。

那么参照“作用单位元”保持集合元素稳定不动的想法，定义共轭作用下的稳定化子为中心化子 $C(x) = \set{\forall g\in G| gxg^{-1} = x}, x\in G$ 保持元素 $x$ 在共轭作用下不动；整个群的中心为 $Z(G) = \set{\forall g\in G|\forall x\in G, gxg^{-1} = x}$。

再因中心化子只对特定的元素 $x$ 起交换作用，不妨套用先前的轨道稳定子定理的推演过程考察群中心对整个群的作用效果，有映射 

$$\begin{aligned}
&f:G\to G/Z(G)\\ &\forall x\in G, x\to xZ(G)\\
\Rightarrow & \forall y\in Z(G), xy = yx
\\ \therefore  & \forall g\in G, xyg = yxg \Rightarrow xygy^{-1}x^{-1} = x(ygy^{-1})x^{-1} = xgx^{-1} \in \operatorname{Conj}(g)
\end{aligned}$$

而因 $Z(G)$ 的定义可推 $Z(G) = \bigcap\limits_{g\in G}C(g)$ 和 $C(c) = G \iff c\in Z(G)\iff \operatorname{Conj}(c) = \set{c} = [c]$。

这种情况下，$\forall c\in Z(G), |\operatorname{Conj}(c)| = 1, |Z(G)| = \sum\limits_{c\in Z(G)}|\operatorname{Conj}(c)|$。此时有

$$\begin{aligned}
  |G| &= |Z(G)| + \sum\limits_{x_{i} \in \Omega}|\operatorname{Conj}(x_{i})| && \Omega = \Set{\Big(\forall x_{i}, x_{j}\notin Z(G)\Big): x_{i}\neq x_{j} \bigcap \operatorname{Conj}(x_{i}) \cap \operatorname{Conj}(x_{j}) = \varnothing}\\
      &= |Z(G)| + \sum\limits_{g\notin Z(G)}|G: C(g)| 
\end{aligned}$$


至此群作用的概念很初步地写成了。考虑通过上述概念推理求证 sylow 定理。

对一个一般情形的群 $G, |G| = n = p_{0}^{\alpha_{0}}p_{1}^{\alpha_{1}}\cdots p_{m - 1}^{\alpha_{m - 1}}$，它有没有 $p_i^{k},  k\in \set{1,2,3,\ldots,\alpha_i - 1}, i\in \set{0, 1,\ldots, m-1}$ 阶子群呢？

为证明需要，考虑从最简单的 $p_1$ 阶子群起证。即 $p_1 \mid |G|, \exist H\subset G, |H| = p_1$ 是否成立。

**使群自身与自身作直积 $p_1$ 次**，得到扩张后的群元素（或称向量基底） $(g_1, g_2, \ldots, g_{p_1}) \in \overbrace{G \times G \times \cdots \times  G}^{p_{1}} = G^{p_{1}}$。

 构造集合 $X = \set{(x_0, x_1, \ldots, x_{p_1 - 1}) \in G^{p_{1}}| x_0x_1\cdots x_{p_1 - 1} = e_{G}}$。

由于 $\forall x_0, x_1,\ldots, x_{p_{1} - 2}, \Big( x_0\cdot x_1\cdots x_{p_{1} - 2}\Big)^{-1} = x_{p_{1} - 1} \in G$，因限制死 $x_{p_{1} - 1}$ 后，$x_0\sim x_{p_{1} - 2}$ 完全独立，能取遍整个群 $G$，故此处存在 $|X| = |G|^{p_{1} - 1}$。又因为 $p_{1} \mid |G|\Rightarrow p_{1} \mid |X| \Rightarrow |X| \equiv 0\pmod{p_{1}}$。

注意到 $(x_0, x_1, \ldots, x_{p_1 - 1})\in X \Rightarrow x_0x_1\cdots x_{p_1 - 1} = e_{G}\Rightarrow x_1\cdots x_{p_1 - 1}x_0 = e_G \Rightarrow (x_1, \ldots, x_{p_1 - 1}, x_0)\in X$。不难看出这相当于 $\mathbb{Z}/p_1\mathbb{Z} = \lang\set{0,1,\ldots,p_1-1}, +_{p_1}\rang$ 作用在集合 $X$ 元素的下标上，即 $(x_0, x_1, \ldots, x_{p_1 - 1}) \to (x_{0 + 1\pmod{p_1}}, x_{1+1\pmod{p_1}}, \ldots, x_{p_1 - 1 + 1\pmod{p_1}})$。

进一步有 $\forall x\in X, \set{|\operatorname{Orb}(x)|} = \set{1, p_1}$。而考虑 $\operatorname{Fix}_{\mathbb{Z}_{p_1}^{+}}$，这意味着不管怎么平移下标，都不会引起 $\operatorname{Fix}_{\mathbb{Z}_{p_1}^{+}}$ 内元素的改变，这意味着当且仅当基底的所有分量都是同一个时满足。即 $(x, x,\ldots, x)\in X \Rightarrow x^{p_1} = e_G$。

考虑将 $X$ 拆为 $\operatorname{Fix}_{\mathbb{Z}_{p_1}^{+}}, X - \operatorname{Fix}_{\mathbb{Z}_{p_1}^{+}}$。由于非不动点集的部分轨道长度为 $p$ 可使得固定一种情况即可沿轨道找到其它 $p_1-1$ 个属于 $X - \operatorname{Fix}_{\mathbb{Z}_{p_1}^{+}}$ 的情况，从而 $|X - \operatorname{Fix}_{\mathbb{Z}_{p}^{+}}| = \lambda p_1$。那么结合 $p_1 \mid |X|$ 来看，$p\mid |\operatorname{Fix}_{\mathbb{Z}_{p_1}^{+}}|\Rightarrow |\operatorname{Fix}_{\mathbb{Z}_{p_1}^{+}}|\equiv |X| \equiv 0\pmod{p_1}$。

因 $p_1\in \mathbb{P}\Rightarrow p_1 > 1$，故除去所有位置都是单位元的情况 $(e_G, e_G, \ldots, e_G)$ 后，必定有 $g\in G, \operatorname{ord}(g) = p_1$。即 $G$ 存在可生成 $p_1$ 阶子群的生成元。

进而考虑对 $G$ 的任意 $p_{1}^{k}, 1 < k < \alpha_1$ 阶子群 $P$，是否存在 $p_{1}^{k + 1}$ 阶子群 $H \subset G, H \rhd P$?


<!-- todo 从此处开始。 -->
<!-- 

考虑群内元素构成的所有子集 $P\subset G, |P| = p_{0}^{k}$ 的并集 $X = G/P, \forall x\in G, x\to xP\in X$；以及子集的置换群对并集 $X$ 的左平移作用： $\forall a\in P, P\cdot X\to X, xP \to a\cdot xP = axP$。

此时不动点集为 
$$\begin{aligned}
  \operatorname{Fix}_{P} &= \set{xP|\forall a\in P, x\in X, axP = xP} \\ 
  &= \set{xP|\forall a\in P, x\in X, x^{-1}axP = P}\\
 &= \set{xP|\forall a\in P, x\in X, x^{-1}ax \in P}\\
 &= \set{xP| \forall x \in X, x^{-1}Px = P}\\
&=\set{\boxed{xP}| \forall x\in C(P)}\\
&=C(P)/P
\end{aligned}$$

由于 $|P| = p_{0}^{k}, |X| \equiv |\operatorname{Fix}_{P}|\pmod{p}$ 故有

$$\begin{aligned}
  &|G: P| \equiv p_{0}^{\alpha_0 - k}\prod_{i = 1}^{m - 1} p_i^{\alpha_i}\equiv |C(P):P| \equiv 0\pmod{p}
\end{aligned}$$

因 $C(P)\geqslant P, C(P) \rhd P$，故存在自然的满同态 $\pi: C(P) \to C(P) / P$。从而结合上述条件，得到：

$$|C(P):P| \equiv |C(P)/P| \equiv 0 \pmod{p}$$

在此考虑整数集 $\mathbb{Z}$ 与模 $p_{1}$ 加法得到的质数群 $\mathbb{Z}^{+}_{p_{1}} = \lang\mathbb{Z}, +_{p_{1}} \rang = \lang\set{0,1,2,\ldots,p_{1}-1}, +_{p_{1}}\rang$。

又因保持了 $x_{p_{1}}$ 的选取，交换基底的分量后仍使得连乘条件成立，即 $(x_1,x_2,\ldots,x_i,\ldots,x_j,\ldots,x_{p_{1}}) \in X \Rightarrow (x_1,x_2,\ldots,x_j,\ldots,x_i,\ldots,x_{p_{1}}) \in X$，所以对同一个 $x_{p_{1}}$，这里共有 $(p-1)!$ 种排列方式能映射到。

至此，我们可以初步借助群同态、正规子群等工具来初步描述群和群之间的关系。



若将“不操作”映射，即映射 $\sigma_e(S) = \sigma_e(\{x_1, x_2, \ldots, x_n\}) = \{x_1, x_2, \ldots, x_n\}$ 作为映射集合的单位元，那么对于任意一个映射 $\sigma_i$，集合中必然有另一个映射 $\sigma_j$ 与之在完成对集合 $S$ 的两次映射后，保持集合不变，形成与单位元映射一致的变换。即 $\sigma_j \circ \sigma_i = \sigma_i \circ \sigma_j = \sigma_e$，也即映射之间存在逆映射。

不难发现，经过多轮映射，总能在映射集合中找到一个映射使得最终对集合排列的结果依然一致。即 $\exist j \in \Phi, \operatorname{s.t.}\sigma_j = \sigma_m\circ\sigma_{m-1}\circ\cdots\circ\sigma_1$。


还能注意到，在保持计算顺序不变的前提下，即 $\forall \sigma_i, \sigma_j, \sigma_k \in \Phi, (\sigma_i \circ \sigma_j) \circ \sigma_k =  \sigma_i \circ (\sigma_j \circ \sigma_k) $ 一定成立。
-->
--------


同时，还可将这种保持集合不变的映射称为对 $S$ 的置换。


**归纳所有** 对集合 $S$ 的置换，使之构成『映射集合』，即 $\Phi = \{\sigma_1,\sigma_2,\ldots, \sigma_n \}$，其中 $n = (| S |) !$。

再指定“从映射集合中任取出 $m$ 次的映射并 **严格按抽取顺序连续** 施行于 **同一个集合**” 的操作表示为：$\sigma_m(\sigma_{m-1}(\cdots(\sigma_1(S)))) = \sigma_m\circ\sigma_{m-1}\circ\cdots\circ\sigma_1(S) = \sigma_m\circ\sigma_{m-1}\circ\cdots\circ\sigma_1$。当作用对象变为群上的元素时，称映射为对群的作用。





那么，$\lang \Phi, \circ \rang$ 形成对集合 $S$ 施行交换作用的自同构群 $\operatorname{Aut}(S)$。

由于单位元映射 $\sigma_e(\{x_1, x_2, \ldots, x_n\}) = \{x_1, x_2, \ldots, x_n\}$ 在映射中总会使得 $\sigma_e \circ \sigma_i = \sigma_i \circ \sigma_e$，考虑 $\operatorname{Aut}(S)$ 的正规子群  $H$，即 $\forall x\in \Phi, H\circ x = x\circ H$。

进而有性质：

$\forall x, y \in H, \forall g \in \operatorname{Aut}(S), g\circ x = x\circ g, g\circ y = y\circ g\Rightarrow \begin{cases}
    y^{-1}\circ g =  g\circ y^{-1} \\
    x\circ(y^{-1}\circ g) = \boxed{(x\circ y^{-1})\circ g} = (g\circ y^{-1})\circ x = \boxed{g \circ (y^{-1}\circ x)} \\
\end{cases}$。

并称此正规子群为集合的 **内自同构群 $\operatorname{Inn}(S)$**。

且可沿用换位子定义 $\forall \sigma_{i}, \sigma_{j}\in \Phi,  [\sigma_{i}, \sigma_{j}] \stackrel{\operatorname{def}}{=} \sigma_{j}^{-1}\circ \sigma_{i}^{-1}\circ\sigma_{j}\circ \sigma_{i}$；在作用上，即令原先对集合或者群元素所做的作用 $\sigma_{i}\circ\sigma_{j}$ 变为 $\sigma_{j}\circ\sigma_{i}$。


<!--

同时考虑群直积得到的新群阶数 $\forall s_i \in S, t_i \in T, (s_i, t_i)^{x} = (s_i^x, t_i^x)$。那么若同时使得两群中的任意元素能最快回到自身的单位元，就不可避免地要求  $\operatorname{ord}(s_i) \mid x\cap  \operatorname{ord}(t_i)\mid x\Rightarrow\operatorname{ord}\Big((s_i, t_i)\Big) = \min x = \operatorname{lcm}(\operatorname{ord}(s_i), \operatorname{ord}(t_i)) = \dfrac{\operatorname{ord}(s_i)\operatorname{ord}(t_i)}{\gcd\Big(\operatorname{ord}(s_i), \operatorname{ord}(t_i)\Big)}$。

因设定 $\phi:G \longrightarrow H$，根据 $H$ 而划分整个群，那么直接可以通过

$$\phi:\lang G, \circ\rang\mapsto \lang H, \circ\rang \Rightarrow G/\lang\ker\phi, \circ\rang   \cong   H$$
只需要让 $H$ 中的所有元素与 $\ker\phi$ 中的所有元素做一次运算，即 $\forall h \in H, a \in \ker\phi, a\circ h\in G$。

且更加特别地，如果固定 $\ker\phi$，此时中。即 $\forall a \in \ker\phi, aH$ 

框起来的式子可以形象表示为


所以 $f_{i} = g^{-1}_{i}$。所以 $\exists f_{i}, f_{i}^{-1}, i = 0, 1,2,\ldots$ 使得 $H$ 能生成新的等价类覆盖整个集合。将 $H$ 和通过划分生成的等价类放置于新的集合，形成对群 $G$ 的映射。记 $H$ 形成的等价关系为 $\sim$ ，则此时有

$$\begin{aligned}
  &g: \\
  &G/\sim \stackrel{\sim}{\longrightarrow} G/H, \quad\\
  &[x] \stackrel{\sim}{\longrightarrow} xH = Hx
\end{aligned}$$

体现起来就是：设生成的新等价类为 $H_{i}, i = 1, 2, 3, \ldots$。那么以 $H$ 取集合 $G$ 的划分：$G = H\cup H_{1}\cup H_{2}\cup \cdots$。得到： 

$$\begin{aligned}
  G &=  H\cup H_{1}\cup H_{2}\cup \cdots && \\
  &= (e\cup a_{1}\cup a_{2}\cup \cdots)H = H(e\cup a_{1}\cup a_{2}\cup \cdots)&& \\
  &= \Set{e, a_{1}, a_{2}, \ldots}H = H\Set{e, a_{1}, a_{2}, \ldots}&& \\
  % &= \lang\Set{e, a_{1}, a_{2}, \ldots} \circ\rang H = H\lang\Set{e, a_{1}, a_{2}, \ldots} \circ\rang&&
\end{aligned}$$

第二行等号成立是由于这种对等价类的分配律能成立。因等价类是集合，故实质上完全可用群自身的集合替代。

显然，这种恒等映射是一种双射，可以描述两个群是构造相同（即同构）的。
至此，自然可以从同态着手研究。群到自身的同态（自同态）、借助两个群之间的同态来研究两个群是否构造相同（同构）。并研究上述映射关系构成的是否可构成群以及有何特征。

首先，同构一定要求两群所具有的同态是双射。相应地，仅满足满射的同态称为满同态，仅满足单射的称为单同态。
-->


<!-- 
https://mandal.ku.edu/math791/spFteen791/P3Homomorph.pdf
-->
----------

为了统一并方便对此类对称多项式的描述，先定义生成所有根的一元多项式及其相关性质，以及一元多项式所在的集合。

记 $\mathbb{Q}[x] \stackrel{\operatorname{def}}{=} \{\displaystyle\sum_{i = 0}^{n-1} a_{i}x^{i} | \forall a_{i} \in \mathbb{Q}, i = 0, 1, 2, \ldots, n-1\}$ 表示所有系数在原有有理数集合的多项式形成的集合。

考虑多项式的带余除法。

