from Chapter1 import Chapter1_Screen, Chapter1_Test1, Chapter1_Test2, Chapter1_Test3
from Chapter1 import Chapter1_Test4, Chapter1_Test5,Chapter1_Test6, Chapter1_Test7, Chapter1_Test8
from Excel import ExcelOperations


class Chapter1_mainCaller:
    def Caller(self, url):
        excel = ExcelOperations.ExcelData()

        # Test of chapter1 Screen
        if excel.readData("Chapter1_Data", 1, 3) == "FAIL" \
                or excel.readData("Chapter1_Data", 1, 3) == "NORUN":
            test = Chapter1_Screen.chapter1Screen()
            test.Chapter1(url)
        else:
            print("This scenario is PASSED")

        # Test1 of chapter1 Screen
        if excel.readData("Chapter1_Data", 2, 3) == "FAIL" \
                or excel.readData("Chapter1_Data", 2, 3) == "NORUN":
            test1 = Chapter1_Test1.chapter1Test1()
            test1.Chapter1_Test1(url)
        else:
            print("This scenario is PASSED")

        # Test2 of chapter1 Screen
        if excel.readData("Chapter1_Data", 3, 3) == "FAIL" \
                or excel.readData("Chapter1_Data", 3, 3) == "NORUN":
            test2 = Chapter1_Test2.chapter1Test2()
            test2.Chapter1_Test2(url)
        else:
            print("This scenario is PASSED")

        # Test3 of chapter1 Screen
        if excel.readData("Chapter1_Data", 4, 3) == "FAIL" \
                or excel.readData("Chapter1_Data", 4, 3) == "NORUN":
            test3 = Chapter1_Test3.chapter1Test3()
            test3.Chapter1_Test3(url)
        else:
            print("This scenario is PASSED")

        # Test4 of chapter1 Screen
        if excel.readData("Chapter1_Data", 5, 3) == "FAIL" \
                or excel.readData("Chapter1_Data", 5, 3) == "NORUN":
            test4 = Chapter1_Test4.chapter1Test4()
            test4.Chapter1_Test4(url)
        else:
            print("This scenario is PASSED")

        # Test5 of chapter1 Screen
        if excel.readData("Chapter1_Data", 6, 3) == "FAIL" \
                or excel.readData("Chapter1_Data", 6, 3) == "NORUN":
            test5 = Chapter1_Test5.chapter1Test5()
            test5.Chapter1_Test5(url)
        else:
            print("This scenario is PASSED")

        # Test6 of chapter1 Screen
        if excel.readData("Chapter1_Data", 7, 3) == "FAIL" \
                or excel.readData("Chapter1_Data", 7, 3) == "NORUN":
            test6 = Chapter1_Test6.chapter1Test6()
            test6.Chapter1_Test6(url)
        else:
            print("This scenario is PASSED")

        # Test7 of chapter1 Screen
        if excel.readData("Chapter1_Data", 8, 3) == "FAIL" \
                or excel.readData("Chapter1_Data", 8, 3) == "NORUN":
            test7 = Chapter1_Test7.chapter1Test7()
            test7.Chapter1_Test7(url)
        else:
            print("This scenario is PASSED")

        # Test8 of chapter1 Screen
        if excel.readData("Chapter1_Data", 9, 3) == "FAIL" \
                or excel.readData("Chapter1_Data", 9, 3) == "NORUN":
            test8 = Chapter1_Test8.chapter1Test8()
            test8.Chapter1_Test8(url)
        else:
            print("This scenario is PASSED")