from solution import sq_in_rect
import codewars_test as test
from random import randint


@test.describe("Tests...")
def _():

    @test.it("Basic Tests")
    def _():
        test.assert_equals(sq_in_rect(5, 5), None)
        test.assert_equals(sq_in_rect(5, 3), [3, 2, 1, 1])
        test.assert_equals(sq_in_rect(3, 5), [3, 2, 1, 1])
        test.assert_equals(sq_in_rect(20, 14), [14, 6, 6, 2, 2, 2])
