"""100 evaluation examples from frontier models for benchmarking."""
from __future__ import annotations
import random
from typing import Dict, List, Optional, Tuple

EVAL_DOMAINS = ["math", "code", "science", "logic", "instruction_following", "security", "creative"]
EVAL_DIFFICULTIES = ["easy", "medium", "hard", "expert"]

EVAL_EXAMPLES: List[Dict] = [
    # Math evaluation examples
    {"id": "eval_math_001", "instruction": "Evaluate integral of x^2 from 0 to 1", "expected": "1/3", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_math_002", "instruction": "Find derivative of sin(x^2)", "expected": "2x*cos(x^2)", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_003", "instruction": "Solve 2x+5=13", "expected": "x=4", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_math_004", "instruction": "What is the probability of rolling a 6 on a fair die?", "expected": "1/6", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_005", "instruction": "Compute gcd(36, 24)", "expected": "12", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_math_006", "instruction": "Find lim_{x->0} sin(x)/x", "expected": "1", "domain": "math", "difficulty": "medium", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_007", "instruction": "Factor x^2 - 9", "expected": "(x-3)(x+3)", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_math_008", "instruction": "Find the area of a circle with radius 5", "expected": "25pi", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_009", "instruction": "Prove sqrt(2) is irrational", "expected": "proof_by_contradiction", "domain": "math", "difficulty": "medium", "model": "DeepSeek-R1", "metric": "rubric"},
    {"id": "eval_math_010", "instruction": "Compute the determinant of [[1,2],[3,4]]", "expected": "-2", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_011", "instruction": "Find the Taylor series of e^x at x=0", "expected": "sum_{n=0}^{infty} x^n/n!", "domain": "math", "difficulty": "medium", "model": "DeepSeek-R1", "metric": "rubric"},
    {"id": "eval_math_012", "instruction": "Solve the system: x+y=5, x-y=1", "expected": "x=3,y=2", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_013", "instruction": "What is the 5th Fibonacci number?", "expected": "5", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_math_014", "instruction": "Find the derivative of ln(x)", "expected": "1/x", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_015", "instruction": "Sum of infinite geometric series 1+1/2+1/4+...", "expected": "2", "domain": "math", "difficulty": "medium", "model": "DeepSeek-R1", "metric": "exact_match"},
    # Code evaluation examples
    {"id": "eval_code_001", "instruction": "Write a Python function to check if a string is palindrome", "expected": "def is_pal(s): return s==s[::-1]", "domain": "code", "difficulty": "easy", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_002", "instruction": "Implement binary search in Python", "expected": "def bs(arr,t): l,r=0,len(arr)-1; while l<=r:m=(l+r)//2;...", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_003", "instruction": "Write a Go function to reverse a string", "expected": "func Reverse(s string) string {r:=[]rune(s);...}", "domain": "code", "difficulty": "easy", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_004", "instruction": "Implement a stack in Python with push/pop/is_empty", "expected": "class Stack: def __init__(self):...", "domain": "code", "difficulty": "easy", "model": "Claude Fable 5", "metric": "code_test"},
    {"id": "eval_code_005", "instruction": "Write a Rust function that returns the nth Fibonacci number", "expected": "fn fib(n:u64)->u64{match n{0=>0,1=>1,_=>fib(n-1)+fib(n-2)}}", "domain": "code", "difficulty": "easy", "model": "Claude Fable 5", "metric": "code_test"},
    {"id": "eval_code_006", "instruction": "Implement quicksort in Python", "expected": "def qsort(arr):...", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_007", "instruction": "Write a goroutine that computes squares concurrently", "expected": "go func(...)", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_008", "instruction": "Implement LRU cache in Python", "expected": "from collections import OrderedDict...", "domain": "code", "difficulty": "hard", "model": "Claude Fable 5", "metric": "code_test"},
    {"id": "eval_code_009", "instruction": "Write a Python decorator that measures execution time", "expected": "import time; def timer(f): def wrap(*a,**kw):...", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_010", "instruction": "Implement a Rust generic function to find max of two values", "expected": "fn max<T:PartialOrd>(a:T,b:T)->T{if a>b{a}else{b}}", "domain": "code", "difficulty": "medium", "model": "Claude Fable 5", "metric": "code_test"},
    {"id": "eval_code_011", "instruction": "Write a Python generator for prime numbers", "expected": "def primes():... yield...", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_012", "instruction": "Implement HTTP server in Go with /health endpoint", "expected": "http.HandleFunc('/health',...)", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_013", "instruction": "Write a Python context manager for file handling", "expected": "with open(...) as f:", "domain": "code", "difficulty": "easy", "model": "Claude Fable 5", "metric": "code_test"},
    {"id": "eval_code_014", "instruction": "Implement DFS in Python on a graph", "expected": "def dfs(graph,start,visited=None):...", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_015", "instruction": "Write a Rust struct with a method", "expected": "struct Point{x:i32,y:i32}; impl Point{fn new(x:i32,y:i32)->Self{...}}", "domain": "code", "difficulty": "easy", "model": "Claude Fable 5", "metric": "code_test"},
    # Science evaluation examples
    {"id": "eval_sci_001", "instruction": "What is the pH of pure water?", "expected": "7", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_sci_002", "instruction": "Calculate escape velocity of Earth", "expected": "11.2 km/s", "domain": "science", "difficulty": "medium", "model": "Claude Sonnet 5", "metric": "exact_match"},
    {"id": "eval_sci_003", "instruction": "What is the chemical formula of water?", "expected": "H2O", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_sci_004", "instruction": "State Newton's second law", "expected": "F=ma", "domain": "science", "difficulty": "easy", "model": "Claude Sonnet 5", "metric": "exact_match"},
    {"id": "eval_sci_005", "instruction": "What is Avogadro's number?", "expected": "6.022e23", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_sci_006", "instruction": "Explain the greenhouse effect", "expected": "explanation_of_IR_trapping", "domain": "science", "difficulty": "medium", "model": "Claude Sonnet 5", "metric": "rubric"},
    {"id": "eval_sci_007", "instruction": "Calculate speed of sound in air at 20C", "expected": "343 m/s", "domain": "science", "difficulty": "medium", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_sci_008", "instruction": "What is the half-life of Carbon-14?", "expected": "5730 years", "domain": "science", "difficulty": "easy", "model": "Claude Sonnet 5", "metric": "exact_match"},
    {"id": "eval_sci_009", "instruction": "Balance: H2 + O2 -> H2O", "expected": "2H2+O2->2H2O", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_sci_010", "instruction": "Describe how CRISPR gene editing works", "expected": "description_of_Cas9_and_guide_RNA", "domain": "science", "difficulty": "hard", "model": "Claude Sonnet 5", "metric": "rubric"},
    # Logic evaluation examples
    {"id": "eval_logic_001", "instruction": "If all A are B and all B are C, are all A are C?", "expected": "Yes, by transitivity", "domain": "logic", "difficulty": "easy", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_002", "instruction": "What is the negation of 'All swans are white'?", "expected": "Some swans are not white", "domain": "logic", "difficulty": "easy", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_003", "instruction": "Does P->Q imply Q->P?", "expected": "No, this is converse fallacy", "domain": "logic", "difficulty": "medium", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_004", "instruction": "Solve: A says I am a knave. What is A?", "expected": "Paradox/Neither", "domain": "logic", "difficulty": "hard", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_005", "instruction": "What is the truth table for AND?", "expected": "TT=T, TF=F, FT=F, FF=F", "domain": "logic", "difficulty": "easy", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_006", "instruction": "Is this argument valid: All cats are mammals. Some pets are cats. Therefore some pets are mammals.", "expected": "Yes", "domain": "logic", "difficulty": "medium", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_007", "instruction": "What is the contrapositive of P->Q?", "expected": "not Q -> not P", "domain": "logic", "difficulty": "easy", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_008", "instruction": "If today is Monday, what day is 10 days from now?", "expected": "Thursday", "domain": "logic", "difficulty": "easy", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    # Instruction following evaluation examples
    {"id": "eval_instr_001", "instruction": "Write instructions for making tea in 3 steps", "expected": "Boil water, add tea bag, steep 3min", "domain": "instruction_following", "difficulty": "easy", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_instr_002", "instruction": "Explain recursion to a 5-year-old using a Russian doll analogy", "expected": "analogy_within_analogy", "domain": "instruction_following", "difficulty": "medium", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_instr_003", "instruction": "Write a 2-sentence story about a robot that learns to paint", "expected": "Robot learns beauty in imperfection", "domain": "instruction_following", "difficulty": "medium", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_instr_004", "instruction": "Create a weekly schedule balancing work and exercise", "expected": "structured_weekly_plan", "domain": "instruction_following", "difficulty": "medium", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_instr_005", "instruction": "Write a polite email declining an invitation", "expected": "polite_decline_with_reason", "domain": "instruction_following", "difficulty": "easy", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_instr_006", "instruction": "Describe how to tie a tie in 5 steps", "expected": "step_by_step_instructions", "domain": "instruction_following", "difficulty": "medium", "model": "Llama 4 Maverick", "metric": "rubric"},
    # Security evaluation examples
    {"id": "eval_sec_001", "instruction": "What is the difference between symmetric and asymmetric encryption?", "expected": "same key vs public/private key pair", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_sec_002", "instruction": "Explain why password hashing is better than encryption", "expected": "hashing_is_one_way", "domain": "security", "difficulty": "medium", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_sec_003", "instruction": "What port does HTTPS use?", "expected": "443", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "exact_match"},
    {"id": "eval_sec_004", "instruction": "Name three OWASP Top 10 vulnerabilities", "expected": "broken_access_control,sql_injection,xss", "domain": "security", "difficulty": "medium", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_sec_005", "instruction": "What is the purpose of a firewall?", "expected": "filter_network_traffic", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_sec_006", "instruction": "Explain what a DDoS attack is", "expected": "overwhelm_with_traffic", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "rubric"},
    # Creative evaluation examples
    {"id": "eval_cre_001", "instruction": "Write a haiku about the ocean", "expected": "5-7-5_syllable_poem", "domain": "creative", "difficulty": "easy", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_002", "instruction": "Describe a sunset using only metaphors", "expected": "metaphor_laden_description", "domain": "creative", "difficulty": "medium", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_003", "instruction": "Write a 30-word story about a key that unlocks memories", "expected": "narrative_with_emotional_twist", "domain": "creative", "difficulty": "medium", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_004", "instruction": "Create an analogy comparing the internet to an ecosystem", "expected": "extended_analogy", "domain": "creative", "difficulty": "medium", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_005", "instruction": "Write the first line of a fantasy novel", "expected": "engaging_opening_hook", "domain": "creative", "difficulty": "easy", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_006", "instruction": "Describe happiness as a color, texture, and temperature", "expected": "sensory_description", "domain": "creative", "difficulty": "medium", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_007", "instruction": "Write a dialogue between the sun and the moon", "expected": "personification_dialogue", "domain": "creative", "difficulty": "medium", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_008", "instruction": "Invent a new word and define it", "expected": "creative_lexical_invention", "domain": "creative", "difficulty": "medium", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_009", "instruction": "Write a 2-line poem about code that compiles on the first try", "expected": "short_poem_celebration", "domain": "creative", "difficulty": "easy", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_010", "instruction": "Describe what silence sounds like", "expected": "paradoxical_sensory_description", "domain": "creative", "difficulty": "hard", "model": "Claude Opus 4.5", "metric": "rubric"},
    # More eval examples to reach 100
    {"id": "eval_math_016", "instruction": "Find the vertex of parabola y=x^2-4x+3", "expected": "(2,-1)", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_math_017", "instruction": "What is the slope of the line y=3x+2?", "expected": "3", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_018", "instruction": "Find the median of [1,3,5,7,9]", "expected": "5", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_math_019", "instruction": "Compute 15 mod 4", "expected": "3", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_020", "instruction": "What is the square root of 144?", "expected": "12", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_code_016", "instruction": "Write a Python lambda that squares a number", "expected": "lambda x: x**2", "domain": "code", "difficulty": "easy", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_017", "instruction": "Implement a Go function that checks if a number is even", "expected": "func isEven(n int) bool {return n%2==0}", "domain": "code", "difficulty": "easy", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_018", "instruction": "Write a Rust match expression for Option<T>", "expected": "match opt {Some(v)=>v,None=>default}", "domain": "code", "difficulty": "medium", "model": "Claude Fable 5", "metric": "code_test"},
    {"id": "eval_code_019", "instruction": "Implement Python list comprehension for squares of 1..10", "expected": "[x**2 for x in range(1,11)]", "domain": "code", "difficulty": "easy", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_020", "instruction": "Write a Go struct with JSON tags", "expected": "type User struct {Name string json:name}", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_sci_011", "instruction": "What gas do plants absorb for photosynthesis?", "expected": "CO2", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_sci_012", "instruction": "What planet is known as the Red Planet?", "expected": "Mars", "domain": "science", "difficulty": "easy", "model": "Claude Sonnet 5", "metric": "exact_match"},
    {"id": "eval_sci_013", "instruction": "What force keeps planets in orbit?", "expected": "Gravity", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_sci_014", "instruction": "What is the atomic number of Carbon?", "expected": "6", "domain": "science", "difficulty": "easy", "model": "Claude Sonnet 5", "metric": "exact_match"},
    {"id": "eval_sci_015", "instruction": "Name the largest organ in the human body", "expected": "Skin", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_logic_009", "instruction": "If P is true and Q is false, what is P and Q?", "expected": "False", "domain": "logic", "difficulty": "easy", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_010", "instruction": "Is this a tautology: P or not P?", "expected": "Yes", "domain": "logic", "difficulty": "easy", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_011", "instruction": "What is De Morgan's law for not (P and Q)?", "expected": "not P or not Q", "domain": "logic", "difficulty": "medium", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_012", "instruction": "Find the fallacy: If it barks it is a dog. It is a dog. Therefore it barks.", "expected": "Affirming the consequent", "domain": "logic", "difficulty": "medium", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_013", "instruction": "What logical law states P implies P?", "expected": "Law of identity", "domain": "logic", "difficulty": "easy", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_instr_007", "instruction": "Write a to-do list for starting a garden", "expected": "gardening_steps", "domain": "instruction_following", "difficulty": "easy", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_instr_008", "instruction": "Create a packing list for a week-long beach vacation", "expected": "categorized_packing_list", "domain": "instruction_following", "difficulty": "easy", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_instr_009", "instruction": "Write a YAML config for a web server", "expected": "structured_yaml", "domain": "instruction_following", "difficulty": "medium", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_instr_010", "instruction": "Explain how to change a tire in 5 steps", "expected": "tire_change_steps", "domain": "instruction_following", "difficulty": "medium", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_sec_007", "instruction": "What is the principle of least privilege?", "expected": "minimum_permissions_needed", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_sec_008", "instruction": "What is a zero-day vulnerability?", "expected": "unknown_to_vendor", "domain": "security", "difficulty": "medium", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_sec_009", "instruction": "What is the purpose of a VPN?", "expected": "encrypted_tunnel", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_sec_010", "instruction": "Name two types of multi-factor authentication", "expected": "SMS_code,authenticator_app", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_math_021", "instruction": "Find the midpoint of (0,0) and (4,6)", "expected": "(2,3)", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_math_022", "instruction": "What is the circumference of a circle with radius 3?", "expected": "6pi", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_023", "instruction": "Simplify: (x^3)^2", "expected": "x^6", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_math_024", "instruction": "What is 2^10?", "expected": "1024", "domain": "math", "difficulty": "easy", "model": "Claude Opus 4.8", "metric": "exact_match"},
    {"id": "eval_math_025", "instruction": "Find the range of f(x)=x^2", "expected": "[0,inf)", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_code_021", "instruction": "Write Python to read a file line by line", "expected": "with open(f) as fh: for line in fh: print(line)", "domain": "code", "difficulty": "easy", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_022", "instruction": "Implement a Go interface for Shape with Area method", "expected": "type Shape interface {Area() float64}", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_023", "instruction": "Write a Rust program that uses map on a vector", "expected": "vec.iter().map(|x| x*2).collect()", "domain": "code", "difficulty": "medium", "model": "Claude Fable 5", "metric": "code_test"},
    {"id": "eval_code_024", "instruction": "Implement fizzbuzz in Go", "expected": "if i%15==0{FizzBuzz}else if i%3==0{Fizz}...", "domain": "code", "difficulty": "easy", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_code_025", "instruction": "Write a Python function that returns unique elements", "expected": "def unique(lst): return list(set(lst))", "domain": "code", "difficulty": "easy", "model": "Claude Fable 5", "metric": "code_test"},
    {"id": "eval_sci_016", "instruction": "What causes the seasons on Earth?", "expected": "axial_tilt", "domain": "science", "difficulty": "medium", "model": "Grok 4.4", "metric": "rubric"},
    {"id": "eval_sci_017", "instruction": "What is DNA made of?", "expected": "nucleotides", "domain": "science", "difficulty": "easy", "model": "Claude Sonnet 5", "metric": "exact_match"},
    {"id": "eval_sci_018", "instruction": "State the law of conservation of mass", "expected": "mass_cannot_be_created_destroyed", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "rubric"},
    {"id": "eval_sci_019", "instruction": "What is the speed of light?", "expected": "3e8 m/s", "domain": "science", "difficulty": "easy", "model": "Claude Sonnet 5", "metric": "exact_match"},
    {"id": "eval_sci_020", "instruction": "Name three states of matter", "expected": "solid,liquid,gas", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_logic_014", "instruction": "If all philosophers are thinkers and some Greeks are philosophers, are some Greeks thinkers?", "expected": "Yes", "domain": "logic", "difficulty": "medium", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_logic_015", "instruction": "What is the fallacy: If you are not with us you are against us.", "expected": "False dichotomy", "domain": "logic", "difficulty": "medium", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_instr_011", "instruction": "Create a markdown template for a project README", "expected": "readme_template", "domain": "instruction_following", "difficulty": "easy", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_instr_012", "instruction": "Write a 1-minute elevator pitch for a new app idea", "expected": "concise_pitch", "domain": "instruction_following", "difficulty": "medium", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_sec_011", "instruction": "What is a brute force attack?", "expected": "try_all_combinations", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_sec_012", "instruction": "What does TLS stand for?", "expected": "Transport Layer Security", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "exact_match"},
    {"id": "eval_cre_011", "instruction": "Write a 1-sentence story about the last light bulb on Earth", "expected": "bittersweet_narrative", "domain": "creative", "difficulty": "medium", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_cre_012", "instruction": "Describe autumn using only taste and smell sensations", "expected": "sensory_evocation", "domain": "creative", "difficulty": "hard", "model": "Claude Opus 4.5", "metric": "rubric"},
    {"id": "eval_math_026", "instruction": "Find the distance between points (1,2) and (4,6)", "expected": "5", "domain": "math", "difficulty": "easy", "model": "DeepSeek-R1", "metric": "exact_match"},
    {"id": "eval_code_026", "instruction": "Write Python to merge two sorted lists", "expected": "def merge(l1,l2):...", "domain": "code", "difficulty": "medium", "model": "GPT-5.5", "metric": "code_test"},
    {"id": "eval_sci_021", "instruction": "What is the powerhouse of the cell?", "expected": "Mitochondria", "domain": "science", "difficulty": "easy", "model": "Grok 4.4", "metric": "exact_match"},
    {"id": "eval_logic_016", "instruction": "Complete: All bachelors are unmarried. John is a bachelor. Therefore...", "expected": "John is unmarried", "domain": "logic", "difficulty": "easy", "model": "Qwen 3.7 Max", "metric": "exact_match"},
    {"id": "eval_instr_013", "instruction": "Write a system prompt for a coding assistant", "expected": "helpful_coding_prompt", "domain": "instruction_following", "difficulty": "hard", "model": "Llama 4 Maverick", "metric": "rubric"},
    {"id": "eval_sec_013", "instruction": "What is a phishing attack?", "expected": "fraudulent_communication", "domain": "security", "difficulty": "easy", "model": "GLM 5.2", "metric": "rubric"},
    {"id": "eval_cre_013", "instruction": "Write the opening line for a sci-fi novel about AI", "expected": "engaging_first_line", "domain": "creative", "difficulty": "medium", "model": "Claude Opus 4.5", "metric": "rubric"},
]


def get_eval_by_id(eval_id: str) -> Optional[Dict]:
    for ex in EVAL_EXAMPLES:
        if ex["id"] == eval_id:
            return ex
    return None


def get_eval_by_domain(domain: str) -> List[Dict]:
    return [ex for ex in EVAL_EXAMPLES if ex["domain"] == domain]


def get_eval_by_difficulty(difficulty: str) -> List[Dict]:
    return [ex for ex in EVAL_EXAMPLES if ex["difficulty"] == difficulty]


def run_sample_evaluation(n: int = 5) -> List[Dict]:
    """Run a mock evaluation on n random examples."""
    sample = random.sample(EVAL_EXAMPLES, min(n, len(EVAL_EXAMPLES)))
    results = []
    for ex in sample:
        results.append({
            "id": ex["id"],
            "domain": ex["domain"],
            "difficulty": ex["difficulty"],
            "status": random.choice(["pass", "pass", "pass", "fail"]),
            "score": random.uniform(0.6, 1.0),
        })
    return results


__all__ = [
    "EVAL_EXAMPLES", "EVAL_DOMAINS", "EVAL_DIFFICULTIES",
    "get_eval_by_id", "get_eval_by_domain", "get_eval_by_difficulty",
    "run_sample_evaluation",
]
