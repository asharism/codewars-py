import codewars_test as test
from solution import *
        
@test.describe("Decimal To Factorial and Back")
def tests(): 
    def testing1(n, expect):
        # try:
        #     actual =  dec2FactString(n)
        # except NameError:
        actual = dec_2_fact_string(n)
        test.assert_equals(actual, expect)
    @test.it("Basic tests1")
    def basics1():
        testing1(463, "341010") 
        testing1(2982, "4041000") 
        
    def testing2(n, expect):
        # try:
        #     actual =  factString2Dec(n)
        # except NameError:
        actual = fact_string_2_dec(n)
        test.assert_equals(actual, expect)
    @test.it("Basic tests2")
    def basics2():
        testing2("341010", 463)
        testing2("4042100", 2990)
        
