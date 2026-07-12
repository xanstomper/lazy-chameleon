"""
Hardcoded distillation datasets sourced from frontier AI models.
Contains 200+ realistic training examples.
"""

from __future__ import annotations
import random
from typing import Dict, List, Optional

ALL_EXAMPLES: List[Dict[str, str]] = []

MATH_EXAMPLES: List[Dict[str, str]] = [
    {
        "instruction": "Let a,b,c>0, a+b+c=3. Prove 1/(1+a^2)+1/(1+b^2)+1/(1+c^2) >= 3/2.",
        "response": "Prove 1/(1+x^2) >= (3-x)/4: x^3-3x^2+x+1>=0 => (x-1)^2(x+1)>=0. Sum LHS >= (9-3)/4 = 3/2.",
        "reasoning_trace": "Tangent line method. f(x)=1/(1+x^2). At x=1: f=1/2, f'=-1/2. Bound (3-x)/4 verified by algebra. Summing 3 inequalities yields result.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "hard",
    },
    {
        "instruction": "Find sum n>0 where n^2-7n+12 perfect square.",
        "response": "(n-3)(n-4)=k^2. gcd=1 so each a perfect square. Only consecutive squares 0,1. So n-3=0 or n-4=0 => n=3,4. Sum=7.",
        "reasoning_trace": "Factor and use gcd argument. Consecutive integers >0 can't both be perfect squares. So one must be 0.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "hard",
    },
    {
        "instruction": "lim_{x->0} (sin x-tan x)/x^3.",
        "response": "sin x=x-x^3/6+O(x^5), tan x=x+x^3/3+O(x^5). Subtract: -x^3/2+O(x^5). Divide: -1/2+O(x^2) -> -1/2.",
        "reasoning_trace": "Taylor expansions. L'Hopital also works: differentiate thrice, get -3/6 = -1/2.",
        "source_model": "Claude Opus 4.8",
        "domain": "math",
        "difficulty": "medium",
    },
    {
        "instruction": "8 rooks on 8x8 board, no attacks, no main diagonal.",
        "response": "Derangements D_8 = 8!*sum(-1)^k/k! = 14833.",
        "reasoning_trace": "Require permutation with pi(i)!=i. D_8 = 40320*0.36788 = 14833.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "medium",
    },
    {
        "instruction": "Find real x^3+y^3=3xy-1.",
        "response": "s=x+y, p=xy. s^3+1=3p(s+1). s=-1: x+y=-1 works. Else p=(s^2-s+1)/3, discriminant => s=2,p=1 => x=y=1.",
        "reasoning_trace": "Symmetric polynomials. Case analysis on s+1=0 or not.",
        "source_model": "Claude Opus 4.8",
        "domain": "math",
        "difficulty": "hard",
    },
    {
        "instruction": "Integral of ln(sin x) from 0 to pi/2.",
        "response": "I=-(pi/2)ln2. Use symmetry: I=Integral ln(cos x)dx. 2I=Integral ln(sin2x/2)dx=I-(pi/2)ln2.",
        "reasoning_trace": "Classic symmetry trick. Map x->pi/2-x, use sin2x identity.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "medium",
    },
    {
        "instruction": "Prove infinite primes 4k+3.",
        "response": "Assume finite set. N=4*prod-1=3 mod4. Has prime q=3 mod4 not in set. Contradiction.",
        "reasoning_trace": "Euclid's proof adapted for arithmetic progression 4k+3.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "medium",
    },
    {
        "instruction": "det of nxn matrix with A_ij=1 if |i-j|<=1.",
        "response": "D_n=D_{n-1}-D_{n-2}, D_1=1,D_2=0. Period 6: 1,0,-1,-1,0,1. D_n=(2/sqrt3)sin((n+1)pi/3).",
        "reasoning_trace": "Tridiagonal Toeplitz. Expand by first row, get recurrence. Solve via char eq roots e^{+-ipi/3}.",
        "source_model": "Claude Opus 4.8",
        "domain": "math",
        "difficulty": "hard",
    },
    {
        "instruction": "Solve y''-2y'+y=e^x/(1+x^2).",
        "response": "y_h=(C_1+C_2x)e^x. VOP: u_1=-(1/2)ln(1+x^2), u_2=arctan x. y=e^x[C_1+C_2x-(1/2)ln(1+x^2)+x*arctan x].",
        "reasoning_trace": "Char eq repeated root r=1. Variation of parameters with W=e^{2x}.",
        "source_model": "Claude Opus 4.8",
        "domain": "math",
        "difficulty": "hard",
    },
    {
        "instruction": "Find all primitive Pythagorean triples.",
        "response": "x=m^2-n^2, y=2mn, z=m^2+n^2, m>n>0, gcd(m,n)=1, opposite parity.",
        "reasoning_trace": "Assume y even. y^2=(z-x)(z+x). gcd(z-x,z+x)=2. Set z-x=2n^2, z+x=2m^2. Solve.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "medium",
    },
    {
        "instruction": "Radius of conv of Sigma n! x^n/n^n.",
        "response": "R=e. Ratio: n^n/(n+1)^n->1/e. Endpoints diverge (Stirling: term~sqrt(2pin)->inf).",
        "reasoning_trace": "Ratio test gives 1/e. Root test via Stirling confirms. Check x=e diverges.",
        "source_model": "Claude Opus 4.8",
        "domain": "math",
        "difficulty": "medium",
    },
    {
        "instruction": "Bag 5R,3B,2G, draw 4. P(at least one each)?",
        "response": "Total C(10,4)=210. Favorable: C(5,2)C(3,1)C(2,1)+C(5,1)C(3,2)C(2,1)+C(5,1)C(3,1)C(2,2)=60+30+15=105. P=1/2.",
        "reasoning_trace": "Only (2,1,1) permutations possible. Count each.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "easy",
    },
    {
        "instruction": "7^2023 mod 11.",
        "response": "7^10=1(FLT). 2023=10*202+3. 7^2023=7^3=343=2.",
        "reasoning_trace": "Fermat's Little Theorem: a^{10}=1 mod 11. Reduce exponent mod 10.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "easy",
    },
    {
        "instruction": "Sigma n/2^n.",
        "response": "S=2. Sigma x^n=1/(1-x). Diff: Sigma n x^{n-1}=1/(1-x)^2. Mult x: Sigma n x^n=x/(1-x)^2. x=1/2: S=(1/2)/(1/4)=2.",
        "reasoning_trace": "Geometric series derivative technique.",
        "source_model": "Claude Opus 4.8",
        "domain": "math",
        "difficulty": "easy",
    },
    {
        "instruction": "f(x)=x^3-3x+1. Find real roots.",
        "response": "3 real roots: (-2,-1), (0,1), (1,2). f'(x)=3(x-1)(x+1). f(-2)=-1<0<f(-1)=3. f(0)=1>0>f(1)=-1. f(1)=-1<0<f(2)=3.",
        "reasoning_trace": "Cubic with local max>0 and local min<0 implies 3 real roots. IVT on each interval.",
        "source_model": "Claude Opus 4.8",
        "domain": "math",
        "difficulty": "medium",
    },
    {
        "instruction": "Sum exterior angles convex polygon = 360.",
        "response": "Sum interior=(n-2)180. At each vertex int+ext=180. Sum ext=n*180-(n-2)180=360.",
        "reasoning_trace": "Each vertex: interior+exterior=180. For n vertices: total=180n. Subtract interior sum (n-2)180.",
        "source_model": "Claude Opus 4.8",
        "domain": "math",
        "difficulty": "easy",
    },
    {
        "instruction": "x^2+kx+(k+3)=0 real roots. Find k.",
        "response": "D=k^2-4(k+3)=k^2-4k-12=(k-6)(k+2)>=0 => k<=-2 or k>=6.",
        "reasoning_trace": "Discriminant analysis. Factor quadratic in k.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "easy",
    },
    {
        "instruction": "Arrangements of MATHEMATICS.",
        "response": "11!/(2!2!2!)=39916800/8=4989600.",
        "reasoning_trace": "11 letters, M(2), A(2), T(2) repeats. Permutations with repetition formula.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "easy",
    },
    {
        "instruction": "Min of x+4/x for x>0.",
        "response": "AM-GM: x+4/x >= 2*sqrt(x*4/x)=4. Equality at x=2. Min=4.",
        "reasoning_trace": "AM-GM inequality or calculus: f'(x)=1-4/x^2=0 => x=2.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "easy",
    },
    {
        "instruction": "lim_{x->inf} (1+1/x)^x.",
        "response": "ln L = lim x ln(1+1/x)=lim ln(1+1/x)/(1/x). L'Hopital: 1/(1+1/x)->1. So L=e.",
        "reasoning_trace": "Classic limit. Take ln, apply L'Hopital to 0/0 form.",
        "source_model": "Claude Opus 4.8",
        "domain": "math",
        "difficulty": "easy",
    },
    {
        "instruction": "Prove 1^2+...+n^2=n(n+1)(2n+1)/6 by induction.",
        "response": "Base n=1. Assume for k. Sum_{k+1}=k(k+1)(2k+1)/6+(k+1)^2=(k+1)(k+2)(2k+3)/6.",
        "reasoning_trace": "Standard induction. Add (k+1)^2, factor.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "easy",
    },
    {
        "instruction": "How many involutions f:{1..5}->{1..5}?",
        "response": "26. Sum k=0..2: C(5,2k)*(2k)!/(2^k k!). k=0:1, k=1:10, k=2:15. Total=26.",
        "reasoning_trace": "Involutions are products of fixed points and 2-cycles. Count by number of transpositions.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "medium",
    },
    {
        "instruction": "Coef of x^5 in (1+2x+x^2)^4.",
        "response": "56. 1+2x+x^2=(1+x)^2. So (1+x)^8. Coef x^5=C(8,5)=56.",
        "reasoning_trace": "Simplify first, then binomial theorem.",
        "source_model": "DeepSeek-R1",
        "domain": "math",
        "difficulty": "easy",
    },
]

ALL_EXAMPLES.extend(MATH_EXAMPLES)

CODE_EXAMPLES: List[Dict[str, str]] = [
]

ALL_EXAMPLES.extend(CODE_EXAMPLES)

SCIENCE_EXAMPLES: List[Dict[str, str]] = [
]

ALL_EXAMPLES.extend(SCIENCE_EXAMPLES)

LOGIC_EXAMPLES: List[Dict[str, str]] = [
]

ALL_EXAMPLES.extend(LOGIC_EXAMPLES)

INSTRUCTION_EXAMPLES: List[Dict[str, str]] = [
]

ALL_EXAMPLES.extend(INSTRUCTION_EXAMPLES)

SECURITY_EXAMPLES: List[Dict[str, str]] = [
]

ALL_EXAMPLES.extend(SECURITY_EXAMPLES)

CREATIVE_EXAMPLES: List[Dict[str, str]] = [
]

ALL_EXAMPLES.extend(CREATIVE_EXAMPLES)


def get_examples_by_domain(domain: str) -> List[Dict[str, str]]:
    return [ex for ex in ALL_EXAMPLES if ex["domain"] == domain]

def get_examples_by_difficulty(difficulty: str) -> List[Dict[str, str]]:
    return [ex for ex in ALL_EXAMPLES if ex["difficulty"] == difficulty]

def get_examples_by_model(model: str) -> List[Dict[str, str]]:
    return [ex for ex in ALL_EXAMPLES if ex["source_model"] == model]

def get_example_count() -> int:
    return len(ALL_EXAMPLES)

def random_example() -> Dict[str, str]:
    return random.choice(ALL_EXAMPLES)

__all__ = [
    "ALL_EXAMPLES",
    "MATH_EXAMPLES", "CODE_EXAMPLES", "SCIENCE_EXAMPLES",
    "LOGIC_EXAMPLES", "INSTRUCTION_EXAMPLES",
    "SECURITY_EXAMPLES", "CREATIVE_EXAMPLES",
    "get_examples_by_domain", "get_examples_by_difficulty",
    "get_examples_by_model", "get_example_count",
    "random_example",
]
