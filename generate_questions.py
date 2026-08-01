#!/usr/bin/env python3
"""
generate_questions.py
----------------------
Builds the MCQ question bank (questions.json) used by the Concrete Technology
exam-prep site.

Why this exists
----------------
The original page tried to call the Anthropic Messages API directly from
browser JavaScript on every "New Question" click. That can never work from a
static HTML page: there is no API key available client-side, and even with
one, a browser fetch straight to api.anthropic.com from a static site is
blocked by CORS. That is why the MCQ section never actually produced a
question.

The fix: generate a real, curated question bank offline (this script) and
have the front end simply read the resulting questions.json file. This keeps
the requested language set (Python, HTML, JavaScript, CSS3) and makes the
quiz work with zero server / API dependency.

Run it with:
    python3 generate_questions.py

It (re)writes questions.json next to this script. Edit QUESTIONS below to
add, remove, or correct questions; each unit should keep a healthy number of
entries so "Random Unit" and per-unit filters stay meaningful.
"""

import json
from pathlib import Path

# Each question: unit (1-6), question text, 4 options (no leading "A)" etc,
# the front end adds the letters), the 0-based index of the correct option,
# and an explanation shown after answering.
QUESTIONS = [
    # ───────────────────────── UNIT 1 — Ingredients of Concrete ─────────────────────────
    {
        "unit": 1,
        "question": "During Portland cement manufacturing, gypsum is added to the clinker mainly to:",
        "options": [
            "Increase the compressive strength of cement",
            "Control (retard) the setting time by slowing C3A hydration",
            "Reduce the kiln burning temperature",
            "Improve the fineness of the final cement",
        ],
        "correct": 1,
        "explanation": "3–5% gypsum is interground with clinker specifically to retard the very fast hydration of C3A (Celite), preventing flash setting.",
    },
    {
        "unit": 1,
        "question": "Which Bogue compound is the FIRST to hydrate and produces the highest heat of hydration?",
        "options": ["C3S (Alite)", "C2S (Belite)", "C3A (Celite)", "C4AF (Felite)"],
        "correct": 2,
        "explanation": "C3A (Tricalcium Aluminate / Celite) hydrates first and generates the highest heat, causing flash setting — which is why gypsum is added to control it.",
    },
    {
        "unit": 1,
        "question": "In the fineness test on cement (IS 4031 Part 1), the maximum permissible residue on the 90-micron IS sieve is:",
        "options": ["5%", "10%", "15%", "25%"],
        "correct": 1,
        "explanation": "IS 4031 Part 1 limits the residue retained on the 90-micron sieve to a maximum of 10%.",
    },
    {
        "unit": 1,
        "question": "In the Vicat standard consistency test, water is added to cement paste until the plunger penetrates to within:",
        "options": ["0–2 mm from the bottom", "5–7 mm from the bottom", "10–12 mm from the bottom", "15–20 mm from the bottom"],
        "correct": 1,
        "explanation": "Standard consistency is reached when the Vicat plunger settles 5–7 mm short of the mould's bottom.",
    },
    {
        "unit": 1,
        "question": "Which cement type achieves initial setting in about 5 minutes and is used for underwater / running-water construction?",
        "options": ["Rapid Hardening Cement (RHC)", "Quick Setting Cement", "Low Heat Cement", "Sulphate Resisting Cement"],
        "correct": 1,
        "explanation": "Quick Setting Cement sets within about 5 minutes (reduced gypsum + added aluminium sulphate) — it is not the same thing as Rapid Hardening Cement.",
    },
    {
        "unit": 1,
        "question": "For general water used in concrete (IS 456-2000), the maximum permissible chloride content is:",
        "options": ["200 mg/L", "400 mg/L", "500 mg/L", "2000 mg/L"],
        "correct": 2,
        "explanation": "Chloride content in mixing water must stay below 500 mg/L to limit reinforcement corrosion risk (sulphates: <400 mg/L, TDS: <2000 mg/L).",
    },
    {
        "unit": 1,
        "question": "In the aggregate crushing value test, the sample is loaded to 40 tonnes over 10 minutes and the crushed material passing which sieve is weighed?",
        "options": ["1.18 mm", "2.36 mm", "4.75 mm", "10 mm"],
        "correct": 1,
        "explanation": "Both the Aggregate Crushing Value and Aggregate Impact Value tests use the 2.36 mm sieve to separate the crushed/fine fraction.",
    },
    {
        "unit": 1,
        "question": "An aggregate particle is classified as 'flaky' when its thickness is less than:",
        "options": ["1/3 of its mean dimension", "3/5 of its mean dimension", "9/5 of its mean dimension", "2/3 of its mean dimension"],
        "correct": 1,
        "explanation": "IS 2386 defines a flaky particle as one whose thickness is less than 3/5 of its mean dimension; elongated means length greater than 9/5 of the mean dimension.",
    },
    # ───────────────────────── UNIT 2 — Fresh Concrete ─────────────────────────
    {
        "unit": 2,
        "question": "Which type of batching is recommended for all quality concrete work over volume batching?",
        "options": ["Volume batching", "Weigh batching", "Arbitrary batching", "Estimate batching"],
        "correct": 1,
        "explanation": "Weigh batching is far more accurate than volume batching, which is only acceptable for minor or temporary works.",
    },
    {
        "unit": 2,
        "question": "The standard slump cone has a height, bottom diameter, and top diameter of:",
        "options": ["25 cm / 15 cm / 10 cm", "30 cm / 20 cm / 10 cm", "30 cm / 25 cm / 15 cm", "20 cm / 15 cm / 5 cm"],
        "correct": 1,
        "explanation": "The slump cone is 30 cm tall with a 20 cm bottom diameter and a 10 cm top diameter, filled in 3 layers of 25 tamps each.",
    },
    {
        "unit": 2,
        "question": "A slump test in which one side of the concrete mass slides down while the rest stays intact is called:",
        "options": ["True slump", "Shear slump", "Collapse slump", "Zero slump"],
        "correct": 1,
        "explanation": "Shear slump indicates low cohesion in the mix; true slump is uniform subsidence, and collapse slump signals an overly wet mix.",
    },
    {
        "unit": 2,
        "question": "The Vee-Bee consistometer test is most suitable for concrete mixes that are:",
        "options": ["Very high workability, flowing mixes", "Medium workability mixes only", "Low workability / stiff, dry mixes", "Self-compacting mixes"],
        "correct": 2,
        "explanation": "Vee-Bee time is used when slump would read zero — i.e. for stiff, low-workability mixes not suited to the slump cone.",
    },
    {
        "unit": 2,
        "question": "In the Compaction Factor test, a value greater than 0.95 indicates:",
        "options": ["Very low workability", "Medium workability", "High workability / flowability", "An invalid test"],
        "correct": 2,
        "explanation": "CF is the ratio of partially compacted weight to fully compacted weight; CF > 0.95 corresponds to high workability, while CF < 0.75 is very low workability.",
    },
    {
        "unit": 2,
        "question": "Segregation in fresh concrete most directly leads to which hardened-concrete defect?",
        "options": ["Bleeding", "Honeycombing", "Carbonation", "Efflorescence"],
        "correct": 1,
        "explanation": "Segregation — coarse aggregate separating from the paste — results in honeycombed (voided) zones once the concrete hardens.",
    },
    {
        "unit": 2,
        "question": "In the Nurse–Saul maturity rule M = Σ(T − T0) × Δt, T0 (the datum temperature) is usually taken as:",
        "options": ["0°C", "−10°C", "10°C", "20°C"],
        "correct": 1,
        "explanation": "The datum temperature T0 below which hydration is assumed negligible is conventionally taken as −10°C in the Nurse–Saul maturity equation.",
    },
    {
        "unit": 2,
        "question": "Which curing method is most commonly used to rapidly gain strength in precast concrete elements?",
        "options": ["Ponding", "Wet burlap curing", "Steam curing", "Membrane curing"],
        "correct": 2,
        "explanation": "Steam curing accelerates hydration and can achieve close to 28-day strength within hours, making it standard for precast production.",
    },
    # ───────────────────────── UNIT 3 — Hardened Concrete ─────────────────────────
    {
        "unit": 3,
        "question": "In the standard IS 516 compressive strength test, the cube specimen is loaded at a rate of:",
        "options": ["14 kg/cm²/min", "140 kg/cm²/min", "1400 kg/cm²/min", "40 kg/cm²/min"],
        "correct": 1,
        "explanation": "IS 516-1959 specifies a loading rate of 140 kg/cm² per minute, applied without shock until failure, on 150 mm cubes.",
    },
    {
        "unit": 3,
        "question": "According to typical strength-gain curves, concrete reaches approximately what percentage of its 28-day strength at 7 days?",
        "options": ["16%", "40%", "65%", "90%"],
        "correct": 2,
        "explanation": "The commonly cited strength-gain sequence is 1 day ≈16%, 7 days ≈65%, 28 days ≈99% of the ultimate 28-day strength.",
    },
    {
        "unit": 3,
        "question": "The IS 456 formula for the modulus of elasticity of concrete is:",
        "options": ["Ec = 0.7√fck", "Ec = 5000√fck", "Ec = 1.65 × fck", "Ec = 0.43fck"],
        "correct": 1,
        "explanation": "IS 456-2000 gives the short-term static modulus of elasticity as Ec = 5000√fck (N/mm²), while flexural strength uses fcr = 0.7√fck.",
    },
    {
        "unit": 3,
        "question": "Per IS 456 creep coefficients, which age at loading produces the HIGHEST creep coefficient?",
        "options": ["7 days", "28 days", "1 year", "It is the same at all ages"],
        "correct": 0,
        "explanation": "Loading concrete early (7 days) causes the highest creep coefficient (2.2), decreasing to 1.6 at 28 days and 1.1 at 1 year as concrete matures.",
    },
    {
        "unit": 3,
        "question": "Shrinkage caused by self-desiccation, where hydration itself consumes internal water, is called:",
        "options": ["Plastic shrinkage", "Drying shrinkage", "Autogenous shrinkage", "Carbonation shrinkage"],
        "correct": 2,
        "explanation": "Autogenous shrinkage results from water being consumed by ongoing hydration reactions; it is significant especially in low W/C mixes.",
    },
    {
        "unit": 3,
        "question": "In the Rebound Hammer test (IS 13311 Part 2), a rebound number below 20 indicates:",
        "options": ["Very good, hard concrete", "Good layer", "Fair concrete", "Poor concrete"],
        "correct": 3,
        "explanation": "Rebound numbers are interpreted as: >40 very good, 30–40 good, 20–30 fair, <20 poor, and 0 indicates delaminated concrete.",
    },
    {
        "unit": 3,
        "question": "In the Ultrasonic Pulse Velocity (UPV) test, a pulse velocity below 3.0 km/s classifies the concrete quality as:",
        "options": ["Excellent", "Good", "Medium", "Doubtful"],
        "correct": 3,
        "explanation": "UPV grading: >4.5 km/s excellent, 3.5–4.5 good, 3.0–3.5 medium, and below 3.0 km/s is classified doubtful.",
    },
    {
        "unit": 3,
        "question": "The Rebound Hammer test primarily assesses concrete's:",
        "options": ["Internal homogeneity and voids", "Surface hardness", "Water permeability", "Sulphate resistance"],
        "correct": 1,
        "explanation": "The rebound hammer measures surface hardness only (accuracy ±25%) and cannot detect internal cracks — that is UPV's role.",
    },
    # ───────────────────────── UNIT 4 — Mix Design ─────────────────────────
    {
        "unit": 4,
        "question": "In concrete grade designation 'M25', the number 25 refers to:",
        "options": [
            "The maximum aggregate size in mm",
            "The characteristic compressive strength at 28 days in N/mm²",
            "The water-cement ratio percentage",
            "The slump value in mm",
        ],
        "correct": 1,
        "explanation": "'M' stands for Mix, and the number is the characteristic compressive strength (fck) at 28 days in N/mm², as per IS 456-2000.",
    },
    {
        "unit": 4,
        "question": "The IS 10262 target mean strength formula is f'ck = fck + 1.65S. The factor 1.65 corresponds to:",
        "options": ["1% acceptable defectives", "5% acceptable defectives", "10% acceptable defectives", "25% acceptable defectives"],
        "correct": 1,
        "explanation": "The 1.65 multiplier on standard deviation S corresponds to a 5% acceptable proportion of defective (below-target) results.",
    },
    {
        "unit": 4,
        "question": "As per IS 10262, when concrete is to be pumped, the volume of coarse aggregate in the mix should be:",
        "options": ["Increased by 10%", "Decreased by 10%", "Kept unchanged", "Decreased by 25%"],
        "correct": 1,
        "explanation": "For pumped concrete, coarse aggregate volume is reduced by about 10% to boost cohesion and pumpability and avoid pipe blockage.",
    },
    {
        "unit": 4,
        "question": "For every 25 mm increase in required slump, the IS 10262 water content should be adjusted by approximately:",
        "options": ["+1%", "+3%", "+10%", "-3%"],
        "correct": 1,
        "explanation": "IS 10262 Table 2 water contents are adjusted by roughly +3% for every 25 mm increase in target slump above the base value.",
    },
    {
        "unit": 4,
        "question": "Which mix-design method uses an absolute-volume approach and is widely referenced internationally, distinct from the Indian method?",
        "options": ["IS 10262", "DOE Method", "ACI 211.1", "Marsh Cone Method"],
        "correct": 2,
        "explanation": "ACI 211.1 is the American Concrete Institute's absolute-volume based mix design method; DOE is the British method, and IS 10262 is the Indian standard method.",
    },
    {
        "unit": 4,
        "question": "Per IS 456 acceptance criteria for concrete strength, the mean of any 4 consecutive test results should be at least:",
        "options": ["fck", "fck + 0.825S", "fck − 3 N/mm²", "fck + 1.65S"],
        "correct": 1,
        "explanation": "IS 456 Clause 16 requires the mean of 4 consecutive results to be ≥ fck + 0.825 × standard deviation, and every individual result ≥ fck − 3 N/mm².",
    },
    # ───────────────────────── UNIT 5 — Admixtures ─────────────────────────
    {
        "unit": 5,
        "question": "Superplasticizers (HRWRAs) typically reduce mixing water by about:",
        "options": ["1–5%", "10–15%", "20–30%", "50–60%"],
        "correct": 2,
        "explanation": "Superplasticizers achieve a much higher water reduction (20–30%) than ordinary plasticizers (10–15%), at a maximum dosage of about 2% by cement mass.",
    },
    {
        "unit": 5,
        "question": "Calcium chloride (CaCl2), a common accelerator, should be avoided in which application?",
        "options": ["Cold weather concreting", "Prestressed concrete", "Mass concrete dams", "Ready mixed concrete"],
        "correct": 1,
        "explanation": "CaCl2 promotes corrosion of steel and is specifically harmful to prestressed concrete's high-tensile tendons, even though it's a common cold-weather accelerator.",
    },
    {
        "unit": 5,
        "question": "As a retarder, sugar is effective only up to a dosage of about:",
        "options": ["0.2% by cement mass", "2% by cement mass", "5% by cement mass", "10% by cement mass"],
        "correct": 0,
        "explanation": "Sugar acts as a retarder only up to roughly 0.2% by cement mass; beyond that it can inhibit cement hydration and prevent setting almost entirely.",
    },
    {
        "unit": 5,
        "question": "Air-entraining admixtures primarily improve concrete's resistance to:",
        "options": ["Sulphate attack", "Freeze-thaw cycles", "Carbonation", "Alkali-silica reaction"],
        "correct": 1,
        "explanation": "Entrained micro air bubbles (around 0.05 mm) relieve internal pressure from freezing water, greatly improving freeze-thaw durability, though they slightly reduce strength.",
    },
    {
        "unit": 5,
        "question": "The Marsh Cone test is used to determine:",
        "options": [
            "Setting time of cement",
            "Optimum dosage of superplasticizer for fluidity",
            "Soundness of cement",
            "Compressive strength of mortar",
        ],
        "correct": 1,
        "explanation": "The Marsh Cone test measures the time for a fixed volume of admixed cement paste to flow through an orifice, used to find the optimum superplasticizer dosage.",
    },
    {
        "unit": 5,
        "question": "Silica fume is characterized by an SiO2 content of roughly:",
        "options": ["30–40%", "50–60%", "90–95%", "99–100%"],
        "correct": 2,
        "explanation": "Silica fume (micro-silica) is 90–95% amorphous SiO2 and is used at 5–15% cement replacement due to its very high pozzolanic reactivity.",
    },
    # ───────────────────────── UNIT 6 — Special Concretes & Durability ─────────────────────────
    {
        "unit": 6,
        "question": "Ready Mixed Concrete (RMC) must generally be placed within how long after batching?",
        "options": ["60 minutes", "120 minutes", "210 minutes", "300 minutes"],
        "correct": 2,
        "explanation": "RMC has an IS code limit of 210 minutes from batching to placement, though retarding admixtures may extend this slightly.",
    },
    {
        "unit": 6,
        "question": "Ferrocement is distinguished from ordinary reinforced concrete mainly because it:",
        "options": [
            "Uses only coarse aggregate, no sand",
            "Contains no coarse aggregate at all — only mortar and wire mesh",
            "Uses polymer resin instead of cement",
            "Has zero water-cement ratio",
        ],
        "correct": 1,
        "explanation": "Ferrocement is cement mortar (sand + cement, no coarse aggregate) reinforced with closely spaced steel wire mesh — ideal for thin, curved shapes like boats and tanks.",
    },
    {
        "unit": 6,
        "question": "In Fiber Reinforced Concrete (FRC), increasing coarse aggregate size beyond 10 mm typically:",
        "options": ["Increases FRC strength", "Has no effect on strength", "Decreases FRC strength", "Eliminates the need for fibers"],
        "correct": 2,
        "explanation": "Coarse aggregate larger than about 10 mm interferes with fiber distribution and bonding, reducing the strength of fiber reinforced concrete — a classic exam trap.",
    },
    {
        "unit": 6,
        "question": "Roller Compacted Concrete (RCC) is characterized by:",
        "options": [
            "High slump and conventional vibration",
            "Zero slump, compacted by vibratory rollers, no formwork",
            "Use of polymer resin as the sole binder",
            "Wire mesh reinforcement with no coarse aggregate",
        ],
        "correct": 1,
        "explanation": "RCC is a dry, zero-slump mix compacted with vibratory rollers and placed via asphalt pavers without conventional formwork — used in dams and heavy pavements.",
    },
    {
        "unit": 6,
        "question": "In concrete durability, which pore type is the MAIN contributor to permeability?",
        "options": ["Gel pores", "Capillary pores", "Entrained air voids", "None — permeability is unrelated to pore structure"],
        "correct": 1,
        "explanation": "Gel pores are too fine (water is adsorbed, not free) to matter; capillary pores, formed by excess unreacted water, are the primary path for fluid movement.",
    },
    {
        "unit": 6,
        "question": "Sulphate attack on concrete is chemically driven by the formation of an expansive compound called:",
        "options": ["Calcium carbonate", "Ettringite", "Calcium silicate hydrate", "Portlandite"],
        "correct": 1,
        "explanation": "Sulphates react with C3A and calcium hydroxide to form ettringite, an expansive compound that causes cracking; Sulphate Resisting Cement (low C3A) is the standard defense.",
    },
    {
        "unit": 6,
        "question": "The carbonation of concrete is typically detected on a broken/cored surface using:",
        "options": ["Litmus paper", "Phenolphthalein indicator", "Rebound hammer", "Marsh cone"],
        "correct": 1,
        "explanation": "Phenolphthalein turns pink in the still-alkaline (uncarbonated) zone and stays colourless in the carbonated zone, revealing carbonation depth.",
    },
    {
        "unit": 6,
        "question": "Lightweight concrete is defined by IS/general practice as concrete with a density below:",
        "options": ["1200 kg/m³", "1500 kg/m³", "1900 kg/m³", "2400 kg/m³"],
        "correct": 2,
        "explanation": "Lightweight concrete is generally defined as having a density under 1900 kg/m³, achieved via lightweight aggregates, aeration, or no-fines mixes.",
    },
]


def main() -> None:
    folder = Path(__file__).parent
    json_path = folder / "questions.json"
    js_path = folder / "questions.js"

    # Basic sanity checks so a bad edit fails loudly instead of shipping silently.
    for i, q in enumerate(QUESTIONS):
        assert len(q["options"]) == 4, f"Question {i} does not have exactly 4 options"
        assert 0 <= q["correct"] <= 3, f"Question {i} has an out-of-range 'correct' index"
        assert 1 <= q["unit"] <= 6, f"Question {i} has an invalid unit number"

    payload = json.dumps(QUESTIONS, indent=2, ensure_ascii=False)

    # questions.json — human-readable copy of the bank, handy if this is ever
    # served over http(s):// where fetch() works fine.
    json_path.write_text(payload, encoding="utf-8")

    # questions.js — the same data as a plain JS global. index.html loads
    # THIS file with a normal <script> tag, which works even when the page
    # is opened directly as a local file:// document (fetch() of local JSON
    # is blocked by browsers under file://, which is why a pure fetch-based
    # approach silently fails for anyone who just double-clicks index.html).
    js_path.write_text(
        "// Auto-generated by generate_questions.py — do not edit by hand.\n"
        f"const QUESTION_BANK = {payload};\n",
        encoding="utf-8",
    )

    print(f"Wrote {len(QUESTIONS)} questions to {json_path} and {js_path}")
    for unit in range(1, 7):
        count = sum(1 for q in QUESTIONS if q["unit"] == unit)
        print(f"  Unit {unit}: {count} questions")


if __name__ == "__main__":
    main()
