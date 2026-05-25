#!/usr/bin/env python3
"""Compile the master IELTS vocabulary wordlist - v2 with IELTS 4000."""

import os
import re

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORD_DIR = os.path.join(PROJECT_DIR, "wordbook")

# ============================================================
# 1. AWL 570 - Complete Academic Word List (Coxhead 2000)
# ============================================================
AWL = {
    1: ["analyse", "approach", "area", "assess", "assume", "authority", "available",
        "benefit", "concept", "consist", "constitute", "context", "contract", "create",
        "data", "define", "derive", "distribute", "economy", "environment", "establish",
        "estimate", "evident", "export", "factor", "finance", "formula", "function",
        "identify", "income", "indicate", "individual", "interpret", "involve", "issue",
        "labour", "legal", "legislate", "major", "method", "occur", "percent", "period",
        "policy", "principle", "proceed", "process", "require", "research", "respond",
        "role", "section", "sector", "significant", "similar", "source", "specific",
        "structure", "theory", "vary"],
    2: ["achieve", "acquire", "administrate", "affect", "appropriate", "aspect",
        "assist", "category", "chapter", "commission", "community", "complex",
        "compute", "conclude", "conduct", "consequent", "construct", "consume",
        "credit", "culture", "design", "distinct", "element", "equate", "evaluate",
        "feature", "final", "focus", "impact", "injure", "institute", "invest",
        "item", "journal", "maintain", "normal", "obtain", "participate", "perceive",
        "positive", "potential", "previous", "primary", "purchase", "range", "region",
        "regulate", "relevant", "reside", "resource", "restrict", "secure", "seek",
        "select", "site", "strategy", "survey", "text", "tradition", "transfer"],
    3: ["alternative", "circumstance", "comment", "compensate", "component", "consent",
        "considerable", "constant", "constrain", "contribute", "convention", "coordinate",
        "core", "corporate", "correspond", "criteria", "deduce", "demonstrate",
        "document", "dominate", "emphasis", "ensure", "exclude", "framework", "fund",
        "illustrate", "immigrate", "imply", "initial", "instance", "interact", "justify",
        "layer", "link", "locate", "maximise", "minor", "negate", "outcome", "partner",
        "philosophy", "physical", "proportion", "publish", "react", "register", "rely",
        "remove", "scheme", "sequence", "sex", "shift", "specify", "sufficient", "task",
        "technical", "technique", "technology", "valid", "volume"],
    4: ["access", "adequate", "annual", "apparent", "approximate", "attitude",
        "attribute", "civil", "code", "commit", "communicate", "concentrate", "confer",
        "contrast", "cycle", "debate", "despite", "dimension", "domestic", "emerge",
        "error", "ethnic", "goal", "grant", "hence", "hypothesis", "implement",
        "implicate", "impose", "integrate", "internal", "investigate", "job", "label",
        "mechanism", "obvious", "occupy", "option", "output", "parallel", "parameter",
        "phase", "predict", "principal", "prior", "professional", "project", "promote",
        "regime", "resolve", "retain", "series", "statistic", "status", "stress",
        "subsequent", "sum", "summary", "undertake"],
    5: ["academy", "adjust", "alter", "amend", "aware", "capacity", "challenge",
        "clause", "compound", "conflict", "consult", "contact", "decline", "discrete",
        "draft", "enable", "energy", "enforce", "entity", "equivalent", "evolve",
        "expand", "expose", "external", "facilitate", "fundamental", "generate",
        "generation", "image", "liberal", "licence", "logic", "margin", "medical",
        "mental", "modify", "monitor", "network", "notion", "objective", "orient",
        "perspective", "precise", "prime", "psychology", "pursue", "ratio", "reject",
        "revenue", "stable", "style", "substitute", "sustain", "symbol", "target",
        "transit", "trend", "version", "welfare", "whereas"],
    6: ["abstract", "accurate", "acknowledge", "aggregate", "allocate", "assign",
        "attach", "author", "bond", "brief", "capable", "cite", "cooperate",
        "discriminate", "display", "diverse", "domain", "edit", "enhance", "estate",
        "exceed", "expert", "explicit", "federal", "fee", "flexible", "furthermore",
        "gender", "ignorance", "incentive", "incidence", "incorporate", "index",
        "inhibit", "input", "instruct", "intelligence", "interval", "lecture", "migrate",
        "minimum", "ministry", "motive", "neutral", "nevertheless", "overseas", "precede",
        "presume", "rational", "recover", "reveal", "scope", "subsidiary", "tape",
        "trace", "transform", "transport", "underlie", "utilise", "vision"],
    7: ["adapt", "adult", "advocate", "aid", "channel", "chemical", "classic",
        "comprehensive", "comprise", "confirm", "contrary", "convert", "couple",
        "decade", "definite", "deny", "differentiate", "dispose", "dynamic", "eliminate",
        "empirical", "equip", "extract", "file", "finite", "foundation", "globe",
        "grade", "guarantee", "hierarchy", "identical", "ideology", "infer", "innovate",
        "insert", "intervene", "isolate", "media", "mode", "paragraph", "phenomenon",
        "priority", "prohibit", "publication", "quotation", "release", "reverse",
        "simulate", "sole", "somewhat", "submit", "successor", "survive", "thesis",
        "topic", "transmit", "ultimate", "unique", "visible", "voluntary"],
    8: ["abandon", "accompany", "accumulate", "ambiguous", "append", "appreciate",
        "arbitrary", "automate", "bias", "chart", "clarify", "commodity", "complement",
        "conform", "contemporary", "contradict", "crucial", "currency", "denote",
        "detect", "deviate", "displace", "drama", "eventual", "exhibit", "exploit",
        "fluctuate", "guideline", "highlight", "implicit", "induce", "inevitable",
        "infrastructure", "inspect", "intense", "manipulate", "minimise", "nuclear",
        "offset", "plus", "practitioner", "predominantly", "prospect", "radical",
        "random", "reinforce", "restore", "revise", "schedule", "tense", "terminate",
        "theme", "thereby", "uniform", "vehicle", "via", "virtual", "visual", "widespread"],
    9: ["accommodate", "analogy", "anticipate", "assure", "attain", "behalf", "bulk",
        "cease", "coherent", "coincide", "commence", "compatible", "concurrent",
        "confine", "controversy", "converse", "device", "devote", "diminish", "distort",
        "duration", "erode", "ethic", "format", "found", "inherent", "insight",
        "integral", "intermediate", "manual", "mature", "mediate", "medium", "military",
        "minimal", "mutual", "norm", "overlap", "passive", "portion", "preliminary",
        "protocol", "qualitative", "refine", "relax", "restrain", "revolution", "rigid",
        "route", "scenario", "sphere", "subordinate", "supplement", "suspend", "team",
        "temporary", "trigger", "unify", "violate", "vision"],
    10: ["adjacent", "albeit", "assemble", "collapse", "colleague", "compile", "conceive",
         "convince", "depress", "encounter", "enormous", "forthcoming", "incline",
         "integrity", "intrinsic", "invoke", "levy", "likewise", "nonetheless",
         "notwithstanding", "odd", "ongoing", "panel", "persist", "pose", "reluctance",
         "so-called", "straightforward", "undergo", "whereby"],
}

# ============================================================
# 2. IELTS Topic Vocabulary
# ============================================================
TOPIC_VOCAB = [
    "curriculum", "pedagogy", "literacy", "enrol", "attainment", "compulsory",
    "scholarship", "dissertation", "vocational", "syllabus", "academic", "tuition",
    "discipline", "cognitive", "assessment", "collaborate", "autonomous", "proficiency",
    "undergraduate", "postgraduate", "innate", "competence", "seminar", "plagiarism",
    "dropout", "extracurricular", "stimulate", "aptitude", "prerequisite", "accreditation",
    "inclusive", "empirical", "nurture", "holistic", "tertiary", "disparity",
    "benchmark", "rote", "sustainability", "biodiversity", "emissions", "renewable",
    "deforestation", "ecosystem", "contamination", "conservation", "drought", "erosion",
    "habitat", "pollutant", "biodegradable", "endangered", "glacier", "ozone", "recycle",
    "toxic", "flora", "fauna", "greenhouse", "pesticide", "preservation", "smog",
    "aquifer", "afforestation", "ecological", "degradation", "sustainable", "carbon",
    "automation", "cybersecurity", "algorithm", "innovation", "obsolete", "surveillance",
    "bandwidth", "encryption", "biotechnology", "connectivity", "proliferation",
    "streamline", "misinformation", "epidemic", "sedentary", "diagnosis", "preventive",
    "malnutrition", "rehabilitation", "wellbeing", "chronic", "vaccination", "obesity",
    "sanitation", "pharmaceutical", "immunity", "therapy", "pandemic", "contagious",
    "hygiene", "prognosis", "deterrent", "offender", "recidivism", "incarceration",
    "juvenile", "verdict", "legislation", "prosecution", "custody", "delinquency",
    "probation", "fraud", "corruption", "penalty", "parole", "litigation", "tribunal",
    "vandalism", "homicide", "acquit", "accomplice", "statute", "jurisdiction", "plea",
    "manslaughter", "burglary", "embezzlement", "reoffend", "unemployment", "productivity",
    "recession", "inflation", "entrepreneur", "commodity", "outsource", "downturn",
    "surplus", "deficit", "subsidiary", "monopoly", "freelance", "redundancy",
    "remuneration", "turnover", "diversify", "procurement", "fiscal", "depreciation",
    "austerity", "subsidy", "tariff", "stakeholder", "merger", "privatisation",
    "democracy", "bureaucracy", "sovereignty", "referendum", "constitution", "welfare",
    "accountability", "transparency", "diplomacy", "sanction", "ratify", "census",
    "constituency", "devolution", "mandate", "coalition", "propaganda", "embargo",
    "totalitarian", "autocracy", "bilateral", "geopolitical", "governance", "electorate",
    "regulation", "broadcast", "censorship", "tabloid", "editorial", "sensationalism",
    "circulation", "paparazzi", "defamation", "headline", "columnist", "clickbait",
    "disinformation", "viral", "subscription", "podcast", "influencer", "whistleblower",
    "rhetoric", "libel", "objectivity", "satire", "variable", "correlation",
    "methodology", "synthesis", "paradigm", "quantitative", "specimen", "replicate",
    "longitudinal", "anomaly", "catalyst", "theorem", "spectrum", "molecule", "genome",
    "prototype", "patent", "breakthrough", "urbanisation", "congestion", "suburb",
    "metropolitan", "gentrification", "slum", "commute", "overpopulation", "migration",
    "pedestrian", "regeneration", "zoning", "density", "sprawl", "tenancy", "landlord",
    "homelessness", "megacity", "globalisation", "multinational", "integration",
    "interdependence", "protectionism", "liberalisation", "homogenisation", "remittance",
    "exploitation", "diaspora", "indigenous", "colonialism", "heritage", "ritual",
    "folklore", "assimilation", "diversity", "multiculturalism", "stereotype", "taboo",
    "artefact", "intangible", "aesthetics", "renaissance", "ancestor", "ceremony",
    "cuisine", "dialect", "pilgrimage", "sacred", "secular", "symbolism", "iconic",
    "craftsmanship", "patriotism",
]

# ============================================================
# 3. Additional IELTS High-Frequency Words
# ============================================================
EXTRA_IELTS = [
    "abolish", "abrupt", "absorb", "absurd", "abuse", "accelerate", "accessible",
    "accompany", "accomplish", "acquaintance", "adolescent", "adverse",
    "aesthetic", "affection", "agenda", "aggravate", "aggregate", "allege",
    "alleviate", "allocate", "allusion", "ambiguous", "amend", "analogy",
    "anguish", "anonymous", "antagonism", "antibiotic", "apparatus", "applaud",
    "appraisal", "arbitrary", "arid", "articulate", "aspiration", "assassination",
    "assert", "assimilate", "astounding", "atrocity", "audit", "authentic", "autonomy",
    "bankruptcy", "barren", "beforehand", "belligerent", "benevolent", "besiege",
    "beverage", "bewilder", "bizarre", "bland", "blatant", "bleak", "blunder",
    "bolster", "boycott", "breach", "brink", "brisk", "browse", "brutal",
    "budget", "bulletin", "burden", "camouflage", "candid", "captivate",
    "cardinal", "catastrophe", "cater", "caution", "celestial", "censor",
    "chronicle", "circumvent", "civic", "clamour", "clarity", "clientele",
    "climax", "coerce", "coherent", "collaborate", "commemorate", "commence",
    "commend", "commonplace", "comparable", "compassion", "compel", "compensate",
    "complacent", "complement", "compliance", "comply", "concede", "concise",
    "condone", "confiscate", "conscientious", "consecutive", "consensus",
    "consolidate", "conspicuous", "contemplate", "contempt", "contend",
    "contentious", "contingent", "contradiction", "convene", "converge",
    "conviction", "cope", "cordial", "cosmopolitan", "counterpart", "courteous",
    "credibility", "criterion", "culminate", "cultivate", "cumulative", "curb",
    "curtail", "cushion", "daunting", "debris", "deceive", "decipher", "decisive",
    "declaration", "dedicate", "deem", "defect", "defer", "deficiency",
    "definitive", "defy", "delegate", "deliberate", "delicate", "demolish",
    "denounce", "depict", "deplete", "deploy", "depreciate", "deprive",
    "designate", "desolate", "destitute", "deter", "deteriorate", "detrimental",
    "devastate", "deviate", "devise", "diagnose", "diffuse", "dilemma",
    "diligent", "diminish", "dire", "discern", "disclose", "discourse",
    "discrepancy", "discretion", "disdain", "dismantle", "dismay", "dispatch",
    "dispel", "disperse", "disposition", "dispute", "disrupt", "disseminate",
    "dissent", "dissolve", "distort", "divert", "doctrine", "dogma",
    "domain", "drastic", "dread", "dubious", "dwell", "eccentric", "eclipse",
    "elaborate", "elapse", "elevate", "elicit", "eloquent", "elude",
    "embark", "embed", "embody", "embrace", "emerge", "eminent", "emit",
    "encompass", "endeavour", "endorse", "endure", "engender", "enhance",
    "enigma", "enormous", "enrich", "entail", "envisage", "epitome",
    "equitable", "eradicate", "erratic", "escalate", "essence", "esteem",
    "evoke", "exacerbate", "excel", "excerpt", "excessive", "exclude",
    "exemplify", "exempt", "exert", "exile", "expedite", "explicit",
    "exploit", "exquisite", "extensive", "extol", "extravagant", "exuberant",
    "facet", "fallacy", "famine", "feasible", "fervent", "fiasco",
    "fidelity", "flagrant", "flaw", "flourish", "fluctuate", "forge",
    "formidable", "fortify", "foster", "fragile", "friction", "frugal",
    "futile", "gauge", "generic", "genesis", "genuine", "gigantic",
    "glamour", "grapple", "gratitude", "gravity", "grievance", "gruesome",
    "hamper", "haphazard", "hardship", "harmony", "harsh", "hazard",
    "heed", "heighten", "hereditary", "hinder", "hostile", "humane",
    "hurdle", "hypocrisy", "illicit", "illuminate", "immense", "immerse",
    "imminent", "impair", "impartial", "impede", "imperative", "imperial",
    "impetus", "implement", "implicit", "impoverish", "improvise", "inadvertent",
    "inaugurate", "incessant", "inclination", "increment", "indictment",
    "indigenous", "indignant", "indispensable", "indulge", "inertia",
    "inflict", "influx", "ingenious", "inhabit", "inhibit", "initiate",
    "innocuous", "innovative", "insatiable", "instigate", "insufficient",
    "intact", "integral", "interim", "intricate", "intrinsic", "intuition",
    "inundate", "invariably", "inventory", "invoke", "irrevocable",
    "jeopardize", "jovial", "judicious", "junction", "juxtapose",
    "keen", "knack", "lament", "landmark", "latent", "lavish", "legacy",
    "legitimate", "lenient", "lethal", "levy", "liability", "likelihood",
    "linger", "lucrative", "luminous", "magnitude", "malice", "mandatory",
    "manifest", "manipulate", "marginal", "maritime", "massive", "mediate",
    "mediocre", "menace", "meticulous", "milestone", "mitigate", "mobilize",
    "momentum", "monopoly", "monotonous", "moratorium", "mundane", "municipal",
    "myriad", "negligence", "negotiate", "nominal", "nonchalant", "notable",
    "notorious", "novel", "nuance", "nurture", "obligation", "obscure",
    "obstacle", "offset", "ominous", "onset", "opaque", "oppress",
    "optimum", "ordeal", "orthodox", "oscillate", "ostensible", "outbreak",
    "outweigh", "overhaul", "overlap", "overlook", "override", "oversight",
    "overt", "paradox", "paralyze", "paramount", "partisan", "pathetic",
    "patron", "peculiar", "pending", "penetrate", "peril", "peripheral",
    "permeate", "perpetual", "perplex", "persevere", "persistent", "pertain",
    "pertinent", "pervasive", "petition", "pinpoint", "pivotal", "plague",
    "plausible", "pledge", "plummet", "plunder", "poignant", "polarize",
    "ponder", "portray", "postulate", "pragmatic", "precarious", "precedent",
    "precipitate", "predicament", "predominant", "prejudice", "premise",
    "prescribe", "prestige", "presume", "prevail", "prevalent", "pristine",
    "probe", "proclaim", "prodigious", "profound", "prohibit", "proliferate",
    "prominent", "prone", "propagate", "propensity", "proposition", "prosecute",
    "prosper", "provoke", "prudent", "punctual", "pungent", "quandary",
    "quarantine", "quota", "ramification", "rampant", "ratify", "rationale",
    "ravage", "rebut", "recede", "recipient", "reciprocal", "reckon",
    "reconcile", "redeem", "refrain", "refute", "regime", "reiterate",
    "relentless", "relinquish", "relish", "remedy", "reminiscent", "remnant",
    "render", "renovate", "repeal", "repercussion", "replenish", "repress",
    "reprimand", "reproach", "repudiate", "requisite", "resilient", "resonance",
    "respite", "restoration", "restrain", "resume", "retaliate", "retention",
    "retract", "retrospect", "revelation", "revere", "revitalize", "rhetoric",
    "rigorous", "robust", "rudimentary", "rupture", "sabotage", "salient",
    "salvage", "sanction", "saturate", "savvy", "scarcity", "sceptical",
    "scrutiny", "secrete", "sediment", "seismic", "seminal", "sentiment",
    "sever", "simulate", "skeptical", "solicit", "solidarity", "soothe",
    "sparse", "speculate", "spontaneous", "sporadic", "stagnant", "stark",
    "statutory", "steadfast", "steep", "stem", "stigma", "stipulate",
    "strive", "stubborn", "subjective", "subordinate", "subsequent", "subside",
    "subsidize", "substantiate", "subtle", "succession", "succumb", "suffice",
    "summit", "superfluous", "supplant", "suppress", "supreme", "surge",
    "susceptible", "suspension", "sweeping", "symmetry", "symptom", "synopsis",
    "synthesis", "tangible", "tedious", "temper", "tentative", "tenure",
    "terrain", "testament", "threshold", "thrive", "tolerate", "trajectory",
    "tranquil", "transcend", "transient", "traverse", "treacherous", "treaty",
    "tremendous", "trigger", "trivial", "turbulent", "turmoil", "unanimous",
    "undermine", "underscore", "unequivocal", "unprecedented", "unravel",
    "upheaval", "uphold", "utmost", "utter", "validate", "vanguard",
    "venerate", "venture", "verdict", "versatile", "vested", "viable",
    "vibrant", "vigilant", "vigorous", "vindicate", "vivid", "vocal",
    "vogue", "void", "volatile", "vouch", "vulnerable", "wane",
    "warrant", "weary", "wholesale", "wield", "withhold", "withstand",
    "witness", "wretched", "yield", "zeal",
]

# ============================================================
# Functions
# ============================================================
def clean_word(w):
    """Clean a word: lowercase, strip, remove non-alpha except hyphen."""
    w = w.strip().lower()
    # Remove leading/trailing punctuation
    w = w.strip(".,;:!?\"'()[]{}")
    # Remove phrases with spaces (multi-word entries)
    if " " in w:
        return None
    # Remove entries that are clearly not words
    if not w or len(w) < 2:
        return None
    # Only allow letters and hyphens
    if not re.match(r'^[a-z-]+$', w):
        return None
    return w

def load_existing():
    existing_file = os.path.join(WORD_DIR, "existing-words.txt")
    words = set()
    with open(existing_file, "r", encoding="utf-8-sig") as f:
        for line in f:
            w = clean_word(line)
            if w:
                words.add(w)
    return words

def load_ielts4000():
    """Parse IELTS-4000.txt: format is 'word: definition'"""
    ielts_file = os.path.join(WORD_DIR, "ielts4000_raw.txt")
    words = set()
    if not os.path.exists(ielts_file):
        print(f"WARNING: {ielts_file} not found!")
        return words
    with open(ielts_file, "r", encoding="utf-8-sig") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('IELTS') or line.startswith('4000'):
                continue
            # Extract word before colon
            if ':' in line:
                word_part = line.split(':')[0].strip()
                w = clean_word(word_part)
                if w:
                    words.add(w)
    return words

def compile_master():
    existing = load_existing()
    print(f"现有词汇: {len(existing)}")

    # Build priority sets
    awl_high = set()
    for sl in [1, 2, 3]:
        for w in AWL[sl]:
            awl_high.add(w.lower())
    awl_mid = set()
    for sl in [4, 5, 6, 7]:
        for w in AWL[sl]:
            awl_mid.add(w.lower())
    awl_low = set()
    for sl in [8, 9, 10]:
        for w in AWL[sl]:
            awl_low.add(w.lower())
    topic = set(w.lower() for w in TOPIC_VOCAB)
    extra = set(w.lower() for w in EXTRA_IELTS)
    ielts4k = load_ielts4000()

    print(f"IELTS 4000 词表: {len(ielts4k)}")
    print(f"AWL 高优先级: {len(awl_high)}")
    print(f"AWL 中优先级: {len(awl_mid)}")
    print(f"AWL 低优先级: {len(awl_low)}")
    print(f"话题词汇: {len(topic)}")
    print(f"额外词汇: {len(extra)}")

    # Merge all
    all_sources = awl_high | awl_mid | awl_low | topic | extra | ielts4k
    print(f"全部来源合并: {len(all_sources)}")

    # Deduplicate
    new_words = all_sources - existing
    print(f"剔除已有后: {len(new_words)}")

    # Sort by priority
    result = []
    p1 = sorted(new_words & awl_high)
    result.extend(p1)
    p2 = sorted((new_words & awl_mid) - set(result))
    result.extend(p2)
    p3 = sorted((new_words & topic) - set(result))
    result.extend(p3)
    p4 = sorted((new_words & awl_low) - set(result))
    result.extend(p4)
    # IELTS 4000 words that aren't in any other category
    other_ielts4k = sorted(new_words - set(result))
    result.extend(other_ielts4k)

    p5 = len(other_ielts4k)

    print(f"\n最终主词表: {len(result)} 词")
    print(f"  P1-AWL高: {len(p1)}")
    print(f"  P2-AWL中: {len(p2)}")
    print(f"  P3-话题: {len(p3)}")
    print(f"  P4-AWL低: {len(p4)}")
    print(f"  P5-IELTS4000+其他: {p5}")
    print(f"  折合单词本: {len(result) // 100} 本 (余{len(result) % 100}词)")

    # Write master list
    output_file = os.path.join(WORD_DIR, "master-wordlist.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for w in result:
            f.write(w + "\n")

    # Write priority groups
    groups_file = os.path.join(WORD_DIR, "master-wordlist-groups.txt")
    with open(groups_file, "w", encoding="utf-8") as f:
        f.write(f"# Total: {len(result)} words\n\n")
        f.write(f"# P1 - AWL Sublist 1-3 ({len(p1)} words)\n")
        for w in p1:
            f.write(f"{w}\n")
        f.write(f"\n# P2 - AWL Sublist 4-7 ({len(p2)} words)\n")
        for w in p2:
            f.write(f"{w}\n")
        f.write(f"\n# P3 - Topic Vocabulary ({len(p3)} words)\n")
        for w in p3:
            f.write(f"{w}\n")
        f.write(f"\n# P4 - AWL Sublist 8-10 ({len(p4)} words)\n")
        for w in p4:
            f.write(f"{w}\n")
        f.write(f"\n# P5 - IELTS 4000 General + Extra ({p5} words)\n")
        for w in other_ielts4k:
            f.write(f"{w}\n")

    print(f"\n输出文件:")
    print(f"  {output_file}")
    print(f"  {groups_file}")
    return result

if __name__ == "__main__":
    compile_master()
