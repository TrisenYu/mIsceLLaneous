> 注意化简途中的省略与变形。

考虑李群求解微分方程 $F(x, y, y') = 0$ 的解。

将解之间的变换，即 $(x, y, y')\to (\hat{x}, \hat{y}, \hat{y}')$， 视为 $\mathbb{R}$ 上加法群 $\mathbb{R}^{+}$ 的某个参数(元素)对解集构成的三维流形的作用 $\varphi:\mathbb R^{+} \times \mathcal M^{3}\to \mathcal M^{3}$。此时有

$\begin{cases}
    (\hat{x}, \hat{y}, \hat{y}') = \varphi_{a}(x, y, y') = \varphi(a; x, y, y') \\ 
    \varphi_{b}(\hat{x}, \hat{y}, \hat{y}') = \varphi_{b+a}(x, y, y') = \varphi_{a+b}(x, y, y') \\
    (x, y, y') = \varphi_{-a}(\hat{x}, \hat{y}, \hat{y}') = \varphi_{a-a}(x, y, y') = \varphi_{0}(x, y, y')
\end{cases}$

同时有 $F(x, y, y') = F(\hat{x}, \hat{y}, \hat{y}') = 0$。

因为群作用得到的映射又可视为函数。故针对参数，考虑在 $(0; x, y)$ 附近泰勒展开。此时有

$$\begin{aligned}
   (\hat{x}, \hat{y}, \hat{y}')  &= \varphi_{0}(x, y, y') + (a-0)\cdot\frac{\partial\varphi_a(x, y, y')}{\partial a}\Bigg|_{a = 0} + \frac{a^2}{2}\cdot\frac{\partial^2\varphi_a(x, y, y')}{\partial a^2}\Bigg|_{a = 0} + \cdots + \frac{a^{n}}{n!}\cdot\frac{\partial^n\varphi_a(x, y, y')}{\partial a^n}\Bigg|_{a = 0} \\
    %
    &= (x, y, y') + a\cdot\frac{\partial\varphi_a(x, y, y')}{\partial a}\Bigg|_{a = 0} + \mathcal{O}(a^2)
\end{aligned}$$

略去二阶及以上的无穷小量，并记 $\phi(x, y, y') = \dfrac{\partial\varphi_a(x, y, y')}{\partial a}\Bigg|_{a = 0}$ 得到无穷小变换 $(\hat{x}, \hat{y}, \hat{y}') = (x, y, y') + a\phi(x, y, y')$。

> 至于为什么只截取到一阶无穷小，个人理解是：切线、切平面为代表的微分基本思路。

事实上，如果把 $\varphi_{a}(x, y, y')$ 拆分为 $x\mapsto \hat{x}$、 $y \mapsto \hat{y}$ 和 $y' \mapsto \hat{y}'$ 的映射时，此时得到 $\varphi_{a}(x, y, y') \iff \begin{cases}
    \hat{x} = x + a\cdot\alpha(x,y, y') \\
    \hat{y} = y + a\cdot\beta(x,y, y') \\
    \hat{y}' = y' + a\cdot\gamma(x,y, y') \\
\end{cases}, \phi(x,y, y') \iff \begin{cases}
    \hat{x} \hookleftarrow\alpha(x,y, y') \\
    \hat{y} \hookleftarrow\beta(x,y, y') \\
    \hat{y}'\hookleftarrow\gamma(x,y, y') \\
\end{cases}$

那么不加证明地引用^[1]并变形可以得到

$$\begin{aligned}
    F(\hat{x}, \hat{y}, \hat{y}') &= F\Big(x + a\cdot\alpha(x,y, y'), y + a\cdot\beta(x,y, y'), y' + a\cdot\gamma(x,y, y')\Big) \\
    % ... 1 ...
    &= F(x, y, y') + a\Big(\alpha\frac{\partial}{\partial x} + \beta\frac{\partial}{\partial y} + \gamma\frac{\partial}{\partial y'}\Big)F(x, y, y') + \cdots \\
    % ... 2 ...
    &= \Big[1 + a\Big(\alpha\frac{\partial}{\partial x} + \beta\frac{\partial}{\partial y} + \gamma\frac{\partial}{\partial y'}\Big) + \cdots \Big]F(x, y, y')\\
    % ... 3 ...
    &= e^{a\triangle_{a}}F(x, y, y'),\quad \triangle_{a} = \alpha\frac{\partial}{\partial x} + \beta\frac{\partial}{\partial y} + \gamma\frac{\partial}{\partial y'}\\
    % ... 4 ...
    &= 0\\
\end{aligned}$$

称 $\triangle_{a} = \alpha\dfrac{\partial}{\partial x} + \beta\dfrac{\partial}{\partial y} + \gamma\dfrac{\partial}{\partial y'}$ 为 $F(x, y, y')$ 的无穷小生成元(infinitesimal generator)。


还可见 $\triangle_{a}F = 0 \Rightarrow F(\hat{x}, \hat{y}, \hat{y}') = F(x, y, y')$。

还需要考虑微分关系 $y' = \dfrac{\mathrm{d}y}{\mathrm{d} x}$ 和 $\beta$ 对 $\gamma$ 的影响。

此时可得

$$\begin{aligned}
    \hat{y}' &= \dfrac{\mathrm{d}\hat{y}}{\mathrm{d} \hat{x}}= \dfrac{\mathrm{d}\hat{y}}{\mathrm{d} x} \cdot \dfrac{\mathrm{d}x}{\mathrm{d} \hat{x}} \\
    % ... 1 ... 
    &=\dfrac{\mathrm{d} (y + a\beta)}{\mathrm{d} x} \cdot \dfrac{\mathrm{d}x}{\mathrm{d} (x + a\alpha)} =\boxed{ \dfrac{y'+a(\beta_x + y'\beta_y + y''\beta_{y'})}{1+a(\alpha_x+ y'\alpha_y + y''\alpha_{y'})}}\\
    % ... 2 ... 
    &=y' + a\gamma\\
    % ... 3 ...
    \Rightarrow \gamma &= \dfrac{(\beta_x + y'\beta_y + y''\beta_{y'})  - (y'\alpha_x+ y'^{2}\alpha_y + y'y''\alpha_{y'})}{1+a(\alpha_x+ y'\alpha_y + y''\alpha_{y'})}
\end{aligned}$$

$\gamma$ 的形式过于复杂。考虑全微分算子 $\dfrac{\mathrm D}{\mathrm D x} = \dfrac{\partial}{\partial x} + y^{(1)}\dfrac{\partial}{\partial y} + \cdots + y^{(k)}\dfrac{\partial}{\partial y^{k-1}} $。

回顾框起来的式子，姑且有 

$$\begin{aligned}
    \hat{y}' &= \dfrac{y' + a\dfrac{\mathrm D\beta}{\mathrm D x} }{1 + a\dfrac{\mathrm D\alpha}{\mathrm D x}} \approx \dfrac{(y' + a\dfrac{\mathrm D\beta}{\mathrm D x} )(1 - a\dfrac{\mathrm D\alpha}{\mathrm D x})}{1} \\
    % ... 1 ...
    &= y' - ay'\dfrac{\mathrm D\alpha}{\mathrm D x} + a\dfrac{\mathrm D\beta}{\mathrm D x} - a^2\dfrac{\mathrm D\beta}{\mathrm D x}\dfrac{\mathrm D\alpha}{\mathrm D x} \\
    % ... 2 ...
    &\approx y' + a(\dfrac{\mathrm D\beta}{\mathrm D x}-y'\dfrac{\mathrm D\alpha}{\mathrm D x}) \\
    % ... 3 ...
    &= y' + a\gamma \\
    \therefore \gamma &= \dfrac{\mathrm D\beta}{\mathrm D x}-y'\dfrac{\mathrm D\alpha}{\mathrm D x}
\end{aligned}$$

进而可以推广到 $n$ 阶导数的情形。记为 $\gamma^{(n)} = \dfrac{\mathrm D\gamma^{(n-1)}}{\mathrm D x}-y^{(n)}\dfrac{\mathrm D\alpha}{\mathrm D x}$

----------------------

做了以上陈述性工作，接下来考虑求解方式。

首先考虑到 $F(x, y, y') \stackrel{\operatorname{def}}{=} y' - f(x,y) = 0$

将 $y', f(x, y)$ 视为两独立变量，并展开 $\triangle_{a}F = 0$ 有

$$\begin{aligned}
    \alpha F_{x} + \beta F_{y} + \gamma F_{y'} &=  \alpha F_{x} + \beta F_{y} + \Big(\beta_{x} + y'\beta_{y} - y'(\alpha_{x} + y'\alpha_{y})\Big)F_{y'} \\
    % ... 1 ...
    &= \alpha F_{x} + \beta F_{y} +  (\beta_{x} + y'(\beta_{y} - \alpha_{x}) - y'^2\alpha_{y})F_{y'} \\
    % ... 2 ...
    &= -\alpha f_{x} - \beta f_y + \beta_{x} + y'(\beta_{y} - \alpha_{x}) - y'^2\alpha_{y} = 0 \\
    % --- 3 ---
    \therefore \alpha f_{x} + \beta f_y &= \beta_{x} + f(\beta_{y} - \alpha_{x}) - f^2\alpha_{y}
\end{aligned}$$

_注意到_ 替换 $\beta = f\alpha + \mu$ 可使等式变为 

$$
\begin{aligned}
&\alpha f_x + f\alpha f_y + \mu f_y = \alpha f_x + \mu_x  + f\alpha f_y + f\mu_y \\
\Rightarrow &\mu_x + f\mu_y = \mu f_y
\end{aligned}
$$

求通解就需要解特征方程，但没有降低求解的难度。特别是找到合适的 $\mu$ 在很多情况下先要依靠直觉找到合适的 $\alpha(x, y), \beta(x, y)$。

另外，解微分方程最能降低计算难度的方式是换元。若 $(x, y) \to (u, v)$ 后能方便求解时，考察无穷小生成元有

$$\begin{aligned}
    \triangle_{a} &= \alpha\dfrac{\partial}{\partial x} + \beta\dfrac{\partial}{\partial y} + \gamma\dfrac{\partial}{\partial y'}\\ 
    % ... 1 ...
    &= \alpha(\dfrac{\partial u}{\partial x}\cdot\dfrac{\partial }{\partial u} + \dfrac{\partial v}{\partial x}\cdot\dfrac{\partial }{\partial v}) + \beta(\dfrac{\partial u}{\partial y}\cdot\dfrac{\partial }{\partial u} + \dfrac{\partial v}{\partial y}\cdot\dfrac{\partial }{\partial v})+ \gamma(\dfrac{\partial u}{\partial y'}\cdot\dfrac{\partial }{\partial u} + \dfrac{\partial v}{\partial y'}\cdot\dfrac{\partial }{\partial v})\\
    % ... 2 ...
    &= (\alpha\dfrac{\partial u}{\partial x} + \gamma\dfrac{\partial u}{\partial y'} + \beta\dfrac{\partial u}{\partial y})\dfrac{\partial }{\partial u} + (\alpha\dfrac{\partial v}{\partial x} + \beta\dfrac{\partial v}{\partial y} + \gamma\dfrac{\partial v}{\partial y'})\dfrac{\partial }{\partial v}\\
    % ... 3 ...
    &= \Big(\triangle_{a}u\Big)\dfrac{\partial }{\partial u} + \Big(\triangle_{a}v\Big)\dfrac{\partial }{\partial v}\\
\end{aligned}
$$

预期上理应减少了变量。进而要求在所得的 $\Big(\triangle_{a}u\Big), \Big(\triangle_{a}v\Big)$ 中，存在一个为 $0$。

但是依然极其折腾。

[1]: [Lie Groups and Differential Equation](http://physics.drexel.edu/~bob/LieGroups/LG_16.pdf)