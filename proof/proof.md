# Proof of Lemma 6

**This proof is outdated! Check Overleaf for the newest version.**

**Lemma 6** When $a^2$ satisfies (19), the set $C_0(a,b):=\bigcup_{u\in\mathbb{S}}C(u,u)$ covers the right hemisphere of $\mathbb{D}$.
**Proof** $C(u, u)$ is centered at $s(u):= (a^2-b^2u)^2$ with radius $r(u):= a^2b^2|1+u|^2$. It is tangent to the unit circle since
$$
\begin{equation}
    |s(u)|+r(u)=1.
\end{equation}
$$
We only need to prove that for every $z$ in the right hemisphere of $\mathbb{D}$, there exists $u_0\in \mathbb{S}$ such that $z$ is inside $C(u, u)$ (because $C(-1, -1)$ is a single point, $z$ is outside $C(-1, -1)$. When $u'$ goes from $-1$ to $u$, $C(u', u')$ varies continuously, so there must be a $u'$ such that $z$ is on the boundary of $C(u', u')$).
If $a=b$, this automatically holds since origin is on the path of $s$, and $C(0,0)$ covers the whole unit circle. In following steps, we assume $a \neq b$.
*Step 1. Identify a segment of curve $s$ that lies in the  right hemisphere, with two endpoints on the positive and negative part of imaginary axis respectively.*
When $u=1$, $s(u)=(a^2-b^2)^2$ is on the positive part of real axis. Now we first need to find out when it intersects with imaginary axis. We write $u=u(\theta):=\cos(\theta)+i\sin(\theta)$, and $t(\theta):=s(u)$, then
$$
\begin{equation}
    \begin{aligned}
        t(\theta)&=(a^2-b^2(\cos(\theta)+i\sin(\theta)))^2\\
        &=((a^2-b^2\cos(\theta))+i\sin(\theta))^2
    \end{aligned}
\end{equation}
$$
Consider the real part of $s(u)$, we have
$$
\begin{equation}
    \begin{aligned}
        {\rm Re}\ t(\theta)&=(a^2-b^2\cos(\theta))^2-b^4\sin^2(\theta)\\
        &=a^4-2a^2b^2\cos(\theta)+b^4\cos^2(\theta)-b^4\sin^2(\theta)\\
        &=2b^4\cos^2(\theta)-2a^2b^2\cos(\theta)+(a^4-b^4)
    \end{aligned}
\end{equation}
$$
To calculate the intersection points of the curve $s$ with imaginary axis, let the real part of $s(u)$ be zero, getting the equation
$$
\begin{equation}
    2b^4\cos^2(\theta)-2a^2b^2\cos(\theta)+(a^4-b^4)=0
\end{equation}
$$
Condition (19) implies $2b^4-a^4 \geq 0$, so it haves roots $\cos(\theta)=\frac{a^2\pm\sqrt{2b^4-a^4}}{2b^2}$. Considering the larger root $\delta=\frac{a^2+\sqrt{2b^4-a^4}}{2b^2}$ and compare it with $1$, we have
$$
\begin{equation}
    1-\frac{a^2+\sqrt{2b^4-a^4}}{2b^2}=\frac{2b^2-a^2-\sqrt{2b^4-a^4}}{2b^2}
\end{equation}
$$
Note that when $a^2$ satisfies (19), $2b^2>a^2$ always holds. Hence, by calculating
$$
\begin{equation}
    (2b^2-a^2)^2-(2b^4-a^4)=2a^4-4a^2b^2+2b^4=2(a^2-b^2)^2>0
\end{equation}
$$
we could derive $\delta<1$.
Denote $\alpha=\arccos(\delta)$, then when $\theta\in[-\alpha,\alpha]$, $s(u)=t(\theta)$ is always in the right hemisphere. Meanwhile, $t(-\alpha)^*=t(\alpha)\neq0$ indicates that these two endpoints are at different side of origin, finishing the step 1 of this proof.
*Step 2. Show that for every point $s(u)$ on this segment, its distance to imaginary axis is no longer than $r(u)$.*
To prove this, we just need to compare the real part of $s(u)$ and $r(u)$. By doing subtraction, we have
$$
\begin{equation}
    \begin{aligned}
        {\rm Re}\ s(u)-r(u)=&2b^4\cos^2(\theta)-2a^2b^2\cos(\theta)+(a^4-b^4)-a^2b^2|1+u|^2\\
        =&2b^4\cos^2(\theta)-2a^2b^2\cos(\theta)+(a^4-b^4)-a^2b^2(1+\cos(\theta)+i\sin(\theta))(1+\cos(\theta)-i\sin(\theta))\\
        =&2b^4\cos^2(\theta)-2a^2b^2\cos(\theta)+(a^4-b^4)-a^2b^2(1+\cos(\theta))^2-a^2b^2\sin^2(\theta)\\
        =&2b^4\cos^2(\theta)-2a^2b^2\cos(\theta)+(a^4-b^4)-2a^2b^2-2a^2b^2\cos(\theta)\\
        =&2b^4\cos^2(\theta)-4a^2b^2\cos(\theta)+(a^4-b^4-2a^2b^2)\\
        =&2b^4\cos^2(\theta)-4a^2b^2\cos(\theta)+2a^4+(-a^4-b^4-2a^2b^2)\\
        =&2(b^2\cos(\theta)-a^2)^2-(a^2+b^2)^2\\
        =&2(b^2\cos(\theta)-a^2)^2-1\\
        =&2(b^2(\cos(\theta)+1)-1)^2-1
    \end{aligned}
\end{equation}
$$
Since $\theta\in[-\alpha,\alpha]$, we have $\cos(\theta)\geq\delta>0$, which could be relaxed to $0<\cos(\theta)\leq1$. From (19), we know $b^2$ satisfies $\frac{1}{1+\sqrt2}\leq b^2\leq\frac{3+2\sqrt{2}}{4+2\sqrt{2}}$. It could be easily verified that within these ranges, ${\rm Re}\ s(u)-r(u)$ is always nonpositive. Therefore, for every point $s(u)$ on the segment given in step 1, its distance to imaginary axis is no longer than $r(u)$.
*Step 3. Show that for every point $z$ in the right hemisphere, there exists $u_0\in\mathbb{S}$ such that $z$ is inside $C(u,u)$.*
For every point $z$ in the right hemisphere, at least one of the following statement must hold:
(i) the line segment connecting $z$ and the origin intersects with $t(\theta),\theta\in[-\alpha,\alpha]$, and
(ii) there exists $\gamma\in[-\alpha,\alpha]$ such that $t(\gamma)$ is just to the right of $z$, i.e., $t(\gamma)-z$ is a positive real number.
If the first statement holds, assume they intersect at the point $t(\beta)$, where $\beta\in[-\alpha,\alpha]$. Since the circle $C(u(\beta),u(\beta))$ is tangent to unit circle, $z$ must lies in $C(u(\beta),u(\beta))$. For the second case, the result of step 2 indicates that $C(u(\gamma),u(\gamma))$ covers all the points to the left of $t(\gamma)$ in right hemisphere of unit disk, which implies $z$ must be inside $C(u(\gamma),u(\gamma))$.
The only thing left to complete this proof is showing that at least one of two statements above should be satisfied. We prove it by contradiction. Assume neither of these two cases holds, then the path of
$$
v_z(\lambda)=\begin{cases}(1-\lambda)i{\rm Im}\ z+\lambda z&0\leq\lambda\leq1\\\lambda z&\lambda>1\end{cases}
$$
do not intersect with $t(\theta),\theta\in[-\alpha,\alpha]$. However, $v_z(\lambda)$ actually splits the right hemisphere of unit disk, and two endpoints are located in different part of split unit disk, so there must be an intersection point, which causes a contradiction.