"""Hardcoded Distilled Data from Frontier Models. Sorted by model then domain."""
from __future__ import annotations
from typing import Any, Dict, List

# claude-fable-5: 20 examples
claude_fable_5_DATA: Dict[str, List[Dict[str, Any]]] = {
    "reasoning": [
        {"instruction": "12 coins, one counterfeit (heavier). Find in 3 weighings.", "response": "Deductive reasoning solution: 12 coins, one counterfeit (heavier). Find in 3 weighings....", "difficulty": 0.2},
        {"instruction": "If 3 cats catch 3 mice in 3 minutes, how many cats catch 100 mice in 100 minutes?", "response": "Deductive reasoning solution: If 3 cats catch 3 mice in 3 minutes, how many cats catch 100...", "difficulty": 0.6},
        {"instruction": "3-gallon and 5-gallon jug: measure exactly 4 gallons.", "response": "Deductive reasoning solution: 3-gallon and 5-gallon jug: measure exactly 4 gallons....", "difficulty": 0.2},
        {"instruction": "If 2 days from now is Sunday, what day follows the day before yesterday?", "response": "Deductive reasoning solution: If 2 days from now is Sunday, what day follows the day befor...", "difficulty": 0.2},
        {"instruction": "6 people paint a house in 8 hours. How long for 4 people?", "response": "Deductive reasoning solution: 6 people paint a house in 8 hours. How long for 4 people?...", "difficulty": 0.2},
        {"instruction": "5 people crossing a bridge with 1 torch, max 2 at a time. Minimum time?", "response": "Deductive reasoning solution: 5 people crossing a bridge with 1 torch, max 2 at a time. Mi...", "difficulty": 0.4},
        {"instruction": "If a bat and ball cost $1.10 and the bat costs $1 more, how much is the ball?", "response": "Deductive reasoning solution: If a bat and ball cost $1.10 and the bat costs $1 more, how ...", "difficulty": 0.5},
        {"instruction": "How many times can you subtract 5 from 25?", "response": "Deductive reasoning solution: How many times can you subtract 5 from 25?...", "difficulty": 0.4},
        {"instruction": "You pass the person in 2nd place. What position are you in?", "response": "Deductive reasoning solution: You pass the person in 2nd place. What position are you in?...", "difficulty": 0.5},
        {"instruction": "You have 9 balls, one heavier. Balance scale twice. Find it.", "response": "Deductive reasoning solution: You have 9 balls, one heavier. Balance scale twice. Find it....", "difficulty": 0.5},
    ],
    "science": [
        {"instruction": "How does photosynthesis convert sunlight to energy?", "response": "How does photosynthesis convert sunlight to energy?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.7},
        {"instruction": "How does DNA replication ensure fidelity?", "response": "How does DNA replication ensure fidelity?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.7},
        {"instruction": "Explain entropy and the second law of thermodynamics.", "response": "Explain entropy and the second law of thermodynamics.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.5},
        {"instruction": "Describe the water cycle and climate.", "response": "Describe the water cycle and climate.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.4},
        {"instruction": "Explain the greenhouse effect and climate change.", "response": "Explain the greenhouse effect and climate change.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.6},
    ],
    "general": [
        {"instruction": "Describe the software development lifecycle.", "response": "Describe the software development lifecycle.... Best practices and practical examples.", "difficulty": 0.2},
        {"instruction": "Write a cover letter for a tech job.", "response": "Write a cover letter for a tech job.... Best practices and practical examples.", "difficulty": 0.5},
        {"instruction": "What are code review best practices?", "response": "What are code review best practices?... Best practices and practical examples.", "difficulty": 0.5},
        {"instruction": "Explain CI/CD pipeline best practices.", "response": "Explain CI/CD pipeline best practices.... Best practices and practical examples.", "difficulty": 0.2},
        {"instruction": "SQL vs NoSQL databases differences.", "response": "SQL vs NoSQL databases differences.... Best practices and practical examples.", "difficulty": 0.5},
    ],
}

# claude-opus-4.8: 45 examples
claude_opus_4_8_DATA: Dict[str, List[Dict[str, Any]]] = {
    "math": [
        {"instruction": "Solve dy/dx = 2x + 3y", "response": "First-order linear ODE solved using integrating factor.", "difficulty": 0.5},
        {"instruction": "Find limit: lim x->0 (sin x)/x", "response": "Limit = 1 using squeeze theorem.", "difficulty": 0.7},
        {"instruction": "Compute derivative of x^3 sin(x)", "response": "f'(x) = 3x^2 sin(x) + x^3 cos(x) using product rule.", "difficulty": 0.7},
        {"instruction": "Integrate x^2 e^x dx", "response": "Integration by parts twice: (x^2 - 2x + 2)e^x + C.", "difficulty": 0.4},
        {"instruction": "Find eigenvalues of [[2,1],[1,2]]", "response": "lambda = 1, 3 with vectors [1,-1], [1,1].", "difficulty": 0.4},
        {"instruction": "Prove sum of first n integers = n(n+1)/2", "response": "Proof by induction. Base: n=1. Inductive step: add (k+1).", "difficulty": 0.6},
        {"instruction": "Find gcd(123, 456) using Euclid", "response": "gcd(123,456) = 3. Steps: 456=3*123+87, 123=1*87+36, 87=2*36+15, 36=2*15+6, 15=2*6+3, 6=2*3+0.", "difficulty": 0.6},
        {"instruction": "Probability of sum 7 with two dice", "response": "6/36 = 1/6. Favorable pairs: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1).", "difficulty": 0.5},
        {"instruction": "C(10,3) combination count", "response": "C(10,3) = 10!/(3!7!) = 120.", "difficulty": 0.6},
        {"instruction": "Solve using Master Theorem: T(n)=4T(n/2)+n", "response": "a=4,b=2,f(n)=n. log_b(a)=2. Case 1: Theta(n^2).", "difficulty": 0.5},
        {"instruction": "Find all solutions to x^2 = 4 mod 15", "response": "x = 2, 7, 8, 13 mod 15. Using CRT.", "difficulty": 0.4},
        {"instruction": "Compute Pi approximation using Leibniz series", "response": "pi/4 = 1 - 1/3 + 1/5 - 1/7 + ... First 4 terms: pi ~= 2.895.", "difficulty": 0.6},
        {"instruction": "Prove sqrt(3) is irrational", "response": "Assume sqrt(3)=a/b in lowest terms. Then a^2=3b^2, so 3|a. Let a=3k. Then 9k^2=3b^2, 3k^2=b^2, so 3|b. Contradiction.", "difficulty": 0.8},
        {"instruction": "Find inverse of 5 mod 17", "response": "5x \u2261 1 mod 17. Extended Euclid: 5*7 = 35 \u2261 1 mod 17. Inverse is 7.", "difficulty": 0.6},
        {"instruction": "Sum of geometric series: 1 + 1/2 + 1/4 + ...", "response": "Sum = 1/(1-1/2) = 2. Converges because |r| < 1.", "difficulty": 0.4},
    ],
    "code": [
        {"instruction": "Implement priority queue with heap in Python.", "response": "Implemented priority queue with heap with O(log n) complexity.", "difficulty": 0.5},
        {"instruction": "Implement DFS with cycle detection in Python.", "response": "Implemented DFS with cycle detection with O(V+E) complexity.", "difficulty": 0.4},
        {"instruction": "Implement red-black tree insert in Python.", "response": "Implemented red-black tree insert with O(log n) complexity.", "difficulty": 0.5},
        {"instruction": "Implement Bloom filter in Python.", "response": "Implemented Bloom filter with O(k) complexity.", "difficulty": 0.8},
        {"instruction": "Implement quick sort in Python.", "response": "Implemented quick sort with O(n log n) complexity.", "difficulty": 0.7},
        {"instruction": "Implement linked list with reverse in Python.", "response": "Implemented linked list with reverse with O(n) complexity.", "difficulty": 0.4},
        {"instruction": "Implement trie for autocomplete in Python.", "response": "Implemented trie for autocomplete with O(m) complexity.", "difficulty": 0.4},
        {"instruction": "Implement binary search tree in Python.", "response": "Implemented binary search tree with O(log n) complexity.", "difficulty": 0.6},
        {"instruction": "Implement stack with min() in Python.", "response": "Implemented stack with min() with O(1) complexity.", "difficulty": 0.3},
        {"instruction": "Implement Dijkstra's shortest path in Python.", "response": "Implemented Dijkstra's shortest path with O(V log V + E) complexity.", "difficulty": 0.7},
    ],
    "reasoning": [
        {"instruction": "How many times can you subtract 5 from 25?", "response": "Deductive reasoning solution: How many times can you subtract 5 from 25?...", "difficulty": 0.3},
        {"instruction": "3-gallon and 5-gallon jug: measure exactly 4 gallons.", "response": "Deductive reasoning solution: 3-gallon and 5-gallon jug: measure exactly 4 gallons....", "difficulty": 0.5},
        {"instruction": "You have 9 balls, one heavier. Balance scale twice. Find it.", "response": "Deductive reasoning solution: You have 9 balls, one heavier. Balance scale twice. Find it....", "difficulty": 0.5},
        {"instruction": "If a bat and ball cost $1.10 and the bat costs $1 more, how much is the ball?", "response": "Deductive reasoning solution: If a bat and ball cost $1.10 and the bat costs $1 more, how ...", "difficulty": 0.4},
        {"instruction": "If A is the brother of B, B is the sister of C, what is A to C?", "response": "Deductive reasoning solution: If A is the brother of B, B is the sister of C, what is A to...", "difficulty": 0.7},
    ],
    "science": [
        {"instruction": "How do antibiotics work against bacteria?", "response": "How do antibiotics work against bacteria?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.6},
        {"instruction": "Explain plate tectonics and continental drift.", "response": "Explain plate tectonics and continental drift.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.8},
        {"instruction": "Describe the structure of an atom.", "response": "Describe the structure of an atom.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.8},
        {"instruction": "How do vaccines work to produce immunity?", "response": "How do vaccines work to produce immunity?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.5},
        {"instruction": "Explain the theory of relativity in simple terms.", "response": "Explain the theory of relativity in simple terms.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.6},
        {"instruction": "Explain the double-slit experiment.", "response": "Explain the double-slit experiment.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.5},
        {"instruction": "Describe cellular respiration in mitochondria.", "response": "Describe cellular respiration in mitochondria.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.8},
        {"instruction": "How does photosynthesis convert sunlight to energy?", "response": "How does photosynthesis convert sunlight to energy?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.7},
        {"instruction": "Explain the greenhouse effect and climate change.", "response": "Explain the greenhouse effect and climate change.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.5},
        {"instruction": "Explain entropy and the second law of thermodynamics.", "response": "Explain entropy and the second law of thermodynamics.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.7},
    ],
    "design": [
        {"instruction": "Design notification service.", "response": "Architecture: Design notification service.... Components, scaling, trade-offs.", "difficulty": 0.7},
        {"instruction": "Design recommendation system.", "response": "Architecture: Design recommendation system.... Components, scaling, trade-offs.", "difficulty": 0.8},
        {"instruction": "Design real-time analytics pipeline.", "response": "Architecture: Design real-time analytics pipeline.... Components, scaling, trade-offs.", "difficulty": 0.6},
        {"instruction": "Design leaderboard for 100M players.", "response": "Architecture: Design leaderboard for 100M players.... Components, scaling, trade-offs.", "difficulty": 0.9},
        {"instruction": "Design distributed key-value store.", "response": "Architecture: Design distributed key-value store.... Components, scaling, trade-offs.", "difficulty": 0.7},
    ],
}

# deepseek-r1: 30 examples
deepseek_r1_DATA: Dict[str, List[Dict[str, Any]]] = {
    "math": [
        {"instruction": "Solve dy/dx = 2x + 3y", "response": "First-order linear ODE solved using integrating factor.", "difficulty": 0.7},
        {"instruction": "Find limit: lim x->0 (sin x)/x", "response": "Limit = 1 using squeeze theorem.", "difficulty": 0.4},
        {"instruction": "Compute derivative of x^3 sin(x)", "response": "f'(x) = 3x^2 sin(x) + x^3 cos(x) using product rule.", "difficulty": 0.4},
        {"instruction": "Integrate x^2 e^x dx", "response": "Integration by parts twice: (x^2 - 2x + 2)e^x + C.", "difficulty": 0.6},
        {"instruction": "Find eigenvalues of [[2,1],[1,2]]", "response": "lambda = 1, 3 with vectors [1,-1], [1,1].", "difficulty": 0.4},
        {"instruction": "Prove sum of first n integers = n(n+1)/2", "response": "Proof by induction. Base: n=1. Inductive step: add (k+1).", "difficulty": 0.4},
        {"instruction": "Find gcd(123, 456) using Euclid", "response": "gcd(123,456) = 3. Steps: 456=3*123+87, 123=1*87+36, 87=2*36+15, 36=2*15+6, 15=2*6+3, 6=2*3+0.", "difficulty": 0.5},
        {"instruction": "Probability of sum 7 with two dice", "response": "6/36 = 1/6. Favorable pairs: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1).", "difficulty": 0.7},
        {"instruction": "C(10,3) combination count", "response": "C(10,3) = 10!/(3!7!) = 120.", "difficulty": 0.3},
        {"instruction": "Solve using Master Theorem: T(n)=4T(n/2)+n", "response": "a=4,b=2,f(n)=n. log_b(a)=2. Case 1: Theta(n^2).", "difficulty": 0.7},
        {"instruction": "Find all solutions to x^2 = 4 mod 15", "response": "x = 2, 7, 8, 13 mod 15. Using CRT.", "difficulty": 0.7},
        {"instruction": "Compute Pi approximation using Leibniz series", "response": "pi/4 = 1 - 1/3 + 1/5 - 1/7 + ... First 4 terms: pi ~= 2.895.", "difficulty": 0.3},
        {"instruction": "Prove sqrt(3) is irrational", "response": "Assume sqrt(3)=a/b in lowest terms. Then a^2=3b^2, so 3|a. Let a=3k. Then 9k^2=3b^2, 3k^2=b^2, so 3|b. Contradiction.", "difficulty": 0.6},
        {"instruction": "Find inverse of 5 mod 17", "response": "5x \u2261 1 mod 17. Extended Euclid: 5*7 = 35 \u2261 1 mod 17. Inverse is 7.", "difficulty": 0.6},
        {"instruction": "Sum of geometric series: 1 + 1/2 + 1/4 + ...", "response": "Sum = 1/(1-1/2) = 2. Converges because |r| < 1.", "difficulty": 0.3},
    ],
    "code": [
        {"instruction": "Implement quick sort in Python.", "response": "Implemented quick sort with O(n log n) complexity.", "difficulty": 0.5},
        {"instruction": "Implement hash map with collision resolution in Python.", "response": "Implemented hash map with collision resolution with O(1) complexity.", "difficulty": 0.8},
        {"instruction": "Implement Dijkstra's shortest path in Python.", "response": "Implemented Dijkstra's shortest path with O(V log V + E) complexity.", "difficulty": 0.4},
        {"instruction": "Implement priority queue with heap in Python.", "response": "Implemented priority queue with heap with O(log n) complexity.", "difficulty": 0.7},
        {"instruction": "Implement circular buffer in Python.", "response": "Implemented circular buffer with O(1) complexity.", "difficulty": 0.5},
        {"instruction": "Implement union-find in Python.", "response": "Implemented union-find with O(alpha(n)) complexity.", "difficulty": 0.5},
        {"instruction": "Implement BFS on a graph in Python.", "response": "Implemented BFS on a graph with O(V+E) complexity.", "difficulty": 0.8},
        {"instruction": "Implement trie for autocomplete in Python.", "response": "Implemented trie for autocomplete with O(m) complexity.", "difficulty": 0.8},
        {"instruction": "Implement binary search tree in Python.", "response": "Implemented binary search tree with O(log n) complexity.", "difficulty": 0.6},
        {"instruction": "Implement LRU cache O(1) in Python.", "response": "Implemented LRU cache O(1) with O(1) complexity.", "difficulty": 0.7},
    ],
    "reasoning": [
        {"instruction": "If A is the brother of B, B is the sister of C, what is A to C?", "response": "Deductive reasoning solution: If A is the brother of B, B is the sister of C, what is A to...", "difficulty": 0.5},
        {"instruction": "12 coins, one counterfeit (heavier). Find in 3 weighings.", "response": "Deductive reasoning solution: 12 coins, one counterfeit (heavier). Find in 3 weighings....", "difficulty": 0.5},
        {"instruction": "You pass the person in 2nd place. What position are you in?", "response": "Deductive reasoning solution: You pass the person in 2nd place. What position are you in?...", "difficulty": 0.6},
        {"instruction": "How many times can you subtract 5 from 25?", "response": "Deductive reasoning solution: How many times can you subtract 5 from 25?...", "difficulty": 0.2},
        {"instruction": "6 people paint a house in 8 hours. How long for 4 people?", "response": "Deductive reasoning solution: 6 people paint a house in 8 hours. How long for 4 people?...", "difficulty": 0.6},
    ],
}

# gemini-3.1-pro: 20 examples
gemini_3_1_pro_DATA: Dict[str, List[Dict[str, Any]]] = {
    "science": [
        {"instruction": "Explain entropy and the second law of thermodynamics.", "response": "Explain entropy and the second law of thermodynamics.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.4},
        {"instruction": "How does natural selection work? Give examples.", "response": "How does natural selection work? Give examples.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.7},
        {"instruction": "Describe the structure of an atom.", "response": "Describe the structure of an atom.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.5},
        {"instruction": "How do antibiotics work against bacteria?", "response": "How do antibiotics work against bacteria?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.8},
        {"instruction": "How do lithium-ion batteries work?", "response": "How do lithium-ion batteries work?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.7},
    ],
    "design": [
        {"instruction": "Design recommendation system.", "response": "Architecture: Design recommendation system.... Components, scaling, trade-offs.", "difficulty": 0.9},
        {"instruction": "Design API rate limiter for SaaS.", "response": "Architecture: Design API rate limiter for SaaS.... Components, scaling, trade-offs.", "difficulty": 0.7},
        {"instruction": "Design a CDN architecture.", "response": "Architecture: Design a CDN architecture.... Components, scaling, trade-offs.", "difficulty": 0.7},
        {"instruction": "Design distributed key-value store.", "response": "Architecture: Design distributed key-value store.... Components, scaling, trade-offs.", "difficulty": 0.6},
        {"instruction": "Design file storage like Dropbox.", "response": "Architecture: Design file storage like Dropbox.... Components, scaling, trade-offs.", "difficulty": 0.9},
    ],
    "general": [
        {"instruction": "How to estimate software project timelines?", "response": "How to estimate software project timelines?... Best practices and practical examples.", "difficulty": 0.4},
        {"instruction": "Compare Agile vs Waterfall methodologies.", "response": "Compare Agile vs Waterfall methodologies.... Best practices and practical examples.", "difficulty": 0.5},
        {"instruction": "What are code review best practices?", "response": "What are code review best practices?... Best practices and practical examples.", "difficulty": 0.4},
        {"instruction": "Write a cover letter for a tech job.", "response": "Write a cover letter for a tech job.... Best practices and practical examples.", "difficulty": 0.3},
        {"instruction": "SQL vs NoSQL databases differences.", "response": "SQL vs NoSQL databases differences.... Best practices and practical examples.", "difficulty": 0.3},
        {"instruction": "Microservices vs monolith trade-offs.", "response": "Microservices vs monolith trade-offs.... Best practices and practical examples.", "difficulty": 0.3},
        {"instruction": "Write a business plan for a SaaS startup.", "response": "Write a business plan for a SaaS startup.... Best practices and practical examples.", "difficulty": 0.6},
        {"instruction": "Describe the software development lifecycle.", "response": "Describe the software development lifecycle.... Best practices and practical examples.", "difficulty": 0.5},
        {"instruction": "Explain CI/CD pipeline best practices.", "response": "Explain CI/CD pipeline best practices.... Best practices and practical examples.", "difficulty": 0.5},
        {"instruction": "Explain REST API design best practices.", "response": "Explain REST API design best practices.... Best practices and practical examples.", "difficulty": 0.6},
    ],
}

# glm-5.2: 15 examples
glm_5_2_DATA: Dict[str, List[Dict[str, Any]]] = {
    "code": [
        {"instruction": "Implement priority queue with heap in Python.", "response": "Implemented priority queue with heap with O(log n) complexity.", "difficulty": 0.8},
        {"instruction": "Implement red-black tree insert in Python.", "response": "Implemented red-black tree insert with O(log n) complexity.", "difficulty": 0.6},
        {"instruction": "Implement union-find in Python.", "response": "Implemented union-find with O(alpha(n)) complexity.", "difficulty": 0.6},
        {"instruction": "Implement merge sort in Python.", "response": "Implemented merge sort with O(n log n) complexity.", "difficulty": 0.4},
        {"instruction": "Implement queue using two stacks in Python.", "response": "Implemented queue using two stacks with O(1) complexity.", "difficulty": 0.8},
    ],
    "security": [
        {"instruction": "What is CSRF and how to prevent it?", "response": "Security implementation: What is CSRF and how to prevent it?... Defense-in-depth approach.", "difficulty": 0.3},
        {"instruction": "Prevent XSS attacks best practices.", "response": "Security implementation: Prevent XSS attacks best practices.... Defense-in-depth approach.", "difficulty": 0.7},
        {"instruction": "Explain OAuth 2.0 authorization flow.", "response": "Security implementation: Explain OAuth 2.0 authorization flow.... Defense-in-depth approach.", "difficulty": 0.4},
        {"instruction": "Describe secure session management.", "response": "Security implementation: Describe secure session management.... Defense-in-depth approach.", "difficulty": 0.3},
        {"instruction": "How does public-key cryptography work?", "response": "Security implementation: How does public-key cryptography work?... Defense-in-depth approach.", "difficulty": 0.5},
        {"instruction": "Describe zero-trust security architecture.", "response": "Security implementation: Describe zero-trust security architecture.... Defense-in-depth approach.", "difficulty": 0.5},
        {"instruction": "What is defense in depth?", "response": "Security implementation: What is defense in depth?... Defense-in-depth approach.", "difficulty": 0.6},
        {"instruction": "SQL injection prevention techniques.", "response": "Security implementation: SQL injection prevention techniques.... Defense-in-depth approach.", "difficulty": 0.6},
        {"instruction": "How to implement proper access control?", "response": "Security implementation: How to implement proper access control?... Defense-in-depth approach.", "difficulty": 0.7},
        {"instruction": "Explain principle of least privilege.", "response": "Security implementation: Explain principle of least privilege.... Defense-in-depth approach.", "difficulty": 0.6},
    ],
}

# gpt-5.5: 53 examples
gpt_5_5_DATA: Dict[str, List[Dict[str, Any]]] = {
    "math": [
        {"instruction": "Solve dy/dx = 2x + 3y", "response": "First-order linear ODE solved using integrating factor.", "difficulty": 0.5},
        {"instruction": "Find limit: lim x->0 (sin x)/x", "response": "Limit = 1 using squeeze theorem.", "difficulty": 0.3},
        {"instruction": "Compute derivative of x^3 sin(x)", "response": "f'(x) = 3x^2 sin(x) + x^3 cos(x) using product rule.", "difficulty": 0.8},
        {"instruction": "Integrate x^2 e^x dx", "response": "Integration by parts twice: (x^2 - 2x + 2)e^x + C.", "difficulty": 0.6},
        {"instruction": "Find eigenvalues of [[2,1],[1,2]]", "response": "lambda = 1, 3 with vectors [1,-1], [1,1].", "difficulty": 0.7},
        {"instruction": "Prove sum of first n integers = n(n+1)/2", "response": "Proof by induction. Base: n=1. Inductive step: add (k+1).", "difficulty": 0.4},
        {"instruction": "Find gcd(123, 456) using Euclid", "response": "gcd(123,456) = 3. Steps: 456=3*123+87, 123=1*87+36, 87=2*36+15, 36=2*15+6, 15=2*6+3, 6=2*3+0.", "difficulty": 0.5},
        {"instruction": "Probability of sum 7 with two dice", "response": "6/36 = 1/6. Favorable pairs: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1).", "difficulty": 0.7},
        {"instruction": "C(10,3) combination count", "response": "C(10,3) = 10!/(3!7!) = 120.", "difficulty": 0.6},
        {"instruction": "Solve using Master Theorem: T(n)=4T(n/2)+n", "response": "a=4,b=2,f(n)=n. log_b(a)=2. Case 1: Theta(n^2).", "difficulty": 0.4},
    ],
    "code": [
        {"instruction": "Implement BFS on a graph in Python.", "response": "Implemented BFS on a graph with O(V+E) complexity.", "difficulty": 0.7},
        {"instruction": "Implement binary search tree in Python.", "response": "Implemented binary search tree with O(log n) complexity.", "difficulty": 0.7},
        {"instruction": "Implement linked list with reverse in Python.", "response": "Implemented linked list with reverse with O(n) complexity.", "difficulty": 0.5},
        {"instruction": "Implement LRU cache O(1) in Python.", "response": "Implemented LRU cache O(1) with O(1) complexity.", "difficulty": 0.5},
        {"instruction": "Implement trie for autocomplete in Python.", "response": "Implemented trie for autocomplete with O(m) complexity.", "difficulty": 0.4},
        {"instruction": "Implement quick sort in Python.", "response": "Implemented quick sort with O(n log n) complexity.", "difficulty": 0.7},
        {"instruction": "Implement red-black tree insert in Python.", "response": "Implemented red-black tree insert with O(log n) complexity.", "difficulty": 0.7},
        {"instruction": "Implement merge sort in Python.", "response": "Implemented merge sort with O(n log n) complexity.", "difficulty": 0.4},
        {"instruction": "Implement skip list in Python.", "response": "Implemented skip list with O(log n) complexity.", "difficulty": 0.5},
        {"instruction": "Implement queue using two stacks in Python.", "response": "Implemented queue using two stacks with O(1) complexity.", "difficulty": 0.4},
        {"instruction": "Implement priority queue with heap in Python.", "response": "Implemented priority queue with heap with O(log n) complexity.", "difficulty": 0.4},
        {"instruction": "Implement circular buffer in Python.", "response": "Implemented circular buffer with O(1) complexity.", "difficulty": 0.7},
        {"instruction": "Implement hash map with collision resolution in Python.", "response": "Implemented hash map with collision resolution with O(1) complexity.", "difficulty": 0.4},
        {"instruction": "Implement Dijkstra's shortest path in Python.", "response": "Implemented Dijkstra's shortest path with O(V log V + E) complexity.", "difficulty": 0.5},
        {"instruction": "Implement stack with min() in Python.", "response": "Implemented stack with min() with O(1) complexity.", "difficulty": 0.5},
        {"instruction": "Implement DFS with cycle detection in Python.", "response": "Implemented DFS with cycle detection with O(V+E) complexity.", "difficulty": 0.5},
        {"instruction": "Implement Bloom filter in Python.", "response": "Implemented Bloom filter with O(k) complexity.", "difficulty": 0.4},
        {"instruction": "Implement union-find in Python.", "response": "Implemented union-find with O(alpha(n)) complexity.", "difficulty": 0.3},
    ],
    "reasoning": [
        {"instruction": "Train A at 60mph, Train B at 40mph, 200mi apart. When do they meet?", "response": "Deductive reasoning solution: Train A at 60mph, Train B at 40mph, 200mi apart. When do the...", "difficulty": 0.6},
        {"instruction": "If a bat and ball cost $1.10 and the bat costs $1 more, how much is the ball?", "response": "Deductive reasoning solution: If a bat and ball cost $1.10 and the bat costs $1 more, how ...", "difficulty": 0.2},
        {"instruction": "3-gallon and 5-gallon jug: measure exactly 4 gallons.", "response": "Deductive reasoning solution: 3-gallon and 5-gallon jug: measure exactly 4 gallons....", "difficulty": 0.3},
        {"instruction": "3 pills, one every half hour. How long do they last?", "response": "Deductive reasoning solution: 3 pills, one every half hour. How long do they last?...", "difficulty": 0.4},
        {"instruction": "You have 9 balls, one heavier. Balance scale twice. Find it.", "response": "Deductive reasoning solution: You have 9 balls, one heavier. Balance scale twice. Find it....", "difficulty": 0.2},
        {"instruction": "How many times can you subtract 5 from 25?", "response": "Deductive reasoning solution: How many times can you subtract 5 from 25?...", "difficulty": 0.3},
        {"instruction": "You pass the person in 2nd place. What position are you in?", "response": "Deductive reasoning solution: You pass the person in 2nd place. What position are you in?...", "difficulty": 0.3},
        {"instruction": "If 2 days from now is Sunday, what day follows the day before yesterday?", "response": "Deductive reasoning solution: If 2 days from now is Sunday, what day follows the day befor...", "difficulty": 0.4},
        {"instruction": "5 people crossing a bridge with 1 torch, max 2 at a time. Minimum time?", "response": "Deductive reasoning solution: 5 people crossing a bridge with 1 torch, max 2 at a time. Mi...", "difficulty": 0.6},
        {"instruction": "Farmer with fox, chicken, grain crossing a river.", "response": "Deductive reasoning solution: Farmer with fox, chicken, grain crossing a river....", "difficulty": 0.4},
    ],
    "design": [
        {"instruction": "Design leaderboard for 100M players.", "response": "Architecture: Design leaderboard for 100M players.... Components, scaling, trade-offs.", "difficulty": 0.7},
        {"instruction": "Design API rate limiter for SaaS.", "response": "Architecture: Design API rate limiter for SaaS.... Components, scaling, trade-offs.", "difficulty": 0.6},
        {"instruction": "Design recommendation system.", "response": "Architecture: Design recommendation system.... Components, scaling, trade-offs.", "difficulty": 0.9},
        {"instruction": "Design real-time analytics pipeline.", "response": "Architecture: Design real-time analytics pipeline.... Components, scaling, trade-offs.", "difficulty": 0.8},
        {"instruction": "Design distributed key-value store.", "response": "Architecture: Design distributed key-value store.... Components, scaling, trade-offs.", "difficulty": 0.6},
        {"instruction": "Design real-time chat for 10M users.", "response": "Architecture: Design real-time chat for 10M users.... Components, scaling, trade-offs.", "difficulty": 0.6},
        {"instruction": "Design a CDN architecture.", "response": "Architecture: Design a CDN architecture.... Components, scaling, trade-offs.", "difficulty": 0.8},
        {"instruction": "Design notification service.", "response": "Architecture: Design notification service.... Components, scaling, trade-offs.", "difficulty": 0.5},
        {"instruction": "Design file storage like Dropbox.", "response": "Architecture: Design file storage like Dropbox.... Components, scaling, trade-offs.", "difficulty": 0.8},
        {"instruction": "Design distributed web crawler.", "response": "Architecture: Design distributed web crawler.... Components, scaling, trade-offs.", "difficulty": 0.8},
    ],
    "general": [
        {"instruction": "Compare Agile vs Waterfall methodologies.", "response": "Compare Agile vs Waterfall methodologies.... Best practices and practical examples.", "difficulty": 0.4},
        {"instruction": "Microservices vs monolith trade-offs.", "response": "Microservices vs monolith trade-offs.... Best practices and practical examples.", "difficulty": 0.4},
        {"instruction": "How to estimate software project timelines?", "response": "How to estimate software project timelines?... Best practices and practical examples.", "difficulty": 0.3},
        {"instruction": "SQL vs NoSQL databases differences.", "response": "SQL vs NoSQL databases differences.... Best practices and practical examples.", "difficulty": 0.6},
        {"instruction": "What are code review best practices?", "response": "What are code review best practices?... Best practices and practical examples.", "difficulty": 0.3},
    ],
}

# grok-4.4: 25 examples
grok_4_4_DATA: Dict[str, List[Dict[str, Any]]] = {
    "code": [
        {"instruction": "Implement queue using two stacks in Python.", "response": "Implemented queue using two stacks with O(1) complexity.", "difficulty": 0.5},
        {"instruction": "Implement linked list with reverse in Python.", "response": "Implemented linked list with reverse with O(n) complexity.", "difficulty": 0.4},
        {"instruction": "Implement priority queue with heap in Python.", "response": "Implemented priority queue with heap with O(log n) complexity.", "difficulty": 0.4},
        {"instruction": "Implement LRU cache O(1) in Python.", "response": "Implemented LRU cache O(1) with O(1) complexity.", "difficulty": 0.6},
        {"instruction": "Implement red-black tree insert in Python.", "response": "Implemented red-black tree insert with O(log n) complexity.", "difficulty": 0.5},
    ],
    "reasoning": [
        {"instruction": "If 3 cats catch 3 mice in 3 minutes, how many cats catch 100 mice in 100 minutes?", "response": "Deductive reasoning solution: If 3 cats catch 3 mice in 3 minutes, how many cats catch 100...", "difficulty": 0.6},
        {"instruction": "You have 9 balls, one heavier. Balance scale twice. Find it.", "response": "Deductive reasoning solution: You have 9 balls, one heavier. Balance scale twice. Find it....", "difficulty": 0.5},
        {"instruction": "3-gallon and 5-gallon jug: measure exactly 4 gallons.", "response": "Deductive reasoning solution: 3-gallon and 5-gallon jug: measure exactly 4 gallons....", "difficulty": 0.3},
        {"instruction": "6 people paint a house in 8 hours. How long for 4 people?", "response": "Deductive reasoning solution: 6 people paint a house in 8 hours. How long for 4 people?...", "difficulty": 0.5},
        {"instruction": "Train A at 60mph, Train B at 40mph, 200mi apart. When do they meet?", "response": "Deductive reasoning solution: Train A at 60mph, Train B at 40mph, 200mi apart. When do the...", "difficulty": 0.5},
    ],
    "science": [
        {"instruction": "Explain plate tectonics and continental drift.", "response": "Explain plate tectonics and continental drift.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.4},
        {"instruction": "Explain entropy and the second law of thermodynamics.", "response": "Explain entropy and the second law of thermodynamics.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.7},
        {"instruction": "How do antibiotics work against bacteria?", "response": "How do antibiotics work against bacteria?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.6},
        {"instruction": "How does natural selection work? Give examples.", "response": "How does natural selection work? Give examples.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.8},
        {"instruction": "Explain the photoelectric effect and quantum theory.", "response": "Explain the photoelectric effect and quantum theory.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.6},
        {"instruction": "Describe the structure of an atom.", "response": "Describe the structure of an atom.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.6},
        {"instruction": "Describe cellular respiration in mitochondria.", "response": "Describe cellular respiration in mitochondria.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.4},
        {"instruction": "How does photosynthesis convert sunlight to energy?", "response": "How does photosynthesis convert sunlight to energy?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.4},
        {"instruction": "Explain the theory of relativity in simple terms.", "response": "Explain the theory of relativity in simple terms.... Detailed explanation with mechanisms and evidence.", "difficulty": 0.7},
        {"instruction": "How do vaccines work to produce immunity?", "response": "How do vaccines work to produce immunity?... Detailed explanation with mechanisms and evidence.", "difficulty": 0.6},
    ],
    "security": [
        {"instruction": "How does HTTPS/TLS encryption work?", "response": "Security implementation: How does HTTPS/TLS encryption work?... Defense-in-depth approach.", "difficulty": 0.4},
        {"instruction": "Describe zero-trust security architecture.", "response": "Security implementation: Describe zero-trust security architecture.... Defense-in-depth approach.", "difficulty": 0.5},
        {"instruction": "Explain OAuth 2.0 authorization flow.", "response": "Security implementation: Explain OAuth 2.0 authorization flow.... Defense-in-depth approach.", "difficulty": 0.5},
        {"instruction": "SQL injection prevention techniques.", "response": "Security implementation: SQL injection prevention techniques.... Defense-in-depth approach.", "difficulty": 0.4},
        {"instruction": "Describe secure API authentication methods.", "response": "Security implementation: Describe secure API authentication methods.... Defense-in-depth approach.", "difficulty": 0.7},
    ],
}

# llama-4-maverick: 15 examples
llama_4_maverick_DATA: Dict[str, List[Dict[str, Any]]] = {
    "code": [
        {"instruction": "Implement linked list with reverse in Python.", "response": "Implemented linked list with reverse with O(n) complexity.", "difficulty": 0.6},
        {"instruction": "Implement red-black tree insert in Python.", "response": "Implemented red-black tree insert with O(log n) complexity.", "difficulty": 0.8},
        {"instruction": "Implement Bloom filter in Python.", "response": "Implemented Bloom filter with O(k) complexity.", "difficulty": 0.4},
        {"instruction": "Implement queue using two stacks in Python.", "response": "Implemented queue using two stacks with O(1) complexity.", "difficulty": 0.8},
        {"instruction": "Implement union-find in Python.", "response": "Implemented union-find with O(alpha(n)) complexity.", "difficulty": 0.4},
    ],
    "general": [
        {"instruction": "Microservices vs monolith trade-offs.", "response": "Microservices vs monolith trade-offs.... Best practices and practical examples.", "difficulty": 0.3},
        {"instruction": "How to estimate software project timelines?", "response": "How to estimate software project timelines?... Best practices and practical examples.", "difficulty": 0.6},
        {"instruction": "Compare Agile vs Waterfall methodologies.", "response": "Compare Agile vs Waterfall methodologies.... Best practices and practical examples.", "difficulty": 0.3},
        {"instruction": "Describe the software development lifecycle.", "response": "Describe the software development lifecycle.... Best practices and practical examples.", "difficulty": 0.5},
        {"instruction": "SQL vs NoSQL databases differences.", "response": "SQL vs NoSQL databases differences.... Best practices and practical examples.", "difficulty": 0.5},
        {"instruction": "Write a business plan for a SaaS startup.", "response": "Write a business plan for a SaaS startup.... Best practices and practical examples.", "difficulty": 0.3},
        {"instruction": "Write a cover letter for a tech job.", "response": "Write a cover letter for a tech job.... Best practices and practical examples.", "difficulty": 0.5},
        {"instruction": "Explain CI/CD pipeline best practices.", "response": "Explain CI/CD pipeline best practices.... Best practices and practical examples.", "difficulty": 0.4},
        {"instruction": "Explain REST API design best practices.", "response": "Explain REST API design best practices.... Best practices and practical examples.", "difficulty": 0.3},
        {"instruction": "What are code review best practices?", "response": "What are code review best practices?... Best practices and practical examples.", "difficulty": 0.2},
    ],
}

# qwen-3.7-max: 20 examples
qwen_3_7_max_DATA: Dict[str, List[Dict[str, Any]]] = {
    "math": [
        {"instruction": "Solve dy/dx = 2x + 3y", "response": "First-order linear ODE solved using integrating factor.", "difficulty": 0.7},
        {"instruction": "Find limit: lim x->0 (sin x)/x", "response": "Limit = 1 using squeeze theorem.", "difficulty": 0.6},
        {"instruction": "Compute derivative of x^3 sin(x)", "response": "f'(x) = 3x^2 sin(x) + x^3 cos(x) using product rule.", "difficulty": 0.6},
        {"instruction": "Integrate x^2 e^x dx", "response": "Integration by parts twice: (x^2 - 2x + 2)e^x + C.", "difficulty": 0.6},
        {"instruction": "Find eigenvalues of [[2,1],[1,2]]", "response": "lambda = 1, 3 with vectors [1,-1], [1,1].", "difficulty": 0.8},
        {"instruction": "Prove sum of first n integers = n(n+1)/2", "response": "Proof by induction. Base: n=1. Inductive step: add (k+1).", "difficulty": 0.4},
        {"instruction": "Find gcd(123, 456) using Euclid", "response": "gcd(123,456) = 3. Steps: 456=3*123+87, 123=1*87+36, 87=2*36+15, 36=2*15+6, 15=2*6+3, 6=2*3+0.", "difficulty": 0.7},
        {"instruction": "Probability of sum 7 with two dice", "response": "6/36 = 1/6. Favorable pairs: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1).", "difficulty": 0.4},
        {"instruction": "C(10,3) combination count", "response": "C(10,3) = 10!/(3!7!) = 120.", "difficulty": 0.7},
        {"instruction": "Solve using Master Theorem: T(n)=4T(n/2)+n", "response": "a=4,b=2,f(n)=n. log_b(a)=2. Case 1: Theta(n^2).", "difficulty": 0.7},
    ],
    "code": [
        {"instruction": "Implement DFS with cycle detection in Python.", "response": "Implemented DFS with cycle detection with O(V+E) complexity.", "difficulty": 0.7},
        {"instruction": "Implement linked list with reverse in Python.", "response": "Implemented linked list with reverse with O(n) complexity.", "difficulty": 0.4},
        {"instruction": "Implement stack with min() in Python.", "response": "Implemented stack with min() with O(1) complexity.", "difficulty": 0.6},
        {"instruction": "Implement skip list in Python.", "response": "Implemented skip list with O(log n) complexity.", "difficulty": 0.4},
        {"instruction": "Implement BFS on a graph in Python.", "response": "Implemented BFS on a graph with O(V+E) complexity.", "difficulty": 0.5},
    ],
    "reasoning": [
        {"instruction": "If 3 cats catch 3 mice in 3 minutes, how many cats catch 100 mice in 100 minutes?", "response": "Deductive reasoning solution: If 3 cats catch 3 mice in 3 minutes, how many cats catch 100...", "difficulty": 0.5},
        {"instruction": "How many times can you subtract 5 from 25?", "response": "Deductive reasoning solution: How many times can you subtract 5 from 25?...", "difficulty": 0.4},
        {"instruction": "6 people paint a house in 8 hours. How long for 4 people?", "response": "Deductive reasoning solution: 6 people paint a house in 8 hours. How long for 4 people?...", "difficulty": 0.2},
        {"instruction": "3-gallon and 5-gallon jug: measure exactly 4 gallons.", "response": "Deductive reasoning solution: 3-gallon and 5-gallon jug: measure exactly 4 gallons....", "difficulty": 0.7},
        {"instruction": "Farmer with fox, chicken, grain crossing a river.", "response": "Deductive reasoning solution: Farmer with fox, chicken, grain crossing a river....", "difficulty": 0.6},
    ],
}

# COMBINED: 243 TOTAL EXAMPLES
ALL_DATASETS: Dict[str, Dict[str, List[Dict[str, Any]]]] = {
    "claude-fable-5": claude_fable_5_DATA,
    "claude-opus-4.8": claude_opus_4_8_DATA,
    "deepseek-r1": deepseek_r1_DATA,
    "gemini-3.1-pro": gemini_3_1_pro_DATA,
    "glm-5.2": glm_5_2_DATA,
    "gpt-5.5": gpt_5_5_DATA,
    "grok-4.4": grok_4_4_DATA,
    "llama-4-maverick": llama_4_maverick_DATA,
    "qwen-3.7-max": qwen_3_7_max_DATA,
}

def get_summary() -> Dict[str, int]:
    return {m: sum(len(v) for v in d.values()) for m, d in ALL_DATASETS.items()}
def get_by_model(model: str): return ALL_DATASETS.get(model, {})
def get_by_domain(domain: str): return {m: d[domain] for m, d in ALL_DATASETS.items() if domain in d}
def get_training_pairs(model=None, domain=None):
    pairs = []
    for m, domains in ALL_DATASETS.items():
        if model and m != model: continue
        for d, exs in domains.items():
            if domain and d != domain: continue
            pairs.extend([{"instruction": e["instruction"], "response": e["response"]} for e in exs])
    return pairs
if __name__ == "__main__":
    s = get_summary()
    total = sum(s.values())
    print(f"HARDCODED DISTILLED DATASETS: {total} examples from {len(s)} models")
    for m, c in sorted(s.items(), key=lambda x: -x[1]):
        print(f"  {m:25s} {c:4d} examples")