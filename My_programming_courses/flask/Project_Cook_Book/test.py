from flask import Flask, redirect, url_for, render_template_string, request, session
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = '123GoniszTy!'  # Klucz sesji

# receipts_path = app.static_folder
# print('receipts_path: ', receipts_path)

# receipts_files = os.listdir(receipts_path)
# print('receipts_files: ', receipts_files)


# receipts_links = ''
# downland_links = ''
# comment_links = ''
# subpath_download = "download/"+file
# subpath_receipts = "receipts/"+file
# subpath_comment = "comment/"+file
# for receipt_file in receipts_files:
#     # name = os.listdir(receipt_file)
#     # print('name: ', receipt)
#     name = os.path.splitext(receipt_file)[0]
#     print('name2: ', name)
#     receipts_links += f'<ul><a href={ url_for("receipt", name=name, step=1)}>{name}</a></ul>'
#     print('receipts_links: ', receipts_links)

name = "how to make a coffee"
step = 1

full_file_path = os.path.join(
    app.static_folder, 'receipts', name+'.txt')  # type: ignore
print("full_file_path:", full_file_path)
if os.path.isfile(full_file_path):
    with open(full_file_path) as f:
        content = f.readlines()
        print('content: ', content)
        if len(content) >= step:
            instruction = content[step + 1]
            print('instruction: ', instruction)
