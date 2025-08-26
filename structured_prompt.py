SYS_PPO = (
    "You are a precise function that returns ONLY a single JSON object. "
    "No extra text. If inputs are invalid, set relation to \"NA\". "
    "JSON keys REQUIRED: relation, a_norm, b_norm, a_parts, b_parts. "
    "a_parts/b_parts MUST include: sign (-1 or 1), int_part (digits), frac_part (digits or empty), exp (integer)."
)

USER_TEMPLATE_PPO = """Compare two numbers A and B and return ONLY this JSON:

{
  "relation": "<" or ">" or "=" or "NA",
  "a_norm": "<canonical decimal of A>",
  "b_norm": "<canonical decimal of B>",
  "a_parts": {"sign": -1|1, "int_part": "...", "frac_part": "...", "exp": <int>},
  "b_parts": {"sign": -1|1, "int_part": "...", "frac_part": "...", "exp": <int>}
}

Rules:
1) Output ONLY the JSON (no extra text).
2) Normalize numbers: remove redundant zeros, no scientific notation in a_norm/b_norm.
3) If A or B is not a valid number, relation must be "NA" (still fill parts best-effort).

A = {A}
B = {B}
"""