from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nCHƯƠNG TRÌNH QUẢN LÝ SINH VIÊN")
    print("******************************MENU******************************")
    print("** 1. Them sinh vien.                                        ***")    
    print("** 2. Cap nhat thong tin sinh vien boi ID.                   ***")
    print("** 3. Xoa sinh vien boi ID.                                  ***")
    print("** 4. Tim kiem sinh vien theo ten.                           ***")
    print("** 5. Sap xep sinh vien theo điem trung binh.                ***")   
    print("** 6. Sap xep sinh vien theo ten.                            ***")
    print("** 7. Hien thi danh sach sinh vien.                          ***")
    print("** 0. Thoat.                                                 ***")
    print("*****************************************************************")
    
    key = int(input("Nhập tùy chọn: "))
    if (key == 1):
        print("\n1. Thêm sinh viên.")
        qlsv.nhapSinhVien()
        print("Thêm sinh viên thành công!")
    elif key == 2:
        if (qlsv.soLuongSinhVien() > 0):
            print("\n2. Cập nhật thông tin sinh viên.")
            ID = int(input("Nhập ID: "))
            qlsv.updateSinhVien(ID)
        else:
            print("Danh sách sinh viên trống!")
    elif (key == 3):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n3. Xóa sinh viên.")
            ID = int(input("Nhập ID: "))
            if (qlsv.deleteById(ID)):
                print("\nSinh viên có ID = ", ID , "đã bị xóa.")
            else:
                print("\nSinh viên có ID  = ", ID , " không tồn tại.")
        else:
            print("\nDanh sách sinh viên trống!")
    elif (key == 4):
        if (qlsv.soLuongSinhVien() > 0):
            print("\n4. Tìm kiếm sinh viên theo tên.")
            name = input("Nhập tên để tìm kiếm: ")
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("Danh sách sinh viên trống!")
    elif (key == 5):
        if qlsv.soLuongSinhVien() > 0:
            print("\n5. Sắp xếp sinh viên theo điểm trung bình (GPA).")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống!")
    elif (key == 6):
        if qlsv.soLuongSinhVien() > 0:
            print("\n6. Sắp xếp sinh viên theo tên.")
            qlsv.sortByName()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống!")
    elif (key == 7):
        if qlsv.soLuongSinhVien() > 0:
            print("\n7. Hiển thị danh sách sinh viên.")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("Danh sách sinh viên trống!")
    elif (key == 8):
        print("\nBạn đã chọn thoát chương trình!")
        break
    else:
        print("\nKhông có chức năng này!")
        print("Hãy chọn chức năng trong hợp menu.")