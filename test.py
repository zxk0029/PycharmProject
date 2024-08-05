import PyPDF2  # pip install PyPDF2


def extract_pages(file_path, start_page, end_page, output_folder):
    # 打开PDF文件
    with open(file_path, "rb") as infile:
        reader = PyPDF2.PdfReader(infile)

        # 创建PDF写入器
        writer = PyPDF2.PdfWriter()

        # 从指定的开始页到结束页添加页
        for i in range(start_page - 1, end_page):
            writer.add_page(reader.pages[i])

        # 输出新的PDF文件
        output_filename = f"{output_folder}/output_pages_{start_page}_to_{end_page}.pdf"
        with open(output_filename, "wb") as outfile:
            writer.write(outfile)
        print(f"PDF from page {start_page} to page {end_page} written as {output_filename}")


# 调用函数
extract_pages("xxx.pdf", 112, 120, "./")
