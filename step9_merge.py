import json

# ── Inputs from Zapier ────────────────────────────────────────────────────────
ai_json = input_data['ai_json']
html1 = input_data['html1']
html2 = input_data['html2']
html3 = input_data['html3']
business_type = input_data['business_type']
pain_point = input_data['pain_point']

# ── Parse AI JSON from step 8 ─────────────────────────────────────────────────
bp = json.loads(ai_json)

# ── Token map ─────────────────────────────────────────────────────────────────
# Keys must exactly match every {{PLACEHOLDER}} in the three HTML templates.
# P1_BUSINESS_TYPE and P1_PAIN_POINT come from steps 3/4 (formatter outputs),
# everything else comes from the AI-generated blueprint JSON (step 8).

tokens = {
    # PAGE 1
    '{{P1_BUSINESS_TYPE}}': business_type,
    '{{P1_PAIN_POINT}}': pain_point,
    '{{P1_SUBTITLE}}': bp['P1_SUBTITLE'],

    # PAGE 2 — body paragraphs
    '{{P2_P1}}': bp['P2_P1'],
    '{{P2_P2}}': bp['P2_P2'],
    '{{P2_P3}}': bp['P2_P3'],

    # PAGE 2 — six stats
    '{{P2_S1_NUM}}': str(bp['P2_S1_NUM']),
    '{{P2_S1_DESC}}': bp['P2_S1_DESC'],
    '{{P2_S2_NUM}}': str(bp['P2_S2_NUM']),
    '{{P2_S2_DESC}}': bp['P2_S2_DESC'],
    '{{P2_S3_NUM}}': str(bp['P2_S3_NUM']),
    '{{P2_S3_DESC}}': bp['P2_S3_DESC'],
    '{{P2_S4_NUM}}': str(bp['P2_S4_NUM']),
    '{{P2_S4_DESC}}': bp['P2_S4_DESC'],
    '{{P2_S5_NUM}}': str(bp['P2_S5_NUM']),
    '{{P2_S5_DESC}}': bp['P2_S5_DESC'],
    '{{P2_S6_NUM}}': str(bp['P2_S6_NUM']),
    '{{P2_S6_DESC}}': bp['P2_S6_DESC'],

    # PAGE 3 — body paragraphs
    '{{P3_P1}}': bp['P3_P1'],
    '{{P3_P2}}': bp['P3_P2'],
    '{{P3_P3}}': bp['P3_P3'],
    '{{P3_P4}}': bp['P3_P4'],
    '{{P3_P5}}': bp['P3_P5'],

    # PAGE 3 — section heading + button
    '{{P3_HEADING}}': bp['P3_HEADING'],
    '{{P3_BTN_TEXT}}': bp['P3_BTN_TEXT'],

    # PAGE 3 — quote card 1
    '{{P3_Q1_NAME}}': bp['P3_Q1_NAME'],
    '{{P3_Q1_TITLE}}': bp['P3_Q1_TITLE'],
    '{{P3_Q1_TEXT}}': bp['P3_Q1_TEXT'],

    # PAGE 3 — quote card 2
    '{{P3_Q2_NAME}}': bp['P3_Q2_NAME'],
    '{{P3_Q2_TITLE}}': bp['P3_Q2_TITLE'],
    '{{P3_Q2_TEXT}}': bp['P3_Q2_TEXT'],
}

# ── Replace tokens in each page ───────────────────────────────────────────────
for token, value in tokens.items():
    html1 = html1.replace(token, value)
    html2 = html2.replace(token, value)
    html3 = html3.replace(token, value)

# ── Merge into one final HTML document ───────────────────────────────────────
final_html = html1 + '\n' + html2 + '\n' + html3

# ── Output for step 11 (PDF.co) ───────────────────────────────────────────────
output = {'final_html': final_html}
