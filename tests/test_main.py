import main


class TestTranslate:
    def test_ja2en(self):
        args = ['en', 'こんにちは']
        res = main.translate(args)
        assert res == 'Hello'

    def test_en2ja(self):
        args = ['ja', 'Hello']
        res = main.translate(args)
        assert res == 'こんにちは'

    def test_multi_args(self):
        args = ['ja', 'Hello', 'Bob']
        res = main.translate(args)
        assert res == 'こんにちはボブ'
