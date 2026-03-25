import json

ai_json       = input_data['ai_json']
html1         = input_data['html1']
html2         = input_data['html2']
html3         = input_data['html3']
business_type = input_data['business_type']
pain_point    = input_data['pain_point']

bp = json.loads(ai_json)

tokens = {
    '{{P1_BUSINESS_TYPE}}' : business_type,
    '{{P1_PAIN_POINT}}'    : pain_point,
    '{{P1_SUBTITLE}}'      : bp['P1_SUBTITLE'],
    '{{P2_P1}}'            : bp['P2_P1'],
    '{{P2_P2}}'            : bp['P2_P2'],
    '{{P2_P3}}'            : bp['P2_P3'],
    '{{P2_S1_NUM}}'        : str(bp['P2_S1_NUM']),
    '{{P2_S1_DESC}}'       : bp['P2_S1_DESC'],
    '{{P2_S2_NUM}}'        : str(bp['P2_S2_NUM']),
    '{{P2_S2_DESC}}'       : bp['P2_S2_DESC'],
    '{{P2_S3_NUM}}'        : str(bp['P2_S3_NUM']),
    '{{P2_S3_DESC}}'       : bp['P2_S3_DESC'],
    '{{P2_S4_NUM}}'        : str(bp['P2_S4_NUM']),
    '{{P2_S4_DESC}}'       : bp['P2_S4_DESC'],
    '{{P2_S5_NUM}}'        : str(bp['P2_S5_NUM']),
    '{{P2_S5_DESC}}'       : bp['P2_S5_DESC'],
    '{{P2_S6_NUM}}'        : str(bp['P2_S6_NUM']),
    '{{P2_S6_DESC}}'       : bp['P2_S6_DESC'],
    '{{P3_P1}}'            : bp['P3_P1'],
    '{{P3_Q1_NAME}}'       : bp['P3_Q1_NAME'],
    '{{P3_Q1_TITLE}}'      : bp['P3_Q1_TITLE'],
    '{{P3_Q1_TEXT}}'       : bp['P3_Q1_TEXT'],
    '{{P3_P2}}'            : bp['P3_P2'],
    '{{P3_HEADING}}'       : bp['P3_HEADING'],
    '{{P3_P3}}'            : bp['P3_P3'],
    '{{P3_P4}}'            : bp['P3_P4'],
    '{{P3_P5}}'            : bp['P3_P5'],
    '{{P3_Q2_NAME}}'       : bp['P3_Q2_NAME'],
    '{{P3_Q2_TITLE}}'      : bp['P3_Q2_TITLE'],
    '{{P3_BTN_TEXT}}'      : bp['P3_BTN_TEXT'],
    '{{P3_Q2_TEXT}}'       : bp['P3_Q2_TEXT'],
}

for token, value in tokens.items():
    html1 = html1.replace(token, value)
    html2 = html2.replace(token, value)
    html3 = html3.replace(token, value)

final_html = html1 + '\n' + html2 + '\n' + html3

output = {'final_html': final_html}
