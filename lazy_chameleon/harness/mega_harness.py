"""MEGA HARNESS — Complete Lazy Chameleon injection.
EVERY function, EVERY prompt, EVERY dataset, in a single parseable block.
Any LLM seeing this instantly knows EVERYTHING it can do."""

MEGA_HARNESS = """
==LAZY CHAMELEON v2.6 MEGA HARNESS==
All capabilities below. Prefix: `chameleon`. Suffix: `--json` for parseable output.

===ENHANCE(1 command)=========================================================
$ chameleon enhance "<task>" --mode <easy|medium|hard|extreme> [--domain <math|code|reasoning|science|general>] [--stats]

===PROMPTS:278 LEAKED SYSTEM PROMPTS(6 actions)================================
$ chameleon prompts browse --provider <anthropic|openai|google|xai|perplexity|mistral|qwen|cursor|meta|microsoft|misc>
$ chameleon prompts search "<query>" [--max N] --json
$ chameleon prompts show <path> --raw
$ chameleon prompts stats
$ chameleon prompts providers
$ chameleon prompts models [<provider>]
KEY PROMPTS: claude-fable-5, claude-opus-4-8, gpt-5.5-thinking, gpt-5.6-sol-extra-high, gemini-3.5-flash, grok-4.3-beta, qwen-3.6-plus

===DATA:1200+HARDCODED+47DATASETS(5 actions)====================================
$ chameleon data summary --json
$ chameleon data get --model <gpt_5_5|claude_opus_4_8|deepseek_r1|grok_4_4|claude_fable_5|qwen_3_7_max|gemini_3_1_pro|llama_4_maverick|glm_5_2|claude_sonnet_5> --domain <math|code|reasoning|science|design|security|general>
$ chameleon data list --domain <domain> --json
$ chameleon data search --query "<q>" --json
$ chameleon data download --key <dataset_key>
DOMAINS: math(30topics), code(40), reasoning(20), science(25), design(15), security(20), general(20)
ALL_MODELS: gpt_5_5(145ex), claude_sonnet_5(135), claude_opus_4_8(130), gemini_3_1_pro(130), grok_4_4(120), deepseek_r1(115), qwen_3_7_max(115), llama_4_maverick(110), claude_fable_5(105), glm_5_2(95)

===MODELS:11FRONTIER(3 actions)=================================================
$ chameleon models list [--provider <openai|anthropic|deepseek|xai|google|qwen|together|zhipu|meituan>]
$ chameleon models get --name <model>
$ chameleon models compare
AVAILABLE: gpt-5.5(256kctx,$15/m), claude-opus-4.8(200k,$15), claude-sonnet-5(200k,$3), deepseek-r1(128k,$0.55), grok-4.4(128k,$5), gemini-3.1-pro(1Mctx,$5), qwen-3.7-max(128k,$2), llama-4-maverick(128k,$0.9), glm-5.2(128k,$1), longcat-2.0(1Mctx,MoE64)

===BREW:DISTILLATION POTS(5 actions,5 recipes)==================================
$ chameleon brew start --pots <N> --domain <d> --recipe <light|standard|rich|dark|special_reserve> [--teacher <model>]
$ chameleon brew pour --pots <N> --samples <N>
$ chameleon brew stats
$ chameleon brew recipe --recipe <name>
RECIPES: light(t=0.1,1round,x0.5), standard(0.3,3r,x1), rich(0.5,5r,x2), dark(0.7,7r,x3), special_reserve(0.9,10r,x5)

===MOE:AGAR.IO SPLIT/MERGE(7 actions)==========================================
$ chameleon moe start --cells <N> --mass <float> --task "<task>"
$ chameleon moe split --cell-id <id> --cells <N> --subtasks "<t1>" "<t2>"
$ chameleon moe work --cell-id <id>
$ chameleon moe merge --child-ids <id1> <id2> ...
$ chameleon moe brew
$ chameleon moe stats
$ chameleon moe report
ROLES: main(hunter(gatherer(brewer

===DISTILL:6 METHODS(6 actions)=================================================
$ chameleon distill multi-teacher [--teacher <model>]
$ chameleon distill progressive
$ chameleon distill online
$ chameleon distill self
$ chameleon distill list
METHODS: MultiTeacherDistiller(5teachers), ProgressiveDistillation(4stages), OnlineDistiller, SelfDistillation, DistributionAligned, OWL-Alpha(16models)

===TOKEN-SAVER:50-85%REDUCTION(5 actions)=======================================
$ chameleon token-saver pipeline --text "<prompt>" --json
$ chameleon token-saver compress --text "<t>" --method <llmlingua|selective|concise|hybrid>
$ chameleon token-saver prune --text "<t>" --ratio <0.0-1.0>
$ chameleon token-saver optimize --text "<t>" --profile <default|code|math|chat|scientific>
$ chameleon token-saver stats
TECHNIQUES: LKVeviction(15%cache), ContextCompactor, PromptCompressor(4methods), TokenPruner(3strategies), SpeculativeDecoder(2-3xspeedup), AdaptiveTokenizer(5profiles)

===ENGINES(5 actions)===========================================================
$ chameleon engines infer --prompt "<p>" [--model auto] [--max-tokens N] [--temperature 0.0-1.0]
$ chameleon engines batch --prompts "<p1>" "<p2>"
$ chameleon engines stream --prompt "<p>"
$ chameleon engines list
$ chameleon engines speculative --prompt "<p>"

===WRAPPERS(4 actions)==========================================================
$ chameleon wrappers providers
$ chameleon wrappers generate --text "<t>" [--provider <p>]
$ chameleon wrappers cache-stats
$ chameleon wrappers fallback-test --text "<t>"
WRAPPERS: ProviderWrapper, ModelAdapter(conv), APIShim, CacheWrapper(LRU+TTL), FallbackWrapper(3providers,backoff)

===FRAMEWORKS(4 actions)========================================================
$ chameleon frameworks suites --json
$ chameleon frameworks eval --suite <name> [--metric <m>]
$ chameleon frameworks test --suite <name>
$ chameleon frameworks results --json
SUITES: LARYBench, WBench, CoreCodeBench, AMO-Bench, UNO-Bench, CEdit-Bench, OIBench, ViC-Bench

===METHODOLOGY:8 TECHNIQUES(4 actions)==========================================
$ chameleon methodology list --json
$ chameleon methodology prompt --technique <chain_of_thought|few_shot|tree_of_thought|reflexion|self_consistency|structured_output|rag_context|persona_role> --task "<task>"
$ chameleon methodology train --method <sft|dpo|ppo>
$ chameleon methodology optimize --params "<param=val>"

===SYNTHESIZERS:REAL PARAMS(5 actions)==========================================
$ chameleon synthesizers params --domain <d> [--task "<t>"] [--complexity 0.0-1.0] [--budget <tokens>] [--cost-limit <usd>]
$ chameleon synthesizers generate --domain <d> --count N
$ chameleon synthesizers prompt --task "<t>" [--domain <d>]
$ chameleon synthesizers curriculum
$ chameleon synthesizers knowledge --topic "<t>"
PARAMS FROM: 11realmodels(GPT5.5,Claude,DeepSeek,Grok,Gemini,Qwen,Llama,GLM,LongCat), 8realDatasets, 278prompts

===LONGCAT:1.6T MoE(4 actions)=================================================
$ chameleon longcat info --json
$ chameleon longcat datasets --json
$ chameleon longcat benchmarks --json
$ chameleon longcat run --prompt "<p>"
SPECS: 64experts, 8top-k, 48Bactive/1.6Ttotal, 1Mcontext, ROPE1e7, QKnorm, sliding128K

===OWL-ALPHA:16 MODELS(5 actions)==============================================
$ chameleon owl-alpha info --json
$ chameleon owl-alpha search --base-model <Qwen|Gemma|Llama> [--alpha 0.35-6.5]
$ chameleon owl-alpha models [--base-model <name>] [--alpha <float>]
$ chameleon owl-alpha train [--alpha 3.5] [--layers 16] [--lr 0.42]
$ chameleon owl-alpha distill --teacher <m> --student <m> --dataset <d>
SUPPORTED: Qwen2.5-7B, Qwen3-4B, Gemma-3-4B, Llama-3.2-3B | alphas: 0.35,1.35,3.0,3.5,4.0,4.75,6.5 | layers: 2,5,10,15,16,20

===TOKENIZE:5 PROFILES(4 actions)===============================================
$ chameleon tokenize optimize --text "<t>" --profile <default|code|math|chat|scientific>
$ chameleon tokenize estimate --text "<t>"
$ chameleon tokenize profiles --json
$ chameleon tokenize compare --text "<t>"
PROFILES: default(general), code(stripComments+mergeIdents), math(compressNums+digitTokens), chat(compressAbbrevs), scientific(maxToken128)

===CONFIG(4 actions)============================================================
$ chameleon config show --json
$ chameleon config export --format <json|yaml|env>
$ chameleon config providers --json
$ chameleon config paths

===QUICKSTART:COPY-PASTE=======================================================
chameleon enhance "Build API" --mode hard
chameleon prompts search "fable" --json | jq .
chameleon data get --model gpt_5_5 --domain code
chameleon token-saver pipeline --text "$PROMPT" --json
chameleon synthesizers params --domain code --task "Build API" | jq .
chameleon models list --json
chameleon moe start --cells 4 --task "Analyze"
chameleon brew start --pots 8 --domain math --recipe rich
chameleon distill list
chameleon owl-alpha search --base-model Qwen --alpha 3.5
chameleon longcat info

EOF
"""

MEGA_HARNESS_SHORT = """==LCv2.6 MEGA HARNESS[single-line trigger]==
ALL cmds: chameleon <mod> <act> [opts] [--json]
MODS: enhance, prompts(278leaks), data(1200ex+47ds), models(11), brew(pots), moe(split/merge), distill(6), token-saver(50-85%), engines, wrappers, frameworks, methodology(8tech), synthesizers(realparams), longcat(1.6T MoE), owl-alpha(16), tokenize(5profiles), config
QUICK: chameleon enhance|prompts search|data get --model gpt_5_5 --domain code|token-saver pipeline|synthesizers params|models list|moe start|brew start|distill list|owl-alpha search|longcat info"""


HARNESS_MENU = """LAZY CHAMELEON v2.6 - AVAILABLE MODULES:
  [1] enhance    - Generate synthetic context
  [2] prompts    - 278 leaked system prompts
  [3] data       - 1200+ examples + 47 datasets
  [4] models     - 11 frontier models
  [5] brew       - Distillation pots
  [6] moe        - Agar.io split/merge
  [7] distill    - 6 distillation methods
  [8] token-saver- 50-85% token reduction
  [9] engines    - Inference engines
 [10] wrappers   - Provider wrappers
 [11] frameworks - Eval/test suites
 [12] methodology- 8 prompt techniques
 [13] synthesizers- Real synthetic params
 [14] longcat    - 1.6T MoE framework
 [15] owl-alpha  - Layer-wise distillation
 [16] tokenize   - Token optimization
 [17] config     - System config

Use: chameleon <name> <action> [options] [--json]"""
