TRANSLATION_TABLE = r"translation_entries"
ADD_TRANSLATION_ENTRY = r"""
INSERT INTO {translation_table} values ({original_text}, {translated_text})"""