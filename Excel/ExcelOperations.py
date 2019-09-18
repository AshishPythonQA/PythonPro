import xlrd  # to read xlsx sheet
import openpyxl  # write to Excel Sheet


class ExcelData:
    workbookloc = "C:\\Users\\VinayVinay\\Desktop\\TestData\\ExcelData.xlsx"
    workbook = xlrd.open_workbook(workbookloc)

    def readData(self, sheetname, rownum, cellnum):
        try:
            sheet = ExcelData.workbook.sheet_by_name(sheetname)
            result = sheet.cell_value(rownum, cellnum)
            return result

        except Exception as e:
            print("Exception occurred: %s" % e)

    def writeData(self, sheetname, cellnum,  data):
        try:
            workbook = openpyxl.load_workbook(ExcelData.workbookloc)
            sheet = workbook.get_sheet_by_name(sheetname)
            sheet[cellnum] = data
            workbook.save(ExcelData.workbookloc)

        except Exception as e:
            print("Exception occurred: %s" % e)

    def rowcount(self, sheetname):
        try:
            return ExcelData.workbook.sheet_by_name(sheetname).nrows
        except Exception as e:
            print("Exception occurred: %s" % e)

    def colcount(self, sheetname):
        try:
            return ExcelData.workbook.sheet_by_name(sheetname).ncols
        except Exception as e:
            print("Exception occurred: %s" % e)
