from tasks.caesar_cipher import encrypt

class TestEncrypt:
    def test_encrypt_shifts_each_letter_in_string_by_shift_amount(self):
        assert encrypt("Hello", 2) == "Here is the encoded result: jgnnq"
        assert encrypt("EXCEL", 4) == "Here is the encoded result: ibgip"
        assert encrypt("Test", -1) == "Here is the encoded result: sdrs"