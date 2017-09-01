import sml_auto
import sml_boston
import sml_census
import sml_chronic
import sml_computer
import sml_iris
import sml_seeds
import sml_spam
import sml_titanic
import sml_wine
import sys
import traceback

print("Testing General Model Building Functionality")
try:
    assert sml_auto.test()> 0
    print("Auto Passed")
except Exception as e:
    print("Auto Failed")
    print(str(e))
try:
    assert sml_boston.test()> 0
    print("Boston Passed")
except Exception as e:
    print("Boston Failed")
    print(str(e))
try:
    assert sml_census.test()> 0
    print("Census Passed")
except Exception as e:
    print("Census Failed")
    print(str(e))
try:
    assert sml_chronic.test()> 0
    print("Chronic Passed")
except Exception as e:
    print("Chronic Failed")
    print(str(e))
try:
    assert sml_computer.test()> 0
    print("Computer Passed")
except Exception as e:
    print("Computer Failed")
    print(str(e))
try:
    assert sml_iris.test()> 0
    print("Iris Passed")
except Exception as e:
    print("Iris Failed")
    print(str(e))
try:
    assert sml_seeds.test() != None
    print("Seeds Passed")
except Exception as e:
    print("Seeds Failed")
    print(str(e))
try:
    assert sml_spam.test()> 0
    print("Spam Passed")
except Exception as e:
    print("Spam Failed")
    print(str(e))
try:
    assert sml_titanic.test() > 0
    print("Titanic Passed")
except Exception as e:
    print("Titanic Failed")
    print(str(e))
try:
    assert sml_wine.test() > 0
    print("Wine Passed")
except Exception as e:
    print("Wine Failed")
    print(str(e))
