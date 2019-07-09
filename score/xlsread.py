import xlrd


def read_excel_6(student_system, xls_name):
    # 打开excel文件读取数据
    data0 = xlrd.open_workbook("D:/project/EO16score/static/xls/"+xls_name+"6N.xls").sheet_by_index(0)
    # print(data0.cell(0, 0).value, data0.nrows)
    student_list = []
    for data_row in range(3, data0.nrows):
        student = {
            "student_id": data0.cell(data_row, 0).value,
            "student_name": data0.cell(data_row, 1).value,
            "student_system": student_system,
            "student_identity": "无",

            "academic_score_6": float(data0.cell(data_row, -3).value),
            "credit_6": float(data0.cell(data_row, -4).value),
        }
        student_list.append(student)
        # print(student)
    return student_list


def read_excel_1_5(xls_name):
    # 打开excel文件读取数据
    data1 = xlrd.open_workbook("D:/project/EO16score/static/xls/"+xls_name+".xlsx").sheet_by_index(0)
    # print(data1.cell(0, 0).value, data1.nrows)
    student_list = []
    for data_row in range(2, data1.nrows):
        student = {
            "student_id": data1.cell(data_row, 1).value,
            # "student_name": data1.cell(data_row, 2).value,
            # "student_system": student_system,
            # "student_identity": "无",

            "developmental_score_1": float(data1.cell(data_row, 10).value),
            "science_score_1": float(data1.cell(data_row, 11).value),
            "developmental_score_2": float(data1.cell(data_row, 12).value),
            "science_score_2": float(data1.cell(data_row, 13).value),
            "developmental_score_3": float(data1.cell(data_row, 14).value),
            "science_score_3": float(data1.cell(data_row, 15).value),
            "developmental_score_4": float(data1.cell(data_row, 16).value),
            "science_score_4": float(data1.cell(data_row, 17).value),
            "developmental_score_5": float(data1.cell(data_row, 18).value),
            "science_score_5": float(data1.cell(data_row, 19).value),

            "academic_score_1_5": float(data1.cell(data_row, 9).value),
            "whole_score_1_5": float(data1.cell(data_row, 20).value),

            "credit_1_5": float(data1.cell(data_row, 3).value),
        }
        student_list.append(student)
        # print(student)
    return student_list


# read_excel_6("电子科学与技术", "DK")
