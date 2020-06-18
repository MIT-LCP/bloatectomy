# -*- coding: utf-8 -*-


text = '''Assessment and Plan
61 yo male Hep C cirrhosis and HCC presents with probable lower GIB and
renal failure of unclear duration.
Abd pain:
-other labs: PT / PTT / INR:16.6//                         1.5, CK / CKMB /

Troponin-T:4390/40/0.21, ALT / AST:258/575, Alk Phos / T Bili:232/5.9,
ICU Care
-other labs: PT / PTT / INR:16.6//                         1.5, CK / CKMB /
   Communication:                                              Comments:
icu Care
Assessment and Plan
Chief Complaint:
61 yo male Hep C cirrhosis and HCC presents with probable lower GIB and
renal failure of unclear duration.
Abd pain:
'''

bloatectomy(text, style='highlight', display=False, output='html', output_numbered_tokens=True, output_original_tokens=True)

bloatectomy('sample_text.txt', style='highlight', display=False, filename='sample_txt_output', output='html', output_numbered_tokens=True, output_original_tokens=True)

bloatectomy('sample_text.docx', style='bold', display=False, filename='sample_docx_output', output='docx')
