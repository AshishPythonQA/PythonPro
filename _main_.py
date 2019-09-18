from Callers import Chapter1_Caller
import time


class SelBrowser:
    URL = "http://book.theautomatedtester.co.uk/"

    # Screen 1 Automation
    chapter1 = Chapter1_Caller.Chapter1_mainCaller()
    chapter1.Caller(URL)
