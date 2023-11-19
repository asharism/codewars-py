from program import evaluate
import codewars_test as test

@test.describe("Sample tests:")
def _():
    @test.it("tests:")
    def _():
        tests = [
            ['1 @ 1', 4],
            ['3 @ 2', 13],
            ['6 @ 9', 66],
            ['4 @ -4', -9],
            ['1 @ 1 @ -4', -9],
            ['2 @ 2 @ 2', 40],
            ['0 @ 1 @ 2', 0],
            ['5 @ 0', None]
        ]
        for equation, answer in tests:
            test.assert_equals(evaluate(equation), answer)